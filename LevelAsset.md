**NOTICE:** *You are not reading the most up-to-date documentation. This file is old, and may not reflect the current modding or server capabilities. The latest documentation can be found at [Unturned Documentation](https://docs.smartlydressedgames.com/).*

*This file may be removed in the future. Refer to its more [up-to-date equivalent](https://docs.smartlydressedgames.com/en/stable/assets/level-asset.html) instead.*

Level Asset
===========

Each map can be associated with a **Level Asset**. These assets contain gameplay information not necessary for the main menus. Refer to [Level Config](LevelConfig.md) for information on linking a level asset to a map.

For examples check the `Assets/Levels` directory.

`Dropship` [Master Bundle Pointer](MasterBundlePtr.md): Overrides the model seen flying over the map when a care package is dropped.

`Airdrop` [Asset Pointer](AssetPtr.md): to an [Airdrop Asset](AirdropAsset.md). Overrides the falling care package model.

`Crafting_Blacklists` array of [Asset Pointers](AssetPtr.md) to [Crafting Blacklist(s)](CraftingBlacklistAsset.md). Prevents specific items or blueprints from being used while crafting in the level.

`Min_Stealth_Radius` float: Player stealth skill level cannot reduce minimum detection distance below this value.

`Weather_Types` *array*: determines which weather can occur naturally. Refer to schedulable weather properties. If weather is using legacy weather the default rain and snow will be included.

`Perpetual_Weather_Asset` [Asset Pointer](AssetPtr.md): to a [Weather Asset](WeatherAsset.md). Overrides weather scheduling.

`Global_Weather_Mask` [u32 Mask](Bitmask.md): fallback weather mask while player is not inside an ambience volume. Defaults to 0xFFFFFFFF.

`Skills` *array*: overrides skill default and max levels. Refer to skill rule properties.

`Enable_Admin_Faster_Salvage_Duration` *bool*: by default players in singleplayer and admins in multiplayer have a faster salvage time.

`Has_Clouds` *bool*: disables clouds in skybox when false. Defaults to true.

`Loading_Screen_Music` *array*: randomly selected. Refer to music properties.

`Should_Animate_Background_Image` *bool*: if true, the background image moves left/right with loading progress. Defaults to false because maps have important information on the loading screen.

This is an [Asset v2](AssetsV2.md) class.

Schedulable Weather Properties
------------------------------

`Asset` [Asset Pointer](AssetPtr.md) to a [Weather Asset](WeatherAsset.md).

`Min_Frequency` *float*: When chosen to be the next scheduled weather event, minimum number of in-game days before it will start.

`Max_Frequency` *float*: When chosen to be the next scheduled weather event, maximum number of in-game days before it will start.

`Min_Duration` *float*: Minimum number of in-game days before the weather event will end.

`Max_Duration` *float*: Maximum number of in-game days before the weather event will end.

Skill Rule Properties
---------------------

`Id` string: Name of skill, for example Sharpshooter.

`Default_Level` int: Skill level when player spawns. Note server config Spawn_With_Max_Skills takes priority.

`Max_Unlockable_Level` int: Maximum skill level attainable through gameplay. Higher levels are hidden in the skills menu.

`Cost_Multiplier` *float*: multiplier for XP upgrade cost.

Music Properties
----------------

`Loop` [Master Bundle Pointer](MasterBundlePtr.md): looping audio clip played until loading finishes.

`Outro` [Master Bundle Pointer](MasterBundlePtr.md): audio clip played once loading finishes.
