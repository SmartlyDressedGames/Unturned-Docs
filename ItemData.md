_**NOTICE:** This documentation file has been deprecated, and is no longer receiving updates. It has been superceded in favor of the [ItemAsset directory](/ItemAsset), which contains individual documentation files for each item asset class._

_This deprecated documentation file will be progressively phased out as the new documentation sources are expanded._

----

__Items__ in _Unturned_ encompass anything that can be carried in a player's in-game inventory. All items share some properties, while each item type has its own unique data. Quick links are available below.

- [Non-specific Data](#Non-specific-Data)
- [Attachments](#Attachments)
- [Barricades](#Barricades)
- [Clothing](#Clothing)
- [Consumables](#Consumables)
- [Crafting Supplies](#Crafting-Supplies)
- [Fishing Poles](#Fishing-Poles)
- [Fuel Canisters](#Fuel-Canisters)
- [Growth Supplements](#Growth-Supplements)
- [Mapping Equipment](#Mapping-Equipment)
- [Melee Weapons](#Melee-Weapons)
- [Optics](#Optics)
- [Parachutes](#Parachutes)
- [Projectiles](#Projectiles)
- [Radiation Filters](#Radiation-Filters)
- [Ranged Weapons](#Ranged-Weapons)
- [Remote Triggers](#Remote-Triggers)
- [Restraining Devices](#Restraining-Devices)
- [Structures](#Structures)
- [Tools](#Tools)
- [Water Canisters](#Water-Canisters)

Non-specific Data
=================

* Refer to [README.md](/ItemAsset/README.md).

Quality
-------

__Quality_Min__: The minimum quality to generate. Set to 10 by default.

__Quality_Max__: The maximum quality to generate. Set to 90 by default.

__Override_Show_Quality__:

__Durability__: Either a decimal probability chance of quality loss upon action, or guaranteed loss and durability value is instead representative of the amount lost.

* _Canteens_: Guaranteed quality loss occurs upon drinking. Durability value represents the amount of quality loss.
* _Melee Weapons_: Decimal probability chance of quality loss occurs upon hitting.
* _Ranged Weapons_: Decimal probability chance of quality loss occurs upon shooting.

__Wear__: Increment to degrade quality by. Only applicable to items where durability represents a decimal probability chance of quality loss.

Damage
------

Damage data can be utilized by explosive consumables, explosive throwables, traps, remote explosives, melee weapons, and ranged weapons.

__Player_Damage__: Base damage dealt to player entities, prior to calculating limb modifiers, and used independently from limb modifiers for explosive and trap damage.

__Player_Leg_Multiplier__: The multiplier of player_damage against player legs.

__Player_Arm_Multiplier__: The multiplier of player_damage against player arms.

__Player_Spine_Multiplier__: The multiplier of player_damage against player torso.

__Player_Skull_Multiplier__: The multiplier of player_damage against player head.

__Instakill_Headshots__: `false`, `true`. Defaults to false. If true, headshots bypass hat armor on servers with Allow_Instakill_Headshots enabled.

__Player_Damage_Bleeding__: `Always`, `Default`, `Heal`, `Never`

__Player_Damage_Bones__: `Always`, `Heal`, `None`

__Player_Damage_Food__: Damage dealt to a player's food.

__Player_Damage_Water__: Damage dealt to a player's water.

__Player_Damage_Virus__: Damage dealt to a player's immunity.

__Player_Damage_Hallucination__: Length of hallucinations inflicted upon a player.

__Zombie_Damage__: Base damage dealt to zombie entities, prior to calculating limb modifiers, and used independently from limb modifiers for explosive and trap damage.

__Zombie_Leg_Multiplier__: The multiplier of zombie_damage against zombie legs.

__Zombie_Arm_Multiplier__: The multiplier of zombie_damage against zombie arms.

__Zombie_Spine_Multiplier__: The multiplier of zombie_damage against zombie torso.

__Zombie_Skull_Multiplier__: The multiplier of zombie_damage against zombie head.

__Animal_Damage__: Base damage dealt to animal entities, prior to calculating limb modifiers, and used independently from limb modifiers for explosive and trap damage.

__Animal_Leg_Multiplier__: The multiplier of animal_damage against animal limbs.

__Animal_Spine_Multiplier__: The multiplier of animal_damage against animal torso.

__Animal_Skull_Multiplier__: The multiplier of animal_damage against animal head.

__Barricade_Damage__: Damage dealt to barricades.

__Structure_Damage__: Damage dealt to structures. Multiplied by 3 in single-player.

__Vehicle_Damage__: Damage dealt to vehicles.

__Resource_Damage__: Damage dealt to resources.

__Object_Damage__: Damage dealt to objects.

__Invulnerable__: Specified if damage ignores structures, barricades, and vehicles that are considered invulnerable to low-power weaponry. Not applicable to explosive damage, which always ignores invulnerability.

__Range__: For ranged and melee weapons – max distance in meters before damage is no longer possible. For explosive weapons (including magazine attachments that generate explosive projectiles) – the radius of the explosion in meters.

__Explosive__: Specified if the explosive component is used.

__Explosion__: The visual effect ID to play as the explosion.

__Spawn_Explosion_On_Dedicated_Server__:

Asset Bundles and Error Handling
--------------------------------

See [AssetBundles.md](AssetBundles.md) for full documentation regarding asset bundles.

__Ignore_TexRW__: Specified if read/writeable texture errors for the item should be hidden from the error logs.

Attachments
===========

* Refer to [BarrelAsset.md](/ItemAsset/BarrelAsset.md).
* Refer to [GripAsset.md](/ItemAsset/GripAsset.md).
* Refer to [MagazineAsset.md](/ItemAsset/MagazineAsset.md).
* Refer to [SightAsset.md](/ItemAsset/SightAsset.md).
* Refer to [TacticalAsset.md](/ItemAsset/TacticalAsset.md).

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

Clothing
========

* Refer to [BackpackAsset.md](/ItemAsset/ArrestEndAsset.md).
* Refer to [GlassesAsset.md](/ItemAsset/GlassesAsset.md).
* Refer to [HatAsset.md](/ItemAsset/HatAsset.md).
* Refer to [MaskAsset.md](/ItemAsset/MaskAsset.md).
* Refer to [PantsAsset.md](/ItemAsset/PantsAsset.md).
* Refer to [ShirtAsset.md](/ItemAsset/ShirtAsset.md).
* Refer to [VestAsset.md](/ItemAsset/VestAsset.md).

Body Mesh Replacements
----------------------

Body mesh replacements are only applicable to shirts. See [CharacterMeshReplacement.md](CharacterMeshReplacement.md) for full documentation.

__Has_1P_Character_Mesh_Override__: `false`, `true`

__Character_Mesh_3P_Override_LODs__: Number of LODs.

__Has_Character_Material_Override__: `false`, `true`

__Hair_Visible__: `false`, `true`. Defaults to true.

__Beard_Visible__: `false`, `true`. Defaults to true.

Consumables
===========

* Refer to [FoodAsset.md](/ItemAsset/FoodAsset.md).
* Refer to [MedicalAsset.md](/ItemAsset/MedicalAsset.md).
* Refer to [WaterAsset.md](/ItemAsset/WaterAsset.md).

Crafting Supplies
=================

* Refer to [SupplyAsset.md](/ItemAsset/SupplyAsset.md).

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

Mapping Equipment
=================

* Refer to [CompassAsset.md](/ItemAsset/CompassAsset.md).
* Refer to [MapAsset.md](/ItemAsset/MapAsset.md).

Melee Weapons
=============

No documentation is available at this time.

Optics
======

* Refer to [OpticAsset.md](/ItemAsset/OpticAsset.md).

Parachutes
==========

* Refer to [CloudAsset.md](/ItemAsset/CloudAsset.md).

Projectiles
===========

__Type__: `Throwable`

__Useable__: `Throwable`

__Explode_On_Impact__: Specified if the projectile immediately explodes upon impact.

__Sticky__: Specified if the projectile sticks to objects upon impact.

__Fuse_Length__: Timer in seconds for fuse length. Defaults to 2 seconds.

Limb-independent damage is also applicable.

Radiation Filters
=================

* Refer to [FilterAsset.md](/ItemAsset/FilterAsset.md).

Ranged Weapons
==============

__Type__: `Gun`

__Useable__: `Gun`

__Barrel__: The barrel item ID to spawn attached.

__Grip__: The grip item ID to spawn attached.

__Sight__: The sight item ID to spawn attached.

__Tactical__: The tactical item ID to spawn attached.

__Hook_Barrel__: Specified if a barrel can be manually attached.

__Hook_Grip__: Specified if a grip can be manually attached.

__Hook_Sight__: Specified if a sight can be manually attached.

__Hook_Tactical__: Specified if a tactical can be manually attached.

__Magazine__: The magazine item ID to spawn attached.

__Magazine_Replacements__: Number of unique conditions with alternative default magazine attachments.

__Magazine_Replacement\_#\_Map__: Name of the map the condition applies to.

__Magazine_Replacement\_#\_ID__: ID of the alternative magazine attachment.

__Ammo_Min__: The minimum amount of ammo to generate.

__Ammo_Max__: The maximum amount of ammo to generate.

__Safety__: Specified if the safety firing mode can be swapped to.

__Semi__: Specified if semi-automatic firing mode can be swapped to.

__Bursts__: Number of shots fired in a burst. Specified if burst firing mode can be swapped to.

__Auto__: Specified if automatic firing mode can be swapped to.

__Caliber__: The caliber ID to check for attachment compatibility.

__Attachment_Calibers__: Number of unique attachment calibers.

__Attachment_Caliber\_#__: ID of applicable caliber for hook attachments.

__Magazine_Calibers__: Number of unique magazine calibers.

__Magazine_Caliber\_#__: ID of applicable caliber for magazine attachments.

__Firerate__: The minimum number of ticks between the firing of each bullet.

__Replace__: Multiplier of the reload animation length before the magazine is respawned.

__Unplace__: Multiplier of the reload animation length before the magazine is despawned.

__Reload_Time__: Multiplier on reload animation length.

__Action__: `Bolt`, `Break`, `Minigun`, `Pump`, `Rail`, `Rocket`, `String`, `Trigger`. Rocket action has inherently explosive projectiles, uses ballistic force instead of alternative advanced ballistics options, and has infinite firing range.

__Delete_Empty_Magazines__: Specified if the attached magazine should be deleted when depleted. Deprecated in favor of Should_Delete_Empty_Magazines.

__Should_Delete_Empty_Magazines__: `false`, `true`. No applicable default flag. If set to true, it will override how empty magazines are handled by the action item mode.

__Spread_Aim__: The spread multiplier when aiming down sights. This is multiplied by the spread_hip value.

__Spread_Hip__: The spread multiplier when not aiming down sights.

__Spread_Sprint__: The spread multiplier when sprinting. Defaults to 1. Requires `Can_Aim_During_Sprint true`.

__Spread_Crouch__: The spread multiplier when crouched. Defaults to 1.

__Spread_Prone__: The spread multiplier when prone. Defaults to 1.

__Ballistic_Force__: Measured in Newtons. Primarily applicable to the rocket action, and usage ignores all other advanced ballistic options.

__Ballistic_Steps__: Defaults to (range / 10).

__Ballistic_Travel__: Defaults to 10.

__Ballistic_Drop__: Defaults to 0.002.

__Recoil_Aim__: Multiplier on all recoil parameters when aiming down sights. Defaults to 1.

__Recoil_Sprint__: Multiplier on horizontal and vertical look recoil while sprinting. Defaults to 1. Requires `Can_Aim_During_Sprint true`.

__Recoil_Crouch__: Multiplier on horizontal and vertical look recoil while crouched. Defaults to 1. 

__Recoil_Prone__: Multiplier on horizontal and vertical look recoil while proned. Defaults to 1. 

__Recoil_Min_X__: The minimum horizontal look recoil in degrees.

__Recoil_Min_Y__: The minimum vertical look recoil in degrees.

__Recoil_Max_X__: The maximum horizontal look recoil in degrees.

__Recoil_Max_Y__: The maximum vertical look recoil in degrees.

__Recover_X__: Multiplier on degrees to be counter-animated horizontally over the next 250 milliseconds.

__Recover_Y__: Multiplier on degrees to be counter-animated vertically over the next 250 milliseconds.

__Shake_Min_X__: The minimum X axis physical recoil.

__Shake_Max_X__: The maximum X axis physical recoil.

__Shake_Min_Y__: The minimum Y axis physical recoil.

__Shake_Max_Y__: The maximum Y axis physical recoil.

__Shake_Min_Z__: The minimum Z axis physical recoil.

__Shake_Max_Z__: The maximum Z axis physical recoil.

__Muzzle__: The muzzle effect ID to play when shooting.

__Shell__: The shell effect ID to play after shooting.

__Turret__: Specified if the weapon should be treated as a vehicular turret.

__Can_Ever_Jam__: Specified if the weapon can jam.

__Jam_Quality_Threshold__: Decimal representative of the quality percentage threshold for jamming can begin to occur.

__Jam_Max_Chance__: Decimal-to-percent chance for jamming to occur.

__Unjam_Chamber_Anim__: Name of the animation clip to play for unjamming. Defaults to UnjamChamber.

__Can_Aim_During_Sprint__: `false`, `true`. Defaults to false. If true, the player can sprint while aiming down sights.

__Ammo_Per_Shot__: Numeric option for ammunition consumed per shot.

__Fire_Delay_Seconds__: Numeric option for the delay between initiating attempting to fire, and the actual firing of the weapon.

__Allow_Magazine_Change__: `false`, `true`. Defaults to true. If false, the magazine in the weapon cannot be reloaded, unloaded, or replaced.

Damage data (explosive, limb-dependent, and limb-independent setups), durability, and wear are also applicable.

Remote Triggers
===============

__Type__: `Detonator`

__Useable__: `Detonator`

Restraining Devices
===================

* Refer to [ArrestEndAsset.md](/ItemAsset/ArrestEndAsset.md) for releasers.
* Refer to [ArrestStartAsset.md](/ItemAsset/ArrestStartAsset.md) for catchers.

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
