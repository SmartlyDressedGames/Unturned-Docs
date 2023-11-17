.. _doc_item_asset_magazine:

Magazine Assets
===============

Magazine attachments are inventory items that can be attached to ranged weapons.

This inherits the :ref:`CaliberAsset <doc_item_asset_caliber>` class.

Game Data File
--------------

Item Asset Properties
`````````````````````

**GUID** *32-digit hexadecimal*: Refer to :ref:`doc_data_guid` documentation.

**Type** *enum* (``Magazine``)

**ID** :ref:`uint16 <doc_data_builtin_types>`: Must be a unique identifier.

Magazine Asset Properties
`````````````````````````

.. list-table::
   :widths: 40 40 20
   :header-rows: 1
   
   * - Property Name
     - Type
     - Default Value
   * - :ref:`Pellets <doc_item_asset_magazine_property_pellets>`
     - :ref:`byte <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Projectile_Damage_Multiplier <doc_item_asset_magazine_property_projectile_damage_multiplier>`
     - :ref:`float <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Projectile_Blast_Radius_Multiplier <doc_item_asset_magazine_property_projectile_projectile_blast_radius_multiplier>`
     - :ref:`float <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Projectile_Launch_Force_Multiplier <doc_item_asset_magazine_property_projectile_projectile_launch_force_multiplier>`
     - :ref:`float <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Speed <doc_item_asset_magazine_property_projectile_speed>`
     - :ref:`float <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Stuck <doc_item_asset_magazine_property_projectile_stuck>`
     - :ref:`byte <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Explosive <doc_item_asset_magazine_property_projectile_explosive>`
     - :ref:`flag <doc_data_flag>`
     - n/a
   * - :ref:`Range <doc_item_asset_magazine_property_projectile_range>`
     - :ref:`float <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Player_Damage <doc_item_asset_magazine_property_projectile_player_damage>`
     - :ref:`float <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Zombie_Damage <doc_item_asset_magazine_property_projectile_zombie_damage>`
     - :ref:`float <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Animal_Damage <doc_item_asset_magazine_property_projectile_animal_damage>`
     - :ref:`float <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Barricade_Damage <doc_item_asset_magazine_property_projectile_barricade_damage>`
     - :ref:`float <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Structure_Damage <doc_item_asset_magazine_property_projectile_structure_damage>`
     - :ref:`float <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Vehicle_Damage <doc_item_asset_magazine_property_projectile_vehicle_damage>`
     - :ref:`float <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Resource_Damage <doc_item_asset_magazine_property_projectile_resource_damage>`
     - :ref:`float <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Object_Damage <doc_item_asset_magazine_property_projectile_object_damage>`
     - :ref:`float <doc_data_builtin_types>`
     - See description
   * - :ref:`Explosion_Launch_Speed <doc_item_asset_magazine_property_projectile_explosion_launch_speed>`
     - :ref:`float <doc_data_builtin_types>`
     - See description
   * - :ref:`Explosion <doc_item_asset_magazine_property_projectile_explosion>`
     - :ref:`doc_data_guid` or :ref:`uint16 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Spawn_Explosion_On_Dedicated_Server <doc_item_asset_magazine_property_projectile_spawn_explosion_on_dedicated_server>`
     - :ref:`flag <doc_data_flag>`
     - n/a
   * - :ref:`Tracer <doc_item_asset_magazine_property_projectile_tracer>`
     - :ref:`doc_data_guid` or :ref:`uint16 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Impact <doc_item_asset_magazine_property_projectile_impact>`
     - :ref:`doc_data_guid` or :ref:`uint16 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Delete_Empty <doc_item_asset_magazine_property_projectile_delete_empty>`
     - :ref:`flag <doc_data_flag>`
     - n/a
   * - :ref:`Should_Fill_After_Detach <doc_item_asset_magazine_property_projectile_should_fill_after_detach>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``false``

Property Descriptions
`````````````````````

.. _doc_item_asset_magazine_property_pellets:

Pellets :ref:`byte <doc_data_builtin_types>` ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::

Number of bullet rays shot.

----

.. _doc_item_asset_magazine_property_projectile_damage_multiplier:

Projectile_Damage_Multiplier :ref:`float <doc_data_builtin_types>` ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on the damage dealt by projectile weapons.

