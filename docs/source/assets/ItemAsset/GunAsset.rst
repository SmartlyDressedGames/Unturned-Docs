.. _doc_itemasset_gun:

Gun Assets
==========

Ranged weapons can be used as a source of damage. Ranged weapons always show quality.

This inherits the :ref:`WeaponAsset <doc_itemasset_weapon>` class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Gun``)

**Useable** *enum* (``Gun``)

**Slot** *enum* (``Primary``, ``Secondary``, ``Tertiary``, ``Any``)

**ID** *uint16*: Must be a unique identifier.

Gun Asset Properties
--------------------

**Alert_Radius** *float*: The radius where zombies and animals should be alerted when firing ranged weapons, measured in meters. Defaults to 48 meters.

**Can_Aim_During_Sprint** *bool*: If true, the player can sprint while aiming down sights. Defaults to false.

**Aim\_In\_Duration** *float*. Seconds from pressing aim input to fully aiming down sights. Old hardcoded default was 0.2 seconds.

**Scale\_Aim\_Animation\_Speed** *bool*: If true, length of Aim_Start and Aim_Stop animations are scaled to match **Aim\_In\_Duration** (with modifiers). Defaults to true.

**Gunshot_Rolloff_Distance** *float*: The distance over which the gunshot audio rolls off until it is completely inaudible, in meters. Defaults to 16 when using ``Action String``; defaults to 64 when using ``Action Rocket``; otherwise, defaults to 512.

**Range_Rangefinder** *float*: Overrides the maximum distance displayed when using the Rangefinder tactical attachment on this ranged weapon. For example, it may be useful to set this property when using ``Action Rocket``, as explosive projectiles use ``Range`` to determine the explosion radius rather than the maximum range of the ranged weapon. Defaults to the value of the ``Range`` property.

**Turret** *flag*: Specified if the weapon should be treated as a vehicular turret. This flag affects the player's first-person viewmodel.

**Aiming\_Movement\_Speed\_Multiplier** *float*: Character movement speed multiplier while the gun is aiming down sights. Defaults to 0.75 if **Can_Aim_During_Sprint** is false.

Calibers
````````

**Attachment_Calibers** *int*: Number of unique hook attachment calibers. Cannot be used with ``Caliber``.

**Attachment\_Caliber\_#** *uint16*: ID of a caliber to check for hook attachment compatibility. Requires ``Attachment_Calibers``.

**Caliber** *uint16*: ID of the caliber to check for hook attachment or magazine attachment compatibility. To configure hook attachment and magazine attachment compatibility separately, use ``Attachment_Calibers`` and ``Magazine_Calibers`` together instead.

**Magazine_Calibers** *int*: Number of unique magazine attachment calibers. Cannot be used with ``Caliber``.

**Magazine\_Caliber\_#** *uint16*: ID of a caliber to check for magazine attachment compatibility. Requires ``Magazine_Calibers``.

**Requires_NonZero_Attachment_Caliber** *bool*: If true, attachments must specify at least one non-zero caliber. For example, this can be used to make vanilla attachments incompatible with the ranged weapon. Defaults to false.

Damage
``````

In addition to the damage properties available from the the :ref:`WeaponAsset <assets/ItemAsset/WeaponAsset:Player Damage>` class, GunAssets have some exclusive properties.

**Damage_Falloff_Multiplier** *float*: Percentage of damage to apply at maximum range. For example, a value of 0.25 with a damage of 40 means 10 damage will be dealt at maximum range. Defaults to 1.

**Damage_Falloff_Range** *float*: Percentage of maximum range where damage begins decreasing according to multiplier. For example, a value of 0.3 with a range of 200 means damage begins dropping off after 60 meters. Defaults to 1.

**Damage\_Falloff\_Max\_Range** *float*: Percentage of maximum range where damage finishes decreasing according to multiplier. For example, a value of 0.6 with a range of 200 means damage finishes dropping off after 120 meters. Defaults to 1.

**Instakill_Headshots** *bool*: If true, performing a headshot on a player will instantly kill that player. This does not apply to zombies who have been headshot, unless the single-player world or multiplayer server's difficulty configuration has ``Weapons_Use_Player_Damage`` enabled. Defaults to false.

Effects
```````

**Muzzle** *uint16* or *GUID*: ID or GUID of the effect to play when shooting.

**Explosion** *uint16* or *GUID*: ID or GUID of the effect to play upon an explosive projectile's detonation.

**Shell** *uint16* or *GUID*: ID or GUID of the effect to play after shooting. Defaults to 33 when using ``Action Pump`` or ``Action Break``; defaults to 1 when using any other action mechanism excluding ``Action Rail``; otherwise, defaults to 0.

Firing Mechanism
````````````````

**Action** *enum* (``Bolt``, ``Break``, ``Minigun``, ``Pump``, ``Rail``, ``Rocket``, ``String``, ``Trigger``): The rocket-action mechanism has inherently explosive projectiles, uses physics projectiles instead of ballistic projectiles, and has infinite firing range.

**Auto** *flag*: Specified if the automatic firing mode should be available.

**Fire_Delay_Seconds** *int*: Number of seconds to delay actually firing the weapon after performing the input to do so.

**Firerate** *byte*: Affects the minimum number of ticks between the firing of each bullet. The actual rate of fire is equal to ``50 ÷ (Firerate + 1)``, in rounds per second. Defaults to 0.

**Bursts** *int*: Number of shots to fire when using the burst firing mode. When a value greater than 0 is provided, the burst firing mode is available.

**Safety** *flag*: Specified if the safety firing mode should be available.

**Semi** *flag*: Specified if semi-automatic firing mode should be available.

Hooks Attachments
`````````````````

