.. _doc_item_asset_tactical:

Tactical Assets
===============

Tacticals (or "tactical attachments") are created from the ItemTacticalAsset class. They are inventory items that can be attached to ranged weapons.

This inherits the :ref:`CaliberAsset <doc_item_asset_caliber>` class.

Game Data File
--------------

Tactical attachments inherit properties from the CaliberAsset class, which in turn inherits properties from the ItemAsset class. Properties that are required to be included are listed in the table below.

.. list-table::
   :widths: 30 40 30
   :header-rows: 1

   * - Class
     - Property Name
     - Required Value
   * - :ref:`ItemAsset <doc_item_asset_intro>`
     - :ref:`GUID <doc_item_asset_intro:guid>`
     -
   * - :ref:`ItemAsset <doc_item_asset_intro>`
     - :ref:`ID <doc_item_asset_intro:id>`
     -
   * - :ref:`ItemAsset <doc_item_asset_intro>`
     - :ref:`Type <doc_item_asset_intro:type>`
     - ``Tactical``

Properties
``````````

.. list-table::
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`Laser <doc_item_asset_tactical:laser>`
     - :ref:`flag <doc_data_flag>`
     -
   * - :ref:`Laser_Color <doc_item_asset_tactical:laser_color>`
     - :ref:`color <doc_data_color>`
     - ``#FF0000``
   * - :ref:`Light <doc_item_asset_tactical:light>`
     - :ref:`flag <doc_data_builtin_types>`
     -
   * - :ref:`Melee <doc_item_asset_tactical:melee>`
     - :ref:`flag <doc_data_flag>`
     -
   * - :ref:`Rangefinder <doc_item_asset_tactical:rangefinder>`
     - :ref:`flag <doc_data_flag>`
     -

Property Descriptions
`````````````````````

.. _doc_item_asset_tactical:laser:

Laser :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::

Provides a toggleable laser.

----

.. _doc_item_asset_tactical:laser_color:

Laser_Color :ref:`color <doc_data_color>` ``#FF0000``
:::::::::::::::::::::::::::::::::::::::::::::::::::::

Override the default red color with the specified value. This property supports using legacy color parsing.

----

.. _doc_item_asset_tactical:light:

Light :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::

Provides a toggleable flashlight, and allows for using :ref:`PlayerSpotLightConfig <doc_data_playerspotlightconfig>` properties.

----

.. _doc_item_asset_tactical:melee:

Melee :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::

Provides the ability to perform a melee attack. This attack does 40 damage, and is not configurable.

----

.. _doc_item_asset_tactical:rangefinder:

Rangefinder :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::::::::

Provides a toggleable rangefinder.

Melee-Specific Property Descriptions
`````````````````````````````````````

.. note:: These properties are only applicable if the ``Melee`` flag is set.

.. warning:: This is mostly copied 1:1 from :ref:`doc_item_asset_weapon` and should be tidied up if/when that is updated.

**Melee_Range** *float32*: The maximum distance in meters before damage is no longer possible.

**Melee_Player_Damage** *float32*: Amount of damage that should be dealt to player entities, prior to modifiers such as limb multipliers.

**Melee_Player_Leg_Multiplier** *float32*: Multiplier on damage targeted against a player's legs.

**Melee_Player_Arm_Multiplier** *float32*: Multiplier on damage targeted against a player's arms.

**Melee_Player_Spine_Multiplier** *float32*: Multiplier on damage targeted against a player's torso.

**Melee_Player_Skull_Multiplier** *float32*: Multiplier on damage targeted against a player's head.

**Melee_Player_Damage_Bleeding** *enum* (``Always``, ``Default``, ``Heal``, ``Never``): Determines the effect the weapon has in relation to the "Bleeding" status effect. When using "Always", the Bleeding status effect will always be applied on hit. When using "Default", the Bleeding status effect will only be applied if the necessary damage threshold is met. When using "Heal", anyone hit by the weapon will have their Bleeding status effect removed. When using "Never", the Bleeding status effect is never applied by this weapon. Defaults to "Default" enumerator.

**Melee_Player_Damage_Bones** *enum* (``Always``, ``Heal``, ``None``): Determines the effect the weapon has in relation to the "Broken Bones" status effect. When using "Always", the Broken Bones status effect will always be applied on hit. When using "Heal", anyone hit by the weapon will have their Broken Bones status effect removed. When using "Never", the Broken Bones status effect is never applied by this weapon. Defaults to the "None" enumerator.

**Melee_Zombie_Damage** *float32*: Amount of damage that should be dealt to zombie entities, prior to modifiers such as limb multipliers.

**Melee_Zombie_Leg_Multiplier** *float32*: Multiplier on damage targeted against a zombie's legs.

**Melee_Zombie_Arm_Multiplier** *float32*: Multiplier on damage targeted against a zombie's arms.

**Melee_Zombie_Spine_Multiplier** *float32*: Multiplier on damage targeted against a zombie's torso.

**Melee_Zombie_Skull_Multiplier** *float32*: Multiplier on damage targeted against a zombie's head.

**Melee_Zombie_Ragdoll_Force_Multiplier** *float32*: Scales force applied to zombie ragdoll. Defaults to 1.

**Melee_Stun_Zombie_Always** *flag*: Specified if a zombie should always be stunned when targeted by the weapon.

**Melee_Stun_Zombie_Never** *flag*: Specified if a zombie should never be stunned when targeted by the weapon.

**Melee_Animal_Damage** *float32*: Amount of damage that should be dealt to animal entities, prior to modifiers such as limb multipliers.

**Melee_Animal_Leg_Multiplier** *float32*: Multiplier on damage targeted against a animal's limbs.

**Melee_Animal_Spine_Multiplier** *float32*: Multiplier on damage targeted against a animal's torso.

**Melee_Animal_Skull_Multiplier** *float32*: Multiplier on damage targeted against a animal's head.
