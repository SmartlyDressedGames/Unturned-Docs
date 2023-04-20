.. _doc_item_asset_barricade:

Barricade Assets
================

Barricades can be placed by players.

This inherits the :ref:`PlaceableAsset <doc_item_asset_placeable>` class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Barricade``): When intending to use a child class, refer to that class's documentation instead for the proper enumerator to use.

**Useable** *enum* (``Barricade``)

**Build** *enum* (``Barrel_Rain``, ``Barricade``, ``Beacon``, ``Bed``, ``Cage``, ``Campfire``, ``Charge``, ``Claim``, ``Clock``, ``Door``, ``Farm``, ``Fortification``, ``Freeform``, ``Gate``, ``Generator``, ``Glass``, ``Hatch``, ``Ladder``, ``Library``, ``Mannequin``, ``Note``, ``Oil``, ``Oven``, ``Oxygenator``, ``Safezone``, ``Sentry_Freeform``, ``Sentry``, ``Shutter``, ``Sign_Wall``, ``Sign``, ``Spike``, ``Spot``, ``Stereo``, ``Storage_Wall``, ``Storage``, ``Tank``, ``Torch``, ``Vehicle``, ``Wire``): Some values may not function properly without using a child class instead. When intending to use a child class, refer to that class's documentation instead for the proper enumerator to use.

**ID** *uint16*: Must be a unique identifier.

**InventoryAudio** :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`: See :ref:`ItemAsset <doc_item_asset_intro>` for full documentation. Defaults to ``Sounds/Inventory/Seeds.asset`` if the name contains the word "Seed", to ``Sounds/Inventory/SmallMetal.asset`` if the name contains the word "Metal", to ``Sounds/Inventory/LightMetalEquipment.asset`` if either ``Size_X`` or ``Size_Y`` value is equal to 1, to ``Sounds/Inventory/MediumMetalEquipment.asset`` if either ``Size_X`` or ``Size_Y`` value is less than or equal to 2, or ``Sounds/Inventory/HeavyMetalEquipment.asset`` if none of the criteria is met.

Barricade Asset Properties
--------------------------

**Allow_Collision_While_Animating** *bool*: Whether or not animated interactables should have collision during their animation. If true, animated colliders are enabled while playing the animation even when a player is overlapping. Be wary when enabling this, as it can allow for physics-based exploits such as those involving doors. Defaults to false.

**Allow_Placement_Inside_Clip_Volumes** *bool*: If true, the barricade can be placed inside of player clip volumes. Defaults to false, except when using ``Build Charge``.

**Allow_Placement_On_Vehicle** *bool*: If true, this barricade can be placed on vehicles. Defaults to true, except when using ``Build Bed``, ``Build Sentry``, or ``Build Sentry_Freeform``.

**Armor_Tier** *enum* (``Low``, ``High``): Barricade armor can either be low-tier or high-tier. Defaults to low-tier, except when the barricade's name contains the word "Metal". By default, barricades with low-tier armor take 100% of the damage they receive, while barricades with high-tier armor take 50% of the damage they receive. These multipliers can be configured in the `gameplay config <https://wiki.smartlydressedgames.com/wiki/Gameplay_config>`_.

**Bypass_Claim** *flag*: Can be placed inside someone else's claimed area.

**Bypass_Pickup_Ownership** *bool*: If true, non-owners of the placed barricade can pick it up. Defaults to false, except when using ``Build Charge``.

**Can_Be_Damaged** *bool*: If true, this barricade can be damaged. Defaults to true.

**Eligible_For_Pooling** *bool*: If true, this barricade is eligible for object pooling. Some barricades may not reset properly when pooling is enabled. Defaults to true, except when using ``Build Beacon``.

**Explosion** :ref:`GUID <doc_data_guid>` or *uint16*: GUID or legacy ID of :ref:`EffectAsset <doc_assets_effect>` to play when destroyed. When using ``Build Vehicle``, this is instead the GUID or legacy ID of the vehicle that should be spawned.

**Has_Clip_Prefab** *bool*: Whether or not the barricade has a Clip.prefab. If the barricade should use the same prefab on the server as on the client, set to false. For example, most official content uses ``Has_Clip_Prefab false``. Defaults to true.

**Health** *uint16*: Total health value. Defaults to 0.

**Locked** *flag*: Only the placed barricade's owner(s) can interact with it.

**Offset** *float*: In meters, the distance above the ground the barricade is placed.

**PlacementAudioClip** :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`: AudioClip to play when the barricade is placed.

**Proof_Explosion** *flag*: Immune to area-of-effect explosive damage.

**Radius** *float*: In meters, the radius around the barricade the must be clear in order for it to be placeable.

**Range** *float*: In meters, the maximum distance away the barricade can be placed from the player.

**Salvage_Duration_Multiplier** *float*: Multiplier on how long it takes to salvage this barricade. Setting this to a larger number will cause salvaging to take longer. Defaults to 1.

**Unpickupable** *flag*: Disables the ability to pick up a placed barricade. For example, the `Horde Beacon <https://wiki.smartlydressedgames.com/wiki/Horde_Beacon>`_ uses this flag.

**Unrepairable** *flag*: Cannot be repaired by a MeleeAsset with the "Repair" flag. For example, the `Blowtorch <https://wiki.smartlydressedgames.com/wiki/Blowtorch>`_ would not be able to repair this barricade.

**Unsalvageable** *flag*: Salvaging a damaged barricade yields no partial resources. For example, `small glass plates <https://wiki.smartlydressedgames.com/wiki/Small_Glass_Plate>`_ use this flag.

**Unsaveable** *flag*: This barricade is excluded from being saved. For example, carepackages use this flag.

**Use_Water_Height_Transparent_Sort** *flag*: Useful for transparent barricades, such as glass.

**Vulnerable** *flag*: The barricade can be damaged by lower-power weapons that do not have the ``Invulnerable`` flag.
