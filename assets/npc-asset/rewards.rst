.. _doc_npc_asset_rewards:

Rewards
=======

Rewards can be granted by NPC assets, interactable objects, and item blueprints. The specific property prefix may differ between asset types. For example, quests may use "Rewards" while consumables use "Quest_Rewards".

**Rewards** *byte*: Total number of rewards.

**Reward_#_Type** *enum* (``Flag_Bool``, ``Flag_Math``, ``Flag_Short``, ``Flag_Short_Random``, ``Achievement``, ``Currency``, ``Event``, ``Experience``, ``Item``, ``Item_Random``, ``Hint``, ``Player_Life_Food``, ``Player_Life_Health``, ``Player_Life_Virus``, ``Player_Life_Water``, ``Player_Spawnpoint``, ``Quest``, ``Reputation``, ``Rewards_List_Asset``, ``Teleport``, ``Vehicle``)

**Reward_#_GrantDelaySeconds** *float*: If set, the reward will be queued for the specified number of seconds before being granted to the player. When the player dies any pending rewards are cancelled. Defaults to -1.

Flags
-----

Flag_Bool
`````````

**Reward_#_Type** *enum* (``Flag_Bool``)

**Reward_#_ID** *uint16*: ID of flag to set.

**Reward_#_Value** *bool*: Set flag to Boolean value, of either "True" or "False".

Flag_Math
`````````

**Reward_#_Type** *enum* (``Flag_Math``)

**Reward_#_A_ID** *uint16*: ID of flag to apply math to.

**Reward_#_B_ID** *uint16*: ID of flag containing value to be applied mathematically. If not specified then `B_Value` is used instead.

**Reward_#_B_Value** *int16*: default value to be applied mathematically if flag B has not been set on the player or if `B_ID` is zero.

**Reward_#_Operation** *enum* (``Addition``, ``Assign``, ``Division``, ``Modulo``, ``Multiplication``, ``Subtraction``): For example, using the Addition operation would set A to the value of A + B.

Flag_Short
``````````

**Reward_#_Type** *enum* (``Flag_Short``)

**Reward_#_ID** *uint16*: ID of flag to modify.

**Reward_#_Value** *int*: Modify flag's current value with this short value.

**Reward_#_Modification** *enum* (``Assign``, ``Decrement``, ``Increment``): Set value, subtract value, or add value.

Flag_Short_Random
`````````````````

**Reward_#_Type** *enum* (``Flag_Short_Random``)

**Reward_#_ID** *uint16*: ID of flag to modify.

**Reward_#_Min_Value** *int*: Minimum short value to modify flag's current value by.

**Reward_#_Max_Value** *int*: Maximum short value to modify flag's current value by.

**Reward_#_Modification** *enum* (``Assign``, ``Decrement``, ``Increment``): Set value, subtract value, or add value.

Non-flags
---------

Achievement
```````````

**Reward_#_Type** *enum* (``Achievement``)

**Reward_#_ID** *string*: ID of achievement to grant. Only specific achievements can be granted as a reward.

Currency
````````

Refer to :ref:`Currency <doc_assets_currency>` documentation.

**Reward_#_Type** *enum* (``Currency``)

**Reward_#_GUID** *string*: GUID of currency asset.

**Reward_#_Value** *int*: Amount of currency to reward.

.. _doc_npc_asset_rewards:event:

Event
`````

**Reward_#_Type** *enum* (``Event``)

**Reward_#_ID** *string*: ID of event to broadcast. This can be used by c# plugins with the ``NPCEventManager`` class, or Unity events with the :ref:`NPC Global Event component <doc_assets_mod_hooks:npc_global_event_hook>`. For example, when an event with ID "Fireworks" is broadcast all of the components with event ID "Fireworks" will have their corresponding Unity event triggered as well, in this case perhaps to spawn a fireworks effect.

Experience
``````````

**Reward_#_Type** *enum* (``Experience``)

**Reward_#_Value** *int*: Amount of experience to reward.

Item
````

**Reward_#_Type** *enum* (``Item``)

**Reward_#_ID** *uint16*: ID of item to reward.

**Reward_#_Amount** *int*: Amount of item to reward.

**Reward_#_Auto_Equip** *bool*: Item should be automatically equipped by the player.

**Reward_#_Ammo** *byte*: Override for the amount of ammuntion that should be loaded in the item reward.

**Reward_#_Barrel** *uint16*: Override for the barrel attachment that should be attached to the item reward.

**Reward_#_Grip** *uint16*: Override for the grip attachment that should be attached to the item reward.

**Reward_#_Magazine** *uint16*: Override for the magazine attachment that should be attached to the item reward.

**Reward_#_Origin** :ref:`doc_data_eitemorigin`: Set the item origin. For example, setting the origin to ``Admin`` will cause items to spawn at full quality. Defaults to `Craft`.

**Reward_#_Sight** *uint16*: Override for the sight attachment that should be attached to the item reward.

**Reward_#_Tactical** *uint16*: Override for the tactical attachment that should be attached to the item reward.

Item_Random
```````````