**Barrel** *uint16*: ID of the barrel attachment that should be attached by default. Defaults to 0.

**Grip** *uint16*: ID of the grip attachment that should be attached by default. Defaults to 0.

**Sight** *uint16*: ID of the sight attachment that should be attached by default. Defaults to 0.

**Tactical** *uint16*: ID of the tactical attachment that should be attached by default. Defaults to 0.

**Hook_Barrel** *flag*: Specified if the ranged weapon should have a barrel attachment slot.

**Hook_Grip** *flag*: Specified if the ranged weapon should have a grip attachment slot.

**Hook_Sight** *flag*: Specified if the ranged weapon should have a sight attachment slot.

**Hook_Tactical** *flag*: Specified if the ranged weapon should have a tactical attachment slot.

Jamming
```````

When using the ``Can_Ever_Jam`` flag, ranged weapons have a chance of jamming once their quality drops below a specified threshold. From the initial threshold to 0%, the chance of jamming on each shot is blended between 0% and a specified max chance. The "ChamberJammed" AudioClip is played when a jam occurs, as well as the animation "UnjamChamber" if present. For an example, the Cobra_Jam (ID 1521) is included in the game files.

**Can_Ever_Jam** *flag*: Specified if the weapon can jam.

**Jam_Quality_Threshold** *float*: Decimal representative of the quality percentage threshold for jamming can begin to occur. Defaults to 0.4. Requires ``Can_Ever_Jam``.

**Jam_Max_Chance** *float*: Decimal-to-percent chance for jamming to occur. Defaults to 0.1. Requires ``Can_Ever_Jam``.

**Unjam_Chamber_Anim**: Name of the animation clip to play for unjamming. Defaults to ``UnjamChamber``. Requires ``Can_Ever_Jam``.

Magazine Attachments
````````````````````

**Allow_Magazine_Change** *bool*: If false, the magazine in the weapon cannot be unloaded (unplaced), replaced, or reloaded. This is similar to the "Hook\_" properties available for determining valid hook attachment slots. Defaults to true.

**Ammo_Max** *byte*: Maximum for the random amount of ammo to generate in the magazine attachment that is attached by default. Defaults to 0.

**Ammo_Min** *byte*: Minimum for the random amount of ammo to generate in the magazine attachment that is attached by default. Defaults to 0.

**Ammo_Per_Shot** *byte*: Number of ammunition consumed per shot. Defaults to 1.

**Delete_Empty_Magazines** *flag*: Specified if the attached magazine should be deleted when depleted. Deprecated in favor of ``Should_Delete_Empty_Magazines``.

**Hammer_Time** *float*: Multiplier on the time it takes to finish pulling back the hammer on the ranged weapon after firing.

**Infinite_Ammo** *bool*: If true, ammunition is not depleted from the attached magazine attachment. Effectively, this allows for infinite ammo so long as there is a magazine attachment equipped with at least one round in it. Defaults to false.

**Magazine** *uint16*: ID of the magazine attachment that should be attached by default. Defaults to 0.

**Magazine_Replacements** *int*: Number of unique conditions with alternative default magazine attachments.

**Magazine\_Replacement\_#\_Map** *string*: Name of the map the condition applies to.

**Magazine\_Replacement\_#\_ID** *uint16*: ID of the alternative magazine attachment.

**Reload_Time** *float*: Multiplier on time it takes to finish reloading the ranged weapon.

**Replace** *float*: Multiplier of the reload animation length before the magazine is respawned. Must be greater than or equal to 0.01. Defaults to 1.

**Should_Delete_Empty_Magazines** *bool*: Overrides how empty magazines are handled by the action item mode. When set to true, empty magazine attachments are deleted when completely emptied. The default behavior depends on the Action used by the ranged weapon. Defaults to true when using the following Action enumerators: ``Break``, ``Pump``, ``Rail``, ``Rocket``, ``String``. Otherwise, defaults to false.

**Unplace** *float*: Multiplier of the reload animation length before the magazine is despawned.

Projectiles (Ballistics System)
```````````````````````````````

All ``Action`` mechanisms other than the rocket-action mechanism utilize the ballistics projectile system. To avoid a mismatch between max range and manual ballistic range, it is recommended to only have either ``Ballistic_Steps`` or ``Ballistic_Travel`` specified – not both.

**Ballistic_Steps** *byte*: Lifespan of ballistic projectiles. A higher value relative to ``Ballistic_Travel`` will result in less muzzle velocity. Must be a value greater than 0. Defaults to ``Range ÷ Ballistic_Travel``, rounded up to the nearest integer.

