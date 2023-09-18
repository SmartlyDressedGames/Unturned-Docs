.. _doc_item_asset_magazine:

Magazine Assets
===============

Magazine attachments are inventory items that can be attached to ranged weapons.

This inherits the :ref:`CaliberAsset <doc_item_asset_caliber>` class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Magazine``)

**ID** *uint16*: Must be a unique identifier.

Magazine Asset Properties
-------------------------

**Pellets** *byte*: Number of bullet rays shot. Defaults to 1.

**Projectile_Damage_Multiplier** *float*: Multiplier on the damage dealt by projectile weapons.

**Projectile_Blast_Radius_Multiplier** *float*: Multiplier on the blast radius of projectiles fired from projectile weapons.

**Projectile_Launch_Force_Multiplier** *float*: Multiplier on the launch force applied to projectiles fired from projectile weapons.

**Speed** *float*: Multiplier on reload speed. Defaults to 1.

**Stuck** *byte*: Amount of quality to lose when hit. When this value is greater than 0, fired projectiles can be picked back up until their quality reaches 0. Defaults to 0.

**Explosive** *flag*: Specified if it should cause an area-of-effect explosion.

**Range** *float*: Radius of the area-of-effect explosion.

**Player_Damage** *float*: Damage dealt to players caught in the area-of-effect explosion.

**Zombie_Damage** *float*: Damage dealt to zombies caught in the area-of-effect explosion.

**Animal_Damage** *float*: Damage dealt to animals caught in the area-of-effect explosion.

**Barricade_Damage** *float*: Damage dealt to barricades caught in the area-of-effect explosion.

**Structure_Damage** *float*: Damage dealt to structures caught in the area-of-effect explosion.

**Vehicle_Damage** *float*: Damage dealt to vehicles caught in the area-of-effect explosion.

**Resource_Damage** *float*: Damage dealt to resources caught in the area-of-effect explosion.

**Object_Damage** *float*: Damage dealt to objects caught in the area-of-effect explosion. Defaults to the value used by ``Resource_Damage``.

**Explosion_Launch_Speed** *float*: Launch speed of players caught within the area-of-effect explosion, in meters per second. Defaults to the resulting value from ``Player_Damage * 0.1``. 

**Explosion** *uint16* or *GUID*: ID or GUID of explosion effect. Defaults to 0.

**Spawn_Explosion_On_Dedicated_Server** *bool*: Specified to spawn the explosion effect on the server.

**Tracer** *uint16* or *GUID*: ID or GUID of bullet tracer effect. Defaults to 0.

**Impact** *uint16* or *GUID*: ID or GUID of effect to play on impact. Defaults to 0.

**Delete_Empty** *flag*: Specified if the magazine attachment should be deleted when it is fully depleted.

**Should_Fill_After_Detach** *bool*: Ammunition should be fully refilled after the magazine attachment is detached from a ranged weapon. Defaults to false.
