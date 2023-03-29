Arrest End Assets
=================

Releaser items are used to remove a corresponding [catcher item](/ItemAsset/ArrestStartAsset.md) that is restraining a player.

This inherits the [ItemAsset](/ItemAsset/README.md) class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to [GUID](/GUID.md) documentation.

**Type** *enum* (`Arrest_End`)

**Useable** *enum* (`Arrest_End`)

**ID** *uint16*: Must be a unique identifier.

Arrest End Asset Properties
---------------------------

**Recover** *uint16*: ID of the corresponding catcher item that can be unlocked with this item.
