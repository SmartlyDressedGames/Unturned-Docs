.. _doc_item_asset_tank:

Tank Assets
===========

Tanks (localized as "liquid storages") are placeables used to store water or fuel. Players can siphon from, or deposit into, a liquid storage with certain items. Fuel tanks require a :ref:`fuel canister <doc_item_asset_fuel>`, while water tanks require a :ref:`water canister <doc_item_asset_refill>`.

This inherits the :ref:`BarricadeAsset <doc_item_asset_barricade>` class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Tank``)

**Useable** *enum* (``Barricade``)

**Build** *enum* (``Tank``)

**ID** *uint16*: Must be a unique identifier.

Tank Asset Properties
---------------------

**Resource** *uint16*: Maximum units of liquid that can be stored in the tank. One unit of water is the equivalent of one usage of a water canister. Defaults to 0.

**Source** *enum* (``Fuel``, ``None``, ``Water``): Type of liquid that can be stored in the tank.