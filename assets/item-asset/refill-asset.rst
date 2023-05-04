.. _doc_item_asset_refill:

Refill Assets
=============

Refills (localized as "water canisters") are useables able to siphon, store, and deposit water. Players can also drink from water canisters in order to restore their status bars.

This inherits the :ref:`ItemAsset <doc_item_asset_intro>` class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Refill``)

**Useable** *enum* (``Refill``)

**ID** *uint16*: Must be a unique identifier.

Refill Asset Properties
-----------------------

**ConsumeAudioClip** :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`: AudioClip to play when the consumeable is used.

.. deprecated:: 3.20.9.0 **Water** *byte*: Deprecated in favor of ``Clean_Water``. When this property is used, its value is assigned to ``Clean_Water`` instead.

Clean_Health

Salty_Health

Dirty_Health