----

.. _doc_item_asset_magazine_property_projectile_projectile_blast_radius_multiplier:

Projectile_Blast_Radius_Multiplier :ref:`float <doc_data_builtin_types>` ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on the blast radius of projectiles fired from projectile weapons.

----

.. _doc_item_asset_magazine_property_projectile_projectile_launch_force_multiplier:

Projectile_Launch_Force_Multiplier :ref:`float <doc_data_builtin_types>` ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on the launch force applied to projectiles fired from projectile weapons.

----

.. _doc_item_asset_magazine_property_projectile_speed:

Speed :ref:`float <doc_data_builtin_types>` ``1``
:::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on reload speed.

----

.. _doc_item_asset_magazine_property_projectile_stuck:

Stuck :ref:`byte <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::

Amount of quality to lose when hit. When this value is greater than 0, fired projectiles can be picked back up until their quality reaches 0.

----

.. _doc_item_asset_magazine_property_projectile_explosive:

Explosive :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::::::

Specified if it should cause an area-of-effect explosion.

----

.. _doc_item_asset_magazine_property_projectile_range:

Range :ref:`float <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Radius of the area-of-effect explosion.

----

.. _doc_item_asset_magazine_property_projectile_player_damage:

Player_Damage :ref:`float <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Damage dealt to players caught in the area-of-effect explosion.

----

.. _doc_item_asset_magazine_property_projectile_zombie_damage:

Zombie_Damage :ref:`float <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Damage dealt to zombies caught in the area-of-effect explosion.

----

.. _doc_item_asset_magazine_property_projectile_animal_damage:

Animal_Damage :ref:`float <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Damage dealt to animals caught in the area-of-effect explosion.

----

.. _doc_item_asset_magazine_property_projectile_barricade_damage:

Barricade_Damage :ref:`float <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Damage dealt to barricades caught in the area-of-effect explosion.

----

.. _doc_item_asset_magazine_property_projectile_structure_damage:

Structure_Damage :ref:`float <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Damage dealt to structures caught in the area-of-effect explosion.

----

.. _doc_item_asset_magazine_property_projectile_vehicle_damage:

Vehicle_Damage :ref:`float <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Damage dealt to vehicles caught in the area-of-effect explosion.

----

.. _doc_item_asset_magazine_property_projectile_resource_damage:

Resource_Damage :ref:`float <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Damage dealt to resources caught in the area-of-effect explosion.

----

.. _doc_item_asset_magazine_property_projectile_object_damage:

Object_Damage :ref:`float <doc_data_builtin_types>` See description
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Damage dealt to objects caught in the area-of-effect explosion. Defaults to the value used by ``Resource_Damage``.

----

.. _doc_item_asset_magazine_property_projectile_explosion_launch_speed:

Explosion_Launch_Speed :ref:`float <doc_data_builtin_types>` See description
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Launch speed of players caught within the area-of-effect explosion, in meters per second. Defaults to the resulting value from ``Player_Damage * 0.1``.

----

.. _doc_item_asset_magazine_property_projectile_explosion:

Explosion :ref:`doc_data_guid` or :ref:`uint16 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

GUID or legacy ID of explosion effect.

----

.. _doc_item_asset_magazine_property_projectile_spawn_explosion_on_dedicated_server:

Spawn_Explosion_On_Dedicated_Server :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Specified to spawn the explosion effect on the server.

----

.. _doc_item_asset_magazine_property_projectile_tracer:

Tracer :ref:`doc_data_guid` or :ref:`uint16 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

GUID or legacy ID of bullet tracer effect.

----

.. _doc_item_asset_magazine_property_projectile_impact:

Impact :ref:`doc_data_guid` or :ref:`uint16 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

GUID or legacy ID of effect to play on impact.

----

.. _doc_item_asset_magazine_property_projectile_delete_empty:

Delete_Empty :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::::::::::::::

Specified if the magazine attachment should be deleted when it is fully depleted.

----

.. _doc_item_asset_magazine_property_projectile_should_fill_after_detach:

Should_Fill_After_Detach :ref:`bool <doc_data_builtin_types>` ``false``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Ammunition should be fully refilled after the magazine attachment is detached from a ranged weapon.