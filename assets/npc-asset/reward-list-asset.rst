.. _doc_npc_asset_reward_list:

Rewards List Assets
===================

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``RewardList``)

The `Rewards_List_Asset` NPC reward type can either grant a rewards list asset directly, or a :ref:`Spawn Table Asset <doc_assets_spawn>` which resolves to the final asset. This could be used, for example, to randomly select one of several rewards list assets which then grants the player a gun along with related ammo items.

A `Rewards List Volume` placed in the level editor can also reference a rewards list asset, and will grant the rewards if the conditions are met when a player enters the volume.

Conditions must be met to grant the rewards. For more information, refer to the documentation for :ref:`Conditions <doc_npc_asset_conditions>` and :ref:`Rewards <doc_npc_asset_rewards>` respectively.
