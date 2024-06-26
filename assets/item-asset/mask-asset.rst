.. _doc_item_asset_mask:

Mask Assets
===========

Masks can be worn by players and zombies.

This inherits the :ref:`GearAsset <doc_item_asset_gear>` class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Mask``)

**Useable** *enum* (``Clothing``)

**ID** *uint16*: Must be a unique identifier.

Mask Asset Properties
---------------------

**Earpiece** *flag*: Specified if mask allows for listening on communications by walkie-talkie.

**FilterDegradationRateMultiplier** *float32*: Multiplier for how quickly deadzones deplete a gasmask's filter quality. For example, 2 is faster (2x) and 0.5 is slower.
