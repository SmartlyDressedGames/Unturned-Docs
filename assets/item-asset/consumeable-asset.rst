.. _doc_item_asset_consumeable:

Consumeable Assets
==================

Consumable items are irreversibly consumed by the player on use, and directly affect a player's stats such as food or health.

This inherits the :ref:`WeaponAsset <doc_item_asset_weapon>` class.

Consumeable Asset Properties
----------------------------

**Aid** *flag*: Specified if the item can be used on other players, via the "Secondary" action.

**Bleeding** *flag*: Specified if the item should remove the "Bleeding" status effect. Deprecated in favor of Bleeding_Modifier.

**Bleeding_Modifier** *enum* (``Cut``, ``Heal``, ``None``): Determines the effect the consumable has in relation to the "Bleeding" status effect.

**Broken** *flag*: Specified if the item should remove the "Broken Bones" status effect. Deprecated in favor of Bones_Modifier.

**Bones_Modifier** *enum* (``Break``, ``Heal``, ``None``): Determines the effect the consumable has in relation to the "Broken Bones" status effect.

**ConsumeAudioClip** :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`: AudioClip to play when the consumeable is used.

**Disinfectant** *byte*: Amount of immunity restored.

**Energy** *byte*: Amount of stamina restored.

**Experience** *int*: Amount of experience added or removed.

**Explosion** *uint16* or *GUID*: ID or GUID of the explosion effect to play upon consumption.

**Food** *byte*: Amount of food restored. If the amount of food to restore is larger than the amount of water to restore, then food constrains water.

**Health** *byte*: Amount of health restored.

**Item_Reward_Spawn_ID** *uint16*: ID of the item spawn table to generate an item from upon consuming the consumable. The number of items generated is random, depending on the range defined by Min_Item_Rewards and Max_Item_Rewards.

**Max_Item_Rewards** *int*: Maximum number of items that can be generated from the spawn table specified by Item_Reward_Spawn_ID.

**Min_Item_Rewards** *int*: Minimum number of items that can be generated from the spawn table specified by Item_Reward_Spawn_ID.

**Oxygen** *sbyte*: Amount of oxygen restored or depleted.

**Should_Delete_After_Use** *bool*: Boolean for if the item should be deleted after being consumed. Defaults to true.

**Virus** *byte*: Amount of immunity depleted.

**Vision** *uint*: Length of hallucinations, in seconds. The length does not stack when consuming multiple hallucinogenics. Instead, the timer is reset to the longer value.

**Warmth** *uint*: Amount of warmth added.

**Water** *byte*: Amount of water restored. If the amount of water to restore is less than the amount of food to restore, then water is constrained by food.

Rewards
-------

Consumables can use quest rewards. A common usage is to create consumables with multiple (but still limited) uses, by placing a new item in the player's inventory after consuming the original. Alternatively, consuming a consumable may be required to complete a quest. Refer to :ref:`Rewards <doc_npc_asset_rewards>` documentation for additional documentation.

These rewards are prefixed with ``Quest_``. For example, ``Quest_Rewards 1``.
