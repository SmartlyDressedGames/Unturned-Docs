Throwable Assets
================

Throwables can be thrown by players.

This inherits the [WeaponAsset](/ItemAsset/WeaponAsset.md) class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to [GUID](/GUID.md) documentation.

**Type** *enum* (`Throwable`)

**Useable** *enum* (`Throwable`)

**ID** *uint16*: Must be a unique identifier.

Throwable Asset Properties
--------------------------

Noting this here for now, until throwables are properly documented.

Explode_On_Impact: Specified if the projectile immediately explodes upon impact.

Sticky: Specified if the projectile sticks to objects upon impact.

Fuse_Length: Timer in seconds for fuse length. Defaults to 2 seconds.

**Explosion** *uint16* or *GUID*: ID or GUID of explosion effect to play upon detonation.