**Ballistic_Travel** *float*: Travel speed of ballistic projectiles. A higher value relative to ``Ballistic_Steps`` will result in more muzzle velocity. Must be a value greater than 0.1. Defaults to 10. If ``Ballistic_Steps`` is specified and greater than 0, and ``Ballistic_Travel`` is not specified, then ``Ballistic_Travel`` defaults to ``Range ÷ Ballistic_Steps``.

**Ballistic_Drop** *float*: Rate of projectile drop of ballistic projectiles. A higher value will result in more projectile drop. To disable projectile drop completely, set to 0. Defaults to 0.002.

Projectiles (Physics System)
````````````````````````````

When using ``Action Rocket``, the ranged weapon utilizes the physics projectile system.

**Ballistic_Force** *float*: Measured in Newtons. Applicable to the rocket action, and usage ignores all other advanced ballistic options. Defaults to 0.002.

**Projectile_Explosion_Launch_Speed** *float*: Players caught within an area-of-effect explosion caused by the ranged weapon are launched at this speed. For example, this can be used to create velocity-related items like "rocket-jumping" mods.
Defaults to ``Player_Damage × 0.1``.

**Projectile_Lifespan** *float*: Lifespan of physics projectiles. Defaults to 30 seconds.

**Projectile_Penetrate_Buildables** *flag*: Specified if area-of-effect explosions caused by ``Action Rocket`` physics projectiles should penetrate through buildables.

Recoil
``````

**Aiming\_Recoil\_Multiplier** *float*: Recoil magnitude multiplier while the gun is aiming down sights.

**Recoil_Aim** *float*: Multiplier on the end value for linear interpolation on recoil when aiming down sights, when a sight attachment that has a ``Zoom`` value greater than 2 is attached. For example, it may be desirable for sniper rifles to use this property so that they have reduced recoil while aiming down a scope. Defaults to 1.

**Recoil_Sprint** *float*: Multiplier on camera recoil while sprinting. Defaults to 1.25. Requires ``Can_Aim_During_Sprint true``.

**Recoil_Crouch** *float*: Multiplier on camera recoil while crouched. Defaults to 0.85.

**Recoil_Prone** *float*: Multiplier on camera recoil while proned. Defaults to 0.7.

**Recoil_Min_X** *float*: The minimum horizontal camera recoil in degrees.

**Recoil_Min_Y** *float*: The minimum vertical camera recoil in degrees.

**Recoil_Max_X** *float*: The maximum horizontal camera recoil in degrees.

**Recoil_Max_Y** *float*: The maximum vertical camera recoil in degrees.

**Recover_X** *float*: Multiplier on camera degrees to be counter-animated horizontally over the next 250 milliseconds.

**Recover_Y** *float*: Multiplier on camera degrees to be counter-animated vertically over the next 250 milliseconds.

**Use_Recoil_Aim** *bool*: Specifying a boolean value has no effect, as it will always be overridden based on the value of ``Recoil_Aim``. When a ``Recoil_Aim`` value is specified, defaults to true. When a ``Recoil_Aim`` value is not specified, defaults to false.

Shake
`````

**Shake_Min_X** *float*: The minimum 𝘟-axis model shake.

**Shake_Max_X** *float*: The maximum 𝘟-axis model shake.

**Shake_Min_Y** *float*: The minimum 𝘠-axis model shake.

**Shake_Max_Y** *float*: The maximum 𝘠-axis model shake.

**Shake_Min_Z** *float*: The minimum 𝘡-axis model shake.

**Shake_Max_Z** *float*: The maximum 𝘡-axis model shake.

Spread
``````

**Spread_Aim** *float*: The spread multiplier when aiming down sights. This is multiplied by the ``Spread_Angle_Degrees`` value.

**Spread_Angle_Degrees** *float*: Bullet angle of deviation away from the aiming direction. For example 15 means the shot could hit up to 15 degrees away from the center of the crosshair, whereas 0 will always hit the center of the crosshair. All other spread values are multipliers for this.

**Spread_Hip** *float*: Replaced by ``Spread_Angle_Degrees``, but maintained for backwards compatibility. Running the game with ``-ValidateAssets`` logs the equivalent ``Spread_Angle_Degrees`` value.

**Spread_Sprint** *float*: The spread multiplier when sprinting. Defaults to 1.25. Requires ``Can_Aim_During_Sprint true``.

**Spread_Crouch** *float*: The spread multiplier when crouched. Defaults to 0.85.

**Spread_Prone** *float*: The spread multiplier when prone. Defaults to 0.7.

Rewards
-------

Gun assets can use quest rewards. For example, every time the ranged weapon is fired an item could be spawned in the player's inventory. Alternatively, shooting the ranged weapon may be required to complete a quest. For more information, refer to the :ref:`Rewards <doc_npcasset_rewards>` documentation.

These rewards are prefixed with ``Shoot_Quest_``. For example, ``Shoot_Quest_Rewards 1``.
