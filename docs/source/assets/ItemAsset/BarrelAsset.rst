.. _doc_itemasset_barrel:

Barrel Assets
=============

Barrel attachments are inventory items that can be attached to ranged weapons.

This inherits the :ref:`CaliberAsset <doc_itemasset_caliber>` class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Barrel``)

**ID** *uint16*: Must be a unique identifier.

Barrel Asset Properties
-----------------------

**Ballistic_Drop** *float*: Multiplier on ballistic drop. Defaults to 1.

**Braked** *flag*: Specified if a muzzle flash should be hidden.

**Durability** *byte*: Amount of quality lost after each firing of the ranged weapon. When this value is greater than 0, the item always has a visible item quality shown. Defaults to 0.

**Gunshot_Rolloff_Distance_Multiplier** *float*: Multiplier on gunshot rolloff distance. Defaults to 0.5 if Silenced, otherwise to 1.

**Silenced** *flag*: Specified if alerts should not be generated.

**Volume** *float*: Multiplier on gunfire sound volume.