**Reward_#_Type** *enum* (``Item_Random``)

**Reward_#_ID** *uint16*: ID of spawn table that the random item reward should come from.

**Reward_#_Amount** *int*: Amount of item to reward.

**Reward_#_Auto_Equip** *flag*: Item should be automatically equipped by the player.

**Reward_#_Origin** :ref:`doc_data_eitemorigin`: Set the item origin. For example, setting the origin to ``Admin`` will cause items to spawn at full quality. Defaults to `Craft`.

Hint
````

**Reward_#_Type** *enum* (``Hint``)

**Reward_#_Text** :ref:`doc_data_richtext`: Text to display as a hint.

**Reward_#_Duration** *float*: Duration of the hint, in seconds. Defaults to 2 seconds.

Player Life Food
````````````````

**Reward_#_Type** *enum* (``Player_Life_Food``)

**Reward_#_Value** *int*: Amount of food to add. Can be negative to decrease food.

Player Life Health
``````````````````

**Reward_#_Type** *enum* (``Player_Life_Health``)

**Reward_#_Value** *int*: Amount of health to add. Can be negative to decrease health.

Player Life Virus
`````````````````

**Reward_#_Type** *enum* (``Player_Life_Virus``)

**Reward_#_Value** *int*: Amount of virus to add. Can be negative to decrease virus level.

Player Life Water
`````````````````

**Reward_#_Type** *enum* (``Player_Life_Water``)

**Reward_#_Value** *int*: Amount of water to add. Can be negative to decrease water.

Player Spawnpoint
`````````````````

**Reward_#_Type** *enum* (``Player_Spawnpoint``)

**Reward_#_ID** *string* Override the player's default spawn location, using the spawnpoint name set in the Devkit level editor or a map location node name. For example, ``Liberator_Jet``. Saved and loaded between sessions. If empty, the override is removed and the default spawns are used. The ``SetNpcSpawnId`` admin command is useful for testing this.

.. hint:: On the Buak map, the player can talk with Kira to claim a room in the Factory using this reward type.

Quest
`````

**Reward_#_Type** *enum* (``Quest``)

**Reward_#_ID** *uint16*: Quest ID to give as a reward.

Reputation
``````````

**Reward_#_Type** *enum* (``Reputation``)

**Reward_#_Value** *int*: Amount of reputation to reward.

Rewards_List_Asset
``````````````````

**Reward_#_Type** *enum* (``Rewards_List_Asset``)

**Reward_#_GUID** :ref:`Asset Pointer <doc_data_assetptr>`: :ref:`Reward List<doc_npc_asset_reward_list>` to grant directly, or :ref:`Spawn Table <doc_assets_spawn>` to resolve into one.

Teleport
````````

**Reward_#_Type** *enum* (``Teleport``)

**Reward_#_Spawnpoint** *string*: Location to teleport the player to as a reward, using the spawnpoint name as set in the Devkit level editor. For example, ``Liberator_Jet``.

Vehicle
```````

**Reward_#_Type** *enum* (``Vehicle``)

**Reward_#_ID** : ID of Vehicle to be given.

**Reward_#_Spawnpoint** *string*: Location to spawn the vehicle in as a reward, using the spawnpoint name as set in the Devkit level editor. For example, ``Liberator_Jet``.

Localization
------------

**Reward_#**: Name of the reward as it appears in user interfaces.
