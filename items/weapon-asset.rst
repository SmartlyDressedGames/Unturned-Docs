.. _doc_item_asset_weapon:

Weapon Assets
=============

Weapon assets function as a source of damage. The functional implementation of properties may differ slightly between assets.

This inherits the :ref:`ItemAsset <doc_item_asset_intro>` class.

Weapon Asset Properties
-----------------------

**Allow_Flesh_Fx** *bool*: Boolean for if special effects should occur when damaging flesh. Defaults to true.

**Durability** *float32*: Probability of quality loss upon the weapon being used, as a decimal.

.. _doc_item_asset_weapon:range:

**Range** *float32*: The maximum distance in meters before damage is no longer possible. For ballistic projectile ranged weapons, this is the maximum distance a projectile may travel. For melee weapons, this is the maximum swinging distance. For physics projectile ranged weapons, this is the radius of the explosion.

**Wear** *uint8*: Increment to degrade quality by. Defaults to 1.

.. _doc_item_asset_weapon:player_damage:

Player Damage
`````````````

**Bypass_Allowed_To_Damage_Player** *bool*: Boolean for if the weapon should bypass the requirements for being allowed to damage other players. Typically, a weapon cannot damage another player if the server is set to PvE, or if the target player is a part of the same group and friendly fire is disabled. Defaults to false.

**Player_Damage** *float32*: Amount of damage that should be dealt to player entities, prior to modifiers such as limb multipliers.

**Player_Leg_Multiplier** *float32*: Multiplier on damage targeted against a player's legs. Limb multipliers are not utilized by explosive weapons.

**Player_Arm_Multiplier** *float32*: Multiplier on damage targeted against a player's arms. Limb multipliers are not utilized by explosive weapons.

**Player_Spine_Multiplier** *float32*: Multiplier on damage targeted against a player's torso. Limb multipliers are not utilized by explosive weapons.

**Player_Skull_Multiplier** *float32*: Multiplier on damage targeted against a player's head. Limb multipliers are not utilized by explosive weapons.

**Player_Damage_Bleeding** *enum* (``Always``, ``Default``, ``Heal``, ``Never``): Determines the effect the weapon has in relation to the "Bleeding" status effect. When using "Always", the Bleeding status effect will always be applied on hit. When using "Default", the Bleeding status effect will only be applied if the necessary damage threshold is met. When using "Heal", anyone hit by the weapon will have their Bleeding status effect removed. When using "Never", the Bleeding status effect is never applied by this weapon. Defaults to "Default" enumerator.

**Player_Damage_Bones** *enum* (``Always``, ``Heal``, ``None``): Determines the effect the weapon has in relation to the "Broken Bones" status effect. When using "Always", the Broken Bones status effect will always be applied on hit. When using "Heal", anyone hit by the weapon will have their Broken Bones status effect removed. When using "Never", the Broken Bones status effect is never applied by this weapon. Defaults to the "None" enumerator.

**Player_Damage_Food** *float32*: Amount of degradation dealt to a targeted player's food. Positive values are beneficial (increasing food level), and negative values are detrimental (decreasing food level). Negative values are blocked in the same situations damage is blocked (e.g., in safezones or shortly after respawns).

**Player_Damage_Water** *float32*: Amount of degradation dealt to a targeted player's water. Positive values are beneficial (increasing water level), and negative values are detrimental (decreasing water level). Negative values are blocked in the same situations damage is blocked (e.g., in safezones or shortly after respawns).

**Player_Damage_Virus** *float32*: Amount of degradation dealt to a targeted player's immunity. Positive values are beneficial (increasing immunity level), and negative values are detrimental (decreasing immunity level). Negative values are blocked in the same situations damage is blocked (e.g., in safezones or shortly after respawns).

**Player_Damage_Hallucination** *float32*: Length of hallucinations inflicted onto a targeted player, in seconds. Positive values are detrimental (increasing hallucination duration), and negative values are beneficial (decreasing hallucination duration). Positive values are blocked in the same situations damage is blocked (e.g., in safezones or shortly after respawns).

Zombie Damage
`````````````

**Zombie_Damage** *float32*: Amount of damage that should be dealt to zombie entities, prior to modifiers such as limb multipliers.

**Zombie_Leg_Multiplier** *float32*: Multiplier on damage targeted against a zombie's legs. Limb multipliers are not utilized by explosive weapons.

**Zombie_Arm_Multiplier** *float32*: Multiplier on damage targeted against a zombie's arms. Limb multipliers are not utilized by explosive weapons.

**Zombie_Spine_Multiplier** *float32*: Multiplier on damage targeted against a zombie's torso. Limb multipliers are not utilized by explosive weapons.

**Zombie_Skull_Multiplier** *float32*: Multiplier on damage targeted against a zombie's head. Limb multipliers are not utilized by explosive weapons.

**Stun_Zombie_Always** *flag*: Specified if a zombie should always be stunned when targeted by the weapon.

**Stun_Zombie_Never** *flag*: Specified if a zombie should never be stunned when targeted by the weapon.

Animal Damage
`````````````

**Animal_Damage** *float32*: Amount of damage that should be dealt to animal entities, prior to modifiers such as limb multipliers.

**Animal_Leg_Multiplier** *float32*: Multiplier on damage targeted against a animal's limbs. Limb multipliers are not utilized by explosive weapons.

**Animal_Spine_Multiplier** *float32*: Multiplier on damage targeted against a animal's torso. Limb multipliers are not utilized by explosive weapons.

**Animal_Skull_Multiplier** *float32*: Multiplier on damage targeted against a animal's head. Limb multipliers are not utilized by explosive weapons.

Construct Damage
````````````````

**BladeID** *uint8*: Weapon can damage any resources or objects that have a matching BladeID. Deprecated in favor of BladeIDs and BladeID\_#.

**BladeIDs** *int32*: Total number of unique BladeID\_# values.

**BladeID_#** *uint8*: Weapon can damage any resources or objects that have a matching BladeID\_# value.

**Barricade_Damage** *float32*: Amount of damage that should be dealt to barricades, prior to modifiers.

**Structure_Damage** *float32*: Amount of damage that should be dealt to structures, prior to modifiers.

**Vehicle_Damage** *float32*: Amount of damage that should be dealt to vehicles, prior to modifiers.

**Resource_Damage** *float32*: Amount of damage that should be dealt to resources, prior to modifiers.

**Object_Damage** *float32*: Amount of damage that should be dealt to objects, prior to modifiers. Defaults to the value used by Resource_Damage.

**Invulnerable** *flag*: Specified if damage should affect objects, structures, barricades, and vehicles that are considered invulnerable to low-power weaponry. Not applicable to explosive weapons, which will always ignore invulnerability.
