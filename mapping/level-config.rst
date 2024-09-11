.. _doc_mapping_config:

Level Config
============

Each level is associated with an optional Config.json file. These files were originally added to make it easy to provide extra information about the level on the main menus, but grew over time to include gameplay parameters as well. In the future some of these might be moved to a more appropriate file like a level asset.

Main Menus
----------

**Creators** *string[]*: Names in credits.

**Collaborators** *string[]*: Names in credits.

**Thanks** *string[]*: Names in credits.

**Associated_Stockpile_Items** *int[]*: Economy itemdefids to feature on map screens. One is chosen at random each time the map is shown. Used by curated maps to link their items which have payment splits.

**Feedback** *string*: URL to discussions. If not explicitly set, defaults to the workshop item's discussions page.

**Visible_In_Matchmaking** *bool*: Should this map be listed in the matchmaking menu? Used to filter out test and demo maps.

**Version** *string*: #.#.#.# format version number. Vanilla version numbers use 3.Year.Update.Patch, but that is optional. Incrementing the version number for every upload is good practice because:

1. When client and server files do not match it is more helpful to show a version number error message rather than a generic file mismatch error.
2. Searching by map in the server browser can filter servers running the same version of the map.

**Tips** *int*: Number of Tip_# keys defined in level's localization files, if any. Overrides vanilla tip messages on the loading screen.

Arena Mode
----------

**Use_Arena_Compactor** *bool*: Should circles be randomized periodically?

**Arena_Loadouts**: Array of items to grant when spawning into arena. Each entry has a Table_ID spawn table to generate from, and an Amount number of times to grant from spawn table. For example:

.. code-block:: json

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

**Asset**: Object with GUID of :ref:`Level Asset <doc_assets_level>` to instantiate on this map. For example:

.. code-block:: json

	"Asset": { "GUID": "12dc9fdbe9974022afd21158ad54b76a" }

**Trains**: Array of train vehicles to spawn. Only one of each train asset can exist at a given time because the vehicle ID is used to match saved trains to tracks. Road index can be seen by selecting a road in the level editor. Placement is normalized between the start and end of the track length. For example:

.. code-block:: json

	"Trains":
	[
		{
			"VehicleID": 187,
			"RoadIndex": 0,
			"Min_Spawn_Placement": 0.1,
			"Max_Spawn_Placement": 0.9
		}
	]

**Mode_Config_Overrides**: Pairs of server config properties and values to override them. For example:

.. code-block:: json

	"Mode_Config_Overrides":
	{
		"Zombies.Min_Drops": 5,
		"Zombies.Max_Drops": 10,
		"Vehicles.Armor_Multiplier": 0.1,
		"Gameplay.Allow_Shoulder_Camera": false
	}

**Allow_Underwater_Features** *bool*: Should legacy details and navigation bounds be restricted underwater?

**Terrain_Snow_Sparkle** *bool*: Should IS_SNOWING shader keyword be enabled?

**Use_Legacy_Clip_Borders** *bool*: Should invisible walls matching map size be created? Defaults to true.

**Use_Legacy_Ground** *bool*: Should default terrain be created? Alternative is to use landscape tiles. Defaults to true.

**Use_Legacy_Water** *bool*: Should global water plane be enabled? Alternative is to use water volumes. Defaults to true.

**Use_Vanilla_Bubbles** *bool*: Should vanilla water bubble effects be enabled? Defaults to true.

**Use_Legacy_Snow_Height** *bool*: Should travelling vertically past snow height threshold enable snow effects? Defaults to true.

**Use_Legacy_Oxygen_Height** *bool*: Should travelling vertically past a certain point deplete oxygen? Defaults to true.

**Use_Rain_Volumes** *bool*: Should rain flag in ambiance volume be used?

**Use_Snow_Volumes** *bool*: Should snow flag in ambiance volume be used?

**Use_Underground_Whitelist** *bool*: Should underground players not inside a whitelist volume be teleported to the terrain surface? Useful to curb out-of-bounds exploits.

**Is_Aurora_Borealis_Visible** *bool*: Should aurora borealis effects be enabled?

**Snow_Affects_Temperature** *bool*: Should snow inflict cold damage?

**Weather_Override** *ELevelWeatherOverride*: Can be set to rain or snow to lock weather type.

**Has_Atmosphere** *bool*: If false, disable stars in skybox.

**Has_Global_Electricity** *bool*: Should all powerable items and objects have power by default?

**Gravity** *float*: Acceleration of gravity. Defaults to -9.81.

**Blimp_Altitude** *float*: Height override for blimp buoyancy. Defaults to 150.

**Max_Walkable_Slope** *float*: Steepest ground angle players can walk without sliding. Defaults to 59.

**Prevent_Building_Near_Spawnpoint_Radius** *float*: Closest distance players can build to spawn points. Useful to override for close-quarters maps. Defaults to 16.

**Spawn_Loadouts**: Array of items to grant when spawning in any mode. Refer to ``Arena_Loadouts``.

**Allow_Holiday_Redirects** *bool*: Whether certain assets like objects, trees and landscapes should load alternative versions during holiday events.

HUD
---

Disable various elements of the heads-up display.

**PlayerUI_HealthVisible** *bool*

**PlayerUI_FoodVisible** *bool*

**PlayerUI_WaterVisible** *bool*

**PlayerUI_VirusVisible** *bool*

**PlayerUI_StaminaVisible** *bool*

**PlayerUI_OxygenVisible** *bool*

**PlayerUI_GunVisible** *bool*

**Allow_Crafting** *bool*

**Allow_Skills** *bool*

**Allow_Information** *bool*

Deprecated
----------

**Can_Use_Bundles** *bool*: Used in the past for timed curated maps to disable using their assets in the level editor which could break after moving the map from the vanilla content to the workshop.

**Category** *ESingleplayerMapCategory*: Mostly automated now. Can be set to Misc to explicitly show in the miscellaneous map category.

**Has_Discord_Rich_Presence** *bool*: Only valid for official maps. If discord integration is enabled and this flag is true discord will check for a map icon configured in their partner page.

**Item** *int*: Kept for backwards compatibility. Ignored if ``Associated_Stockpile_Items`` are set.

**Load_From_Resources** *bool*: Used in the past for curated maps with assets in the vanilla Resources/Bundles/* directory. Master Bundles completely replaced this.

**Should_Verify_Objects_Hash** *bool*: With the newer asset integrity checks this is obsolete because each object/tree used in the level is checked with the server, and ignored if the server is missing the asset. Trees.dat and Objects.dat can always be included because missing assets do not factor into those hashes anymore.

**Use_Legacy_Fog_Height** *bool*: Should default terrain height be used for fog falloff? If false, devkit landscape tile limits are used instead. Defaults to true.

**Use_Legacy_Objects** *bool*: Should objects be loaded from Objects.dat file? Devkit objects were moved into this file, so this option no longer has any effect.
