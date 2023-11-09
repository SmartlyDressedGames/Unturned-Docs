.. _doc_item_asset_intro:

Introduction to Items
=====================

Items in *Unturned* encompass anything that can be carried in a player's in-game inventory. All items will share certain properties, but each item type may have its own unique properties as well. Please refer to :ref:`Asset Definitions <doc_asset_definitions>` and :ref:`Asset Bundles <doc_asset_bundles>` for the full documentation regarding assets and asset bundles.

Unity Setup
-----------

.. figure:: /assets/img/UnityExampleItem.png
	
	An example of an item being set up in the Unity editor.

To get started, create a new folder for your custom item. The name of this folder will be relevant when further configuring your item after it has been exported from Unity.

Item (Prefab)
`````````````

Inside this folder, create a new Prefab named "Item". This should be tagged as 4: Item, and layered as 13: Item.

Open the "Item" Prefab, and attach a Box Collider component to the root GameObject. It should have a minimum dimension of (0.2, 0.2, 0.2).

If your item only has one LOD, you can attach Mesh Filter and Mesh Renderer components directly to the root GameObject. Configure these components as desired.

It is recommended to have multiple LODs for your item, so that less needs to be rendered when the item is far away. If your item should have multiple LODs, attach a LOD Group component to the root GameObject. Create a child GameObject for each LOD, named "Model_#" (e.g., "Model_0", "Model_1"). Attach the Mesh Filter and Mesh Renderer components to each one. Configure these components as desired.

Add a new child GameObject named "Icon" to the root GameObject. This will be used to draw an icon with an orthographic camera. To test the position of your icon, temporarily attach a Camera component with its Projection property set to "Orthographic". When satisfied with its position, delete the Camera component.

Animations (Prefab)
```````````````````

For equippable items, create a new Prefab in your custom item's folder named "Animations". This should be tagged as 0: Logic and layered as 8: Logic.

Add an Animation component to the root GameObject of the "Animations" Prefab. Every equippable item should have an animation named "Equip". If your weapon should be inspectable, it should also have an "Inspect" animation.

Equip (Audio Clip)
``````````````````

To have a sound play when the item is equipped, include an Audio Clip named "Equip" in your custom item's folder.

File Setup
----------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Arrest_End``, ``Arrest_Start``, ``Backpack``, ``Barrel``, ``Barricade``, ``Beacon``, ``Box``, ``Charge``, ``Cloud``, ``Compass``, ``Detonator``, ``Farm``, ``Filter``, ``Fisher``, ``Food``, ``Fuel``, ``Generator``, ``Glasses``, ``Grip``, ``Grower``, ``Gun``, ``Hat``, ``Key``, ``Library``, ``Magazine``, ``Map``, ``Mask``, ``Medical``, ``Melee``, ``Oil_Pump``, ``Optic``, ``Pants``, ``Refill``, ``Sentry``, ``Shirt``, ``Sight``, ``Storage``, ``Structure``, ``Supply``, ``Tactical``, ``Tank``, ``Throwable``, ``Tire``, ``Tool``, ``Trap``, ``Vehicle_Repair_Tool``, ``Vest``, ``Water``)

**Rarity** *enum* (``Common``, ``Uncommon``, ``Rare``, ``Epic``, ``Legendary``, ``Mythical``): Rarity of the item, as text shown in menus and colors used for highlights. Defaults to Common rarity.

**Useable** *enum*: Class for how to treat equippable items. Defaults to None.

**Slot** *enum* (``Any``, ``None``, ``Primary``, ``Secondary``, ``Tertiary``): Which equipped item slot the item is valid to be equippable in. Primary restricts the item to the primary slot, and prevents the use of hotkeying. Secondary restricts the item to the primary or secondary slots, and prevents the use of hotkeying. Any has no restrictions on slots or hotkeying. Defaults to None.

**ID** *uint16*: Must be a unique identifier.

Inventory Properties
````````````````````

**Size_X** *byte*: Width in inventory, in slots. Defaults to 1.

**Size_Y** *byte*: Height in inventory, in slots. Defaults to 1.

