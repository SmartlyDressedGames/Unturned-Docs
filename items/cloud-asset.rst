.. _doc_item_asset_cloud:

Cloud Assets
============

Clouds (or "parachutes") are created from the ItemCloudAsset class. They can affect a player's gravity when held.

This inherits the :ref:`ItemAsset <doc_item_asset_intro>` class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Cloud``)

**Useable** *enum* (``Cloud``)

**ID** *uint16*: Must be a unique identifier.

Cloud Asset Properties
----------------------

**Gravity** *float*: Multiplier on the influence of gravity.
