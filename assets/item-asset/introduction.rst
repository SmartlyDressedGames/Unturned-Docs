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

Skin Base Textures
``````````````````

.. note::

	We should eventually add more documentation about this, but items support texture masking. This is rarely relevant for modders creating their own items, but it is important for skins. Items can optionally include ``Albedo_Base.png``, ``Metallic_Base.png``, or ``Emission_Base.png`` textures in their asset-bundled files. When using certain skins, those parts will be masked out and retain their original material.

Game Data File
--------------

The ``GUID``, ``Type``, and ``ID`` properties are required by all item assets. Most item assets will *usually* want (or need) to include the ``Rarity``, ``Useable``, ``Slot``, ``Size_X``, and ``Size_Y`` properties as well, with only a few excepions.

Properties
``````````

.. list-table::
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`Add_Default_Actions <doc_item_asset_intro:add_default_actions>`
     - :ref:`bool <doc_data_builtin_types>`
     - See description
   * - :ref:`Allow_Manual_Drop <doc_item_asset_intro:allow_manual_drop>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - :ref:`Amount <doc_item_asset_intro:amount>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Backward <doc_item_asset_intro:equipablemodelparent>`
     - :ref:`flag <doc_data_flag>`
     - *deprecated*
   * - :ref:`Bypass_Hash_Verification <doc_item_asset_intro:bypass_hash_verification>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``false``
   * - :ref:`Bypass_ID_Limit <doc_item_asset_intro:bypass_id_limit>`
     - :ref:`flag <doc_data_flag>`
     -
   * - :ref:`Can_Player_Equip <doc_item_asset_intro:can_player_equip>`
     - :ref:`bool <doc_data_builtin_types>`
     - See description
   * - :ref:`Can_Use_Underwater <doc_item_asset_intro:can_use_underwater>`
     - :ref:`bool <doc_data_builtin_types>`
     - See description
   * - :ref:`Count_Max <doc_item_asset_intro:count_max>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Count_Min <doc_item_asset_intro:count_min>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Destroy_Item_Colliders <doc_item_asset_intro:destroy_item_colliders>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - :ref:`Equipable_Movement_Speed_Multiplier <doc_item_asset_intro:equipable_movement_speed_multiplier>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`EquipableModelParent <doc_item_asset_intro:equipablemodelparent>`
     - :ref:`EEquipableModelParent <doc_item_asset_intro:eequipablemodelparent>`
     - See description
   * - :ref:`EquipablePrefab <doc_item_asset_intro:equipableprefab>`
     - :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`
     -
   * - :ref:`EquipAudioClip <doc_item_asset_intro:equipaudioclip>`
     - :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`
     - ``Equip``
   * - :ref:`GUID <doc_item_asset_intro:guid>`
     - :ref:`doc_data_guid`
     -
   * - :ref:`ID <doc_item_asset_intro:id>`
     - :ref:`uint16 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Ignore_TexRW <doc_item_asset_intro:ignore_texrw>`
     - :ref:`flag <doc_data_flag>`
     -
   * - :ref:`InspectAudioDef <doc_item_asset_intro:inspectaudiodef>`
     - :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`
     -
   * - :ref:`Instantiated_Item_Name_Override <doc_item_asset_intro:instantiated_item_name_override>`
     - :ref:`string <doc_data_builtin_types>`
     - See description
   * - :ref:`InventoryAudio <doc_item_asset_intro:inventoryaudio>`
     - :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`
     - See description
   * - :ref:`Left_Handed_Characters_Mirror_Equipable <doc_item_asset_intro:left_handed_characters_mirror_equipable>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - :ref:`Override_Show_Quality <doc_item_asset_intro:override_show_quality>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``false``
   * - :ref:`Pro <doc_item_asset_intro:pro>`
     - :ref:`flag <doc_data_flag>`
     -
   * - :ref:`Procedurally_Animate_Inertia <doc_item_asset_intro:procedurally_animate_inertia>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - :ref:`Quality_Max <doc_item_asset_intro:quality_max>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``90``
   * - :ref:`Quality_Min <doc_item_asset_intro:quality_min>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``10``
   * - :ref:`Rarity <doc_item_asset_intro:rarity>`
     - :ref:`doc_data_eitemrarity`
     - ``Common``
   * - :ref:`Shared_Skin_Lookup_ID <doc_item_asset_intro:shared_skin_lookup_id>`
     - :ref:`uint16 <doc_data_builtin_types>`
     - See description
   * - :ref:`Shared_Skin_Apply_Visuals <doc_item_asset_intro:shared_skin_apply_visuals>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - :ref:`Should_Delete_At_Zero_Quality <doc_item_asset_intro:should_delete_at_zero_quality>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``false``
   * - :ref:`Should_Drop_On_Death <doc_item_asset_intro:should_drop_on_death>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - :ref:`Size_X <doc_item_asset_intro:size_x>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Size_Y <doc_item_asset_intro:size_y>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Size_Z <doc_item_asset_intro:size_z>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``-1``
   * - :ref:`Size2_Z <doc_item_asset_intro:size2_z>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``-1``
   * - :ref:`Slot <doc_item_asset_intro:slot>`
     - :ref:`doc_data_eslottype`
     - ``None``
   * - :ref:`Type <doc_item_asset_intro:type>`
     - :ref:`doc_data_eitemtype`
     -
   * - :ref:`Use_Auto_Icon_Measurements <doc_item_asset_intro:use_auto_icon_measurements>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - :ref:`Use_Auto_Stat_Descriptions <doc_item_asset_intro:use_auto_stat_descriptions>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - :ref:`Useable <doc_item_asset_intro:useable>`
     - :ref:`EUseableType <doc_item_asset_intro:euseabletype>`
     - ``None``

