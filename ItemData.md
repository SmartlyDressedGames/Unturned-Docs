Non-specific Data
=================

__GUID__: The GUID is automatically generated for the item when the game is launched. If it is not automatically generated, then it is assumable that the content was not set up properly.

__Type__: Each category of item has its own type. The type to use can be found for each specific item category below, and is used for the item's context type as viewed in the context menu.

__Rarity__: <code>Common</code>, <code>Uncommon</code>, <code>Rare</code>, <code>Epic</code>, <code>Legendary</code>, <code>Mythical</code>

__Useable__: This defines which class to use for the item when equipped. If unspecified it will default to None, meaning that the item cannot be equipped. Which value to use for equippable items can be found below for each item category.

__Slot__: <code>Primary</code>, <code>Secondary</code>, <code>Any</code>

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

__Durability__: Amount of quality loss upon action.

__Wear__:

For fishing, durability is lost upon cast.

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

__Range__:

__Explosion__:

__Spawn_Explosion_On_Dedicated_Server__:

Blueprints
----------

__Blueprints__: The number of blueprints available.

__Blueprint\_#\_Type__: <code>Ammo</code>, <code>Apparel</code>, <code>Barricade</code>, <code>Gear</code>, <code>Repair</code> ,<code>Structure</code>, <code>Supply</code>,<code>Tool</code>

__Blueprint\_#\_Supplies__: The number of unique supplies required for the blueprint.

__Blueprint\_#\_Supply\_#\_ID__: The ID of the unique supply required.

__Blueprint\_#\_Supply\_#\_Amount__: The amount of the unique supply required.

__Blueprint\_#\_Level__: The skill level needed.

__Blueprint\_#\_Skill__: <code>Cook</code>, <code>Craft</code>, <code>None</code>, <code>Repair</code>. The skill required to craft – defaults to None.

__Blueprint\_#\_Product__: The ID of the product created.

__Blueprint\_#\_Products__: The amount of the product created.

__Blueprint\_#\_Outputs__: The number of unique products created from fulfilling the blueprint.

__Blueprint\_#\_Output\_#\_ID__: The ID of the unique product created.

__Blueprint\_#\_Output\_#\_Amount__: The amount of the unique product created.

__Blueprint\_#\_Build__: The auditory effect ID to play.

Actions
-------

__Actions__:

__Action\_#\_Type__: <code>Blueprint</code>

__Action\_#\_Source__: ID of the item with the blueprint this action should perform.

__Action\_#\_Blueprints__:

__Action\_#\_Blueprint\_#\_Index__:

__Action\_#\_Key__: <code>Craft_Dressing</code>, <code>Craft_Seed</code>

Consumables
============

Consumables in _Unturned_ encompass anything that is irreversibly consumed by the player on use, and directly affect a player's stats such as food or health.

__Type__: <code>Food</code>, <code>Medical</code>, <code>Water</code>

__Useable__: <code>Consumeable</code>

__Aid__: Specified if the item can be used on other players via right-click.

__Bleeding_Modifier__: <code>Cut</code>, <code>Heal</code>, <code>None</code>

__Bleeding__: Specified if bleeding is healed. Deprecated in favor of Bleeding_Modifier.

__Bones_Modifier__: <code>Break</code>, <code>Heal</code>, <code>None</code>

__Broken__: Specified if broken legs are healed. Deprecated in favor of Bones_Modifier.

__Health__: The number of health to add.

__Food__: The number of food to add.

__Water__: The number of water to add.

__Food_Constrains_Water__: Max potential water gain is capped by actual food gain. Applies to items where max potential water gain is less than max potential food gain.

__Disinfectant__: The number of immunity to add.

__Virus__: The number of immunity to subtract.

__Energy__: The number of energy to add.

__Vision__: The length of hallucinations. The length does not stack with each time eaten, but the timer is reset for equal or longer Vision values relative to the remaining hallucination time.

__Oxygen__: The number of oxygen to add or subtract.

Fishing
=======

__Type__: <code>Fisher</code>

__Useable__: <code>Fisher</code>

__Reward_ID__: ID of the spawn table to pull catchable items from.
