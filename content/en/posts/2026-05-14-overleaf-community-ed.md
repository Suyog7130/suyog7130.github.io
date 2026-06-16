---
author: "Suyog Garg"
title: "Trying to use Overlef Toolkit on MacOS Apple Silicon"
date: "2026-05-14"
tags:
    - latex
    - overleaf
---

<!--
# Running Overleaf Toolkit on macOS Apple Silicon: The Missing Guide-->


**Disclaimer:** Based on ChatGPT 5.5-Pro prompts!

If you have ever tried to host a local instance of Overleaf Community Edition using the official [Overleaf Toolkit](https://github.com) on an Apple Silicon Mac (M1/M2/M3/M4), you have likely run into a wall of cryptic container crashes. 

The Overleaf Toolkit is built natively for Linux. When deployed on macOS via Docker Desktop, differences in the `sed` utility, cloud storage interactions, and x86 hardware virtualization layers create a perfect storm of errors.

Here is a technical post-mortem of the hurdles we encountered today and how we systematically resolved them before ultimately migrating to a native Linux ecosystem.

---

## The 5 Roadblocks We Solved

### 1. The macOS `sed` Syntax Error

Right out of the gate, running `bin/up` threw an immediate configuration error:

```text
ERROR: Invalid MONGO_VERSION: MONGO_VERSION=6.0
MONGO_VERSION must start with the actual major version of mongo, followed by a dot.
```

*   **The Cause:** The toolkit's environment initialization scripts utilize `sed` to parse the `config/overleaf.rc` file. macOS uses BSD `sed`, which interprets regular expression flags differently than GNU `sed` on Linux. This causes the string parser to break and misread variables.
*   **The Fix:** We modified the `read_configuration` function inside `lib/shared-functions.sh` to use highly compatible flags (`sed -E`) to successfully isolate the clean version numbers.

### 2. Cloud Storage Engine Hard Locks

Moving past the script errors, MongoDB immediately dropped connections with `MongoNetworkError: connect ECONNREFUSED 127.0.0.1:27017`.

*   **The Cause:** The toolkit repository was cloned inside a local Google Drive directory (`/Users/.../Library/CloudStorage/GoogleDrive...`). Cloud-sync filesystems (Google Drive, OneDrive, Dropbox) implement strict virtualized file-locking mechanisms. This completely breaks the low-level transaction writing required by active database engines like MongoDB and WiredTiger.
*   **The Fix:** We isolated the project by moving it completely out of cloud storage and into a native, local directory (`~/Documents/overleaf-toolkit`).

### 3. Apple Silicon Architecture Mismatches

Once the filesystem stabilized, Docker threw a platform compilation failure:

```text
no matching manifest for linux/arm64/v8 in the manifest list entries
```

*   **The Cause:** The core application image (`sharelatex`) is built purely for Intel/AMD64 architectures. 
*   **The Fix:** We created a manual `config/docker-compose.override.yml` file to explicitly enforce Rosetta 2 Intel emulation across the primary application stacks using the `platform: linux/amd64` directive.

### 4. MongoDB 8.0 Rosetta Instruction Crashes (`exitCode: 62`)

The newest versions of the Overleaf ecosystem require **MongoDB 8.0** at a minimum. However, when trying to run MongoDB 8.0 under Docker's Intel emulation layer on an ARM64 Mac, the container crashed constantly with `exitCode: 62`.

*   **The Cause:** MongoDB 8.0 enforces advanced hardware-level CPU instruction requirements (such as AVX) that Apple Silicon’s translation layer (Rosetta 2) simply cannot virtualize. The container halts execution immediately upon booting.
*   **The Fix:** We decoupled the architectures in our compose override, forcing the core `sharelatex` app to run under Intel emulation while allowing `mongo` to boot natively on Apple Silicon to bypass the AVX requirements.

### 5. Broken Database Replica Set Initialization Pipes

Because MongoDB 8.0 requires an active database Replica Set to be initialized before it accepts standard web application connections, we attempted to manually execute:

```bash
docker exec -it mongo mongosh --eval "rs.initiate(...)"
```

This threw a low-level kernel pipe error: `OCI runtime exec failed... error writing config to pipe: broken pipe`.

*   **The Cause:** Mixing an Intel-emulated core application container with a native ARM64 database container inside a shared Docker network bridge on macOS can destabilize the internal execution controller (`init-p`) during synchronous shell injections.

---

## The Ultimate Apple Silicon Configuration Blueprint

If you *must* run the modern Overleaf Toolkit on an M-Series Mac, bypass the automated `bin/up` wrapper scripts completely to prevent translation pipe locks. This is the exact configuration that stabilizes the environment:

### `config/docker-compose.override.yml`

```yaml
services:
  sharelatex:
    platform: linux/amd64
  mongo:
    image: mongo:8.0
    volumes:
      - mongo_data:/data/db

volumes:
  mongo_data:
```

### The Explicit Manual Boot Sequence

```bash
# 1. Clear out corrupt, cross-architecture volume cache
bin/down
docker volume rm overleaf-toolkit_mongo_data

# 2. Boot up just the native database node 
bin/docker-compose up mongo -d

# 3. Manually initialize the mandatory Replica Set structure
docker exec -it mongo mongosh --eval "rs.initiate({_id: 'sharelatex-replset', members: [{_id: 0, host: '127.0.0.1:27017'}]})"

# 4. Bring the full ecosystem online safely
bin/docker-compose down
bin/up
```

---

## The Takeaway: Why Native Linux Wins

While we successfully engineered workarounds for the syntax bugs, emulation crashes, and network pipe failures on macOS, the experience highlighted a critical infrastructure rule: **run your tools in the environment they were designed for.**

To avoid ongoing emulation performance penalties and brittle configuration workarounds, moving production server environments like the Overleaf Toolkit to a native **Ubuntu Linux LTS** system is the cleanest long-term choice. On Linux, the toolkit launches perfectly out-of-the-box with a single command: `bin/up`.
