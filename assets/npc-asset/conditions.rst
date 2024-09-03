.. _doc_npc_asset_conditions:

Conditions
==========

Conditions can be held by NPC assets, interactable objects, and item blueprints. The specific property prefix may differ between asset types. For example, quests may use "Conditions" while blueprints use "Blueprint_#_Conditions".

**Conditions** *byte*: Total number of conditions.

**Condition_#_Type** *enum* (``Compare_Flags``, ``Date_Counter``, ``Flag_Bool``, ``Flag_Short``, ``Currency``, ``Experience``, ``Item``, ``Kills_Animal``, ``Kills_Horde``, ``Kills_Object``, ``Kills_Player``, ``Kills_Tree``, ``Kills_Resource``, ``Player_Life_Food``, ``Player_Life_Health``, ``Player_Life_Stamina``, ``Player_Life_Virus``, ``Player_Life_Water``, ``Quest``, ``Reputation``, ``Skillset``, ``Holiday``, ``Time_Of_Day``, ``Weather_Blend_Alpha``, ``Weather_Status``)

**Condition_#_Reset** *flag*: Set back to equivalent of 0 when completed.

**Condition_#_Logic** *enum* (``Less_Than``, ``Less_Than_Or_Equal_To``, ``Equal``, ``Not_Equal``, ``Greater_Than_Or_Equal_To``, ``Greater_Than``): Compare current state to target state.

**Condition_#_UI_Requirements** *string*: Comma-separated condition indices. If set, only show this condition in the UI when the conditions with these indices are met. For example, a condition with "1, 2" will only be shown when conditions 1 and 2 have been completed.

Flags
-----

Compare_Flags
`````````````

Compare left-hand flag A, to right-hand flag B.

**Condition_#_Type** *enum* (``Compare_Flags``)

**Condition_#_A_ID** *uint16*: Left-hand flag ID.

**Condition_#_Allow_A_Unset** *bool*: Pass condition flag onto player, if they do not have the flag already.

**Condition_#_B_ID** *uint16*: Right-hand flag ID.

**Condition_#_Allow_B_Unset** *bool*: Pass condition if player does not have the flag yet.

Date_Counter
````````````

Every in-game morning, the world's "date counter" is incremented. In a fresh save it starts at zero. This condition takes the remainder of the date counter divided by ``Divisor`` and compares it with ``Value`` according to ``Logic``.

For example, an in-game event can be configured to occur every 4th and 5th day by setting ``Divisor`` to 5, ``Value`` to 3, and ``Logic`` to ``Greater_Than_Or_Equal_To``.

**Condition_#_Type** *enum* (``Date_Counter``)

**Condition_#_Value** *int64*: Number to compare the remainder with.

**Condition_#_Divisor** *int64*: Number to divide the world date counter by.

Flag_Bool
`````````

Boolean flag condition.

**Condition_#_Type** *enum* (``Flag_Bool``)

**Condition_#_ID** *uint16*: ID of flag to check.

**Condition_#_Value** *bool*: Target value, as a boolean.

**Condition_#_Allow_Unset** *flag*: Pass condition if player does not have the flag yet.

Flag_Short
``````````

Short flag condition.

**Condition_#_Type** *enum* (``Flag_Short``)

**Condition_#_ID** *uint16*: ID of flag to check.

**Condition_#_Value** *int*: Target value for the flag, as a 16-bit signed integer.

**Condition_#_Allow_Unset** *flag*: Pass condition if player does not have the flag yet.

Player
------

Currency
````````

Refer to :ref:`Currency <doc_assets_currency>` documentation.

**Condition_#_Type** *enum* (``Currency``)

**Condition_#_GUID** *string*: GUID of currency asset.

**Condition_#_Value** *int*: Target value, in terms of currency.

Experience
``````````

**Condition_#_Type** *enum* (``Experience``)

**Condition_#_Value** *int*: Target value, in terms of experience.

Item
````

**Condition_#_Type** *enum* (``Item``)

**Condition_#_ID** *uint16*: ID of item to search player's inventory for.

**Condition_#_Amount** *int*: Quantity of the item required.

Kills_Animal
````````````

**Condition_#_Type** *enum* (``Kills_Animal``)

**Condition_#_ID** *uint16*: ID of short flag to track stat.

**Condition_#_Value** *int*: Target value, in terms of animal kills.

**Condition_#_Animal** *uint16*: ID of animal required.

