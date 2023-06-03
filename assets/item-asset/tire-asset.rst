.. _doc_item_asset_tire:

Tire Assets
===========

Tires (localized as "tools") are useables that allow for adding and removing tires from vehicles.

This inherits the :ref:`VehicleRepairToolAsset <doc_item_asset_vehicle_repair_tool>` class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Tire``)

**Useable** *enum* (``Tire``)

**ID** *uint16*: Must be a unique identifier.

Tire Asset Properties
---------------------

**Mode** *enum* (``Add``, ``Remove``): How the usable should interact with tires. ``Mode Add`` will consume the item to add a tire to the vehicle. ``Mode Remove`` allows the usable to remove tires, adding the corresponding item to the player's inventory.