Level Asset
===========

Each map can be associated with a **Level Asset**. These assets contain gameplay information not necessary for the main menus. Refer to [Level Config](LevelConfig.md) for information on linking a level asset to a map.

For examples check the `Assets/Levels` directory.

`Dropship` [Master Bundle Pointer](MasterBundlePtr.md): Overrides the model seen flying over the map when a care package is dropped.

`Airdrop` [Asset Pointer](AssetPtr.md): to an [Airdrop Asset](AirdropAsset.md). Overrides the falling care package model.

`Crafting_Blacklists` array of [Asset Pointers](AssetPtr.md) to [Crafting Blacklist(s)](CraftingBlacklistAsset.md). Prevents specific items or blueprints from being used while crafting in the level.

`Min_Stealth_Radius` float: Player stealth skill level cannot reduce minimum detection distance below this value.

`Weather_Types` *array*: determines which weather can be scheduled to occur naturally. Refer to weather properties.

This is an [Asset v2](AssetsV2.md) class.

## Weather Properties

`Asset` [Asset Pointer](AssetPtr.md) to a [Weather Asset](WeatherAsset.md).

`Min_Frequency` *float*: When chosen to be the next scheduled weather event, minimum number of in-game days before it will start.

`Max_Frequency` *float*: When chosen to be the next scheduled weather event, maximum number of in-game days before it will start.

`Min_Duration` *float*: Minimum number of in-game days before the weather event will end.

`Max_Duration` *float*: Maximum number of in-game days before the weather event will end.