.. _doc_item_asset_intro:eequipablemodelparent:

EEquipableModelParent Enumeration
`````````````````````````````````

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Named Value
     - Description
   * - ``RightHook``
     - Item is attached to Right_Hook.
   * - ``LeftHook``
     - Item is attached to Left_Hook.
   * - ``Spine``
     - Item is attached to Spine.
   * - ``SpineHook``
     - Item is attached to Spine_Hook, an optional extra child bone of the Spine bone.

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

.. _doc_item_asset_intro:add_default_actions:

Add_Default_Actions :ref:`bool <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If true, actions are automatically created for refill ammo, repair, and salvage blueprints. Defaults to true if no ``Actions`` are specified.

----

.. _doc_item_asset_intro:allow_manual_drop:

Allow_Manual_Drop :ref:`bool <doc_data_builtin_types>` ``true``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Item can be manually dropped by the player.

----

.. _doc_item_asset_intro:amount:

Amount :ref:`uint8 <doc_data_builtin_types>` ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::

Maximum capacity for container-like items, such as ammunition boxes. Typically used with ``Count_Min`` and ``Count_Max``.

----

.. _doc_item_asset_intro:bypass_hash_verification:

Bypass_Hash_Verification :ref:`bool <doc_data_builtin_types>` ``false``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Disable hash verification check, and allow for mismatched files.

----

.. _doc_item_asset_intro:bypass_id_limit:

Bypass_ID_Limit :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::::::::::::

Allows for using an ``ID`` value within the range reserved for official content.

----

.. _doc_item_asset_intro:can_player_equip:

Can_Player_Equip :ref:`bool <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::

Controls whether or not this item can be equipped by the player. This property *technically* requires that ``Useable`` has been configured to any value other than ``None``, as items are not equippable without the functionality provided by having a Useable class.

While the inclusion of this property may seem unorthodox, it does have some niche uses. For example, you could create a gun that can only be used by sentries.

This property defaults to ``true`` if the ``Useable`` property has been set. Otherwise, this defaults to ``false``.

----

.. _doc_item_asset_intro:can_use_underwater:

Can_Use_Underwater :ref:`bool <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::

Item can be used while underwater. If the ``Slot`` property has *not* been set to ``Primary``, then this defaults to ``true``. Otherwise, this defaults to ``false``.

----

.. _doc_item_asset_intro:count_max:

Count_Min :ref:`uint8 <doc_data_builtin_types>` ``1``
:::::::::::::::::::::::::::::::::::::::::::::::::::::

Minimum amount to generate, for container-like items. Typically used with ``Count_Max`` and ``Amount``.

----

.. _doc_item_asset_intro:count_min:

Count_Max :ref:`uint8 <doc_data_builtin_types>` ``1``
:::::::::::::::::::::::::::::::::::::::::::::::::::::

