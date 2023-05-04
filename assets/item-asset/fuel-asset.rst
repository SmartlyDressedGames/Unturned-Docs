.. _doc_item_asset_fuel:

Fuel Assets
===========

Fuel canisters are useables able to siphon, store, and deposit fuel.

This inherits the :ref:`ItemAsset <doc_item_asset_intro>` class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Fuel``)

**Useable** *enum* (``Fuel``)

**ID** *uint16*: Must be a unique identifier.

Fuel Asset Properties
---------------------

**Always_Spawn_Full** *bool*: If true, this item will always spawn filled at full capacity.

**Delete_After_Filling_Target** *bool*: If true, this item is removed from the player's inventory after adding fuel to target.

**Fuel** *uint16*: Maximum units of fuel that can be stored in the fuel canister.