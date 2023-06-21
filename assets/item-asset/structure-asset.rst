.. _doc_item_asset_structure:

Structure Assets
================

Structures can be placed by players. Some structure pieces require another structure piece in order to be placed.

This inherits the :ref:`PlaceableAsset <doc_item_asset_placeable>` class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Structure``): When intending to use a child class, refer to that class's documentation instead for the proper enumerator to use.

**Useable** *enum* (``Structure``)

**Construct** *enum* (``Floor``, ``Floor_Poly``, ``Pillar``, ``Post``, ``Rampart``, ``Roof``, ``Roof_Poly``, ``Wall``): Determines how this structure can be placed, and how other structure pieces can snap to it.

**ID** *uint16*: Must be a unique identifier.

**InventoryAudio** :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`: See :ref:`ItemAsset <doc_item_asset_intro>` for full documentation. Defaults to ``Sounds/Inventory/SmallMetal.asset`` if the name contains the word "Metal", to ``Sounds/Inventory/LightMetalEquipment.asset`` if either ``Size_X`` or ``Size_Y`` value is equal to 1, to ``Sounds/Inventory/MediumMetalEquipment.asset`` if either ``Size_X`` or ``Size_Y`` value is less than or equal to 2, or ``Sounds/Inventory/HeavyMetalEquipment.asset`` if none of the criteria is met.

Structure Asset Properties
--------------------------

**Armor_Tier** *enum* (``Low``, ``High``): Armor is a multiplier on damage received. A structure's armor tier can either be low-tier or high-tier. By default, structures with low-tier armor take 100% of the damage they receive, while structures with high-tier armor take 50% of the damage they receive. These multipliers can be configured in the `gameplay config <https://wiki.smartlydressedgames.com/wiki/Gameplay_config>`_. Defaults to low-tier, except when the structure's name contains the word "Metal" or "Brick".

**Can_Be_Damaged** *bool*: If true, this structure can be damaged. Defaults to true.

**Eligible_For_Pooling** *bool*: If true, this structure is eligible for object pooling. Some structures may not reset properly when pooling is enabled. Defaults to true.

**Explosion** :ref:`GUID <doc_data_guid>` or *uint16*: GUID or legacy ID of :ref:`EffectAsset <doc_assets_effect>` to play when destroyed.

**Foliage_Cut_Radius** *float*: In meters, the radius around the structure where foliage is removed. Defaults to 6.

**Has_Clip_Prefab** *bool*: Whether or not the structure has a Clip.prefab. If the structure should use the same prefab on the server as on the client, set to false. For example, most official content uses ``Has_Clip_Prefab false``. Defaults to true.

**Health** *uint16*: Total health value. Defaults to 0.

**PlacementAudioClip** :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`: AudioClip to play when the structure is placed.

**PlacementPreviewPrefab** :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`: Overrides the placement preview model spawned when this item is held.

**Proof_Explosion** *flag*: Immune to area-of-effect explosive damage.

**Range** *float*: In meters, the maximum distance away the structure can be placed from the player.

**Salvage_Duration_Multiplier** *float*: Multiplier on how long it takes to salvage this structure. Setting this to a larger number will cause salvaging to take longer. Defaults to 1.

**Terrain_Test_Height** *float*: Length of the raycast downward from the pivot to check if the floor is above terrain. This is the maximum distance a floor can be placed above terrain, in meters. Defaults to 10.

**Unpickupable** *flag*: Disables the ability to pick up a placed structure.

**Unrepairable** *flag*: Cannot be repaired by a :ref:`MeleeAsset <doc_item_asset_melee>` with the ``Repair`` flag. For example, the `Blowtorch <https://wiki.smartlydressedgames.com/wiki/Blowtorch>`_ would not be able to repair this structure.

**Unsalvageable** *flag*: Salvaging a damaged structure yields no partial resources.

**Unsaveable** *flag*: This structure is excluded from being saved.

**Vulnerable** *flag*: The structure can be damaged by lower-power weapons that do not have the ``Invulnerable`` flag.

**Requires_Pillars** *bool*: Whether or not a valid wall placement requires pillars. If true, two pillars are required for a valid placement. Defaults to true.