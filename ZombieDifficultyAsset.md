Zombie Difficulty Asset
=======================

Override the difficulty settings for zombies in a navmesh. For reference, official ZombieDifficulty.asset files can be found at `...\Steam\steamapps\common\Unturned\Bundles\Assets\Zombie_Difficulty`.

This is an [Asset v2](AssetsV2.md) class.

Unique Properties
-----------------

**Overrides_Spawn_Chance** *bool*: Whether or not the spawn chance for zombies in the navmesh should be overridden. For example, you would set this to false if you *only* wanted to tweak properties not related to spawning behavior, such as damage thresholds for stuns. Defaults to true.

**Mega_Stun_Threshold** *int*: Damage threshold for a hit to cause a stun.

**Normal_Stun_Threshold** *int*: Damage threshold for a hit to cause a stun.

**Allow_Horde_Beacon** *bool*: Defaults to true.

Gameplay Config Properties
--------------------------

**Crawler_Chance** *float*: Defaults to 0. Requires `Overrides_Spawn_Chance` to be true.

**Sprinter_Chance** *float*: Defaults to 0. Requires `Overrides_Spawn_Chance` to be true.

**Flanker_Chance** *float*: Defaults to 0. Requires `Overrides_Spawn_Chance` to be true.

**Burner_Chance** *float*: Defaults to 0. Requires `Overrides_Spawn_Chance` to be true.

**Acid_Chance** *float*: Defaults to 0. Requires `Overrides_Spawn_Chance` to be true.

**Boss_Electric_Chance** *float*: Defaults to 0. Requires `Overrides_Spawn_Chance` to be true.

**Boss_Wind_Chance** *float*: Defaults to 0. Requires `Overrides_Spawn_Chance` to be true.

**Boss_Fire_Chance** *float*: Defaults to 0. Requires `Overrides_Spawn_Chance` to be true.

**Spirit_Chance** *float*: Defaults to 0. Requires `Overrides_Spawn_Chance` to be true.

**DL_Red_Volatile_Chance** *float*: Defaults to 0. Requires `Overrides_Spawn_Chance` to be true.

**DL_Blue_Volatile_Chance** *float*: Defaults to 0. Requires `Overrides_Spawn_Chance` to be true.

**Boss_Elver_Stomper_Chance** *float*: Defaults to 0. Requires `Overrides_Spawn_Chance` to be true.

**Boss_Kuwait_Chance** *float*: Defaults to 0. Requires `Overrides_Spawn_Chance` to be true.
