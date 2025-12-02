.. _doc_assets_level:

Level Assets
============

Each map can be associated with a **Level Asset**. These assets contain gameplay information not necessary for the main menus. Refer to :ref:`Level Config <doc_mapping_config>` for information on linking a level asset to a map.

For examples, check the ``Assets/Levels`` directory.

**Type** *string*: ``SDG.Unturned.LevelAsset``

**Dropship** :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`: Overrides the model seen flying over the map when a care package is dropped.

**Airdrop** :ref:`Asset Pointer <doc_data_assetptr>`: Asset pointer to an :ref:`Airdrop Asset <doc_assets_airdrop>`. Overrides the falling care package model.

**Crafting_Blacklists** array of :ref:`Asset Pointers <doc_data_assetptr>`: Asset pointers to :ref:`Crafting Blacklist(s) <doc_assets_crafting_blacklist>`. Prevents specific items or blueprints from being used while crafting in the level.

**Min_Stealth_Radius** *float*: Player stealth skill level cannot reduce minimum detection distance below this value.

**Weather_Types** *array*: Determines which weather can occur naturally. Refer to schedulable weather properties. If weather is using legacy weather the default rain and snow will be included.

**Perpetual_Weather_Asset** :ref:`Asset Pointer <doc_data_assetptr>`: Asset pointer to a :ref:`Weather Asset <doc_assets_weather>`. Overrides weather scheduling.

**Global_Weather_Mask** :ref:`u32 Mask <doc_data_bitmask>`: Fallback weather mask while player is not inside an ambience volume. Defaults to 0xFFFFFFFF.

**Skills** *array*: Overrides skill default and max levels. Refer to skill rule properties.

**Skillset_Loadouts** *dictionary*: Overrides per-skillset starting items. Can be used to prevent skillset default items in singleplayer. Server "Loadout" command takes priority over this option. Please refer to Skillset Loadout properties below for more details.

**TerrainColors** *array*: Specifies which colors are too similar to terrain colors. Please refer to Terrain Color Properties below.

**Enable_Admin_Faster_Salvage_Duration** *bool*: By default, players in singleplayer and admins in multiplayer have a faster salvage time.

**Has_Clouds** *bool*: Disables clouds in skybox when false. Defaults to true.

**Loading_Screen_Music** *array*: Randomly selected. Refer to music properties.

**Should_Animate_Background_Image** *bool*: If true, the background image moves left/right with loading progress. Defaults to false because maps have important information on the loading screen.

**Death_Music** :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`: Audio clip played after death.

**UnderwaterFogDensity** *float*: Overrides fog effect intensity while the camera is underwater. Defaults to ``0.075``.

**Allow_Building_In_Safezone_In_Singleplayer** *bool*: If true, players can bypass safezone's no-buildables mode in singleplayer. Defaults to false.

**Tags** :ref:`list <doc_data_file_format>` of :ref:`Asset Pointer <doc_data_assetptr>` to :ref:`doc_assets_tag`: Blueprints can test for these tags as an alternative to ``Map`` name check. May be extended in the future.

Cloud Override Properties
-------------------------

When clouds are disabled (``Has_Clouds false``), these properties can be used to control a custom particle system using the cloud color and intensity from the lighting settings.

