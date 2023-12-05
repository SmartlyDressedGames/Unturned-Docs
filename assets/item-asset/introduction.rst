.. _doc_item_asset_intro:

Introduction to Items
=====================

Items in *Unturned* encompass anything that can be carried in a player's in-game inventory. All items will share certain properties, but each item type may have its own unique properties as well. Please refer to :ref:`Asset Definitions <doc_asset_definitions>` and :ref:`Asset Bundles <doc_asset_bundles>` for the full documentation regarding assets and asset bundles.

Unity Asset Bundle Contents
---------------------------

.. figure:: /assets/img/UnityExampleItem.png
	
	An example of an item being set up in the Unity editor.

To get started, create a new folder for your custom item. The name of this folder will be relevant when further configuring your item after it has been exported from Unity.

Item (Prefab)
`````````````

Inside this folder, create a new Prefab named "Item". This should be tagged as 4: Item, and layered as 13: Item. Open the "Item" Prefab.

Items can have multiple colliders including different types, but just attaching a Box Collider component to the root GameObject will usually suffice. It is recommended to use a minimum dimension of (0.2, 0.2, 0.2), because the large colliders are less likely to fall through a thin surface in a single physics tick.

If your item only has one LOD, you can attach Mesh Filter and Mesh Renderer components directly to the root GameObject. Configure these components as desired.

It is recommended to have multiple LODs for your item, so that less needs to be rendered when the item is far away. If your item should have multiple LODs, attach a LOD Group component to the root GameObject. Create a child GameObject for each LOD, named "Model_#" (e.g., "Model_0", "Model_1"). Attach the Mesh Filter and Mesh Renderer components to each one. Configure these components as desired.

Add a new child GameObject named "Icon" to the root GameObject. This will be used to draw an icon with an orthographic camera. By default, the game will automatically calculate the position and size of the camera – so the only thing that needs to be configured is its orientation. To test the orientation of your icon, temporarily attach a Camera component with its Projection property set to "Orthographic". When satisified, delete the Camera component.

Animations (Prefab)
```````````````````

For equippable items, a Prefab named "Animations" is required. The Prefab and the animations included can either be created from scratch, or they can be duplicated from the provided Unity packages.

If you have installed the ExampleAssets.unitypackage we provide, you can find the vanilla animations for most item types in the game. Prefabs can be found along the ``CoreMasterBundle/Items`` path, while the raw animation files can be found along ``Game/Sources/Animations``.

To create the Prefab from scratch instead, add a new Prefab named "Animations" in your custom item's folder. Add an Animation component to the root GameObject of the "Animations" Prefab.

Every equippable item should have an animation named "Equip". If your weapon should be inspectable, it should also have an "Inspect" animation.

Equip (Audio Clip)
``````````````````

To have a sound play when the item is equipped, include an Audio Clip named "Equip" in your custom item's folder.

Game Data File
--------------

Most item assets will *always* want to use the ``GUID``, ``Type``, ``Rarity``, ``Useable``, ``Slot``, ``ID``, ``Size_X``, and ``Size_Y`` properties, with only a few exceptions.

Properties
``````````

.. list-table::
   :widths: 40 40 20
   :header-rows: 1
   
   * - Property Name
     - Type
     - Default Value
   * - **Allow_Manual_Drop**
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - **Amount**
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``1``
   * - **Backward**
     - :ref:`bool <doc_data_builtin_types>`
     - ``false``
   * - **Bypass_Hash_Verification**
     - :ref:`bool <doc_data_builtin_types>`
     - ``false``
   * - **Can_Player_Equip**
     - :ref:`bool <doc_data_builtin_types>`
     - See description
   * - **Can_Use_Underwater**
     - :ref:`bool <doc_data_builtin_types>`
     - See description
   * - **Count_Max**
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``1``
   * - **Count_Min**
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``1``
   * - **Destroy_Item_Colliders**
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - **Equipable_Movement_Speed_Multiplier**
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1``
   * - **EquipablePrefab**
     - :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`
     - 
   * - **EquipAudioClip**
     - :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`
     - ``Equip``
   * - **GUID**
     - :ref:`doc_data_guid`
     - 
   * - **ID**
     - :ref:`uint16 <doc_data_builtin_types>`
     - ``0``
   * - **Ignore_TexRW**
     - :ref:`flag <doc_data_flag>`
     - 
   * - **InspectAudioDef**
     - :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`
     - 
   * - **Instantiated_Item_Name_Override**
     - :ref:`string <doc_data_builtin_types>`
     - See description
   * - **InventoryAudio**
     - :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`
     - See description
   * - **Left_Handed_Characters_Mirror_Equipable**
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - **Override_Show_Quality**
     - :ref:`bool <doc_data_builtin_types>`
     - ``false``
   * - **Pro**
     - :ref:`flag <doc_data_flag>`
     - 
   * - **Procedurally_Animate_Inertia**
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - **Quality_Max**
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``90``
   * - **Quality_Min**
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``10``
   * - **Rarity**
     - :ref:`doc_data_eitemrarity`
     - ``Common``
   * - **Shared_Skin_Lookup_ID**
     - :ref:`uint16 <doc_data_builtin_types>`
     - See description
   * - **Should_Delete_At_Zero_Quality**
     - :ref:`bool <doc_data_builtin_types>`
     - ``false``
   * - **Should_Drop_On_Death**
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - **Size_X**
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``1``
   * - **Size_Y**
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``1``
   * - **Size_Z**
     - :ref:`float32 <doc_data_builtin_types>`
     - ``-1``
   * - **Size2_Z**
     - :ref:`float32 <doc_data_builtin_types>`
     - ``-1``
   * - **Slot**
     - :ref:`doc_data_eslottype`
     - ``None``
   * - **Type**
     - :ref:`doc_data_eitemtype`
     - 
   * - **Use_Auto_Icon_Measurements**
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - **Use_Auto_Stat_Descriptions**
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - **Useable**
     - :ref:`EUseableType <doc_item_asset_intro:euseabletype>`
     - ``None``

