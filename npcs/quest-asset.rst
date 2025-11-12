.. _doc_npc_asset_quest:

Quest Assets
============

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Quest``)

**ID** *uint16*: Must be a unique identifier.

Conditions and Rewards
----------------------

Quests can be turned in when conditions are met, and players can receive rewards for turning quests in. For more information, refer to the documentation for :ref:`Conditions <doc_npc_asset_conditions>` and :ref:`Rewards <doc_npc_asset_rewards>` respectively.

Quests have two types of rewards lists:

1. ``Rewards`` are granted when the quest is completed.
2. ``AbandonmentRewards`` are granted when the quest is removed without completing it. These are not granted when the player finishes the quest normally.

Localization
------------

**Name** *string*: Quest name in user interfaces.

**Description** :ref:`doc_data_richtext`: Quest description in user interfaces.
