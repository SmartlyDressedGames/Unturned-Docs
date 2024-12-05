.. _doc_npc_asset_intro:

Introduction to NPCs
====================

Modders can create interactable NPC characters, with a customized appearance. A dialogue box can be made to appear to the player when interacted with, which can display potential responses that can chain into more dialogue options. Dialogue can lead to special interactions, such as quests or vendors. Additionally, NPC interactions can have a set of conditions that dictate what is available to the player, and rewards for performing various actions such as turning in a quest.

Localization
------------

There are additional text formatting features available for NPC localization files.

**\<color=*enum*\>\</color\>**: Use a rarity color as the font color. Valid rarities are: ``common``, ``uncommon``, ``rare``, ``epic``, ``legendary``, ``mythical``, ``gold``, ``red``, ``orange``, ``yellow``, ``green``, ``blue``, and ``purple``. Alternatively, specify a six-digit hexadecimal number representing RGB color.

**\<name_npc\>**: Insert the NPC character's name.

**\<name_char\>**: Insert the player character's name.

**\<br\>**: New line.

**\<pause\>**: Pause dialogue for 0.5 seconds before continuing.