Maximum amount to generate, for container-like items. Typically used with ``Count_Min`` and ``Amount``.

----

.. _doc_item_asset_intro:destroy_item_colliders:

Destroy_Item_Colliders :ref:`bool <doc_data_builtin_types>` ``true``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If ``false``, colliders are not destroyed when the "Item" Prefab is attached to the character. For example equipped vanilla guns do not have any colliders, but some mods (e.g., riot shields) may have relied on child colliders not being destroyed.

----

.. _doc_item_asset_intro:equipable_movement_speed_multiplier:

Equipable_Movement_Speed_Multiplier :ref:`float32 <doc_data_builtin_types>` ``1``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplies character movement speed while equipped in the player's hands. If a gun is equipped, then any gun attachment multipliers are combined as well.

----

.. _doc_item_asset_intro:equipablemodelparent:

EquipableModelParent :ref:`EEquipableModelParent <doc_item_asset_intro:eequipablemodelparent>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Overrides which transform to attach the item to when equipped by the player. Spine may be a better interpolation space for items with animations moving the model between hands.

Normally, this property defaults to ``RightHook``. However, items using the deprecated ``Backward`` flag will cause this to instead use ``LeftHook``.

----

.. _doc_item_asset_intro:equipableprefab:

EquipablePrefab :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Overrides the model spawned when this item is equipped. For example, the "Equipable" Prefab could use an animated skinned mesh component while the regular "Item" Prefab only needs a static mesh component.

----

.. _doc_item_asset_intro:equipaudioclip:

EquipAudioClip :ref:`Master Bundle Pointer <doc_data_masterbundleptr>` ``Equip``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

AudioClip to play when equipping.

----

.. _doc_item_asset_intro:guid:

GUID :ref:`doc_data_guid`
:::::::::::::::::::::::::

Refer to :ref:`GUID <doc_data_guid>` documentation. Item assets are required to have this property.

.. tip::

  If the GUID property has been omitted from the asset file, then the game will automatically attempt to assign a random (and unique) GUID during a successful load.

----

.. _doc_item_asset_intro:id:

ID :ref:`uint16 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::

Must be a unique identifier. Item assets are required to have this property.

----

.. _doc_item_asset_intro:ignore_texrw:

Ignore_TexRW :ref:`flag <doc_data_flag>`
::::::::::::::::::::::::::::::::::::::::

Read/writeable texture errors regarding this asset should be hidden from the error logs.

----

.. _doc_item_asset_intro:inspectaudiodef:

InspectAudioDef :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

AudioClip or OneShotAudioDefinition to play when item is inspected.

----

.. _doc_item_asset_intro:instantiated_item_name_override:

Instantiated_Item_Name_Override :ref:`string <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Name to use when instantiating "Item" Prefab. By default, the value of ``ID`` is used. Since Unity's built-in Animation component references GameObjects by name, this property can help share animations between items.

----

.. _doc_item_asset_intro:inventoryaudio:

InventoryAudio :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

AudioClip or OneShotAudioDefinition to play when item is picked up, moved within the inventory, and dropped. Default value is dependent on the child asset.

----

.. _doc_item_asset_intro:left_handed_characters_mirror_equipable:

Left_Handed_Characters_Mirror_Equipable :ref:`bool <doc_data_builtin_types>` ``true``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If ``false``, the equipped item model is mirrored to counteract the mirrored character.

----

.. _doc_item_asset_intro:override_show_quality:


Override_Show_Quality :ref:`bool <doc_data_builtin_types>` ``false``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Override to forcefully show item quality.

----

.. _doc_item_asset_intro:pro:

Pro :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::

This is a Steam Economy item.

----

.. _doc_item_asset_intro:procedurally_animate_inertia:


Procedurally_Animate_Inertia :ref:`bool <doc_data_builtin_types>` ``true``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Whether viewmodel should accumulate angular velocity from animations. Useful for low-quality older animations, but should probably be disabled for high-quality newer animations.

----

.. _doc_item_asset_intro:quality_max:


Quality_Max :ref:`uint8 <doc_data_builtin_types>` ``90``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Maximum quality to generate.  Typically used with ``Quality_Min``.

----

.. _doc_item_asset_intro:quality_min:


Quality_Min :ref:`uint8 <doc_data_builtin_types>` ``10``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Minimum quality to generate.  Typically used with ``Quality_Max``.

----

.. _doc_item_asset_intro:rarity:


Rarity :ref:`doc_data_eitemrarity` ``Common``
:::::::::::::::::::::::::::::::::::::::::::::

Rarity of the item, as text shown in menus and colors used for highlights.

----

.. _doc_item_asset_intro:shared_skin_lookup_id:

Shared_Skin_Lookup_ID :ref:`uint16 <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Share skins with another item. Defaults to item's ``ID``.

