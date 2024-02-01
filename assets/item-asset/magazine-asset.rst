.. _doc_item_asset_magazine:

Magazine Assets
===============

Magazine attachments are inventory items that can be attached to ranged weapons.

This inherits the :ref:`CaliberAsset <doc_item_asset_caliber>` class.

Game Data File
--------------

Magazine attachments inherit properties from the CaliberAsset class, which in turn inherits properties from the ItemAsset class. Properties that are required to be included are listed in the table below.

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
     - ``Magazine``

Properties
``````````

.. list-table::
   :widths: 40 40 20
   :header-rows: 1
   
   * - Property Name
     - Type
     - Default Value
   * - :ref:`Animal_Damage <doc_item_asset_magazine:animal_damage>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Barricade_Damage <doc_item_asset_magazine:barricade_damage>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Delete_Empty <doc_item_asset_magazine:delete_empty>`
     - :ref:`flag <doc_data_flag>`
     - 
   * - :ref:`Explosion <doc_item_asset_magazine:explosion>`
     - :ref:`doc_data_guid` or :ref:`uint16 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Explosion_Launch_Speed <doc_item_asset_magazine:explosion_launch_speed>`
     - :ref:`float32 <doc_data_builtin_types>`
     - See description
   * - :ref:`Explosive <doc_item_asset_magazine:explosive>`
     - :ref:`flag <doc_data_flag>`
     - 
   * - :ref:`Impact <doc_item_asset_magazine:impact>`
     - :ref:`doc_data_guid` or :ref:`uint16 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Object_Damage <doc_item_asset_magazine:object_damage>`
     - :ref:`float32 <doc_data_builtin_types>`
     - See description
   * - :ref:`Pellets <doc_item_asset_magazine:pellets>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Player_Damage <doc_item_asset_magazine:player_damage>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Projectile_Blast_Radius_Multiplier <doc_item_asset_magazine:projectile_blast_radius_multiplier>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Projectile_Damage_Multiplier <doc_item_asset_magazine:projectile_damage_multiplier>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Projectile_Launch_Force_Multiplier <doc_item_asset_magazine:projectile_launch_force_multiplier>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Range <doc_item_asset_magazine:range>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Resource_Damage <doc_item_asset_magazine:resource_damage>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Should_Fill_After_Detach <doc_item_asset_magazine:should_fill_after_detach>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``false``
   * - :ref:`Spawn_Explosion_On_Dedicated_Server <doc_item_asset_magazine:spawn_explosion_on_dedicated_server>`
     - :ref:`flag <doc_data_flag>`
     - 
   * - :ref:`Speed <doc_item_asset_magazine:speed>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Structure_Damage <doc_item_asset_magazine:structure_damage>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Stuck <doc_item_asset_magazine:stuck>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Tracer <doc_item_asset_magazine:tracer>`
     - :ref:`doc_data_guid` or :ref:`uint16 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Vehicle_Damage <doc_item_asset_magazine:vehicle_damage>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Zombie_Damage <doc_item_asset_magazine:zombie_damage>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``

Property Descriptions
`````````````````````

.. _doc_item_asset_magazine:animal_damage:

Animal_Damage :ref:`float32 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Damage dealt to animals caught within the area-of-effect explosion of a magazine attachment using the ``Explosive`` flag.

----

.. _doc_item_asset_magazine:barricade_damage:

Barricade_Damage :ref:`float32 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Damage dealt to barricades caught within the area-of-effect explosion of a magazine attachment using the ``Explosive`` flag.

----

.. _doc_item_asset_magazine:delete_empty:

Delete_Empty :ref:`flag <doc_data_flag>`
::::::::::::::::::::::::::::::::::::::::

The magazine attachment should be deleted when it is fully depleted.

----

.. _doc_item_asset_magazine:explosion:

Explosion :ref:`doc_data_guid` or :ref:`uint16 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

GUID or legacy ID of the effect that should be used for explosions caused by magazine attachment using the ``Explosive`` flag.

----

.. _doc_item_asset_magazine:explosion_launch_speed:

