.. _doc_assets_zombie_difficulty:

Zombie Difficulty Assets
========================

Override the difficulty settings for zombies in a navmesh. For reference, official ZombieDifficulty.asset files can be found at ``...\Steam\steamapps\common\Unturned\Bundles\Assets\Zombie_Difficulty``.

Properties Reference
--------------------

**Type** *string*: ``SDG.Unturned.ZombieDifficultyAsset``

**Overrides_Spawn_Chance** *bool*: Whether or not the spawn chance for zombies in the navmesh should be overridden by the values set in this asset. For example, it may be useful to set this to ``false`` if you *only* wanted to tweak properties not related to spawn chances, such as the damage thresholds for stuns. Defaults to true.

**Mega_Stun_Threshold** *int*: Override the damage threshold for a hit to cause a stun.

**Normal_Stun_Threshold** *int*: Override the damage threshold for a hit to cause a stun.

**Allow_Horde_Beacon** *bool*: Whether or not Horde Beacons can be placed in the navmesh. Defaults to true.

**Speciality_Health_Override_Mode** ``None``, ``MultiplyEditorHealth``, ``MultiplyDefaultHealth``, or ``Replace``: defaults to ``None``. If set, allows zombie health to overridden per-zombie-type.

- ``None``: Do not override zombie health.
- ``MultiplyEditorHealth``: Per-speciality value is a multiplier for health configured in the level editor.
- ``MultiplyDefaultHealth``: Per-speciality value is a multiplier for vanilla health value.
- ``Replace``: Per-speciality value replaces zombie's health.

**Speciality_Health_Overrides** *dictionary*: If using ``Speciality_Health_Override_Mode``, this pairs zombie speciality (e.g., Crawler, Sprinter, Flanker, etc) to a number. For example:

.. code-block:: unturnedasset
	:linenos:

	Speciality_Health_Overrides
	{
		Crawler 100
		Burner 200
	}

Spawn Chance Properties
-----------------------

**Crawler_Chance** *float*: Decimal-to-percent chance for the zombie to be a Crawler. Defaults to 0. Requires ``Overrides_Spawn_Chance`` to be true.

**Sprinter_Chance** *float*: Decimal-to-percent chance for the zombie to be a Sprinter. Defaults to 0. Requires ``Overrides_Spawn_Chance`` to be true.

**Flanker_Chance** *float*: Decimal-to-percent chance for the zombie to be a Flanker. Defaults to 0. Requires ``Overrides_Spawn_Chance`` to be true.

**Burner_Chance** *float*: Decimal-to-percent chance for the zombie to be a Burner. Defaults to 0. Requires ``Overrides_Spawn_Chance`` to be true.

**Acid_Chance** *float*: Decimal-to-percent chance for the zombie to be a Acid Spitter. Defaults to 0. Requires ``Overrides_Spawn_Chance`` to be true.

**Boss_Electric_Chance** *float*: Decimal-to-percent chance for the zombie to be a Lightningstrike Zombie Boss. Defaults to 0. Requires ``Overrides_Spawn_Chance`` to be true.

**Boss_Wind_Chance** *float*: Decimal-to-percent chance for the zombie to be a Groundpounder Zombie Boss. Defaults to 0. Requires ``Overrides_Spawn_Chance`` to be true.

**Boss_Fire_Chance** *float*: Decimal-to-percent chance for the zombie to be a Flamethrower Zombie Boss. Defaults to 0. Requires ``Overrides_Spawn_Chance`` to be true.

**Spirit_Chance** *float*: Decimal-to-percent chance for the zombie to be a Spirit. Defaults to 0. Requires ``Overrides_Spawn_Chance`` to be true.

**DL_Red_Volatile_Chance** *float*: Decimal-to-percent chance for the zombie to be a Volatile. Defaults to 0. Requires ``Overrides_Spawn_Chance`` to be true.

**DL_Blue_Volatile_Chance** *float*: Decimal-to-percent chance for the zombie to be a Blue Volatile. Defaults to 0. Requires ``Overrides_Spawn_Chance`` to be true.

**Boss_Elver_Stomper_Chance** *float*: Decimal-to-percent chance for the zombie to be a Stomper Zombie Boss. Defaults to 0. Requires ``Overrides_Spawn_Chance`` to be true.

**Boss_Kuwait_Chance** *float*: Decimal-to-percent chance for the zombie to be an Evil Eye Zombie Boss. Defaults to 0. Requires ``Overrides_Spawn_Chance`` to be true.
