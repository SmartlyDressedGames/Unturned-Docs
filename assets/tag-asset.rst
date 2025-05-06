.. _doc_assets_tag:

Tag Assets
==========

Although **Tags** have some display properties, they primarily serve as a unique identifier—particularly useful for compatibility between mods.

**GUID** *32-digit hexadecimal*: Refer to :ref:`doc_data_guid` documentation.

**Type** ``Tag``

Tag Properties
--------------

**NameColor** :ref:`color <doc_data_color>`: Optional override for color of name label in the user interface.

**HasIcon** :ref:`bool <doc_data_builtin_types>`: If true, the game will expect an Icon texture in the asset bundle. Defaults to true.

**IconPath** :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`: Overrides where to load Icon texture from.

**TintIcon** :ref:`bool <doc_data_builtin_types>`: If true, tints the icon according to player's foreground color preference. Defaults to true. Tinted icons are typically white #ffffff to fully change color. If your icons are colorful you may want to set this to false.

Localization
------------

**Name** *string*: Display name in user interfaces.
