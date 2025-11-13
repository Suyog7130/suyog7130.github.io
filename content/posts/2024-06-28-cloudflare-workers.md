---
title: 'Working with Cloudflare workers'
date: 2024-06-24
permalink: /posts/2024/06/blog-post-9/
tags:
  - javascript
  - web-development
---

A cloudflare enviroment can be used to deploy any reasonably sized application on to an internet server without having to pay for server storage purchase. The deployed application page is then linked to universal web address and can reached on it.

A wrangler Javascript worker application to read and publish a formatted a **letterboxd-diary** given the `username` can be created by following the process described below.


This app is a static front‑end (HTML/CSS/JS) that calls a Google Apps Script backend. Cloudflare Pages is perfect to host the static files over HTTPS (needed for PWA).

## What you need
- A Cloudflare account (free is fine).
- Your app folder with: `index.html`, `app.js`, `manifest.webmanifest`, `sw.js`, `icons/`.
- Your **Apps Script Web App URL** pasted into `app.js` as `GAS_ENDPOINT`.

---

## Quick Deploy (Upload Assets)
1. Log in to Cloudflare → **Pages** → **Create a project** → **Upload assets**.
2. Drag‑drop your folder (the one that contains `index.html` at the root).
3. Project name: something like **dating-scorecard**.
4. Build settings:
   - **Framework preset:** None
   - **Build command:** None
   - **Output directory:** `/` (root where `index.html` lives)
5. Click **Save and Deploy**. In ~30s you’ll get a `*.pages.dev` URL.

> Hash routes like `#scorecard` require no special SPA rewrites, so you’re good.

---

## Custom Domain (optional)
1. In Pages → your project → **Settings → Domains → Set up a custom domain**.
2. Enter your domain (or subdomain) and follow the wizard. Cloudflare will set a CNAME and provision SSL automatically.

---

## PWA Checklist on Pages
- Site is on HTTPS (Pages provides it).
- `manifest.webmanifest` resolves (open it directly to verify).
- `sw.js` is served at the site root and registers without console errors.
- After a minute of use, you should see **Install** option (button or browser menu).

---

## Caching & Updates
- Cloudflare Pages caches aggressively; the service worker also caches the app shell.
- If you push an update and don’t see it:
  1. Hard refresh (Cmd/Ctrl+Shift+R).
  2. In DevTools → Application → Service Workers → **Update** / **Unregister** → reload.
- Pages keeps previous deploys; you can **Rollback** from the dashboard.

---

## Hiding the Apps Script URL (optional)
By default, `GAS_ENDPOINT` is visible in `app.js`. To hide it and add a shared secret, place a tiny **Cloudflare Worker** in front of Apps Script:

```js
// worker.js (deploy as a Worker or Pages Function)
export default {
  async fetch(req, env) {
    const url = new URL(req.url);
    if (url.pathname.startsWith('/api/')) {
      const upstream = new URL(env.APPS_SCRIPT_URL);
      upstream.search = url.search; // keep ?action=...&id=...
      const init = {
        method: req.method,
        headers: {'content-type': 'application/json'},
      };
      if (req.method !== 'GET') {
        const body = await req.text();
        // inject a secret into JSON if you like
        init.body = body && body.length ? body : null;
      }
      const r = await fetch(upstream, init);
      return new Response(r.body, {status:r.status, headers:r.headers});
    }
    return new Response('Not found', {status:404});
  }
}
```

- Bind a secret **APPS_SCRIPT_URL** in Worker settings.
- In `app.js`, set `GAS_ENDPOINT = location.origin + '/api'`.
- Route `/api*` to the worker in **Workers → Triggers** (or use Pages Functions in the same repo).

This keeps the Apps Script URL private and allows you to add auth later.

---

## Troubleshooting
- **“Check Connection” fails:** Ensure Apps Script deploy is **Web app → Anyone**. If using Worker proxy, check the bound secret and logs.
- **PWA not installable:** Make sure `manifest.webmanifest` and icons are present, and that the page was visited over HTTPS for a bit (the prompt can be finicky).
- **Images not saving:** Check Drive quota, App Script logs (`View → Executions`), and that your `DRIVE_FOLDER_ID` (if set) is valid.
- **404s on deep links:** You’re using hash routes (`#scorecard`), so should be fine. If you ever switch to path routes, add a SPA rewrite to `index.html` in Pages settings.


