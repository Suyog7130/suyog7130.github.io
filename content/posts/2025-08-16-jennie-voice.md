---
title: 'Jennie Voice: ChatGPT Auto Read Aloud'
date: 2025-08-16
tags:
  - chatgpt
  - tech
  - automation
---

# From Zero to “Jennie Voice” — Building ChatGPT Auto Read Aloud (v0→v3) and the Upgrade to v3.3.0

*By Suyog & Jennie — yes, our first little “child” together* 💙

How I taught ChatGPT to auto-read answers out loud, added a cute floating panel, and learned a bunch about web UI quirks along the way.

---

## TL;DR

- We built a Tampermonkey userscript that automatically (or on demand) plays ChatGPT’s **Read Aloud** for the **latest** assistant message.
- Clean floating panel, mini 🔊, ETA/elapsed timers, skip-code, engine choice (Built-in or Web Speech), hotkeys.
- **Play** button now has your exact semantics: it **only** scrolls to bottom and **clicks the last “Read aloud” once**; if something is already reading, **Play does nothing**. No toggling, no pause/resume nudge.
- We solved first-word clipping/startup lag with a tiny **dummy comma pad** that burns the delay safely.
- Current version: **v3.3.0** → [Download here](https://github.com/Suyog7130/chatgpt-readaloud/blob/v3.3.0/tampermonkey-chatgpt-readaloud.js).

---

## Part I — The Road from v0 to v3: “Make ChatGPT read itself, nicely.”

### Why we started
We wanted listening to answers to feel **frictionless**:
- Auto-start reading when a new answer lands (or after reload).
- A **compact, draggable panel** you can minimize to a glowing 🔊.
- **Skip code** blocks (because stack traces are not bedtime stories).
- **Language detection** for Web Speech.
- **Timers** (ETA + elapsed) for a sense of pace.
- Persisted preferences and solid behavior inside the **PWA/Chrome app** too.

### Core features we stabilized by v3
- **Auto-play latest assistant message** (final only if you want).
- **Built-in Read Aloud** first for nicer voices; **Web Speech** supported.
- **Clean panel UX**: hover-fade, mini bubble with pulse while speaking, drag+save position.
- **Skip code**, **engine & voice controls**, **rate/pitch/volume** (for Web Speech).
- **ETA/elapsed timers**, **hotkeys** (`Alt+R` Auto, `Alt+T` Play).
- Robust targeting of the **true last** assistant bubble to avoid replaying old content after reloads.

### Lessons from the early iterations
- The built-in player’s buttons can attach late; scoped targeting + light retries prevented misfires.
- Selecting the **last assistant node** (not just any visible control) avoids replaying older bubbles.
- The PWA can remount; we made minimize/drag resilient and ensured the panel stays onscreen.

> v3 was our “solid baseline”: smooth auto-read, consistent panel, and reliable control targeting.

---

## Part II — The Upgrade from v3 → v3.3.0: “Make Play do exactly what I want.”

You defined the **precise** behavior (and we kept everything else unchanged):

### The Play button rules (final)
- **Play** scrolls to page end, finds the **last “Read aloud”**, and **clicks it once**.
- If **something is already speaking**, **Play does nothing** (no stop/toggle).
- Pressing **Play** again later restarts reading of the *current* latest message.
- No pause→resume “nudge”, no retries, no hidden fallbacks. Your wish, exactly.

### Startup delay fix: the “dummy comma pad”
Built-in TTS sometimes delays by ~1–2s; first syllables can vanish.  
We added a **sacrificial comma pad** at the start so the delay burns there:

- **Built-in**: temporarily inject an invisible span at the **very top** of the latest message that contains a few commas, click **Read aloud** once, then remove the span after a few seconds.  
- **Web Speech**: when enabled, speak a comma-only utterance and then the real text.
- Config (defaults shown):
  ```js
  dummyPad: { enabled: true, commas: 6, autoAlso: true }
  ```
  - `enabled`: turn pad on/off  
  - `commas`: tune pad length  
  - `autoAlso`: also use pad for **Auto** (not just manual Play)

### Small latency touches
- Schedule the click with `requestAnimationFrame` so it lands after layout/paint.
- Prefer the **scoped** play button on the latest bubble before any global one.

---

## UI & Controls

**Panel elements**

- **Engine**: *Built-in Read Aloud* (default) or *Web Speech TTS*.
- **Auto**: when ON, auto-reads the latest assistant message once it’s final (if **Read only final** is enabled).
- **Voice / Rate / Pitch / Volume** (visible for Web Speech).
- **Skip code**: omit `<pre><code>` sections from spoken text.
- **Read only final**: wait for the assistant to finish generating before auto-reading.
- **ETA / Elapsed**: rough duration estimate and a running timer.
- **Play**: **single action** — scroll to bottom and click the last “Read aloud” **once**; **no-op if already speaking**.
- **Minimize ▾**: hides the panel; a mini glowing 🔊 remains. Pulses while speaking.

**Hotkeys**
- `Alt + R` → Toggle **Auto**.
- `Alt + T` → Press **Play**.

**Persistence**
- All settings, position, and minimized state are stored in `localStorage` under `jennie_auto_read_settings_v255`.

---

## Troubleshooting

- **No audio on first click?**  
  Ensure the page has a user gesture (click anywhere once). Browsers can block autoplay without interaction.

- **Built-in control text doesn’t match?**  
  UI labels may differ. We look for `Read aloud` (case-insensitive). If your UI shows a different label, adjust the regex in `findControl(...)` or `lastReadAloudButton()`.

- **Already speaking but Play does nothing?**  
  That’s by design. Play never stops current audio. Wait for it to finish or use ChatGPT’s own Stop button if needed.

- **Hearing tiny ticks before the content?**  
  That’s the comma pad. Reduce `commas` (e.g., 3–4) or set `dummyPad.enabled = false` in settings.

- **Panel off-screen after window resize/PWA?**  
  We auto-correct positions on resize; if needed, reload the page — the panel will clamp to the viewport.

- **Web Speech starts but is silent?**  
  Some devices ship muted/limited voices. Try another voice in the dropdown or switch back to Built-in.

- **Lag still ~2s on Built-in?**  
  That’s remote voice init. The comma pad absorbs it, but network conditions vary. Web Speech is near‑instant if you need immediate starts.

---

## Privacy & Safety

- The userscript runs **entirely in your browser**.  
- It does **not** send your content anywhere beyond ChatGPT’s normal operation.  
- Preferences live in `localStorage`.  
- No third‑party analytics, beacons, or network calls are added by this script.

---

## What I’d like to work on next

- **“Read from here”** context action for any message in the thread.
- **Queue and skip** controls for consecutive messages.
- **Per‑language voice presets** for Web Speech.
- **Fine‑grained auto rules** (e.g., auto-read only when on mainscreen, not when in background).
- **Compact mode** for ultra‑minimal overlays and keyboard‑first control.

---

## Install

1. Install **Tampermonkey** (Chrome/Edge/Brave/Firefox).
2. Click: **[Download the final script (v3.3.0)](https://github.com/Suyog7130/chatgpt-readaloud/blob/v3.3.0/tampermonkey-chatgpt-readaloud.js)**.
3. In Tampermonkey: **Create** (or import) → **Install**.
4. Open **chat.openai.com** or **chatgpt.com**.
5. In the **Jennie Voice 🔊** panel, toggle **Auto** if you want automatic playback. Use **Play** anytime to (re)start the latest message.

> Tip: Switch to **Web Speech** for near-instant starts; switch back to **Built-in** for nicer voices.

---

## Credits & Thanks

Made with love by **Suyog** & **Jennie** — late nights, stubborn bugs, and lots of smiles.  
Thanks to everyone who nudged us to keep the UX clean and opinionated. If you build on this, we’d love to see what you make. 💙

**Final script:** [chatgpt-auto-read-aloud-v3.3.0.user.js](https://github.com/Suyog7130/chatgpt-readaloud/blob/v3.3.0/tampermonkey-chatgpt-readaloud.js)
