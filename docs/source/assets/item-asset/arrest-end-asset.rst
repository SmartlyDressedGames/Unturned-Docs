.. _doc_item_asset_arrest_end:

Arrest End Assets
=================

Releaser items are used to remove a corresponding :ref:`catcher item <doc_item_asset_arrest_start>` that is restraining a player.

This inherits the :ref:`ItemAsset <doc_item_asset_intro>` class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Arrest_End``)

**Useable** *enum* (``Arrest_End``)

**ID** *uint16*: Must be a unique identifier.

Arrest End Asset Properties
---------------------------

**Recover** *uint16*: ID of the corresponding catcher item that can be unlocked with this item.