.. _doc_item_asset_intro:euseabletype:

EUseableType Enumeration
````````````````````````

.. list-table::
   :widths: 25 75
   :header-rows: 1
   
   * - Named Value
     - Description
   * - ``None``
     - Does not correspond to any useable type.
   * - ``Clothing``
     - Corresponds to the "Clothing" useable type.
   * - ``Gun``
     - Corresponds to the "Gun" useable type.
   * - ``Consumeable``
     - Corresponds to the "Consumeable" useable type.
   * - ``Melee``
     - Corresponds to the "Melee" useable type.
   * - ``Fuel``
     - Corresponds to the "Fuel" useable type.
   * - ``Carjack``
     - Corresponds to the "Carjack" useable type.
   * - ``Barricade``
     - Corresponds to the "Barricade" useable type.
   * - ``Structure``
     - Corresponds to the "Structure" useable type.
   * - ``Throwable``
     - Corresponds to the "Throwable" useable type.
   * - ``Grower``
     - Corresponds to the "Grower" useable type.
   * - ``Optic``
     - Corresponds to the "Optic" useable type.
   * - ``Refill``
     - Corresponds to the "Refill" useable type.
   * - ``Fisher``
     - Corresponds to the "Fisher" useable type.
   * - ``Cloud``
     - Corresponds to the "Cloud" useable type.
   * - ``Arrest_Start``
     - Corresponds to the "Arrest_Start" useable type.
   * - ``Arrest_End``
     - Corresponds to the "Arrest_End" useable type.
   * - ``Detonator``
     - Corresponds to the "Detonator" useable type.
   * - ``Filter``
     - Corresponds to the "Filter" useable type.
   * - ``Carlockpick``
     - Corresponds to the "Carlockpick" useable type.

Property Descriptions
`````````````````````

GUID :ref:`doc_data_guid`
:::::::::::::::::::::::::

Refer to :ref:`GUID <doc_data_guid>` documentation.

----

Type :ref:`doc_data_eitemtype`
::::::::::::::::::::::::::::::

Designates the item's class.

----

Rarity :ref:`doc_data_eitemrarity` ``Common``
:::::::::::::::::::::::::::::::::::::::::::::

Rarity of the item, as text shown in menus and colors used for highlights.

----

Useable :ref:`doc_item_asset_intro:euseabletype` ``None``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Class for how to treat equippable items.

Slot :ref:`doc_data_eslottype` ``None``
:::::::::::::::::::::::::::::::::::::::

Which equipped item slot the item is valid to be equippable in. ``Primary`` restricts the item to the primary slot, and prevents the use of hotkeying. ``Secondary`` restricts the item to the primary or secondary slots, and prevents the use of hotkeying. ``Any`` has no restrictions on slots or hotkeying.

----

ID :ref:`uint16 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::

Must be a unique identifier.

----

Size_X :ref:`uint8 <doc_data_builtin_types>` ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Width in inventory, in slots.

----

Size_Y :ref:`uint8 <doc_data_builtin_types>` ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::

Height in inventory, in slots.

----

Size_Z :ref:`float32 <doc_data_builtin_types>` ``-1``
:::::::::::::::::::::::::::::::::::::::::::::::::::::

Manually specify orthogonal camera size for item icons. This directly corresponds to the value of a Camera component's Size property in Unity.

----

