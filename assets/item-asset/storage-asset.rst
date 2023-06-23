.. _doc_item_asset_storage:

Storage Assets
==============

Storages (localized as "item storages") are placeables used to store items.

This inherits the :ref:`BarricadeAsset <doc_item_asset_barricade>` class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Storage``)

**Useable** *enum* (``Barricade``)

**Build** *enum* (``Storage``, ``Storage_Wall``)

**ID** *uint16*: Must be a unique identifier.

Storage Asset Properties
------------------------

**Display** *flag*: If specified, the first item in the storage will be visibly displayed.

**Should_Close_When_Outside_Range** *bool*: Whether or not the storage should automatically close when the player is outside of the interaction range. Defaults to false.

**Storage_X** *byte*: Number of columns (horizontal storage space). Defaults to 0.

**Storage_Y** *byte*: Number of rows (vertical storage space). Defaults to 0.