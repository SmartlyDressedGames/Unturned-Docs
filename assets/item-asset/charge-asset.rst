.. _doc_item_asset_charge:

Charge Assets
=============

Remote explosives can be placed and then remotely detonated with a :ref:`remote trigger <doc_item_asset_detonator>`.

This inherits the :ref:`BarricadeAsset <doc_item_asset_barricade>` class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Charge``)

**Useable** *enum* (``Barricade``)

**Build** *enum* (``Charge``)

**ID** *uint16*: Must be a unique identifier.

Charge Asset Properties
-----------------------

**Animal_Damage** *float*: 

**Barricade_Damage** *float*: 

**Explosion_2** *uint16* or *GUID*: ID or GUID of effect to play upon detonation.

**Explosion_Launch_Speed** *float*: 

**Object_Damage** *float*: 

**Player_Damage** *float*: 

**Resource_Damage** *float*: 

**Structure_Damage** *float*: 

**Vehicle_Damage** *float*: 

**Range2** *float*: 

**Zombie_Damage** *float*: 
