.. _doc_assets_itemdata:

Item Data (outdated)
====================

.. warning::
	
	This documentation file has been deprecated, and is no longer receiving updates. It has been superseded in favor of the `item-asset directory <item-asset>`_, which contains individual documentation files for each item asset class.
	
	This deprecated documentation file will be progressively phased out as the new documentation sources are expanded.

----

**Items** in *Unturned* encompass anything that can be carried in a player's in-game inventory. All items share some properties, while each item type has its own unique data.

Non-specific Data
-----------------

* Refer to :ref:`doc_item_asset_intro` instead.

**Durability**: Either a decimal probability chance of quality loss upon action, or guaranteed loss and durability value is instead representative of the amount lost.

* *Canteens*: Guaranteed quality loss occurs upon drinking. Durability value represents the amount of quality loss.
* *Melee Weapons*: Decimal probability chance of quality loss occurs upon hitting.
* *Ranged Weapons*: Decimal probability chance of quality loss occurs upon shooting.

**Wear**: Increment to degrade quality by. Only applicable to items where durability represents a decimal probability chance of quality loss.

**Structure_Damage**: Damage dealt to structures. Multiplied by 3 in single-player.

**Invulnerable**: Specified if damage ignores structures, barricades, and vehicles that are considered invulnerable to low-power weaponry. Not applicable to explosive damage, which always ignores invulnerability.

**Range**: For ranged and melee weapons – max distance in meters before damage is no longer possible. For explosive weapons (including magazine attachments that generate explosive projectiles) – the radius of the explosion in meters.

Asset Bundles and Error Handling
````````````````````````````````

See :ref:`Asset Bundles <doc_asset_bundles>` for full documentation regarding asset bundles.

Barricades
----------

**Build**: ``Barrel_Rain``, ``Bed``, ``Cage``, ``Campfire``, ``Claim``, ``Clock``, ``Door``, ``Fortification``, ``Freeform``, ``Gate``, ``Glass``, ``Hatch``, ``Ladder``, ``Mannequin``, ``Note``, ``Oven``, ``Oxygenator``, ``Safezone``, ``Shutter``, ``Sign``, ``Sign_Wall``, ``Spot``, ``Stereo``, ``Torch``, ``Vehicle``

Item Storages
`````````````

**Type**: ``Storage``

**Useable**: ``Barricade``

**Build**: ``Storage``, ``Storage_Wall``

**Storage_X**: Horizontal storage space.

**Storage_Y**: Vertical storage space.

**Display**: Stored item is visible.

**Should_Close_When_Outside_Range**: ``true``. Defaults to false. Only applicable to interactive barricades that generate a UI element, such as item storages and signs.

Liquid Storages
```````````````

**Type**: ``Tank``

**Useable**: ``Barricade``

**Build**: ``Tank``

**Source**: ``Fuel``, ``Water``

**Resource**: Numerical maximum capacity of liquid units that can be stored. Water units are measured in potential drinking uses.

Oil Pumps
`````````

**Type**: ``Oil_Pump``

**Useable**: ``Barricade``

**Build**: ``Oil``

**Fuel_Capacity**: Numerical maximum capacity of fuel units able to be stored. 

Plants
``````

**Type**: ``Farm``

**Useable**: ``Barricade``

**Build**: ``Farm``

**Growth**: Number of seconds required to fully grow.

**Grow**: ID of the item generated when harvesting a fully grown plant.

Remote Explosives
`````````````````

**Type**: ``Charge``

**Useable**: ``Barricade``

**Build**: ``Charge``

**Range2**: Meter radius of range for explosive damage.

**Explosion2**: Explosion effect ID for the damaging explosion.

Limb-independent entity damage is also applicable.

Robotic Turrets
```````````````

**Type**: ``Sentry``, ``Sentry_Freeform``

**Useable**: ``Barricade``

**Build**: ``Sentry``

**Storage_X**: Horizontal storage space.

**Storage_Y**: Vertical storage space.

**Display**: Stored item is visible.

**Mode**: ``Friendly``, ``Hostile``, ``Neutral``

**Infinite_Ammo**: ammunition never depletes.

**Infinite_Quality**: Weapon quality never depletes.

Traps
`````

**Type**: ``Trap``

**Useable**: ``Barricade``

**Build**: ``Spike``, ``Wire``

**Damage_Tires**: Specified if tires can be popped when ran over by a vehicle.

**Range2**: Meter radius of range for explosive damage.

**Explosion2**: Explosion effect ID for the damaging explosion.

Limb-independent entity damage (e.g., Player_Damage) is also applicable.

Fishing Poles
-------------

**Type**: ``Fisher``

**Useable**: ``Fisher``

**Reward_ID**: ID of the spawn table to pull catchable items from.

Fuel Canisters
--------------

**Type**: ``Fuel``

**Useable**: ``Fuel``

**Fuel**: Amount of fuel units added to target.

Growth Supplements
------------------

**Type**: ``Grower``

**Useable**: ``Grower``

Structures
----------

**Type**: ``Structure``

**Useable**: ``Structure``

**Construct**: ``Floor``, ``Floor_Poly``, ``Pillar``, ``Post``, ``Rampart``, ``Roof``, ``Roof_Poly``, ``Wall``

**Health**: Amount of health.

**Range**: Distance away the barricade can be placed from the player.

**Explosion**: Destruction effect ID.

**Foliage_Cut_Radius**: Numerical value in meters for the radius in which foliage is removed from around the structure. Only applicable to floor structure types.

Tools
-----

Car Jacks
`````````

Car jacks launch vehicles into the air as a method of reorienting them if they were flipped over.

**Type**: ``Tool``

**Useable**: ``Carjack``

Car Lock Picks
``````````````

Car lock picks allow players to unlock any locked vehicle, but are single-use.

**Type**: ``Tool``

**Useable**: ``Carlockpick``

Tire Replacements
`````````````````

Tire replacements allow for adding or removing tires from four-wheeled vehicles.

**Type**: ``Tire``

**Useable**: ``Tire``

**Mode**: ``Add``, ``Remove``

Vehicle Batteries
`````````````````

Vehicle batteries can be placed into vehicles, allowing them to perform activities that consume electrical energy rather than fuel. They are affected by quality.

**Type**: ``Vehicle_Repair_Tool``

**Useable**: ``Battery_Vehicle``

Walkie-talkies
``````````````

When initiating voice chat with a walkie-talkie held, voice is transmitted through a two-way radio. An audible cue plays when initiating voice chat.

**Type**: ``Tool``

**Useable**: ``Walkie_Talkie``

Water Canisters
---------------

**Type**: ``Refill``

**Useable**: ``Refill``

**Water**: The number of water to restore.
