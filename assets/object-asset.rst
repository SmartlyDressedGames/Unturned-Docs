.. _doc_assets_object:

Object Assets
=============

**GUID** *32-digit hexadecimal*: Refer to :ref:`doc_data_guid` documentation.

**Type** *enum* (``Small``, ``Medium``, ``Large``, ``NPC``, ``Decal``): The object's type is used for sorting, pathfinding, collision, and culling. Small objects are used for clutter and decoration, medium objects fill out the layout, and large objects make up the level. When using the ``NPC`` enumerator, refer to the documentation for :ref:`doc_object_asset_npc` as well.

**ID** *uint16*: Must be a unique identifier.

Object Properties
-----------------

**Add_Kill_Triggers** *bool*: If true, this adds a kill volume inside the object that will kill players who clip inside it. This is helpful for preventing out-of-bounds exploits, such as players trying to build bases inside boulder objects.

**Add_Night_Light_Script** *flag*: Adds a script to the object that looks for a transform named "Light". During the night, the light will be turned on. During the day, the light will be turned off.

**Allow_Structures** *flag*: Structures can be built on top of this object. For example, a fake grass object may want to use this property.

**Causes_Fall_Damage** *bool*: Whether or not players should take fall damage when landing on this object. Defaults to true.

**Chart** *enum* (:ref:`doc_data_eobjectchart`): When an object obstructs the terrain, it can appear on a map's chart view. The pixel sampled for the object's color on the chart view can be set or overridden with this property. By default, ``Type Large`` objects use the same pixel as the ``Large`` enumerator, and ``Type Medium`` objects use the same pixel as the ``Medium`` enumerator. Defaults to ``Ignore`` when using ``Type NPC`` or ``Type Decal``. Otherwise, defaults to ``None``.

**Christmas_Redirect** :ref:`doc_data_guid`: GUID of the object that should appear during the Festive holiday.

**Collision_Important** *flag*: Prevent collision from being disabled. When using ``Type Large``, this flag is automatically included.

**Exclude_From_Level_Batching** *bool*: Exclude this object from :ref:`level batching <doc_mapping_batching>`. This property may be helpful when using elaborate setups with Unity Event components. Defaults to true when using ``Type Decal`` or ``Type NPC``.

**Foliage** :ref:`GUID <doc_data_guid>`: GUID of a :ref:`foliage asset <doc_assets_foliage>`. This property is useful for objects such as fake grass, which may want foliage to bake on top of the object similar to terrain materials.

**Fuel** *flag*: Fuel can be siphoned from this object. Deprecated in favor of ``Interactability Fuel``.

**Halloween_Redirect** :ref:`doc_data_guid`: GUID of the object that should appear during the Halloween holiday.

**Has_Clip_Prefab** *bool*: Whether or not the object has a Clip.prefab. If the object should use the same prefab on the server as on the client, set to false. For example, most official content uses ``Has_Clip_Prefab false``. Defaults to true.

**Holiday_Restriction** *enum* (:ref:`doc_data_enpcholiday`): If a valid value is specified, then this object will only be visible during the corresponding holiday. The specified holiday will be appended to the object's user-friendly name. Defaults to ``None``.

**Is_Gore** *bool*: Whether or not this object should be visible if the player has disabled "Show Blood Splatters".

**Landmark_Quality** *enum* (``Off``, ``Low``, ``Medium``, ``High``, ``Ultra``): The value that the "Landmarks" graphical setting must be set to in order to see a low detail model of this object from far away distances. Defaults to ``Low``.

**Material_Palette** :ref:`doc_data_guid`: GUID of the :ref:`Material Palette Asset <doc_assets_material_palette>` that should be used by the object.

**Refill** *flag*: Water can be siphoned from this object. Deprecated in favor of ``Interactability Water``.

**Snowshoe** *flag*: This object should not leave a footprint when baking materials.

**Soft** *flag*: Vehicles should not take damage when colliding with this object.

**Use_Water_Height_Transparent_Sort** *flag*: Useful for transparent objects, such as glass.

**Exclude_From_Satellite_Capture** *bool*: If true, object will be hidden when rendering GPS/satellite view. Defaults to true if ``Holiday_Restriction`` is other than ``None``.

Decals
``````

**Decal_Alpha** *flag*: This flag should be set if the decal has a transparent texture. Requires ``Type Decal``.

**Decal_X** *float*: Override the scale of the decal, on the 𝘟-axis. Requires ``Type Decal``.

**Decal_Y** *float*: Override the scale of the decal, on the 𝘠-axis. Requires ``Type Decal``.

**Decal_LOD_Bias** *float*: Multiplier for the LOD's switching distance. Defaults to 1. Requires ``Type Decal``.

Interior Culling
````````````````

**Exclude_From_Culling_Volumes** *bool*: If set to true, this object will not be managed by culling volumes. For example, the aerospace facility on the Germany map is excluded from culling volumes, so that manually-placed culling volumes can hide large objects like shipping containers without accidentally hiding the giant aerospace facility itself.

