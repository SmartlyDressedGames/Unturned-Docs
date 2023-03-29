Arrest Start Assets
===================

Catchers items are used to restrain players, and a corresponding [releaser item](/ItemAsset/ArrestEndAsset.md) can be used to unlock the restraints.

This inherits the [ItemAsset](/ItemAsset/README.md) class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to [GUID](/GUID.md) documentation.

**Type** *enum* (`Arrest_End`)

**Useable** *enum* (`Arrest_End`)

**ID** *uint16*: Must be a unique identifier.

Arrest Start Asset Properties
-----------------------------

**Strength** *uint16*: Number of times a player must lean in order to break free.
