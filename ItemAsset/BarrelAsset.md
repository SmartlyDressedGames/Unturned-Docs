Barrel Assets
=============

Barrel attachments are inventory items that can be attached to ranged weapons.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to [GUID](/GUID.md) documentation.

**Type** *enum* (`Barrel`)

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

Barrel Asset Properties
-----------------------

**Ballistic_Drop** *float*: Multiplier on ballistic drop. Defaults to 1.

**Braked** *bool*: Specified if a muzzle flash should be hidden.

**Durability** *byte*: Amount of quality lost after each firing of the ranged weapon. When this value is greater than 0, the item always has a visible item quality shown. Defaults to 0.

**Gunshot_Rolloff_Distance_Multiplier** *float*: Multiplier on gunshot rolloff distance. Defaults to 0.5 if Silenced, otherwise to 1.

**Silenced** *bool*: Specified if alerts should not be generated.

**Volume** *float*: Multiplier on gunfire sound volume.
