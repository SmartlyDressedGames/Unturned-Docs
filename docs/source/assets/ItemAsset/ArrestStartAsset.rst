.. _doc_itemasset_arreststart:

Arrest Start Assets
===================

Catchers items are used to restrain players, and a corresponding :ref:`releaser item <doc_itemasset_arrestend>` can be used to unlock the restraints.

This inherits the :ref:`ItemAsset <doc_itemasset_intro>` class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Arrest_End``)

**Useable** *enum* (``Arrest_End``)

**ID** *uint16*: Must be a unique identifier.

Arrest Start Asset Properties
-----------------------------

**Strength** *uint16*: Number of times a player must lean in order to break free.
