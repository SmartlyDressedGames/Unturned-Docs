.. _doc_glazier:

Glazier
=======

Unity (the game engine Unturned runs on) has three different incompatible UI systems, each with different bugs:

1. IMGUI
2. uGUI
3. UIToolkit

Unturned has a feature nicknamed **Glazier** which abstracts the underlying UI system, allowing IMGUI, uGUI, or UIToolkit to be used.

uGUI is Unity's current recommended UI system, but unfortunately some players run into visual artifacts and flickering UI with it. In those cases enabling IMGUI is recommended.

IMGUI
-----

You can opt to use Unity's legacy UI system, IMGUI, by enabling a command-line argument:

1. Right-click Unturned in your Steam library
2. Click "Properties..."
3. Click "Select Launch Options..."
4. Add "-Glazier=IMGUI" without quotes

**Pros:**

- Faster on some systems because it has less overhead (no layout, no gameobjects).

**Cons:**

- Certain features like multi-line chat, extended item descriptions, and the main menu news feed are not supported in IMGUI mode.
- Visual bugs (e.g. incorrect gamma) and input issues on both Mac and Linux.
- Slower on some systems due to increased garbage collection.
- Does not support layered interactive UI. Some menus like crafting and inventory selection use workarounds for this, and thus behave differently from their uGUI counterparts.
- Plugin UIs are sorted underneath the game UI i.e. plugin UI cannot overlay.
- Rich text does not fade out in chat.

uGUI
----

This is Unturned's current default UI system, so opting in is not necessary.

**Pros:**

- Faster on some systems because the UI is not rebuilt every frame.
- More user-friendly e.g. can drag items outside the inventory to drop them.
- Looks better e.g. nicer scaling on high DPI monitors, foreground color universally supported.
- Rich text fades out properly in chat.

**Cons:**

- Visual artifacts and flickering on some systems.
- Slower on some systems because it has more overhead (layout, gameobjects).

UIToolkit
----------

Integration into Unturned is experimental. It's not ready to be the default yet. You can check it out with a command-line argument:

1. Right-click Unturned in your Steam library
2. Click "Properties..."
3. Click "Select Launch Options..."
4. Add "-Glazier=UIToolkit" without quotes

**Cons:**

- Scroll views have incorrect content size (for now). With IMGUI and uGUI it was possible to explicitly specify the content size, whereas UIToolkit tries to automatically calculate it from the content bounds. Unfortunately, many of Unturned's scroll views have content clipping outside the intended content area, and so they don't appear correctly. For example, the location labels on the map can intersect the content border.
- Text shadows and outlines are not as nice as with uGUI.
