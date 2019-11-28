Non-specific Data
=================

__GUID__: The GUID is automatically generated for the item when the game is launched. If it is not automatically generated, then it is assumable that the content was not set up properly.

__Type__: Each category of item has its own type. The type to use can be found for each specific item category below, and is used for the item's context type as viewed in the context menu.

__Useable__: This defines which class to use for the item when equipped. If unspecified it will default to None, meaning that the item cannot be equipped. Which value to use for equippable items can be found below for each item category.

__Rarity__: Common, Uncommon, Rare, Epic, Legendary, Mythical

__ID__: The item ID is used to spawn the item into the game, and is represented as an unsigned 16 bit integer (a range of 0–65535). It is recommended not to use a value less than 2,000 as those are reserved for official content. It is also recommended to avoid any ID range being used by curated content, as those are often used by modded servers and custom Workshop maps.

__Size_X__: The width of the item in the inventory.

__Size_Y__: The height of the item in the inventory.

__Size_Z__: The size of the camera for item icons.

Damage
------

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

Blueprints
----------

__Blueprints__:

__Blueprint\_#\_Type__: Supply

__Blueprint\_#\_Supplies__:

__Blueprint\_#\_Supply\_#\_ID__:

__Blueprint\_#\_Level__:

__Blueprint\_#\_Skill__: Cook, Craft

__Blueprint\_#\_Build__:

Actions
-------

__Actions__:

__Action\_#\_Type__: Blueprint

__Action\_#\_Source__: ID of the item with the blueprint this action should perform.

__Action\_#\_Blueprints__:

__Action\_#\_Blueprint\_#\_Index__:

__Action\_#\_Key__: Craft_Seed

Consumables
============

Consumables in _Unturned_ encompass anything that is irreversibly consumed by the player on use, and directly affect a player's stats such as food or health.

__Type__: Food, Medical, Water

__Useable__: Consumeable

__Quality_Max__:

__Aid__: Specified if the item can be used on other players via right-click.

__Bleeding__: Specified if bleeding is cured.

__Broken__: Specified if broken legs are cured.

__Health__: The amount of health to add.

__Food__: The amount of food to add.

__Water__: The amount of water to add.

__Food_Constrains_Water__:

__Disinfectant__: The amount of immunity to add.

__Virus__: The amount of immunity to remove.

__Energy__: The amount of energy to add.

__Vision__: The length of hallucinations. The length does not stack with each time eaten, but the timer is reset for equal or longer Vision values relative to the remaining hallucination time.
