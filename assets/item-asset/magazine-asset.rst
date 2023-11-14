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

**ID** *uint16*: Must be a unique identifier.

Magazine Asset Properties
`````````````````````````

.. list-table::
   :widths: 40 40 20
   :header-rows: 0

   * - **Pellets**
     - *byte*
     - ``1``
   * - **Projectile_Damage_Multiplier**
     - *float*
     - ``1``
   * - **Projectile_Blast_Radius_Multiplier**
     - *float*
     - ``1``
   * - **Projectile_Launch_Force_Multiplier**
     - *float*
     - ``1``
   * - **Speed**
     - *float*
     - ``1``
   * - **Stuck**
     - *byte*
     - ``0``
   * - **Explosive**
     - *flag*
     - n/a
   * - **Range**
     - *float*
     - ``0``
   * - **Player_Damage**
     - *float*
     - ``0``
   * - **Zombie_Damage**
     - *float*
     - ``0``
   * - **Animal_Damage**
     - *float*
     - ``0``
   * - **Barricade_Damage**
     - *float*
     - ``0``
   * - **Structure_Damage**
     - *float*
     - ``0``
   * - **Vehicle_Damage**
     - *float*
     - ``0``
   * - **Resource_Damage**
     - *float*
     - ``0``
   * - **Object_Damage**
     - *float*
     - See description
   * - **Explosion_Launch_Speed**
     - *float*
     - See description
   * - **Explosion**
     - :ref:`doc_data_guid` or *uint16*
     - ``0``
   * - **Spawn_Explosion_On_Dedicated_Server**
     - *flag*
     - n/a
   * - **Tracer**
     - :ref:`doc_data_guid` or *uint16*
     - ``0``
   * - **Impact**
     - :ref:`doc_data_guid` or *uint16*
     - ``0``
   * - **Delete_Empty**
     - *flag*
     - n/a
   * - **Should_Fill_After_Detach**
     - *bool*
     - ``false``

Property Descriptions
`````````````````````

Pellets *byte* = ``1``
::::::::::::::::::::::::::::

Number of bullet rays shot.

Projectile_Damage_Multiplier *float* = ``1``
::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on the damage dealt by projectile weapons.

Projectile_Blast_Radius_Multiplier *float* = ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on the blast radius of projectiles fired from projectile weapons.

Projectile_Launch_Force_Multiplier *float* = ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on the launch force applied to projectiles fired from projectile weapons.

Speed *float* = ``1``
::::::::::::::::::::::::::::

Multiplier on reload speed.

Stuck *byte* = ``0``
::::::::::::::::::::::::::::

Amount of quality to lose when hit. When this value is greater than 0, fired projectiles can be picked back up until their quality reaches 0.

Explosive *flag*
::::::::::::::::::::::::::::

Specified if it should cause an area-of-effect explosion.

Range *float* = ``0``
::::::::::::::::::::::::::::

Radius of the area-of-effect explosion.

Player_Damage *float* = ``0``
:::::::::::::::::::::::::::::

Damage dealt to players caught in the area-of-effect explosion.

Zombie_Damage *float* = ``0``
:::::::::::::::::::::::::::::

Damage dealt to zombies caught in the area-of-effect explosion.

Animal_Damage *float* = ``0``
:::::::::::::::::::::::::::::

Damage dealt to animals caught in the area-of-effect explosion.

Barricade_Damage *float* = ``0``
::::::::::::::::::::::::::::::::::

Damage dealt to barricades caught in the area-of-effect explosion.

Structure_Damage *float* = ``0``
::::::::::::::::::::::::::::::::::

Damage dealt to structures caught in the area-of-effect explosion.

Vehicle_Damage *float* = ``0``
::::::::::::::::::::::::::::::::::

Damage dealt to vehicles caught in the area-of-effect explosion.

Resource_Damage *float* = ``0``
::::::::::::::::::::::::::::::::::

Damage dealt to resources caught in the area-of-effect explosion.

Object_Damage *float* = See description
:::::::::::::::::::::::::::::::::::::::

Damage dealt to objects caught in the area-of-effect explosion. Defaults to the value used by ``Resource_Damage``.

Explosion_Launch_Speed *float* = See description
::::::::::::::::::::::::::::::::::::::::::::::::

Launch speed of players caught within the area-of-effect explosion, in meters per second. Defaults to the resulting value from ``Player_Damage * 0.1``.

Explosion :ref:`doc_data_guid` or *uint16* = ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::

GUID or legacy ID of explosion effect.

Spawn_Explosion_On_Dedicated_Server *flag*
::::::::::::::::::::::::::::::::::::::::::

Specified to spawn the explosion effect on the server.

Tracer :ref:`doc_data_guid` or *uint16* = ``0``
:::::::::::::::::::::::::::::::::::::::::::::::

GUID or legacy ID of bullet tracer effect.

Impact :ref:`doc_data_guid` or *uint16* = ``0``
:::::::::::::::::::::::::::::::::::::::::::::::

GUID or legacy ID of effect to play on impact.

Delete_Empty *flag*
:::::::::::::::::::::::::::::::::::::::::::::

Specified if the magazine attachment should be deleted when it is fully depleted.

Should_Fill_After_Detach *bool* = ``false``
:::::::::::::::::::::::::::::::::::::::::::

Ammunition should be fully refilled after the magazine attachment is detached from a ranged weapon.