.. _doc_item_asset_library:

Library Assets
==============

Libraries are placeable storage containers for experience points.

This inherits the :ref:`BarricadeAsset <doc_item_asset_barricade>` class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Library``)

**Useable** *enum* (``Barricade``)

**Build** *enum* (``Library``)

**ID** *uint16*: Must be a unique identifier.

Library Asset Properties
------------------------

**Capacity** *uint32*: Maximum amount of experience points that can be stored.

**Tax** *byte*: Percentage of the deposit that is taxed. Defaults to 0.