**LOD** *enum* (``None``, ``Mesh``, ``Area``): How interior culling should be determined. Using the ``Mesh`` enumerator will use the mesh bounds to determine what is inside the object. For concave objects, you can use the ``Area`` enumerator instead and add multiple Occlusion Area components for the interior volumes.

**LOD_Bias** *float*: Multiplier on the threshold distance for interior culling. Requires that ``LOD`` has been set.

**LOD_Center_X** float: Offset for the culling volume's local position, on the 𝘟-axis. Requires that ``LOD`` has been set.

**LOD_Center_Y** float: Offset for the culling volume's local position, on the 𝘠-axis. Requires that ``LOD`` has been set.

**LOD_Center_Z** float: Offset for the culling volume's local position, on the 𝘡-axis. Requires that ``LOD`` has been set.

**LOD_Size_X** float: Offset for the culling volume's size, on the 𝘟-axis. Requires that ``LOD`` has been set.

**LOD_Size_Y** float: Offset for the culling volume's size, on the 𝘠-axis. Requires that ``LOD`` has been set.

**LOD_Size_Z** float: Offset for the culling volume's size, on the 𝘡-axis. Requires that ``LOD`` has been set.

Interactables
`````````````

**Interactability** *enum* (``None``, ``Binary_State``, ``Dropper``, ``Note``, ``Water``, ``Fuel``, ``Rubble``, ``NPC``, ``Quest``): All ``Interactability_`` properties will require that this property has been set. The enumerator selected for this property will affect which properties can be used, how these properties will function when used, and how this object will behave in-game. Defaults to the ``NPC`` enumerator when using ``Type NPC``, otherwise this property will default to ``None``.

- ``Binary_State`` objects will change between their two states when interacted with – such as an open or closed door.
- ``Dropper`` objects can spawn items when interacted with.
- ``Note`` objects can display lines of text when interacted with.
- ``Water`` objects can be siphoned for water, and ``Fuel`` objects can be siphoned for fuel.
- ``Rubble`` objects are destructible. It is preferable to use ``Rubble Destroy`` instead of ``Interactability Rubble``.
- ``NPC`` objects can provide access to dialogue, quests, and vendors.
- ``Quest`` objects can be interacted with, but unlike other options they have no additional functionality.

.. note::

	Although ``Interactability`` properties can be used to create a destructible object, it is preferable to use ``Rubble`` properties as they are more specific. This allows for creating destructible objects that are also interactable.


**Interactability_Blade_ID** *byte*: When using ``Interactability Rubble``, weapons are unable to damage this object unless they have a matching ``BladeID_#`` value. Defaults to 0.

**Interactability_Delay** *float*: In seconds, the cooldown before the object can be interacted with again.

**Interactability_Drops** *byte*: Total number of items dropped from an object using ``Interactability Dropper``. This property is used in conjunction with ``Interactability_Drop_#``. Defaults to 0. It is preferable to use the ``Interactability_Reward_ID`` property instead.

**Interactability_Drop_#** *uint16*: ID of an item that should be dropped. This property is used in conjunction with ``Interactability_Drops``.

**Interactability_Editor** *enum* (``None``, ``Toggle``): Determines how this interactable object should appear in the level editor. If this is set to ``Toggle``, then the object's alternative state will be shown. Defaults to ``None``.

**Interactability_Effect** :ref:`doc_data_guid` or *uint16*: GUID or legacy ID of an :ref:`EffectAsset <doc_assets_effect>` to play when interacted with. When using ``Interactability Rubble``, this effect is played when a section of the object is destroyed.

**Interactability_Finale** :ref:`doc_data_guid` or *uint16*: GUID or legacy ID of an :ref:`EffectAsset <doc_assets_effect>` to play when all sections of the object using ``Interactability Rubble`` are destroyed. If this property is used, then all of the dead object's sections will also be hidden when fully destroyed.

**Interactability_Health** *uint16*: Total amount of health each section of the object has, when using ``Interactability Rubble``. Defaults to 0.

**Interactability_Hint** *enum* (``Door``, ``Switch``, ``Fire``, ``Generator``, ``Use``, ``Custom``): Localization key to use for the interact prompt. Setting this to ``Custom`` allows for displaying custom text instead, when used in conjunction with ``Interact``.

**Interactability_Invulnerable** *flag*: This resource cannot be damaged by lower-power :ref:`doc_item_asset_weapon` that do not have the ``Invulnerable`` flag, when using ``Interactability Rubble``.

**Interactability_Nav** *enum* (``None``, ``On``, ``Off``): How navigation should change when the object's state is changed. Defaults to ``None``.

**Interactability_Power** *enum* (``None``, ``Toggle``, ``Stay``): Whether or not this object must be powered to be usable. When set to ``None``, this object cannot be powered. When set to ``Toggle``, the object must be powered to be interacted with. When set to ``Stay``, the object must be powered to remain on. For example, a door might use ``Toggle`` if it should remain open after it loses power, while a streetlight might use ``Stay`` so that the light turns off when it loses power. Defaults to ``None``.

**Interactability_Proof_Explosion** *flag*: Immune to area-of-effect explosive damage, when using ``Interactability Rubble``.

**Interactability_Remote** *flag*: Disables the ability for players to interact with this via a button prompt.

**Interactability_Reset** *float*: Delay before an interacted object resets, or a destroyed object respawns, in seconds.

**Interactability_Resource** *uint16*: When using ``Interactability Fuel`` or ``Interactability Water``, this value is how many units of fuel or water is stored in the object. Defaults to 0.

**Interactability_Reward_ID** *uint16*: ID of an item :ref:`spawn table <doc_assets_spawn>` to use for rewards, when using ``Interactability Rubble``. Defaults to 0.

**Interactability_Rewards_Min** *byte*: Minimum amount of item drops to reward, when using ``Interactability Rubble``. Defaults to 1.

**Interactability_Rewards_Max** *byte*: Maximum amount of item drops to reward, when using ``Interactability Rubble``. Defaults to 1.

**Interactability_Reward_Probability** *float*: Probability of receiving a reward, as a decimal-to-percent chance, when using ``Interactability Rubble``. Defaults to 1.

**Interactability_Reward_XP** *uint32*: Amount of experience to reward when the object using ``Interactability Rubble`` is destroyed.

**Interactability_Text_Lines** *uint16*: Total number of lines to display when an object using ``Interactability Note`` is interacted with. This property is used in conjunction with ``Interactability_Text_Line_#``. Defaults to 0.

Rubble
``````

**Rubble** *enum* (``None``, ``Destroy``): The destruction mode that should be used, although the only functional option for this is ``Destroy``. All ``Rubble_`` properties require that this property has been set.

**Rubble_Blade_ID** *byte*: Weapons are unable to damage this object unless they have a matching ``BladeID_#`` value. Defaults to 0.

**Rubble_Editor** *enum* (``Alive``, ``Dead``): Determines how this destructible object should appear in the level editor. If this is set to ``Dead``, the fully destroyed state of the object will be shown. Defaults to ``Alive``.

**Rubble_Effect** :ref:`doc_data_guid` or *uint16*: GUID or legacy ID of an :ref:`EffectAsset <doc_assets_effect>` to play when a section of the destructible object is destroyed.

**Rubble_Finale** :ref:`doc_data_guid` or *uint16*: GUID or legacy ID of an :ref:`EffectAsset <doc_assets_effect>` to play when all sections of the destructible object are destroyed. If this property is used, then all of the dead object's sections will also be hidden when fully destroyed.

**Rubble_Health** *uint16*: Total amount of health each section of the object has. Defaults to 0.

**Rubble_Invulnerable** *flag*: This resource cannot be damaged by lower-power :ref:`doc_item_asset_weapon` that do not have the ``Invulnerable`` flag.

**Rubble_Proof_Explosion** *flag*: Immune to area-of-effect explosive damage.

**Rubble_Reset** *float*: Delay before a destroyed object respawns, in seconds.

**Rubble_Reward_ID** *uint16*: ID of an item :ref:`spawn table <doc_assets_spawn>` to use for rewards. Defaults to 0.

**Rubble_Rewards_Min** *byte*: Minimum amount of item drops to reward. Defaults to 1.

**Rubble_Rewards_Max** *byte*: Maximum amount of item drops to reward. Defaults to 1.

**Rubble_Reward_Probability** *float*: Probability of receiving a reward, as a decimal-to-percent chance. Defaults to 1.

**Rubble_Reward_XP** *uint32*: Amount of experience to reward when the destructible object is destroyed.

Conditions and Rewards
``````````````````````

:ref:`Conditions <doc_npc_asset_conditions>` can be used to control the visibility of an object. For example, if an object should only be visible after a certain quest has been completed. These properties do not have a unique prefix, and instead use the standard ``Conditions`` and ``Condition_#`` property names.

Conditions and :ref:`rewards <doc_npc_asset_rewards>` can also be tied to the interactability of an object. An object could become interactable during a quest, and then trigger rewards (such as completing the quest) once it has been interacted with. These properties are prefixed with ``Interactability_``. For example, ``Interactability_Conditions`` and ``Interactability_Reward_#``.

Localization
------------

**Name** *string*: Object name in user interfaces.

**Interact** *string*: When an interactable object is using ``Interactability_Hint Custom``, this property is used to set the text that should be displayed as the interact prompt for the object.

**Interactability_Text_Line_#** :ref:`doc_data_richtext`: A line of text that should be displayed when an object using ``Interactability Note`` is interacted with. This property is used in conjunction with ``Interactability_Text_Lines``.
