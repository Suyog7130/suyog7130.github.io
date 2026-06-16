---
author: "Suyog Garg"
title: "How to use backslash \ in JIS keyboard layout"
date: "2026-05-30"
tags:
    - mac
    - keyboard
    - terminal
---
<!--
# How to Fix the Annoying Mac Yen (¥) Key to Type a Backslash (\\) in Google Chrome-->

**Disclaimer:** Made with Google Gemini-Pro prompts

If you use a physical Japanese (JIS) hardware keyboard layout on a modern Mac, you have likely run into a frustrating quirk: even if you change your macOS text settings to output a backslash (`\`) instead of a Yen sign (`¥`), **Google Chrome, VS Code, and Slack will completely ignore your system settings.** 

While the macOS Terminal respects the software substitution, web browsers and electron apps read the raw hardware keycode (`0x5C`) directly from your Japanese keyboard, forcing the `¥` symbol onto your screen unless you hold down `Option + ¥`.

After battling with read-only folder permissions and silent file deletions on modern macOS, here is the definitive guide to fixing this at the layout level without installing heavy background remapping software.

---

## The Core Issue: Why System Settings Fail
When you change the setting under *System Settings > Keyboard > Input Sources > "¥" key generates*, macOS only applies this change as a text-substitution layer. 

Applications like Google Chrome bypass this layer. They look straight at your hardware layout configuration file. Because modern macOS locks down system folders with **System Integrity Protection (SIP)**, trying to manually drop custom keyboard layout files into `/Library/Keyboard Layouts/` will result in macOS silently deleting the file to protect system integrity.

---

## The Solution: A Custom User-Level Layout Bundle

To fix this permanently, we will create a modified keyboard layout using a free utility, and install it to the isolated User Library directory where macOS security policies allow it to run.

### Step 1: Create the Modified Layout in Ukelele
1. Download and install the free keyboard layout editor, [Ukelele](https://sil.org).
2. Open Ukelele and go to **File > New Based on Current Input Source**.
3. By default, Ukelele might show a standard US ANSI grid layout, making your hardware Yen key invisible. To fix this, go to the top Mac menu bar and select **View > Keyboard Type > JIS (Japanese)**.
4. The on-screen keyboard will refresh to match your hardware layout. Locate the `¥` key (usually next to the Backspace/Delete key).
5. Double-click the `¥` key inside the visual editor, type `\` (Backslash) into the field to replace it, and save the project as a **Keyboard Layout Bundle** (e.g., `ABC-JIS.bundle`).

### Step 2: Install the Layout Without Trimming File Permissions
Do **not** try to drag and drop the file manually into the root system folder, or macOS will instantly erase it. Instead, use the built-in macOS installer pipeline:

1. Double-click your saved `.bundle` file from your desktop or downloads folder.
2. A macOS system dialog box will pop up asking if you want to install it. 
3. Click **Install for current user**. 
4. macOS will automatically securely copy the bundle into your hidden user directory: `~/Library/Keyboard Layouts/`.

### Step 3: (Optional) Give Your Layout a Clean Name
By default, macOS might label your newly created input source as something generic like "ABC copy." To customize this:

1. Go to Finder, click **Go** in the top menu bar, hold down the **Option (⌥)** key, and click the hidden **Library** folder that appears.
2. Navigate to **Keyboard Layouts**, right-click your `.bundle` file, and select **Show Package Contents**.
3. Open **Contents > Resources > en.lproj** (or your primary language folder).
4. Open the `InfoPlist.strings` file with TextEdit.
5. Locate the string value showing `"ABC copy"` and change it to your preferred name (e.g., `"ABC-JIS+backslash"`).
6. Save and exit.

### Step 4: Activate and Reboot
1. Click the **Apple Logo > Restart...** to clear the macOS input method cache. A simple logout is not enough!
2. Once rebooted, open **System Settings > Keyboard**.
3. In the *Text Input* section, click **Edit...** next to *Input Sources*.
4. Click the **`+` (Plus)** button at the bottom left, scroll down to **Others**, select your custom layout name, and click **Add**.
5. Remove your old default layout by selecting it and clicking the **`-` (Minus)** button so your system doesn't toggle back to it by accident.

---

## The Verdict
Your Mac will now default to your custom hardware map. Because this fix sits right inside your user-level input sources, Google Chrome, VS Code, and every other stubborn application are forced to read the physical key press as a native backslash. No background apps, no performance lag, and no more holding down the Option key while programming!
