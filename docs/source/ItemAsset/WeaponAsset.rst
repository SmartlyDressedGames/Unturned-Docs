Weapon Assets
=============

Weapon assets function as a source of damage. The functional implementation of properties may differ slightly between assets.

This inherits the `ItemAsset <README.rst>`_ class.

Weapon Asset Properties
=======================

**Allow_Flesh_Fx** *bool*: Boolean for if special effects should occur when damaging flesh. Defaults to true.

**Durability** *float*: Probability of quality loss upon the weapon being used, as a decimal.

**Range** *float*: The maximum distance in meters before damage is no longer possible. For ballistic ranged weapons, this is the maximum distance a projectile may travel. For melee weapons, this is the maximum swinging distance. For explosive weapons, this is the radius of the explosion.

**Wear** *byte*: Increment to degrade quality by. Defaults to 1.

Player Damage
-------------

**Bypass_Allowed_To_Damage_Player** *bool*: Boolean for if the weapon should bypass the requirements for being allowed to damage other players. Typically, a weapon cannot damage another player if the server is set to PvE, or if the target player is a part of the same group and friendly fire is disabled. Defaults to false.

**Player_Damage** *float*: Amount of damage that should be dealt to player entities, prior to modifiers such as limb multipliers.

**Player_Leg_Multiplier** *float*: Multiplier on damage targeted against a player's legs. Limb multipliers are not utilized by explosive weapons.

**Player_Arm_Multiplier** *float*: Multiplier on damage targeted against a player's arms. Limb multipliers are not utilized by explosive weapons.

**Player_Spine_Multiplier** *float*: Multiplier on damage targeted against a player's torso. Limb multipliers are not utilized by explosive weapons.

**Player_Skull_Multiplier** *float*: Multiplier on damage targeted against a player's head. Limb multipliers are not utilized by explosive weapons.

**Player_Damage_Bleeding** *enum* (``Always``, ``Default``, ``Heal``, ``Never``): Determines the effect the weapon has in relation to the "Bleeding" status effect. Defaults to "Default" enumerator.

**Player_Damage_Bones** *enum* (``Always``, ``Heal``, ``None``): Determines the effect the weapon has in relation to the "Broken Bones" status effect. Defaults to the "None" enumerator.

**Player_Damage_Food**: Amount of degradation dealt to a targeted player's food.

**Player_Damage_Water**: Amount of degradation dealt to a targeted player's water.

**Player_Damage_Virus**: Amount of degradation dealt to a targeted player's immunity.

**Player_Damage_Hallucination**: Length of hallucinations inflicted onto a targeted player, in seconds.

Zombie Damage
-------------

**Zombie_Damage** *float*: Amount of damage that should be dealt to zombie entities, prior to modifiers such as limb multipliers.

**Zombie_Leg_Multiplier** *float*: Multiplier on damage targeted against a zombie's legs. Limb multipliers are not utilized by explosive weapons.

**Zombie_Arm_Multiplier** *float*: Multiplier on damage targeted against a zombie's arms. Limb multipliers are not utilized by explosive weapons.

**Zombie_Spine_Multiplier** *float*: Multiplier on damage targeted against a zombie's torso. Limb multipliers are not utilized by explosive weapons.

**Zombie_Skull_Multiplier** *float*: Multiplier on damage targeted against a zombie's head. Limb multipliers are not utilized by explosive weapons.

**Stun_Zombie_Always** *flag*: Specified if a zombie should always be stunned when targeted by the weapon.

**Stun_Zombie_Never** *flag*: Specified if a zombie should never be stunned when targeted by the weapon.

Animal Damage
-------------

**Animal_Damage** *float*: Amount of damage that should be dealt to animal entities, prior to modifiers such as limb multipliers.

**Animal_Leg_Multiplier** *float*: Multiplier on damage targeted against a animal's limbs. Limb multipliers are not utilized by explosive weapons.

**Animal_Spine_Multiplier** *float*: Multiplier on damage targeted against a animal's torso. Limb multipliers are not utilized by explosive weapons.

**Animal_Skull_Multiplier** *float*: Multiplier on damage targeted against a animal's head. Limb multipliers are not utilized by explosive weapons.

Construct Damage
----------------

**BladeID** *byte*: Weapon can damage any resources that have a matching BladeID. Deprecated in favor of BladeIDs and BladeID\_#.

**BladeIDs** *int*: Total number of unique BladeID\_# values.

**BladeID_#** *byte*: Weapon can damage any resources that have a matching BladeID\_# value.

**Barricade_Damage** *float*: Amount of damage that should be dealt to barricades, prior to modifiers.

**Structure_Damage** *float*: Amount of damage that should be dealt to structures, prior to modifiers.

**Vehicle_Damage** *float*: Amount of damage that should be dealt to vehicles, prior to modifiers.

**Resource_Damage** *float*: Amount of damage that should be dealt to resources, prior to modifiers.

**Object_Damage** *float*: Amount of damage that should be dealt to objects, prior to modifiers. Defaults to the value used by Resource_Damage.

**Invulnerable** *flag*: Specified if damage should affect structures, barricades, and vehicles that are considered invulnerable to low-power weaponry. Not applicable to explosive weapons, which will always ignore invulnerability.