----

.. _doc_item_asset_intro:shared_skin_apply_visuals:

Shared_Skin_Apply_Visuals :ref:`bool <doc_data_builtin_types>` ``true``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If false, skin material and mesh are not applied when ``Shared_Skin_Lookup_ID`` is set. For example, a custom axe can transfer the kill counter and ragdoll effect from a vanilla item's skin without also transferring the material and mesh.

----

.. _doc_item_asset_intro:should_delete_at_zero_quality:

Should_Delete_At_Zero_Quality :ref:`bool <doc_data_builtin_types>` ``false``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Item should be deleted when at 0% quality.

----

.. _doc_item_asset_intro:should_drop_on_death:

Should_Drop_On_Death :ref:`bool <doc_data_builtin_types>` ``true``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Item should be dropped on death.

----

.. _doc_item_asset_intro:size_x:

Size_X :ref:`uint8 <doc_data_builtin_types>` ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::

In slots, the total width of the inventory space (i.e., the number of columns).

----

.. _doc_item_asset_intro:size_y:

Size_Y :ref:`uint8 <doc_data_builtin_types>` ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::

In slots, the total height of the inventory space (i.e., the number of rows).

----

.. _doc_item_asset_intro:size_z:

Size_Z :ref:`float32 <doc_data_builtin_types>` ``-1``
:::::::::::::::::::::::::::::::::::::::::::::::::::::

Manually specify orthogonal camera size for item icons. This directly corresponds to the value of a Camera component's Size property in Unity.

----

.. _doc_item_asset_intro:size2_z:

Size2_Z :ref:`float32 <doc_data_builtin_types>` ``-1``
::::::::::::::::::::::::::::::::::::::::::::::::::::::

Orthogonal camera size for economy icons.

----

.. _doc_item_asset_intro:slot:

Slot :ref:`doc_data_eslottype` ``None``
:::::::::::::::::::::::::::::::::::::::

Which equipped item slot an item is valid to be equippable in. This is only relevant if your property has configured the ``Useable`` property.

- ``None`` restricts the useable item to hotkeys.
- ``Primary`` restricts the useable item to the primary slot.
- ``Secondary`` restricts the useable item to the primary or secondary slots.
- ``Tertiary`` is not implemented by this asset.
- ``Any`` has no restrictions on slots or hotkeying.

----

.. _doc_item_asset_intro:type:

Type :ref:`doc_data_eitemtype`
::::::::::::::::::::::::::::::

Designates the item's class. Item assets are required to have this property.

----

.. _doc_item_asset_intro:use_auto_icon_measurements:

Use_Auto_Icon_Measurements :ref:`bool <doc_data_builtin_types>` ``true``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Automatically calculate axis-aligned item icon camera size from bounds.

----

.. _doc_item_asset_intro:use_auto_stat_descriptions:

Use_Auto_Stat_Descriptions :ref:`bool <doc_data_builtin_types>` ``true``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If true, properties like damage, storage, health, etc. are appended to the description.

----

.. _doc_item_asset_intro:useable:

Useable :ref:`doc_item_asset_intro:euseabletype` ``None``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Setting this property adds functionality from a corresponding Useable class. Unless ``Can_Player_Equip`` has been configured otherwise, this *at least* means the item is equippable.

This property is often used in conjunction with the ``Slot`` property, which determines where an item can be equipped from.

Blueprints and Actions
``````````````````````

In addition to the properties already described, item assets can utilize properties for :ref:`crafting blueprints <doc_item_asset_blueprints>` and :ref:`context menu actions <doc_item_asset_actions>`.

Localization
------------

**Name** *string*: Item name in user interfaces.

**Description** :ref:`doc_data_richtext`: Item description in user interfaces.