Kills_Horde
```````````

**Condition_#_Type** *enum* (``Kills_Horde``)

**Condition_#_ID** *uint16*: ID of short flag to track stat.

**Condition_#_Value** *int*: Target value, in terms of beacons completed.

**Condition_#_Nav** *byte*: Index of the navmesh that beacons should be completed in, seen as visible in the level editor.

Kills_Object
````````````

**Condition_#_Type** *enum* (``Kills_Object``)

**Condition_#_ID** *uint16*: ID of short flag to track stat.

**Condition_#_Value** *int*: Target value, in terms of object destructions.

**Condition_#_Object** *string*: GUID of object required.

**Condition_#_Nav** *byte*: Index of the navmesh that objects should be destroyed in, seen as visible in the level editor.

Kills_Player
````````````

**Condition_#_Type** *enum* (``Kills_Player``)

**Condition_#_ID** *uint16*: ID of short flag to track stat.

**Condition_#_Value** *int*: Target value, in terms of player kills.

Kills_Tree
``````````

**Condition_#_Type** *enum* (``Kills_Tree``)

**Condition_#_ID** *uint16*: ID of short flag to track stat.

**Condition_#_Value** *int*: Target value, in terms of resource destructions.

**Condition_#_Tree** *string*: GUID of resource required.

Kills_Zombie
````````````

**Condition_#_Type** *enum* (``Kills_Zombie``)

**Condition_#_ID** *uint16*: ID of short flag to track stat.

**Condition_#_Value** *int*: Target value, in terms of zombies killed.

**Condition_#_Zombie** *enum* (``Acid``, ``Boss_All``, ``Boss_Electric``, ``Boss_Elver_Stomper``, ``Boss_Fire``, ``Boss_Magma``, ``Boss_Nuclear``, ``Boss_Spirit``, ``Boss_Wind``, ``Burner``, ``Crawler``, ``DL_Blue_Volatile``, ``DL_Red_Volatile``, ``Flanker_Friendly``, ``Flanker_Stalk``, ``Mega``, ``None``, ``Normal``, ``Spirit``, ``Sprinter``): Type of zombie required.

**Condition_#_Spawn_Quantity** *int*: Number of zombies to spawn. Defaults to 1.

**Condition_#_Nav** *byte*: Index of the navmesh that zombies should be killed in, seen as visible in the level editor.

**Condition_#_Radius** *float*: Radius around players that zombies should be killed within, in meters. When a navmesh is unset and a radius is not specified, the radius defaults to 512 meters and is used for the condition.

**Condition_#_MinRadius** *float*: Zombies must be killed at least this many meters away from the player.

**Condition_#_Spawn** *flag*: Specified if the zombie type should be forcefully generated upon entering the area, which will then be deleted upon leaving the area.

**Condition_#_LevelTableOverride** *int*: Unique ID of a zombie type shown in the level editor. If set, the zombie spawned will use that type. Defaults to -1.

Player_Life_Food
````````````````

**Condition_#_Type** *enum* (``Player_Life_Food``)

**Condition_#_Value** *int*: Target value, in terms of the player's current food.

Player_Life_Health
``````````````````

**Condition_#_Type** *enum* (``Player_Life_Health``)

**Condition_#_Value** *int*: Target value, in terms of the player's current health.

Player_Life_Stamina
```````````````````

**Condition_#_Type** *enum* (``Player_Life_Stamina``)

**Condition_#_Value** *int*: Target value, in terms of the player's current stamina/energy.

Player_Life_Virus
`````````````````

**Condition_#_Type** *enum* (``Player_Life_Virus``)

**Condition_#_Value** *int*: Target value, in terms of the player's current immunity.

Player_Life_Water
`````````````````

**Condition_#_Type** *enum* (``Player_Life_Water``)

**Condition_#_Value** *int*: Target value, in terms of the player's current water.

Quest
`````

**Condition_#_Type** *enum* (``Quest``)

**Condition_#_ID** *uint16*: ID of quest to check for.

**Condition_#_Status** *enum* (``None``, ``Active``, ``Ready``, ``Completed``): Current state of the quest.

**Condition_#_Ignore_NPC** *flag*: Player does not need to be talking to an NPC within 20 meters for the quest to be completable and turned in.

Reputation
``````````

**Condition_#_Type** *enum* (``Reputation``)

**Condition_#_Value** *int*: Target value, in terms of reputation.

Skillset
````````

**Condition_#_Type** *enum* (``Skillset``)

**Condition_#_Value** *enum* (``Army``, ``Camp``, ``Chef``, ``Farm``, ``Fire``, ``Fish``, ``Medic``, ``None``, ``Police``, ``Thief``, ``Work``): Target value, as the skillset. For example, this condition could be used to offer unique questlines, dialogue, or blueprints depending on the player's chosen skillset.

World
-----

Holiday
```````

**Condition_#_Type** *enum* (``Holiday``)

**Condition_#_Value** *enum* (:ref:`ENPCHoliday <doc_data_enpcholiday>`): Target value, as the holiday.

Is_Full_Moon
````````````

**Condition_#_Type** *enum* (``Is_Full_Moon``)

**Condition_#_Value** *bool*: If true the condition passes when the full moon is up, otherwise if false the condition passes when the full moon is **not** up.

Time_Of_Day
```````````

**Condition_#_Type** *enum* (``Time_Of_Day``)

**Condition_#_Second** *int*: Second of a 24-hour clock (military time) to compare against. For example: ``0`` is midnight (the start of a day), ``43200`` is noon (12 o'clock), and ``86400`` is midnight (the end of a day). This condition respects the map's configured "Bias" values, as well as the day/night cycle length of the world. As a visual reference, the `Clock <https://unturned.wiki/wiki/Clock>`_ item can be used.

Weather_Blend_Alpha
```````````````````

The weather blend alpha condition compares the current intensity to a target value. For example, an NPC could sell umbrellas while rain is greater than 50% (0.5) blended in. This condition is supported by visibility, but is more expensive for visibility than the state condition because each listening object is updated when the intensity changes by 1% (0.01).

**Condition_#_Type** *enum* (``Weather_Blend_Alpha``)

**Condition_#_GUID** *string*: GUID of weather required.

**Condition_#_Value** *float* [0, 1]: Target value, as the weather intensity blend.

Weather_Status
``````````````

The weather status condition tests the state of the global weather. This condition is supported by visibility.

**Condition_#_Type** *enum* (``Weather_Status``)

**Condition_#_GUID** *string*: GUID of weather required.

**Condition_#_Value** *enum* (``Active``, ``Fully_Transitioned_In``, ``Fully_Transitioned_Out``, ``Transitioning``, ``Transitioning_In``, ``Transitioning_Out``): Target value, as the weather status.

Localization
------------

**Condition_#**: Name of the condition as it appears in user interfaces.
