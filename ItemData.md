__Items__ in _Unturned_ encompass anything that can be carried in a player's in-game inventory. All items share some properties, while each item type has its own unique data. All of the data applicable to each possible item type can be found below.

Non-specific Data
=================

This first set of data is universal, and is applicable to any item type. Some of this data is required in order for the item to function.

__GUID__: The GUID is automatically generated for the item when the game is launched. If it is not automatically generated, then it is assumable that the content was not set up properly.

__Type__: Each category of item has its own type. The type to use can be found for each specific item category below, and is used for the item's context type as viewed in the context menu.

__Rarity__: `Common`, `Uncommon`, `Rare`, `Epic`, `Legendary`, `Mythical`

__Useable__: This defines which class to use for the item when equipped. If unspecified it will default to None, meaning that the item cannot be equipped. Which value to use for equippable items can be found below for each item category.

__Slot__: `Primary`, `Secondary`, `Any`

__ID__: The item ID is used to spawn the item into the game, and is represented as an unsigned 16 bit integer (a range of 0–65535). It is recommended not to use a value less than 2,000 as those are reserved for official content. It is also recommended to avoid any ID range being used by curated content, as those are often used by modded servers and custom Workshop maps.

__Size_X__: The width of the item in the inventory.

__Size_Y__: The height of the item in the inventory.

__Size_Z__: The size of the camera for item icons.

__Size2_Z__:

__Backward__: Specified if this item should be visually held in the opposite hand.

Capacity
--------

__Amount__: Maximum capacity of a container.

__Count_Min__: The minimum amount to generate in the container.

__Count_Max__: The maximum amount to generate in the container.

Quality
-------

__Quality_Min__: The minimum quality to generate. Set to 10 by default.

__Quality_Max__: The maximum quality to generate. Set to 90 by default.

__Durability__: Decimal probability chance of quality loss upon action.

* _Canteens_: Durability loss occurs upon drinking.
* _Melee Weapons_: Durability loss occurs upon hitting.
* _Ranged Weapons_: Durability loss occurs upon shooting.

__Wear__:

Damage
------

Damage data can be utilized by explosive consumables, explosive throwables, melee weapons, and ranged weapons.

__Player_Damage__:

__Zombie_Damage__:

__Animal_Damage__:

__Barricade_Damage__:

__Structure_Damage__:

__Vehicle_Damage__:

__Resource_Damage__:

__Object_Damage__:

__Range__: For ranged and melee weapons – max distance in meters before damage is no longer possible. For explosive weapons (including projectiles) – the radius of the explosion in meters.

__Explosive__: Specified if the explosive component is used.

__Explosion__: The visual effect ID to play as the explosion.

__Spawn_Explosion_On_Dedicated_Server__:

Blueprints
----------

__Blueprints__: The number of blueprints available.

__Blueprint\_#\_Type__: `Ammo`, `Apparel`, `Barricade`, `Gear`, `Repair` ,`Structure`, `Supply`,`Tool`

__Blueprint\_#\_Supplies__: The number of unique supplies required for the blueprint.

__Blueprint\_#\_Supply\_#\_ID__: The ID of the unique supply required.

__Blueprint\_#\_Supply\_#\_Amount__: The amount of the unique supply required.

__Blueprint\_#\_Level__: The skill level needed.

__Blueprint\_#\_Skill__: `Cook`, `Craft`, `None`, `Repair`. The skill required to craft – defaults to None.

__Blueprint\_#\_Product__: The ID of the product created.

__Blueprint\_#\_Products__: The amount of the product created.

__Blueprint\_#\_Outputs__: The number of unique products created from fulfilling the blueprint.

__Blueprint\_#\_Output\_#\_ID__: The ID of the unique product created.

__Blueprint\_#\_Output\_#\_Amount__: The amount of the unique product created.

__Blueprint\_#\_Build__: The auditory effect ID to play.

Actions
-------

__Actions__:

__Action\_#\_Type__: `Blueprint`

__Action\_#\_Source__: ID of the item with the blueprint this action should perform.

__Action\_#\_Blueprints__:

__Action\_#\_Blueprint\_#\_Index__:

__Action\_#\_Key__: `Craft_Dressing`, `Craft_Seed`

Attachments
===========

Barrels
-------

Grips
-----

Magazines
---------

Sights
------

Tacticals
---------

Building
========

Barricades
----------

Plants
------

Storage
-------

Structures
----------

Traps
-----

Clothing
========

__Armor__: Decimal multiplier on incoming damage.

__Width__: The amount of horizontal storage space.

__Height__: The amount of vertical storage space.

__Hair__: Specified if hair shows up when wearing. Only applicable to hats, masks, and glasses.

__Beard__: Specified if beard shows up when wearing. Only applicable to hats, masks, and glasses.

Backpacks
---------

Glasses
-------

Hats
----

Masks
-----

Pants
-----

Shirts
------

__Type__: `Shirt`

__Useable__: `Shirt`

Vests
-----

Consumables
===========

Consumables in _Unturned_ encompass anything that is irreversibly consumed by the player on use, and directly affect a player's stats such as food or health.

__Type__: `Food`, `Medical`, `Water`

__Useable__: `Consumeable`

__Aid__: Specified if the item can be used on other players via right-click.

__Bleeding_Modifier__: `Cut`, `Heal`, `None`

__Bleeding__: Specified if bleeding is healed. Deprecated in favor of Bleeding_Modifier.

__Bones_Modifier__: `Break`, `Heal`, `None`

__Broken__: Specified if broken legs are healed. Deprecated in favor of Bones_Modifier.

__Health__: The number of health to restore.

__Food__: The number of food to restore.

__Water__: The number of water to restore.

__Food_Constrains_Water__: Specified if max potential water gain should be capped by actual food gain. Applies to items where max potential water gain is less than max potential food gain.

__Disinfectant__: The number of immunity to restore.

__Virus__: The number of immunity to deplete.

__Energy__: The number of energy to restore.

__Vision__: The length of hallucinations. The length does not stack with each time eaten, but the timer is reset for equal or longer Vision values relative to the remaining hallucination time.

__Oxygen__: The number of oxygen to restore or deplete.

Fishing Poles
=============

__Type__: `Fisher`

__Useable__: `Fisher`

__Reward_ID__: ID of the spawn table to pull catchable items from.

Fuel Canisters
==============

Growth Supplements
==================

__Type__: `Grower`

__Useable__: `Grower`

Optics
======

__Type__: `Optic`

__Useable__: `Optic`

__Zoom__: Multiplicative amount of zoom.

Mapping Equipment
=================

__Type__: `Map`, `Compass`

__Enables_Map__: Specified if this item provides a satellite map display.

__Enables_Chart__: Specified if this item provides a chart map display.

__Enables_Compass__: Specified if this item provides a compass display.

Parachutes
==========

__Type__: `Cloud`

__Useable__: `Cloud`

__Gravity__: Decimal multiplier on the influence of gravity.

Projectiles
===========

__Type__: `Throwable`

__Useable__: `Throwable`

Tools
=====

Walkie-talkies
--------------

Car Lock Picks
--------------

Car Jacks
---------

Vehicle Batteries
-----------------

Tire Replacements
-----------------

Water Canisters
===============

__Type__: `Refill`

__Useable__: `Refill`

__Water__: The number of water to restore.

Weapons
=======

Melee
-----

Ranged
------
