Conditions
==========

Conditions can be held by NPC assets, interactable objects, and item blueprints. The specific property prefix may differ between asset types. For example, quests may use "Conditions" while blueprints use "Blueprint_#\_Conditions".

**Conditions** *byte*: Total number of conditions.

**Condition\_#\_Type** *enum* (`Compare_Flags`, `Flag_Bool`, `Flag_Short`, `Currency`, `Experience`, `Item`, `Kills_Animal`, `Kills_Horde`, `Kills_Object`, `Kills_Player`, `Kills_Tree`, `Kills_Resource`, `Player_Life_Food`, `Player_Life_Health`, `Player_Life_Virus`, `Player_Life_Water`, `Quest`, `Reputation`, `Skillset`, `Holiday`, `Time_Of_Day`, `Weather_Blend_Alpha`, `Weather_Status`)

**Condition\_#\_Reset** *bool*: Set back to equivalent of 0 when completed.

**Condition\_#\_Logic** *enum* (`Less_Than`, `Less_Than_Or_Equal_To`, `Equal`, `Not_Equal`, `Greater_Than_Or_Equal_To`, `Greater_Than`): Compare current state to target state.

Flags
-----

### Compare_Flags

Compare left-hand flag A, to right-hand flag B.

**Condition\_#\_Type** *enum* (`Compare_Flags`)

**Condition\_#\_A\_ID** *uint16*: Left-hand flag ID.

**Condition\_#\_Allow\_A\_Unset** *bool*: Pass condition flag onto player, if they do not have the flag already.

**Condition\_#\_B\_ID** *uint16*: Right-hand flag ID.

**Condition\_#\_Allow\_B\_Unset** *bool*: Pass condition if player does not have the flag yet.

### Flag_Bool

Boolean flag condition.

**Condition\_#\_Type** *enum* (`Flag_Bool`)

**Condition\_#\_ID** *uint16*: ID of flag to check.

**Condition\_#\_Value** *bool*: Target value, as a boolean.

**Condition\_#\_Allow_Unset** *bool*: Pass condition if player does not have the flag yet.

### Flag_Short

Short flag condition.

**Condition\_#\_Type** *enum* (`Flag_Short`)

**Condition\_#\_ID** *uint16*: ID of flag to check.

**Condition\_#\_Value** *int*: Target value for the flag, as a 16-bit signed integer.

**Condition\_#\_Allow\_Unset** *bool*: Pass condition if player does not have the flag yet.

Player
------

### Currency

Refer to [Currency](/Currency.md) documentation.

**Condition\_#\_Type** *enum* (`Currency`)

**Condition\_#\_GUID** *string*: GUID of currency asset.

**Condition\_#\_Value** *int*: Target value, in terms of currency.

### Experience

**Condition\_#\_Type** *enum* (`Experience`)

**Condition\_#\_Value** *int*: Target value, in terms of experience.

### Item

**Condition\_#\_Type** *enum* (`Item`)

**Condition\_#\_ID** *uint16*: ID of item to search player's inventory for.

**Condition\_#\_Amount** *int*: Quantity of the item required.

### Kills_Animal

**Condition\_#\_Type** *enum* (`Kills_Animal`)

**Condition\_#\_ID** *uint16*: ID of short flag to track stat.

**Condition\_#\_Value** *int*: Target value, in terms of animal kills.

**Condition\_#\_Animal** *uint16*: ID of animal required.

### Kills_Horde

**Condition\_#\_Type** *enum* (`Kills_Horde`)

**Condition\_#\_ID** *uint16*: ID of short flag to track stat.

**Condition\_#\_Value** *int*: Target value, in terms of beacons completed.

**Condition\_#\_Nav** *byte*: Index of the navmesh that beacons should be completed in, seen as visible in the level editor.

### Kills_Object

**Condition\_#\_Type** *enum* (`Kills_Object`)

**Condition\_#\_ID** *uint16*: ID of short flag to track stat.

**Condition\_#\_Value** *int*: Target value, in terms of object destructions.

**Condition\_#\_Object** *string*: GUID of object required.

**Condition\_#\_Nav** *byte*: Index of the navmesh that objects should be destroyed in, seen as visible in the level editor.

### Kills_Player

**Condition\_#\_Type** *enum* (`Kills_Player`)

**Condition\_#\_ID** *uint16*: ID of short flag to track stat.

**Condition\_#\_Value** *int*: Target value, in terms of player kills.

### Kills_Tree

**Condition\_#\_Type** *enum* (`Kills_Tree`)

**Condition\_#\_ID** *uint16*: ID of short flag to track stat.

**Condition\_#\_Value** *int*: Target value, in terms of resource destructions.

