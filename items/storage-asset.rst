.. _doc_item_asset_storage:

Storage Assets
==============

Storages (localized as "item storages") are created from the ItemStorageAsset class. They are placeables used to store items.

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

**Default_Contained_Items** *list of dictionaryies*: Items to create inside storage when first spawned. Each item can contain the following properties:

- **Asset**: :ref:`Asset Pointer <doc_data_assetptr>`: Item or spawn table to grant an item from.

- **Amount** *int*: Number of times to grant this item. Defaults to 1.

- **Origin** :ref:`EItemOrigin <doc_data_eitemorigin>`: Determines starting state of the item. Defaults to World.