Explosion_Launch_Speed :ref:`float32 <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Players caught within the area-of-effect explosion caused by projectiles when using the ``Explosive`` property are launched at this speed, in meters per second. Defaults to the resulting value of ``Player_Damage * 0.1``.

----

.. _doc_item_asset_magazine:explosive:

Explosive :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::::::

When this flag is included, the projectile fired from a ballistics projectile weapon will cause an area-of-effect explosion. This is typically used alongside the ``Range`` property.

----

.. _doc_item_asset_magazine:impact:

Impact :ref:`doc_data_guid` or :ref:`uint16 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

GUID or legacy ID of the effect that should be play on impact.

----

.. _doc_item_asset_magazine:object_damage:

Object_Damage :ref:`float32 <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::

Damage dealt to players caught within the area-of-effect explosion of a magazine attachment using the ``Explosive`` flag. Defaults to the value of the ``Resource_Damage`` property.

----

.. _doc_item_asset_magazine:pellets:

Pellets :ref:`uint8 <doc_data_builtin_types>` ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::::

Number of bullet rays shot.

----

.. _doc_item_asset_magazine:player_damage:

Player_Damage :ref:`float32 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Damage dealt to players caught within the area-of-effect explosion of a magazine attachment using the ``Explosive`` flag.

----

.. _doc_item_asset_magazine:projectile_blast_radius_multiplier:

Projectile_Blast_Radius_Multiplier :ref:`float32 <doc_data_builtin_types>` ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on the blast radius of the explosive projectiles fired from physics projectile weapons.

----

.. _doc_item_asset_magazine:projectile_damage_multiplier:

Projectile_Damage_Multiplier :ref:`float32 <doc_data_builtin_types>` ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on the damage dealt by the explosive projectiles fired from physics projectile weapons.

----

.. _doc_item_asset_magazine:projectile_launch_force_multiplier:

Projectile_Launch_Force_Multiplier :ref:`float32 <doc_data_builtin_types>` ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on the launch force applied to the explosive projectiles fired from physics projectile weapons.

----

.. _doc_item_asset_magazine:range:

Range :ref:`float32 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::

In meters, the radius of the area-of-effect explosion caused by a projectile when a magazine attachment is using the ``Explosive`` flag.

----

.. _doc_item_asset_magazine:resource_damage:

Resource_Damage :ref:`float32 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Damage dealt to resources caught within the area-of-effect explosion of a magazine attachment using the ``Explosive`` flag.

----

.. _doc_item_asset_magazine:should_fill_after_detach:

Should_Fill_After_Detach :ref:`bool <doc_data_builtin_types>` ``false``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Ammunition should be fully refilled after the magazine attachment is detached from a ranged weapon.

----

.. _doc_item_asset_magazine:spawn_explosion_on_dedicated_server:

Spawn_Explosion_On_Dedicated_Server :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

When using the ``Explosion`` property, spawn the explosion effect on the server.

----

.. _doc_item_asset_magazine:speed:

Speed :ref:`float32 <doc_data_builtin_types>` ``1``
:::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on reload speed.

----

.. _doc_item_asset_magazine:structure_damage:

Structure_Damage :ref:`float32 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Damage dealt to structures caught within the area-of-effect explosion of a magazine attachment using the ``Explosive`` flag.

----

.. _doc_item_asset_magazine:stuck:

Stuck :ref:`uint8 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::

The amount of quality that should be lost after the projectile hits something. When this value is greater than ``0``, the item will have a visible quality value. This property is typically used with :ref:`ranged weapons <doc_item_asset_gun>` utilizing the ``Action String`` key-value pair, such as a crossbow.

----

.. _doc_item_asset_magazine:tracer:

Tracer :ref:`doc_data_guid` or :ref:`uint16 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

GUID or legacy ID of the effect that should be used for bullet tracers.

----

.. _doc_item_asset_magazine:vehicle_damage:

Vehicle_Damage :ref:`float32 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Damage dealt to vehicles caught within the area-of-effect explosion of a magazine attachment using the ``Explosive`` flag.

----

.. _doc_item_asset_magazine:zombie_damage:

Zombie_Damage :ref:`float32 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Damage dealt to zombies caught within the area-of-effect explosion of a magazine attachment using the ``Explosive`` flag.