**Condition\_#\_Tree** *string*: GUID of resource required.

### Kills_Zombie

**Condition\_#\_Type** *enum* (`Kills_Resource`)

**Condition\_#\_ID** *uint16*: ID of short flag to track stat.

**Condition\_#\_Value** *int*: Target value, in terms of zombies killed.

**Condition\_#\_Zombie** *enum* (`Acid`, `Boss_All`, `Boss_Electric`, `Boss_Elver_Stomper`, `Boss_Fire`, `Boss_Magma`, `Boss_Nuclear`, `Boss_Spirit`, `Boss_Wind`, `Burner`, `Crawler`, `DL_Blue_Volatile`, `DL_Red_Volatile`, `Flanker_Friendly`, `Flanker_Stalk`, `Mega`, `None`, `Normal`, `Spirit`, `Sprinter`): Type of zombie required.

**Condition\_#\_Spawn\_Quantity** *int*: Number of zombies to spawn.

**Condition\_#\_Nav** *byte*: Index of the navmesh that zombies should be killed in, seen as visible in the level editor.

**Condition\_#\_Radius** *float*: Radius around players that zombies should be killed within, in meters. When a navmesh is unset and a radius is not specified, the radius defaults to 512 meters and is used for the condition.

**Condition\_#\_MinRadius** *float*: Zombies must be killed at least this many meters away from the player.

**Condition\_#\_Spawn** *bool*: The zombie type should be forcefully generated upon entering the area, which will then be deleted upon leaving the area.

### Player_Life_Food

**Condition\_#\_Type** *enum* (`Player_Life_Food`)

**Condition\_#\_Value** *int*: Target value, in terms of the player's current food.

### Player_Life_Health

**Condition\_#\_Type** *enum* (`Player_Life_Health`)

**Condition\_#\_Value** *int*: Target value, in terms of the player's current health.

### Player_Life_Virus

**Condition\_#\_Type** *enum* (`Player_Life_Virus`)

**Condition\_#\_Value** *int*: Target value, in terms of the player's current immunity.

### Player_Life_Water

**Condition\_#\_Type** *enum* (`Player_Life_Water`)

**Condition\_#\_Value** *int*: Target value, in terms of the player's current water.

### Quest

**Condition\_#\_Type** *enum* (`Quest`)

**Condition\_#\_ID** *uint16*: ID of quest to check for.

**Condition\_#\_Status** *enum* (`Active`, `Completed`, `Ready`): Current state of the quest.

**Condition\_#\_Ignore\_NPC** *bool*: Player does not need to be talking to an NPC within 20 meters for the quest to be completable and turned in.

### Reputation

**Condition\_#\_Type** *enum* (`Reputation`)

**Condition\_#\_Value** *int*: Target value, in terms of reputation.

### Skillset

**Condition\_#\_Type** *enum* (`Skillset`)

**Condition\_#\_Value** *enum* (`Army`, `Camp`, `Chef`, `Farm`, `Fire`, `Fish`, `Medic`,	`None`, `Police`, `Thief`, `Work`): Target value, as the skillset.

World
-----

### Holiday

**Condition\_#\_Type** *enum* (`Holiday`)

**Condition\_#\_Value** *enum* (`April_Fools`, `Christmas`, `Halloween`, `Max`, `None`): Target value, as the holiday.
    
### Time_Of_Day

**Condition\_#\_Type** *enum* (`Time_Of_Day`)

**Condition\_#\_Second**: Second of a 24-hour clock (military time) to compare against, where 43,200 is noon and 86,400 is a full day.

### Weather_Blend_Alpha

The weather blend alpha condition compares the current intensity to a target value. For example, an NPC could sell umbrellas while rain is greater than 50% (0.5) blended in. This condition is supported by visibility, but is more expensive for visibility than the state condition because each listening object is updated when the intensity changes by 1% (0.01).

**Condition\_#\_Type** *enum* (`Weather_Blend_Alpha`)

**Condition\_#\_GUID** *string*: GUID of weather required.

**Condition\_#\_Value** *float* [`0`, `1`]: Target value, as the weather intensity blend.

### Weather_Status

The weather status condition tests the state of the global weather. This condition is supported by visibility.

**Condition\_#\_Type** *enum* (`Weather_Status`)

**Condition\_#\_GUID** *string*: GUID of weather required.

**Condition\_#\_Value** *enum* (`Active`, `Fully_Transitioned_In`, `Fully_Transitioned_Out`, `Transitioning`, `Transitioning_In`, `Transitioning_Out`): Target value, as the weather status.

Localization
------------

**Condition_#**: Name of the condition as it appears in user interfaces.
