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

**Explosion** *uint16* or *GUID*: ID or GUID of explosion effect to play upon detonation.

**Fuse_Length** *float*: A timer, in seconds, for the fuse length. Defaults to 180 seconds. If the throwable has the `Explosive` flag or the `Flash` flag, then it defaults to 2.5 seconds instead.


**Explosive** *flag*: Specified if the throwable should have an area-of-effect explosion. Robotic turrets using `Mode Friendly` will target players holding a throwable that has this flag.

**Flash** *flag*: Specified if the throwable should cause a flashbang effect to players within the area-of-effect. Robotic turrets using `Mode Friendly` will target players holding a throwable that has this flag.

**Sticky** *flag*:

**Explode_On_Impact** *flag*: Robotic turrets using `Mode Friendly` will target players holding a throwable that has this flag.


**Explosion_Launch_Speed** *float*: Defaults to `Player_Damage × 0.1`.

**Strong_Throw_Force** *float*: Defaults to 1100.

**Weak_Throw_Force** *float*: Defaults to 600.

**Boost_Throw_Force_Multiplier** *float*: Defaults to 1.4.



Noting this here for now, until throwables are properly documented.

Explosive: Specified if the explosive component is used.

Explode_On_Impact: Specified if the projectile immediately explodes upon impact.

Sticky: Specified if the projectile sticks to objects upon impact.
