.. _doc_item_asset_generator:

Generator Assets
================

Generators are a placeable power sources.

This inherits the :ref:`BarricadeAsset <doc_item_asset_barricade>` class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Generator``)

**Useable** *enum* (``Barricade``)

**Build** *enum* (``Generator``)

**ID** *uint16*: Must be a unique identifier.

Generator Asset Properties
--------------------------

**Capacity** *uint16*: Maximum units of fuel that can be stored in the generator. Defaults to 0.

**Wirerange** *float* [0, 256]: In meters, the radius around the generator that is provided electricity.

**Burn** *float*: How many seconds it takes to burn one unit of fuel.
