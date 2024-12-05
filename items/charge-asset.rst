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

**Animal_Damage** *float*: Damage dealt to animals caught within the area-of-effect explosion.

**Barricade_Damage** *float*: Damage dealt to barricades caught within the area-of-effect explosion.

**Explosion2** *uint16* or *GUID*: ID or GUID of effect to play upon detonation.

**Explosion_Launch_Speed** *float*: Launch speed of players caught within the area-of-effect explosion, in meters per second. Defaults to the value of ``Player_Damage * 0.1``.

**Object_Damage** *float*: Damage dealt to objects caught within the area-of-effect explosion. Defaults to the value of ``Resource_Damage``.

**Player_Damage** *float*: Damage dealt to players caught within the area-of-effect explosion.

**Resource_Damage** *float*: Damage dealt to resources caught within the area-of-effect explosion.

**Structure_Damage** *float*: Damage dealt to structures caught within the area-of-effect explosion.

**Vehicle_Damage** *float*: Damage dealt to vehicles caught within the area-of-effect explosion.

**Range2** *float*: Radius of the damaging, area-of-effect explosion.

**Zombie_Damage** *float*: Damage dealt to zombies caught within the area-of-effect explosion.
