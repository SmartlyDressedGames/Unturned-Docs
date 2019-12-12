Level Config
============

Each level is associated with an optional Config.json file. These files were originally added to make it easy to provide extra information about the level on the main menus, but grew over time to include gameplay parameters as well. In the future some of these might be moved to a more appropriate file like a level asset.

Main Menus
----------

__Creators__ _string[]_: Names in credits.

__Collaborators__ _string[]_: Names in credits.

__Thanks__ _string[]_: Names in credits.

__Associated_Stockpile_Items__ _int[]_: Economy itemdefids to feature on map screens. One is chosen at random each time the map is shown. Used by curated maps to link their items which have payment splits.

__Feedback__ _string_: URL to discussions. If not explicitly set, defaults to the workshop item's discussions page.

__Visible_In_Matchmaking__ _bool_: Should this map be listed in the matchmaking menu? Used to filter out test and demo maps.

__Version__ _string_: X.Y.Z.W style version number. Vanilla version numbers use 3.Year.Update.Patch, but that's optional. Servers will reject clients with different map versions.

__Tips__ _int_: Number of Tip_# keys defined in level's localization files, if any. Overrides vanilla tip messages on the loading screen.

Arena Mode
----------

__Use_Arena_Compactor__ _bool_: Should circles be randomized periodically?

__Arena_Loadouts__: Array of items to grant when spawning into arena. Each entry has a Table_ID spawn table to generate from, and an Amount number of times to grant from spawn table. For example:

	"Arena_Loadouts":
	[
		{
			"Table_ID": 28007,
			"Amount": 1
		},
		{
			"Table_ID": 28008,
			"Amount": 1
		}
	]

General
-------

__Asset__: Object with GUID of level asset to instantiate on this map. For example:

	"Asset": { "GUID": "12dc9fdbe9974022afd21158ad54b76a" }

__Trains__: Array of train vehicles to spawn. Only one of each train asset can exist at a given time because the vehicle ID is used to match saved trains to tracks. Road index can be seen by selecting a road in the level editor. Placement is normalized between the start and end of the track length. For example:

	"Trains":
	[
		{
			"VehicleID": 187,
			"RoadIndex": 0,
			"Min_Spawn_Placement": 0.1,
			"Max_Spawn_Placement": 0.9
		}
	]

__Mode_Config_Overrides__: Pairs of server config properties and values to override them. For example:

	"Mode_Config_Overrides":
	{
		"Zombies.Min_Drops": 5,
		"Zombies.Max_Drops": 10,
		"Vehicles.Armor_Multiplier": 0.1,
		"Gameplay.Allow_Shoulder_Camera": false
	}

__Allow_Underwater_Features__ _bool_: Should legacy details and navigation bounds be restricted underwater?

__Terrain_Snow_Sparkle__ _bool_: Should IS_SNOWING shader keyword be enabled?

__Use_Legacy_Clip_Borders__ _bool_: Should invisible walls matching map size be created? Defaults to true.

__Use_Legacy_Ground__ _bool_: Should default terrain be created? Alternative is to use devkit landscape tiles. Defaults to true.

__Use_Legacy_Water__ _bool_: Should global water plane be enabled? Alternative is to use water volumes in devkit. Defaults to true.

__Use_Vanilla_Bubbles__ _bool_: Should vanilla water bubble effects be enabled? Defaults to true.

__Use_Legacy_Objects__ _bool_: Should objects be loaded from Objects.dat file? Using devkit objects is not as well supported, so safest to leave at true.

__Use_Legacy_Snow_Height__ _bool_: Should travelling vertically past snow height threshold enable snow effects? Defaults to true.

__Use_Legacy_Oxygen_Height__ _bool_: Should travelling vertically past a certain point deplete oxygen? Defaults to true.

__Use_Rain_Volumes__ _bool_: Should rain flag in ambiance volume be used?

__Use_Snow_Volumes__ _bool_: Should snow flag in ambiance volume be used?

__Is_Aurora_Borealis_Visible__ _bool_: Should aurora borealis effects be enabled?

__Snow_Affects_Temperature__ _bool_: Should snow inflict cold damage?

__Weather_Override__ _ELevelWeatherOverride_: Can be set to rain or snow to lock weather type.

__Has_Atmosphere__ _bool_: If false, disable stars in skybox.

__Should_Verify_Objects_Hash__ _bool_: Should server verify client level files match? Not recommended for maps with tons of required downloads because loading mismatch will break hash. Maps with one or two dependencies should be fine.

__Can_Use_Bundles__ _bool_: Should assets in the map's Bundles directory be usable from the level editor? Was disabled for older curated maps to prevent breaking after transitioning to the workshop.

__Has_Global_Electricity__ _bool_: Should all powerable items and objects have power by default?

__Gravity__ _float_: Acceleration of gravity. Defaults to -9.81.

__Blimp_Altitude__ _float_: Height override for blimp buoyancy. Defaults to 150.

__Max_Walkable_Slope__ _float_: Steepest ground angle players can walk without sliding. Defaults to 59.

__Prevent_Building_Near_Spawnpoint_Radius__ _float_: Closest distance players can build to spawn points. Useful to override for close-quarters maps. Defaults to 16.

__Spawn_Loadouts__ Array of items to grant when spawning in any mode. Refer to Arena_Loadouts.

__Allow_Holiday_Redirects__ _bool_: Whether certain assets like objects, trees and landscapes should load alternative versions during holiday events.

HUD
---

Disable various elements of the heads-up display.

__PlayerUI_HealthVisible__ bool

__PlayerUI_FoodVisible__ bool

__PlayerUI_WaterVisible__ bool

__PlayerUI_VirusVisible__ bool

__PlayerUI_StaminaVisible__ bool

__PlayerUI_OxygenVisible__ _bool_

__PlayerUI_GunVisible__ _bool_

__Allow_Crafting__ bool

__Allow_Skills__ bool

__Allow_Information__ bool

Deprecated
----------

__Use_Legacy_Fog_Height__ _bool_: Should default terrain height be used for fog falloff? If false, devkit landscape tile limits are used instead. Defaults to true.

__Load_From_Resources__ _bool_: Used in the past for curated maps with assets in the vanilla Resources/Bundles/* directory. Master Bundles completely replaced this.

__Item__ _int_: Kept for backwards compatibility. Ignored if Associated_Stockpile_Items are set.

__Has_Discord_Rich_Presence__ _bool_: Only valid for official maps. If discord integration is enabled and this flag is true discord will check for a map icon configured in their partner page.

__Category__ _ESingleplayerMapCategory_: Mostly automated now. Can be set to Misc to explicitly show in the miscellaneous map category.
