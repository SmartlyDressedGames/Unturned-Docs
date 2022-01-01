Magazine Assets
===============

Magazine attachments are inventory items that can be attached to ranged weapons.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to [GUID](/GUID.md) documentation.

**Type** *enum* (`Magazine`)

**ID** *uint16*: Must be a unique identifier.

Caliber Asset Properties
------------------------

**Ballistic_Damage_Multiplier** *float*: Multiplier on damage. Defaults to the value used for the Damage property.

**Calibers** *uint16*: Total amount of unique calibers.

**Caliber_#** *uint16*: Caliber ID for acceptable attachment compatibility.

**Damage** *float*: Multiplier on damage. Defaults to 1. Deprecated in favor of Ballistic_Damage_Multiplier.

**Firerate** *byte*: Amount to decrease ranged weapon's firerate value by. Decreasing by a larger value will allow the ranged weapon to fire more often.

**Paintable** *bool*: Specified if the attachment should be affected by Steam Economy ranged weapon skins that include support for attachments.

**Recoil_X** *float*: Multiplier on horizontal recoil.

**Recoil_Y** *float*: Multiplier on vertical recoil.

**Shake** *float*: Multiplier on shake.

**Spread** *float*: Multiplier on spread.

**Sway** *float*: Multiplier on sway.

Magazine Asset Properties
-------------------------

**Pellets** *byte*: Number of bullet rays shot. Defaults to 1.

**Projectile_Damage_Multiplier** *float*: Multiplier on the damage dealt by projectile weapons.

**Projectile_Blast_Radius_Multiplier** *float*: Multiplier on the blast radius of projectiles fired from projectile weapons.

**Projectile_Launch_Force_Multiplier** *float*: Multiplier on the launch force applied to projectiles fired from projectile weapons.

**Speed** *float*: Multiplier on reload speed. Defaults to 1.

**Stuck** *byte*: Amount of quality to lose when hit. When this value is greater than 0, fired projectiles can be picked back up until their quality reaches 0. Defaults to 0.

**Explosive** *bool*: Specified if it should cause an area-of-effect explosion.

**Range** *float*: Radius of the area-of-effect explosion.

**Player_Damage** *float*: Damage dealt to players caught in the area-of-effect explosion.

**Zombie_Damage** *float*: Damage dealt to zombies caught in the area-of-effect explosion.

**Animal_Damage** *float*: Damage dealt to animals caught in the area-of-effect explosion.

**Barricade_Damage** *float*: Damage dealt to barricades caught in the area-of-effect explosion.

**Structure_Damage** *float*: Damage dealt to structures caught in the area-of-effect explosion.

**Vehicle_Damage** *float*: Damage dealt to vehicles caught in the area-of-effect explosion.

**Resource_Damage** *float*: Damage dealt to resources caught in the area-of-effect explosion.

**Object_Damage** *float*: Damage dealt to zombies caught in the area-of-effect explosion. Defaults to the value used by Resource_Damage.

**Explosion_Launch_Speed** *float*: Launch speed of players caught within the area-of-effect explosion, in meters per second. Defaults to the resulting value from Player_Damage * 0.1. 

**Explosion** *uint16*: Explosion effect ID. Defaults to 0.

**Spawn_Explosion_On_Dedicated_Server** *bool*: Specified to spawn the explosion effect on the server.

**Tracer** *uint16*: Tracer effect ID. Defaults to 0.

**Impact** *uint16*: Impact effect ID. Defaults to 0.

**Delete_Empty** *bool*: Specified if the magazine attachment should be deleted when it is fully depleted.

**Should_Fill_After_Detach** *bool*: Ammunition should be fully refilled after the magazine attachment is detached from a ranged weapon. Defaults to false.