**CloudOverride_Prefab** :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`: Prefab to instantiate and attach to lighting.

**CloudOverride_ParticleSystems** *list*: Dictionaries describing particle systems in ``CloudOverride_Prefab`` with the following additional properties:

**Path** *string*: Path to a Particle System component relative to ``CloudOverride_Prefab``. This renderer should likely use the Unturned "Particles/Standard Surface (ZClip False)" shader to prevent a harsh transition with low max draw distance.

**RateOverTimeScale** *float*: Particle System's emission rate is multiplied by current time of day's cloud slider value (between zero and one) scaled by this value.

**MaterialColorPropertyNames** *list*: Particle System's material instance will have these color properties set to the current time of day's cloud color. Defaults to just _Color.

**WarmupTime** *float*: When restarting the particle system it is simulated this number of seconds. Alternative to enabling Particle System's ``Prewarm`` option. Defaults to zero.

For example:

.. code-block:: unturnedasset
	:linenos:

	CloudOverride_ParticleSystems
	[
		{
			Path System1
			RateOverTimeScale 1.5
			WarmupTime 10
			MaterialColorPropertyNames
			[
				_Color
				_EmissionColor
			]
		}
		{
			Path System2
			RateOverTimeScale 3
			MaterialColorPropertyNames
			[
				_Color
				_EmissionColor
			]
		}
	]

Schedulable Weather Properties
------------------------------

**Asset** :ref:`Asset Pointer <doc_data_assetptr>`: Points to a :ref:`Weather Asset <doc_assets_weather>`.

**Min_Frequency** *float*: When chosen to be the next scheduled weather event, minimum number of in-game days before it will start.

**Max_Frequency** *float*: When chosen to be the next scheduled weather event, maximum number of in-game days before it will start.

**Min_Duration** *float*: Minimum number of in-game days before the weather event will end.

**Max_Duration** *float*: Maximum number of in-game days before the weather event will end.

Skill Rule Properties
---------------------

**Id** *string*: Name of skill, for example Sharpshooter.

**Default_Level** *int*: Skill level when player spawns. The ``Spawn_With_Max_Skills`` gameplay config option takes priority.

**Max_Unlockable_Level** *int*: Maximum skill level attainable through gameplay. Higher levels are hidden in the skills menu.

**Base_Cost** *int*: If set, overrides XP cost to purchase first level of the skill.

**Per_Level_Cost_Increase** *int*: If set, overrides XP cost increase with each level. Added to ``Base_Cost`` after the first level.

**Cost_Multiplier** *float*: Multiplier for total XP upgrade cost.

.. code-block:: unturnedasset
	:linenos:

	Skills
	[
		{
			Id Overkill
			Default_Level 0
			Max_Unlockable_Level 0
		}
		{
			Id Parkour
			Default_Level 2
			Max_Unlockable_Level 2
		}
		{
			Id Crafting
			Default_Level 1
			Max_Unlockable_Level 3
			Cost_Multiplier 5
		}
	]

Skillset Loadout Properties
---------------------------

Can contain the following keys: ``None``, ``Fire``, ``Police``, ``Army``, ``Farm``, ``Fish``, ``Camp``, ``Work``, ``Chef``, ``Thief``, ``Medic``

Each key is a list of items with the following properties:

**Asset**: :ref:`Asset Pointer <doc_data_assetptr>`: Item or spawn table to grant an item from.

**Amount** *int*: Number of times to grant this item. Defaults to 1.

**Origin** :ref:`EItemOrigin <doc_data_eitemorigin>`: Determines starting state of the item. Defaults to World.

Example:

.. code-block:: unturnedasset
	:linenos:

	Skillset_Loadouts
	{
		Army
		[
			{
				// Eaglefire at max quality with full ammo
				Asset 4
				Origin Admin
			}
			{
				// Military magazine x2 with random ammo
				Asset dbfb1d0d11ca438e9dffb95f76e61274
				Amount 2
			}
		]

		// Other skillsets will spawn with nothing
	}

Terrain Color Properties
------------------------

**Color** :ref:`color <doc_data_color>`: Actual base color/albedo of terrain material. Players will be kicked from multiplayer servers if their customized skin color is too similar to the value of this property.

**HueThreshold** :ref:`float32 <doc_data_builtin_types>`: Values are clamped from 0 to 1. If difference between hues is greater than this threshold, the colors are not too similar.

**SaturationThreshold** :ref:`float32 <doc_data_builtin_types>`: Values are clamped from 0 to 1. If difference between saturations is greater than this threshold, the colors are not too similar.

**ValueThreshold** :ref:`float32 <doc_data_builtin_types>`: Values are clamped from 0 to 1. If difference between values is greater than this threshold, the colors are not too similar.

Music Properties
----------------

**Loop** :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`: Looping audio clip played until loading finishes.

**Outro** :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`: Audio clip played once loading finishes.