**Size_Z** *float*: Manually specify orthogonal camera size for item icons. This directly corresponds to the value of a Camera component's Size property in Unity. Defaults to -1.

**Use_Auto_Icon_Measurements** *bool*: Automatically calculate axis-aligned item icon camera size from bounds. Defaults to true.

**Can_Player_Equip** *bool*: Item can be equipped by the player. If the Useable property has been set, then defaults to true. Otherwise, defaults to false.

**Can_Use_Underwater** *bool*: Item can be used while underwater. If the Slot property has not been set to Primary, then defaults to true. Otherwise, defaults to false.

**Should_Drop_On_Death** *bool*: Item should be dropped on death. Defaults to true.

**Allow_Manual_Drop** *bool*: Item can be manually dropped by the player. Defaults to true.

**InspectAudioDef** :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`: AudioClip or OneShotAudioDefinition to play when item is inspected.

**InventoryAudio** :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`: AudioClip or OneShotAudioDefinition to play when item is picked up, moved within the inventory, and dropped. Default value is dependent on the child asset.

**Procedurally_Animate_Inertia** *bool*: Whether viewmodel should accumulate angular velocity from animations. Useful for low-quality older animations, but should probably be disabled for high-quality newer animations.

**Equipable_Movement_Speed_Multiplier** *float*: Multiplies character movement speed while equipped in hands (not while wearing). If a gun is equipped then any gun attachment multipliers are combined as well.

**EquipAudioClip** :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`: AudioClip to play when equipping.

Economy
```````

**Size2_Z** *float*: Orthogonal camera size for economy icons. Defaults to -1.

**Pro** *flag*: Specified if this is an economy item.

**Shared_Skin_Lookup_ID** *uint16*: Share skins with another item. Defaults to item ID.

Container
`````````

**Amount** *byte*: Maximum capacity for container-like items, such as ammunition boxes. Defaults to 1.

**Count_Min** *byte*: Minimum amount to generate, for container-like items. Defaults to 1.

**Count_Max** *byte*: Maximum amount to generate, for container-like items. Defaults to 1.

Quality
```````

**Quality_Min** *byte*: Minimum quality to generate. Defaults to 10.

**Quality_Max** *byte*: Maximum quality to generate. Defaults to 90.

**Should_Delete_At_Zero_Quality** *bool*: Item should be deleted when at 0% quality. Defaults to false.

**Override_Show_Quality** *bool*: Override to forcefully show item quality. Defaults to false.

Miscellaneous
`````````````

**Backward** *bool*: Set the item to be held in the non-dominant hand. Defaults to false.

**Bypass_Hash_Verification** *bool*: Disable hash verification check, and allow for mismatched files. Defaults to false.

**Destroy_Item_Colliders** *bool*: If false, colliders are not destroyed when the Item prefab is attached to the character. For example equipped vanilla guns do not have any colliders, but some mods (e.g., riot shields) may have relied on child colliders not being destroyed. Defaults to true.

**EquipablePrefab** :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`: Overrides the model spawned when this item is equipped. For example, the Equipable prefab could use an animated skinned mesh component while the regular Item prefab only needs a static mesh component.

**Ignore_TexRW** *flag*: Specified if read/writeable texture errors for the asset should be hidden from the error logs.

**Left_Handed_Characters_Mirror_Equipable** *bool*: If false, the equipped item model is mirrored to counteract the mirrored character. Defaults to true.

**Instantiated_Item_Name_Override** *string*: Name to use when instantiating item prefab. By default, the legacy 16-bit asset ID is used. Since Unity's built-in Animation component references GameObjects by name, this property can help share animations between items.

**Use_Auto_Stat_Descriptions** *bool*: If true, properties like damage, storage, health, etc. are appended to the description. Defaults to true.

Blueprints and Actions
``````````````````````

Items can have crafting blueprints and context menu actions. Refer to :ref:`Blueprints <doc_item_asset_blueprints>` and :ref:`Actions <doc_item_asset_actions>` for documentation.

Localization
------------

**Name** *string*: Item name in user interfaces.

**Description** :ref:`doc_data_richtext`: Item description in user interfaces.
