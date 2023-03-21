Arrest Start Assets
===================

Catchers items are used to restrain players, and a corresponding `releaser item <ArrestEndAsset.rst>`_ can be used to unlock the restraints.

This inherits the `ItemAsset <README.rst>`_ class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to `GUID <GUID.rst>`_ documentation.

**Type** *enum* (``Arrest_End``)

**Useable** *enum* (``Arrest_End``)

**ID** *uint16*: Must be a unique identifier.

Arrest Start Asset Properties
-----------------------------

**Strength** *uint16*: Number of times a player must lean in order to break free.
