.. _doc_item_asset_intro:

Introduction to Items
=====================

Please refer to :ref:`Asset Definitions <doc_asset_definitions>` and :ref:`Asset Bundles <doc_asset_bundles>` for the full documentation regarding assets and asset bundles.

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Arrest_End``, ``Arrest_Start``, ``Backpack``, ``Barrel``, ``Barricade``, ``Beacon``, ``Box``, ``Charge``, ``Cloud``, ``Compass``, ``Detonator``, ``Farm``, ``Filter``, ``Fisher``, ``Food``, ``Fuel``, ``Generator``, ``Glasses``, ``Grip``, ``Grower``, ``Gun``, ``Hat``, ``Key``, ``Library``, ``Magazine``, ``Map``, ``Mask``, ``Medical``, ``Melee``, ``Oil_Pump``, ``Optic``, ``Pants``, ``Refill``, ``Sentry``, ``Shirt``, ``Sight``, ``Storage``, ``Structure``, ``Supply``, ``Tactical``, ``Tank``, ``Throwable``, ``Tire``, ``Tool``, ``Trap``, ``Vehicle_Repair_Tool``, ``Vest``, ``Water``)

**Rarity** *enum* (``Common``, ``Uncommon``, ``Rare``, ``Epic``, ``Legendary``, ``Mythical``): Rarity of the item, as text shown in menus and colors used for highlights. Defaults to Common rarity.

**Useable** *enum*: Class for how to treat equippable items. Defaults to None.

**Slot** *enum* (``Any``, ``None``, ``Primary``, ``Secondary``, ``Tertiary``): Which equipped item slot the item is valid to be equippable in. Primary restricts the item to the primary slot, and prevents the use of hotkeying. Secondary restricts the item to the primary or secondary slots, and prevents the use of hotkeying. Any has no restrictions on slots or hotkeying. Defaults to None.

**ID** *uint16*: Must be a unique identifier.

Inventory Properties
--------------------

**Size_X** *byte*: Width in inventory, in slots. Defaults to 1.

**Size_Y** *byte*: Height in inventory, in slots. Defaults to 1.

**Size_Z** *float*: Orthogonal camera size for item icons. Defaults to -1.

**Use\_Auto\_Icon\_Measurements** *bool*: Automatically calculate axis-aligned item icon camera size from bounds. Defaults to true.

**Can\_Player\_Equip** *bool*: Item can be equipped by the player. If the Useable property has been set, then defaults to true. Otherwise, defaults to false.

**Can\_Use\_Underwater** *bool*: Item can be used while underwater. If the Slot property has not been set to Primary, then defaults to true. Otherwise, defaults to false.

**Should\_Drop\_On\_Death** *bool*: Item should be dropped on death. Defaults to true.

**Allow\_Manual\_Drop** *bool*: Item can be manually dropped by the player. Defaults to true.

**InventoryAudio** :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`: AudioClip or OneShotAudioDefinition to play when item is picked up, moved within the inventory, and dropped. Default value is dependent on the child asset.

**Procedurally\_Animate\_Inertia** *bool*: Whether viewmodel should accumulate angular velocity from animations. Useful for low-quality older animations, but should probably be disabled for high-quality newer animations.

**Equipable\_Movement\_Speed\_Multiplier** *float*: Multiplies character movement speed while equipped in hands (not while wearing). If a gun is equipped then any gun attachment multipliers are combined as well.

Economy Properties
------------------

**Size2_Z** *float*: Orthogonal camera size for economy icons. Defaults to -1.

**Pro** *flag*: Specified if this is an economy item.

**Shared\_Skin\_Lookup\_ID** *uint16*: Share skins with another item. Defaults to item ID.

Container Properties
--------------------

**Amount** *byte*: Maximum capacity for container-like items, such as ammunition boxes. Defaults to 1.

**Count_Min** *byte*: Minimum amount to generate, for container-like items. Defaults to 1.

**Count_Max** *byte*: Maximum amount to generate, for container-like items. Defaults to 1.

Quality Properties
------------------

**Quality_Min** *byte*: Minimum quality to generate. Defaults to 10.

**Quality_Max** *byte*: Maximum quality to generate. Defaults to 90.

**Should\_Delete\_At\_Zero\_Quality** *bool*: Item should be deleted when at 0% quality. Defaults to false.

**Override\_Show\_Quality** *bool*: Override to forcefully show item quality. Defaults to false.

Other Properties
----------------

**Backward** *bool*: Set the item to be held in the non-dominant hand. Defaults to false.

**Bypass\_Hash\_Verification** *bool*: Disable hash verification check, and allow for mismatched files. Defaults to false.

**EquipablePrefab** :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`: Overrides the model spawned when this item is equipped. For example the Equipable prefab could use an animated skinned mesh component while the regular Item prefab only needs a static mesh component.

**Ignore_TexRW** *flag*: Specified if read/writeable texture errors for the asset should be hidden from the error logs.

**Destroy_Item_Colliders** *bool*: If false, colliders are not destroyed when the Item prefab is attached to the character. For example equipped vanilla guns do not have any colliders, but some mods (e.g., riot shields) may have relied on child colliders not being destroyed. Defaults to true.

Blueprints and Actions
----------------------

Items can have crafting blueprints and context menu actions. Refer to :ref:`Blueprints <doc_item_asset_blueprints>` and :ref:`Actions <doc_item_asset_actions>` for documentation.

Localization
------------

**Name** *string*: Item name in user interfaces.

**Description** *string*: Item description in user interfaces.