Use_Auto_Icon_Measurements :ref:`bool <doc_data_builtin_types>` ``true``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Automatically calculate axis-aligned item icon camera size from bounds.

----

Can_Player_Equip :ref:`bool <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::

Item can be equipped by the player. If the ``Useable`` property has been set, then defaults to ``true``. Otherwise, defaults to ``false``.

----

Can_Use_Underwater :ref:`bool <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::

Item can be used while underwater. If the ``Slot`` property has not been set to ``Primary``, then defaults to ``true``. Otherwise, defaults to ``false``.

----

Should_Drop_On_Death :ref:`bool <doc_data_builtin_types>` ``true``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Item should be dropped on death.

----

Allow_Manual_Drop :ref:`bool <doc_data_builtin_types>` ``true``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Item can be manually dropped by the player.

----

InspectAudioDef :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

AudioClip or OneShotAudioDefinition to play when item is inspected.

----

InventoryAudio :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

AudioClip or OneShotAudioDefinition to play when item is picked up, moved within the inventory, and dropped. Default value is dependent on the child asset.

----

Procedurally_Animate_Inertia :ref:`bool <doc_data_builtin_types>` ``true``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Whether viewmodel should accumulate angular velocity from animations. Useful for low-quality older animations, but should probably be disabled for high-quality newer animations.

----

Equipable_Movement_Speed_Multiplier :ref:`float32 <doc_data_builtin_types>` ``1``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplies character movement speed while equipped in the player's hands. If a gun is equipped, then any gun attachment multipliers are combined as well.

----

EquipAudioClip :ref:`Master Bundle Pointer <doc_data_masterbundleptr>` ``Equip``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
AudioClip to play when equipping.

**Size2_Z** :ref:`float32 <doc_data_builtin_types>` ``-1``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Orthogonal camera size for economy icons.

----

**Pro** :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::::

Specified if this is an economy item.

----

**Shared_Skin_Lookup_ID** :ref:`uint16 <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Share skins with another item. Defaults to item's ``ID``.

----

**Amount** :ref:`uint8 <doc_data_builtin_types>` ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::::::

Maximum capacity for container-like items, such as ammunition boxes.

----

**Count_Min** :ref:`uint8 <doc_data_builtin_types>` ``1``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Minimum amount to generate, for container-like items.

----

**Count_Max** :ref:`uint8 <doc_data_builtin_types>` ``1``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Maximum amount to generate, for container-like items.

----

**Quality_Min** :ref:`uint8 <doc_data_builtin_types>` ``10``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Minimum quality to generate.

----

**Quality_Max** :ref:`uint8 <doc_data_builtin_types>` ``90``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Maximum quality to generate.

----

**Should_Delete_At_Zero_Quality** :ref:`bool <doc_data_builtin_types>` ``false``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Item should be deleted when at 0% quality.

----

**Override_Show_Quality** :ref:`bool <doc_data_builtin_types>` ``false``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Override to forcefully show item quality.

----

**Backward** :ref:`bool <doc_data_builtin_types>` ``false``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Set the item to be held in the non-dominant hand.

----

**Bypass_Hash_Verification** :ref:`bool <doc_data_builtin_types>` ``false``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Disable hash verification check, and allow for mismatched files.

----

**Destroy_Item_Colliders** :ref:`bool <doc_data_builtin_types>` ``true``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If false, colliders are not destroyed when the "Item" Prefab is attached to the character. For example equipped vanilla guns do not have any colliders, but some mods (e.g., riot shields) may have relied on child colliders not being destroyed.

----

**EquipablePrefab** :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Overrides the model spawned when this item is equipped. For example, the "Equipable" Prefab could use an animated skinned mesh component while the regular "Item" Prefab only needs a static mesh component.

----

**Ignore_TexRW** :ref:`flag <doc_data_flag>`
::::::::::::::::::::::::::::::::::::::::::::

Specified if read/writeable texture errors for the asset should be hidden from the error logs.

----

**Left_Handed_Characters_Mirror_Equipable** :ref:`bool <doc_data_builtin_types>` ``true``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If false, the equipped item model is mirrored to counteract the mirrored character.

----

**Instantiated_Item_Name_Override** :ref:`string <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Name to use when instantiating "Item" Prefab. By default, the legacy 16-bit asset ID is used. Since Unity's built-in Animation component references GameObjects by name, this property can help share animations between items.

----

**Use_Auto_Stat_Descriptions** :ref:`bool <doc_data_builtin_types>` ``true``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If true, properties like damage, storage, health, etc. are appended to the description.

Blueprints and Actions
``````````````````````

Items can have crafting blueprints and context menu actions. Refer to :ref:`Blueprints <doc_item_asset_blueprints>` and :ref:`Actions <doc_item_asset_actions>` for documentation.