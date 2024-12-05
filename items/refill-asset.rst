.. _doc_item_asset_refill:

Refill Assets
=============

Refills (localized as "water canisters") are useables able to siphon, store, and deposit water. Players can also drink from water canisters in order to restore their status bars. Water canisters have four potential states: empty, salty, dirty, or clean.

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

**Clean_Food** *float*: Amount of food restored when drinking clean water.

**Clean_Health** *float*: Amount of health restored when drinking clean water.

**Clean_Oxygen** *float*: Amount of oxygen restored when drinking clean water.

**Clean_Stamina** *float*: Amount of stamina restored when drinking clean water.

**Clean_Virus** *float*: Amount of immunity depleted when drinking clean water.

**Clean_Water** *float*: Amount of water restored when drinking clean water.

**Dirty_Food** *float*: Amount of food restored when drinking dirty water. Defaults to the result of ``Clean_Food * 0.6``.

**Dirty_Health** *float*: Amount of health restored when drinking dirty water. Defaults to the result of ``Clean_Health * 0.6``.

**Dirty_Oxygen** *float*: Amount of oxygen restored when drinking dirty water. Defaults to the result of ``Clean_Oxygen * 0.6``.

**Dirty_Stamina** *float*: Amount of stamina restored when drinking dirty water. Defaults to the result of ``Clean_Stamina * 0.6``.

**Dirty_Virus** *float*: Amount of immunity depleted when drinking dirty water. Defaults to the result of ``Clean_Virus * -0.399999976``.

**Dirty_Water** *float*: Amount of water restored when drinking dirty water. Defaults to the result of ``Clean_Water * 0.6``.

**Salty_Food** *float*: Amount of food restored when drinking salty water. Defaults to the result of ``Clean_Food * 0.25``.

**Salty_Health** *float*: Amount of health restored when drinking salty water. Defaults to the result of ``Clean_Health * 0.25``.

**Salty_Oxygen** *float*: Amount of oxygen restored when drinking salty water. Defaults to the result of ``Clean_Oxygen * 0.25``.

**Salty_Stamina** *float*: Amount of stamina restored when drinking salty water. Defaults to the result of ``Clean_Stamina * 0.25``.

**Salty_Virus** *float*: Amount of immunity depleted when drinking salty water. Defaults to the result of ``Clean_Virus * -0.75``.

**Salty_Water** *float*: Amount of water restored when drinking salty water. Defaults to the result of ``Clean_Water * 0.25``.

.. deprecated:: 3.20.9.0 **Water** *byte*: Deprecated in favor of ``Clean_Water``. When this property is used, its value is assigned to ``Clean_Water`` instead.