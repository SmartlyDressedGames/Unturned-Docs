Throwable Assets
================

Throwables can be thrown by players. Throwables cannot be used in any safezones that disallow weapons.

This inherits the [WeaponAsset](/ItemAsset/WeaponAsset.md) class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to [GUID](/GUID.md) documentation.

**Type** *enum* (`Throwable`)

**Useable** *enum* (`Throwable`)

**ID** *uint16*: Must be a unique identifier.

Throwable Asset Properties
--------------------------

**Boost_Throw_Force_Multiplier** *float*: A multiplier on the amount of throwing force when the player has the "Olympic" random boost. Defaults to 1.4.

**Explode_On_Impact** *flag*: Specified if the throwable should immediately detonate upon impact. Robotic turrets using `Mode Friendly` will target players holding a throwable that has this flag.

**Explosion** *uint16* or *GUID*: ID or GUID of explosion effect to play upon detonation.

**Explosion_Launch_Speed** *float*: Velocity at which players are launched by area-of-effect explosions. Defaults to `Player_Damage × 0.1`.

**Explosive** *flag*: Specified if the throwable should have an area-of-effect explosion. Robotic turrets using `Mode Friendly` will target players holding a throwable that has this flag.

**Flash** *flag*: Specified if the throwable should cause a flashbang effect for players caught within the area-of-effect. Robotic turrets using `Mode Friendly` will target players holding a throwable that has this flag.

**Fuse_Length** *float*: A timer, in seconds, for the fuse length. Defaults to 180 seconds. If the throwable has the `Explosive` flag or the `Flash` flag, then it defaults to 2.5 seconds instead.

**Sticky** *flag*: Specified if the throwable should stick to the environment, barricades, and structures.

**Strong_Throw_Force** *float*: The amount of force throwables are thrown with when performing a strong throw, measured in Newtons. Defaults to 1100.

**Weak_Throw_Force** *float*: The amount of force throwables are thrown with when performing a weak throw, measured in Newtons. Defaults to 600.
