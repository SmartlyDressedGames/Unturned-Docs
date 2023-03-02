Item Data (outdated)
====================

_**NOTICE:** This documentation file has been deprecated, and is no longer receiving updates. It has been superceded in favor of the [ItemAsset directory](/ItemAsset), which contains individual documentation files for each item asset class._

_This deprecated documentation file will be progressively phased out as the new documentation sources are expanded._

----

__Items__ in _Unturned_ encompass anything that can be carried in a player's in-game inventory. All items share some properties, while each item type has its own unique data. Quick links are available below.

- [Non-specific Data](#Non-specific-Data)
- [Barricades](#Barricades)
- [Fishing Poles](#Fishing-Poles)
- [Fuel Canisters](#Fuel-Canisters)
- [Growth Supplements](#Growth-Supplements)
- [Melee Weapons](#Melee-Weapons)
- [Remote Triggers](#Remote-Triggers)
- [Structures](#Structures)
- [Tools](#Tools)
- [Water Canisters](#Water-Canisters)

Non-specific Data
=================

* Refer to [README.md](/ItemAsset/README.md).

__Durability__: Either a decimal probability chance of quality loss upon action, or guaranteed loss and durability value is instead representative of the amount lost.
* _Canteens_: Guaranteed quality loss occurs upon drinking. Durability value represents the amount of quality loss.
* _Melee Weapons_: Decimal probability chance of quality loss occurs upon hitting.
* _Ranged Weapons_: Decimal probability chance of quality loss occurs upon shooting.

__Wear__: Increment to degrade quality by. Only applicable to items where durability represents a decimal probability chance of quality loss.

__Structure_Damage__: Damage dealt to structures. Multiplied by 3 in single-player.

__Invulnerable__: Specified if damage ignores structures, barricades, and vehicles that are considered invulnerable to low-power weaponry. Not applicable to explosive damage, which always ignores invulnerability.

__Range__: For ranged and melee weapons – max distance in meters before damage is no longer possible. For explosive weapons (including magazine attachments that generate explosive projectiles) – the radius of the explosion in meters.

Asset Bundles and Error Handling
--------------------------------

See [AssetBundles.md](AssetBundles.md) for full documentation regarding asset bundles.

__Ignore_TexRW__: Specified if read/writeable texture errors for the item should be hidden from the error logs.

Barricades
==========

__Type__: `Barricade`

__Useable__: `Barricade`

__Build__: `Barrel_Rain`, `Barricade`, `Bed`, `Cage`, `Campfire`, `Claim`, `Clock`, `Door`, `Fortification`, `Freeform`, `Gate`, `Glass`, `Hatch`, `Ladder`, `Mannequin`, `Note`, `Oven`, `Oxygenator`, `Safezone`, `Shutter`, `Sign`, `Sign_Wall`, `Spot`, `Stereo`, `Torch`, `Vehicle`

__Health__: Amount of health.

__Range__: Distance away the barricade can be placed from the player.

__Radius__:

__Offset__: Inherent distance above the point to place.

__Locked__: Usability/interactivity access restricted to owner.

__Explosion__: Destruction effect ID.

__Salvage_Duration_Multiplier__: Multiplier on salvage duration.

__Unpickupable__: Cannot be salvaged.

__Unrepairable__: Cannot be repaired.

__Unsalvageable__: If damaged, salvaging yields no partial ingredients.

__Unsaveable__: Cannot be saved by the game.

__Vulnerable__: Specified if the barricade can be destroyed by low-power weaponry.

__Proof_Explosion__: Specified in immune to explosion damage.

__Armor_Tier__: `High`. Doubles health value.

__Use_Water_Height_Transparent_Sort__:

__Should_Close_When_Outside_Range__: `true`. Defaults to false. Only applicable to interactive barricades that generate a UI element, such as item storages and signs.

__Allow_Collision_While_Animating__: Allows animated interactables (e.g., doors) to perform collision movement upon players.

__Allow_Placement_On_Vehicle__: `false`, `true`. Defaults to false for beds and robotic turrets.

Beacons
-------

__Type__: `Beacon`

__Useable__: `Barricade`

__Build__: `Beacon`

__Wave__: Number of zombies that must be killed.

__Rewards__: Number of rewards spawned.

__Reward_ID__: Spawn table ID for rewards.

Experience Storages
-------------------

__Type__: `Library`

__Useable__: `Barricade`

__Build__: `Library`

__Capacity__: Numerical maximum capacity of experience able to be stored.

__Tax__: Percent tax on deposits.

Generators
----------

__Type__: `Generator`

__Useable__: `Barricade`

__Build__: `Generator`

__Capacity__: Numerical maximum capacity of fuel units able to be stored.

__Wirerange__: Radius range in meters (representative of a sphere) for how large of an area is considered powered.

__Burn__: Number of seconds before one fuel unit is burned.

Item Storages
-------------

__Type__: `Storage`

__Useable__: `Barricade`

__Build__: `Storage`, `Storage_Wall`

__Storage_X__: Horizontal storage space.

__Storage_Y__: Vertical storage space.

__Display__: Stored item is visible.

Liquid Storages
---------------

__Type__: `Tank`

__Useable__: `Barricade`

__Build__: `Tank`

__Source__: `Fuel`, `Water`

__Resource__: Numerical maximum capacity of liquid units that can be stored. Water units are measured in potential drinking uses.

Oil Pumps
---------

__Type__: `Oil_Pump`

__Useable__: `Barricade`

__Build__: `Oil`

__Fuel_Capacity__: Numerical maximum capacity of fuel units able to be stored. 

Plants
------

__Type__: `Farm`

__Useable__: `Barricade`

__Build__: `Farm`

__Growth__: Number of seconds required to fully grow.

__Grow__: ID of the item generated when harvesting a fully grown plant.

Remote Explosives
-----------------

__Type__: `Charge`

__Useable__: `Barricade`

__Build__: `Charge`

__Range2__: Meter radius of range for explosive damage.

__Explosion2__: Explosion effect ID for the damaging explosion.

Limb-independent entity damage is also applicable.

Robotic Turrets
---------------

__Type__: `Sentry`, `Sentry_Freeform`

__Useable__: `Barricade`

__Build__: `Sentry`

__Storage_X__: Horizontal storage space.

__Storage_Y__: Vertical storage space.

__Display__: Stored item is visible.

__Mode__: `Friendly`, `Hostile`, `Neutral`

__Infinite_Ammo__: ammunition never depletes.

__Infinite_Quality__: Weapon quality never depletes.

Traps
-----

__Type__: `Trap`

__Useable__: `Barricade`

__Build__: `Spike`, `Wire`

__Damage_Tires__: Specified if tires can be popped when ran over by a vehicle.

__Range2__: Meter radius of range for explosive damage.

__Explosion2__: Explosion effect ID for the damaging explosion.

Limb-independent entity damage (e.g., Player_Damage) is also applicable.

Fishing Poles
=============

__Type__: `Fisher`

__Useable__: `Fisher`

__Reward_ID__: ID of the spawn table to pull catchable items from.

Fuel Canisters
==============

__Type__: `Fuel`

__Useable__: `Fuel`

__Fuel__: Amount of fuel units added to target.

Growth Supplements
==================

__Type__: `Grower`

__Useable__: `Grower`

Melee Weapons
=============

No documentation is available at this time.

Remote Triggers
===============

__Type__: `Detonator`

__Useable__: `Detonator`

Structures
==========

__Type__: `Structure`

__Useable__: `Structure`

__Construct__: `Floor`, `Floor_Poly`, `Pillar`, `Post`, `Rampart`, `Roof`, `Roof_Poly`, `Wall`

__Health__: Amount of health.

__Range__: Distance away the barricade can be placed from the player.

__Explosion__: Destruction effect ID.

__Foliage_Cut_Radius__: Numerical value in meters for the radius in which foliage is removed from around the structure. Only applicable to floor structure types.

Tools
=====

Car Jacks
---------

Car jacks launch vehicles into the air as a method of reorienting them if they were flipped over.

__Type__: `Tool`

__Useable__: `Carjack`

Car Lock Picks
--------------

Car lock picks allow players to unlock any locked vehicle, but are single-use.

__Type__: `Tool`

__Useable__: `Carlockpick`

Tire Replacements
-----------------

Tire replacements allow for adding or removing tires from four-wheeled vehicles.

__Type__: `Tire`

__Useable__: `Tire`

__Mode__: `Add`, `Remove`

Vehicle Batteries
-----------------

Vehicle batteries can be placed into vehicles, allowing them to perform activities that consume electrical energy rather than fuel. They are affected by quality.

__Type__: `Vehicle_Repair_Tool`

__Useable__: `Battery_Vehicle`

Walkie-talkies
--------------

When initiating voice chat with a walkie-talkie held, voice is transmitted through a two-way radio. An audible cue plays when initiating voice chat.

__Type__: `Tool`

__Useable__: `Walkie_Talkie`

Water Canisters
===============

__Type__: `Refill`

__Useable__: `Refill`

__Water__: The number of water to restore.
