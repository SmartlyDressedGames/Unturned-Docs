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


**Explosive** *flag*: Robotic turrets using `Mode Friendly` will target players holding a throwable that has this flag.

**Flash** *flag*: Robotic turrets using `Mode Friendly` will target players holding a throwable that has this flag.

**Sticky** *flag*:

**Explode_On_Impact** *flag*: Robotic turrets using `Mode Friendly` will target players holding a throwable that has this flag.


Noting this here for now, until throwables are properly documented.

Explosive: Specified if the explosive component is used.

Explode_On_Impact: Specified if the projectile immediately explodes upon impact.

Sticky: Specified if the projectile sticks to objects upon impact.

Fuse_Length: Timer in seconds for fuse length. Defaults to 2 seconds.

**Explosion** *uint16* or *GUID*: ID or GUID of explosion effect to play upon detonation.
