.. _doc_item_asset_trap:

Trap Assets
===========

Traps are placeable damage sources.

This inherits the :ref:`BarricadeAsset <doc_item_asset_barricade>` class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Trap``)

**Useable** *enum* (``Barricade``)

**Build** *enum* (``Spike``, ``Wire``)

**ID** *uint16*: Must be a unique identifier.

Trap Asset Properties
---------------------

**Animal_Damage** *float*: Damage dealt to animals caught within the area-of-effect explosion.

**Barricade_Damage** *float*: Damage dealt to barricades caught within the area-of-effect explosion.

**Broken** *flag*: Players who trigger the trap will be inflicted with the `Broken Bones <https://wiki.smartlydressedgames.com/wiki/Broken%20Bones>`_ status effect.

**Damage_Tires** *flag*: This trap can pop the tires of vehicles that drive over it.

**Explosion_Launch_Speed** *float*: Launch speed of players caught within the area-of-effect explosion, in meters per second. Defaults to the value of ``Player_Damage * 0.1``.

**Explosion2** *uint16* or *GUID*: ID or GUID of effect to play upon detonation.

**Explosive** *flag*: Specified if the trap should have an area-of-effect explosion when triggered.

**Object_Damage** *float*: Damage dealt to objects caught within the area-of-effect explosion. Defaults to the value of ``Resource_Damage``.

**Player_Damage** *float*: Damage dealt to players caught within the area-of-effect explosion.

**Range2** *float*: In meters, the radius of the damaging, area-of-effect explosion.

**Resource_Damage** *float*: Damage dealt to resources caught within the area-of-effect explosion.

**Structure_Damage** *float*: Damage dealt to structures caught within the area-of-effect explosion.

**Trap_Cooldown** *float*: In seconds, the time until trap is active again.

**Trap_Setup_Delay** *float*: In seconds, delay before a trap becomes active after being placed. Defaults to 0.25 seconds.

**Vehicle_Damage** *float*: Damage dealt to vehicles caught within the area-of-effect explosion.
