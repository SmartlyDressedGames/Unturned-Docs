Sight Assets
============

Sight attachments are inventory items that can be attached to ranged weapons.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to [GUID](GUID.md) documentation.

**Type** *enum* (`Sight`)

**ID** *uint16*: Must be a unique identifier.

Sight Asset Properties
----------------------

**Holographic** *bool*: Specified if sight is holographic.

**Vision** *enum* (`None`, `Military`, `Civilian`, `Headlamp`): Type of unique lighting vision effect to use. Defaults to None.

**Zoom** *float*: Multiplicative amount of zoom. Defaults to 1.
