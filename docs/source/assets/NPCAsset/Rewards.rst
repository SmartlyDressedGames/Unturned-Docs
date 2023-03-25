.. _doc_npcasset_rewards:

Rewards
=======

Rewards can be granted by NPC assets, interactable objects, and item blueprints. The specific property prefix may differ between asset types. For example, quests may use "Rewards" while consumables use "Quest_Rewards".

**Rewards** *byte*: Total number of rewards.

**Reward\_#\_Type** *enum* (``Flag_Bool``, ``Flag_Math``, ``Flag_Short``, ``Flag_Short_Random``, ``Achievement``, ``Currency``, ``Event``, ``Experience``, ``Item``, ``Item_Random``, ``Hint``, ``Player_Spawnpoint``, ``Quest``, ``Reputation``, ``Teleport``, ``Vehicle``)

Flags
-----

Flag_Bool
`````````

**Reward\_#\_Type** *enum* (``Flag_Bool``)

**Reward\_#\_ID** *uint16*: ID of flag to set.

**Reward\_#\_Value** *bool*: Set flag to boolean value, of either "True" or "False".

Flag_Math
`````````

**Reward\_#\_Type** *enum* (``Flag_Math``)

**Reward\_#\_A\_ID** *uint16*: ID of flag to apply math to.

**Reward\_#\_B\_ID** *uint16*: ID of flag containing value to be applied mathematically. If not specified then `B_Value` is used instead.

**Reward\_#\_B\_Value** *int16*: default value to be applied mathematically if flag B has not been set on the player or if `B_ID` is zero.

**Reward\_#\_Operation** *enum* (``Addition``, ``Assign``, ``Division``, ``Modulo``, ``Multiplication``, ``Subtraction``): For example, using the Addition operation would set A to the value of A + B.

Flag_Short
``````````

**Reward\_#\_Type** *enum* (``Flag_Short``)

**Reward\_#\_ID** *uint16*: ID of flag to modify.

**Reward\_#\_Value** *int*: Modify flag's current value with this short value.

**Reward\_#\_Modification** *enum* (``Assign``, ``Decrement``, ``Increment``): Set value, subtract value, or add value.

Flag_Short_Random
`````````````````

**Reward\_#\_Type** *enum* (``Flag_Short_Random``)

**Reward\_#\_ID** *uint16*: ID of flag to modify.

**Reward\_#\_Min\_Value** *int*: Minimum short value to modify flag's current value by.

**Reward\_#\_Max\_Value** *int*: Maximum short value to modify flag's current value by.

**Reward\_#\_Modification** *enum* (``Assign``, ``Decrement``, ``Increment``): Set value, subtract value, or add value.

Non-flags
---------

Achievement
```````````

**Reward\_#\_Type** *enum* (``Achievement``)

**Reward\_#\_ID** *string*: ID of achievement to grant. Only specific achievements can be granted as a reward.

Currency
````````

Refer to [Currency](/Currency.md) documentation.

**Reward\_#\_Type** *enum* (``Currency``)

**Reward\_#\_GUID** *string*: GUID of currency asset.

**Reward\_#\_Value** *int*: Amount of currency to reward.

Event
`````

**Reward\_#\_Type** *enum* (``Event``)

**Reward\_#\_ID** *string*: ID of event to broadcast. This can be used by c# plugins with the ``NPCEventManager`` class, or Unity events with the :ref:`NPC Global Event component <assets/ModHooks:NPC Global Event Hook>`. For example, when an event with ID "Fireworks" is broadcast all of the components with event ID "Fireworks" will have their corresponding Unity event triggered as well, in this case perhaps to spawn a fireworks effect.

Experience
``````````

**Reward\_#\_Type** *enum* (``Experience``)

**Reward\_#\_Value** *int*: Amount of experience to reward.

Item
````

**Reward\_#\_Type** *enum* (``Item``)

**Reward\_#\_ID** *uint16*: ID of item to reward.

**Reward\_#\_Amount** *int*: Amount of item to reward.

**Reward\_#\_Auto\_Equip** *bool*: Item should be automatically equipped by the player.

**Reward\_#\_Ammo** *byte*: Override for the amount of ammuntion that should be loaded in the item reward.

**Reward\_#\_Barrel** *uint16*: Override for the barrel attachment that should be attached to the item reward.

**Reward\_#\_Grip** *uint16*: Override for the grip attachment that should be attached to the item reward.

**Reward\_#\_Magazine** *uint16*: Override for the magazine attachment that should be attached to the item reward.

**Reward\_#\_Origin** *enum* (``World``, ``Admin``, ``Craft``, ``Nature``): Set the item origin. For example, setting the origin to ``Admin`` will cause items to spawn at full quality. Defaults to `Craft`.

**Reward\_#\_Sight** *uint16*: Override for the sight attachment that should be attached to the item reward.

**Reward\_#\_Tactical** *uint16*: Override for the tactical attachment that should be attached to the item reward.

Item_Random
```````````

**Reward\_#\_Type** *enum* (``Item_Random``)

**Reward\_#\_ID** *uint16*: ID of spawn table that the random item reward should come from.

**Reward\_#\_Amount** *int*: Amount of item to reward.

**Reward\_#\_Auto\_Equip** *flag*: Item should be automatically equipped by the player.

**Reward\_#\_Origin** *enum* (``World``, ``Admin``, ``Craft``, ``Nature``): Set the item origin. For example, setting the origin to ``Admin`` will cause items to spawn at full quality. Defaults to `Craft`.

Hint
````

**Reward\_#\_Type** *enum* (``Hint``)

**Reward\_#\_Text** *string*: Text to display as a hint.

**Reward\_#\_Duration** *float*: Duration of the hint, in seconds. Defaults to 2 seconds.

### Player Spawnpoint

**Reward\_#\_Type** *enum* (``Player_Spawnpoint``)

**Reward\_#\_ID** *string* Location to spawn the player, using the spawnpoint name as set in the Devkit level editor or a map location node name. For example, ``Liberator_Jet``.

Quest
`````

**Reward\_#\_Type** *enum* (``Quest``)

**Reward\_#\_ID** *uint16*: Quest ID to give as a reward.

Reputation
``````````

**Reward\_#\_Type** *enum* (``Reputation``)

**Reward\_#\_Value** *int*: Amount of reputation to reward.

Teleport
````````

**Reward\_#\_Type** *enum* (``Teleport``)

**Reward\_#\_Spawnpoint** *string*: Location to teleport the player to as a reward, using the spawnpoint name as set in the Devkit level editor. For example, ``Liberator_Jet``.

Vehicle
```````

**Reward\_#\_Type** *enum* (``Vehicle``)

**Reward\_#\_ID** : ID of Vehicle to be given.

**Reward\_#\_Spawnpoint** *string*: Location to spawn the vehicle in as a reward, using the spawnpoint name as set in the Devkit level editor. For example, ``Liberator_Jet``.

Localization
------------

**Reward\_#**: Name of the reward as it appears in user interfaces.
