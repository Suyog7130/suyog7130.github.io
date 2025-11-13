---
title: "Mac No‑Mouse Keyboard-only Rescue"
date: 2025-11-07
tags:
   - macos
   - guide
---

## How to turn on Bluetooth & Reconnect Your Mouse Using Only the Keyboard (Sonoma/Ventura)

iMac when used with bluetooth Apple keyboards and mouse has a faintly annoying problem of the inability to use the mouse if it doesn't automatically gets connected to the system. A possible remedy and workaround for this is to use keyboard keys for mouse control.

- Press `F8` (or `F7` in the Macbook) key on the keyboard to enable switching the command palettes in the settings window.
- Use the `Tab` to scroll up and down in the command palette.
- Use the `Space` bar to make the selection click at the desired command.

In a bit more detail:

When your **Apple mouse disconnects** and you’ve only got a **keyboard**, you can still get to **Bluetooth** and reconnect, no clicks needed. This guide is my personal, step‑by‑step checklist for macOS **Sonoma/Ventura**.

> Why this exists: Apple’s designs are… quirky. The **Magic Mouse** still can’t be used **while charging** because its port sits on the bottom; pairing or charging often means you’re temporarily mouseless. So let’s master the keyboard‑only path and move on with life.

---

## TL;DR (60‑second rescue)

1) **Enable Full Keyboard Access** (Keyboard Navigation): press **⌥⌘F5** (Accessibility Shortcuts) and turn **Keyboard navigation** on. If needed, press **^F7** (or **fn+^F7** on laptops) to make **Tab** move focus across *all controls*.

2) **Open Bluetooth**: press **⌘Space**, type **Bluetooth**, press **Return**.

3) **Toggle & Connect**: Use **Tab** (and sometimes **F6**) to move focus, **↑/↓** to pick your mouse, **Return** to **Connect**. If Bluetooth is off, focus the **Turn Bluetooth On** button and hit **Return**.

4) **If that fails**: Launch **Bluetooth File Exchange** (⌘Space → type *Bluetooth File Exchange* → **Return**) and accept the prompt to **Turn Bluetooth On**. Then connect from the **Bluetooth** pane.

5) **Emergency cable pair** (Magic Mouse/Trackpad/Keyboard): plug it into your Mac via USB/USB‑C/Lightning → it **auto‑pairs**, then unplug and use wirelessly.

---

## The detailed, reproducible flow

### 1) Turn on keyboard navigation for everything
- Press **⌥⌘F5** to open the **Accessibility Shortcuts** panel. Turn **Keyboard navigation** (Full Keyboard Access) **On**.
- If the panel doesn’t appear or toggling doesn’t stick, press **^F7** (or **fn+^F7**) to switch Tab behavior so it highlights *all* interactive controls (buttons, lists, etc.).
- Tip: on laptops with media keys, remember to hold **fn** with **F‑keys**.

### 2) Open the Bluetooth pane without a mouse
- Press **⌘Space**, type **Bluetooth**, hit **Return**. System Settings → **Bluetooth** opens.
- **Alternate** (works even if search is flaky): press **⌘Space**, type **Terminal**, **Return**, then run:  

```bash
  open /System/Library/PreferencePanes/Bluetooth.prefPane
```
  
  This jumps straight to the Bluetooth settings pane.

### 3) Navigate the pane and connect
- **Move focus**: press **Tab** to cycle through sidebar, search, and the main Bluetooth content. If focus gets stuck, press **F6** to move between regions.
- **Turn Bluetooth On**: when the **Turn Bluetooth On** button is highlighted, press **Return**.
- **Select your mouse**: in the devices list, use **↑/↓**, press **Return** on **Connect** (or **Options** → **Connect**, depending on the UI).
- If pairing fails, turn the mouse **Off → On**, wait 5–10 seconds, and try **Connect** again.

### 4) Fast toggle via *Bluetooth File Exchange*
Sometimes the quickest way to bring back Bluetooth is to start **Bluetooth File Exchange**:

1. **⌘Space** → type **Bluetooth File Exchange** → **Return**.

2. If Bluetooth is Off, macOS shows **Turn Bluetooth On**, press **Return**.

3. Close the window; go back to **System Settings → Bluetooth** and connect.

### 5) Menu bar route (works when the status menu is responsive)
- Move focus to the **menu bar** with **^F2** (or **fn+^F2**).  Use **→** to reach the **Bluetooth** status item, **↓** to open it, and **Return** to toggle or connect.
- Note: in full‑screen apps or certain macOS builds, **^F2/^F8** behavior can be inconsistent. If it doesn’t respond, exit full screen (**Esc**) or use the **System Settings** method above.

### 6) Last‑resort: pair via a cable
- Plug the **Magic Mouse/Trackpad/Keyboard** into your Mac with its cable. With the device switched **On**, the Mac typically **pairs it automatically**. Unplug after a minute and use it wirelessly.
- Reminder: the Magic Mouse **cannot be used while charging**, this is by design. Quick top‑ups (a few minutes) usually give enough battery to finish pairing and reconnect.

---

## Troubleshooting

- **Tab won’t move between buttons/lists** → Toggle **^F7** (or **fn+^F7**) to enable **Full Keyboard Access** behavior for all controls.  
- **Menu bar shortcut not working** → Not in full screen? Try **^F3** (Dock) then **^F2** (menu bar), or return to the **System Settings** flow. Recheck the shortcut in **System Settings → Keyboard → Keyboard Shortcuts**.  
- **Bluetooth pane loads but nothing is clickable** → Press **F6** to jump regions, then **Tab**.  
- **Mouse doesn’t appear** → Switch mouse **Off → On**, bring it closer, or power‑cycle Bluetooth (**Turn Off** → **On**).  
- **Persistent issues** → Reboot Bluetooth via `sudo pkill bluetoothd` (advanced), or just **Restart** the Mac when convenient.

---

## Cheat sheet (print me)

- **Open Accessibility Shortcuts**: **⌥⌘F5**  
- **Toggle “Tab moves focus to all controls”**: **^F7** (use **fn** on laptops)  
- **Open Spotlight**: **⌘Space** → type → **Return**  
- **Focus menu bar**: **^F2** (or **fn+^F2**) → **↓** to open menus  
- **Move between UI regions**: **F6**  
- **Activate focused control**: **Return** (or **Space**)  
- **Open Bluetooth pane directly**: `open /System/Library/PreferencePanes/Bluetooth.prefPane`


---

**That’s it.** Whenever you’re stranded without a mouse: **⌥⌘F5**, **^F7**, **⌘Space → Bluetooth**, and **Return** your way back to a connected mouse.




