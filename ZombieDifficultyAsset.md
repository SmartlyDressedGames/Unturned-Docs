**NOTICE:** *You are not reading the most up-to-date documentation. This file is old, and may not reflect the current modding or server capabilities. The latest documentation can be found at [Unturned Documentation](https://docs.smartlydressedgames.com/).*

*This file may be removed in the future. Refer to its more [up-to-date equivalent](https://docs.smartlydressedgames.com/en/stable/assets/zombie-difficulty-asset.html) instead.*

Zombie Difficulty Asset
=======================

Override the difficulty settings for zombies in a navmesh. For reference, official ZombieDifficulty.asset files can be found at `...\Steam\steamapps\common\Unturned\Bundles\Assets\Zombie_Difficulty`.

This is an [Asset v2](AssetsV2.md) class.

Properties Reference
--------------------

**Overrides_Spawn_Chance** *bool*: Whether or not the spawn chance for zombies in the navmesh should be overridden by the values set in this asset. For example, it may be useful to set this to `false` if you *only* wanted to tweak properties not related to spawn chances, such as the damage thresholds for stuns. Defaults to true.

**Mega_Stun_Threshold** *int*: Override the damage threshold for a hit to cause a stun.

**Normal_Stun_Threshold** *int*: Override the damage threshold for a hit to cause a stun.

**Allow_Horde_Beacon** *bool*: Whether or not Horde Beacons can be placed in the navmesh. Defaults to true.

Spawn Chance Properties
-----------------------

**Crawler_Chance** *float*: Decimal-to-percent chance for the zombie to be a Crawler. Defaults to 0. Requires `Overrides_Spawn_Chance` to be true.

**Sprinter_Chance** *float*: Decimal-to-percent chance for the zombie to be a Sprinter. Defaults to 0. Requires `Overrides_Spawn_Chance` to be true.

**Flanker_Chance** *float*: Decimal-to-percent chance for the zombie to be a Flanker. Defaults to 0. Requires `Overrides_Spawn_Chance` to be true.

**Burner_Chance** *float*: Decimal-to-percent chance for the zombie to be a Burner. Defaults to 0. Requires `Overrides_Spawn_Chance` to be true.

**Acid_Chance** *float*: Decimal-to-percent chance for the zombie to be a Acid Spitter. Defaults to 0. Requires `Overrides_Spawn_Chance` to be true.

**Boss_Electric_Chance** *float*: Decimal-to-percent chance for the zombie to be a Lightningstrike Zombie Boss. Defaults to 0. Requires `Overrides_Spawn_Chance` to be true.

**Boss_Wind_Chance** *float*: Decimal-to-percent chance for the zombie to be a Groundpounder Zombie Boss. Defaults to 0. Requires `Overrides_Spawn_Chance` to be true.

**Boss_Fire_Chance** *float*: Decimal-to-percent chance for the zombie to be a Flamethrower Zombie Boss. Defaults to 0. Requires `Overrides_Spawn_Chance` to be true.

**Spirit_Chance** *float*: Decimal-to-percent chance for the zombie to be a Spirit. Defaults to 0. Requires `Overrides_Spawn_Chance` to be true.

**DL_Red_Volatile_Chance** *float*: Decimal-to-percent chance for the zombie to be a Volatile. Defaults to 0. Requires `Overrides_Spawn_Chance` to be true.

**DL_Blue_Volatile_Chance** *float*: Decimal-to-percent chance for the zombie to be a Blue Volatile. Defaults to 0. Requires `Overrides_Spawn_Chance` to be true.

**Boss_Elver_Stomper_Chance** *float*: Decimal-to-percent chance for the zombie to be a Stomper Zombie Boss. Defaults to 0. Requires `Overrides_Spawn_Chance` to be true.

**Boss_Kuwait_Chance** *float*: Decimal-to-percent chance for the zombie to be an Evil Eye Zombie Boss. Defaults to 0. Requires `Overrides_Spawn_Chance` to be true.
