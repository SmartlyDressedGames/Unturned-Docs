.. _doc_assets_resource:

Resource Assets
===============

**GUID** *32-digit hexadecimal*: Refer to :ref:`doc_data_guid` documentation.

**Type** *enum* (``Resource``)

**ID** *uint16*: Must be a unique identifier.

Resource Properties
-------------------

**Auto_Skybox** *flag*: Generate and assign a material and texture to the resource's Skybox prefab. The mesh should have custom normals to match the lighting. For example, vanilla pine trees have upward normals, whereas spherical trees have outward normals.

**BladeID** *byte*: Weapons are unable to damage this resource unless they have a matching ``BladeID_#`` value. Defaults to 0.

**Bypass_ID_Limit** *flag*: Allows for using an ``ID`` value within the range reserved for official content.

**Chart** *enum* (:ref:`doc_data_eobjectchart`): When a resource obstructs the terrain, it can appear on a map's chart view. The pixel sampled for the resource's color on the chart view can be set or overridden with this property. Defaults to ``None``, and will sample (14, 0) from the Layer_Strip.

**Christmas_Redirect** :ref:`doc_data_guid`: GUID of the resource that should appear during the Festive holiday.

**Debris_Vertical_Offset** *float*:  Distance along tree's local up axis to offset debris spawn position. Defaults to 1.0.

**Exclude_From_Level_Batching** *bool*: Exclude this resource from :ref:`level batching <doc_mapping_batching>`. This property may be helpful when using elaborate setups with Unity Event components. Defaults to true when the ``SpeedTree`` flag is set.

**Explosion** :ref:`GUID <doc_data_guid>` or *uint16*: GUID or legacy ID of :ref:`EffectAsset <doc_assets_effect>` to play when destroyed.

**Forage** *flag*: Instead of being destroyable, this resource can be foraged from by interacting with it.

**Forage_Reward_Experience** *uint32*: Amount of experience to reward when the resource is foraged from. Defaults to 1.

**Halloween_Redirect** :ref:`doc_data_guid`: GUID of the resource that should appear during the Halloween holiday.

**Health** *uint16*: Total amount of health the resource has. Defaults to 0.

**Holiday_Restriction** *enum* (:ref:`doc_data_enpcholiday`): If a valid value is specified, then this resource will only be visible during the corresponding holiday. The specified holiday will be appended to the resource's user-friendly name. Defaults to ``None``.

**Ignore_Collision_Between_Stump_And_Debris** *bool*: If true, prevent collisions between falling tree and the stump. (i.e., debris can fall through stump) Defaults to true.

**Log** *uint16*: ID of an item that should be dropped when the resource is destroyed. Before multipliers, this item is dropped in bunches of 3 to 7. Defaults to 0. Deprecated in favor of ``Reward_ID``.

**No_Debris** *flag*: This resource does not have debris that should appear when it has been destroyed.

**RandomAngleDeviation_Max** *float*: Maximum angle in degrees away from the up direction. Defaults to 5.

**RandomAngleDeviation_Min** *float*: Minimum angle in degrees away from the up direction. For example, can be set to 0 to allow the tree to be perfectly upright, or a higher value to prevent the tree from ever being upright. Defaults to 5.

**RandomUniformScale_Max** *float*: Maximum scale. The same randomized value is used for all axes (uniform). Defaults to 1.1 for backwards compatibility.

**RandomUniformScale_Min** *float*: Minimum scale. The same randomized value is used for all axes (uniform). Defaults to 1.1 for backwards compatibility.

**Reset** *float*: Delay before respawning, in seconds.

**Reward_ID** *uint16*: ID of an item :ref:`spawn table <doc_assets_spawn>` to use for rewards. Defaults to 0.

**Reward_Min** *byte*: Minimum amount of item drops to reward. Defaults to 6.

**Reward_Max** *byte*: Maximum amount of item drops to reward. Defaults to 9.

**Reward_XP** *uint32*: Amount of experience to reward when the resource is destroyed.

**Scale** *float*: The tree's in-game scale is a random number between 1.1 and the result of ``1.1 + (Scale * 2)``.

.. deprecated:: 3.24.7.0
	Scale is replaced by the ``RandomUniformScale_Min`` and ``RandomUniformScale_Max`` properties.

**SpeedTree** *flag*: This resource should be considered a SpeedTree when using higher graphical settings.

**SpeedTree_Default_LOD_Weights** *flag*: Use the default LOD weights intended for a SpeedTree.

**Stick** *uint16*: ID of an item that should be dropped when the resource is destroyed. Before multipliers, this item is dropped in bunches of 2 to 5. Defaults to 0. Deprecated in favor of ``Reward_ID``.

**Vertical_Offset** *float*: A vertical offset above or below wherever this resource is placed, in meters. Defaults to -0.75.

**Vulnerable_To_All_Melee_Weapons** *bool*: When true, this resource can be damaged by melee weapons that do not have a corresponding ``BladeID_#`` value. Defaults to false.

**Vulnerable_To_Fists** *bool*: When true, this resource can be damaged by a player's fists. Defaults to false.

Localization
------------

**Name** *string*: Resource name in user interfaces.

**Interact** *string*: Override the text shown for interactable resources using the ``Forage`` flag.
