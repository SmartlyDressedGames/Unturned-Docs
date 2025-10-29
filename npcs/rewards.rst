.. _doc_npc_asset_rewards:

Rewards
=======

Rewards can be granted by NPC assets, interactable objects, and item blueprints. The specific property prefix may differ between asset types. For example, quests may use "Rewards" while consumables use "Quest_Rewards".

**Rewards** *byte*: Total number of rewards.

**Reward_#_Type** *enum* (``Airdrop``, ``Flag_Bool``, ``Flag_Math``, ``Flag_Short``, ``Flag_Short_Random``, ``Achievement``, ``Currency``, ``Cutscene_Mode``, ``Effect``, ``Event``, ``Experience``, ``Item``, ``Item_Random``, ``Hint``, ``Player_Life_Food``, ``Player_Life_Health``, ``Player_Life_Stamina``, ``Player_Life_Virus``, ``Player_Life_Water``, ``Player_Spawnpoint``, ``Quest``, ``Reputation``, ``Rewards_List_Asset``, ``Teleport``, ``Vehicle``, ``Zombie``)

**Reward_#_GrantDelaySeconds** *float*: If set, the reward will be queued for the specified number of seconds before being granted to the player. Defaults to -1.

**Reward_#_GrantDelayApplyWhenInterrupted** *bool*: If true, the reward will be granted when the player dies or disconnects. Defaults to false, in which case when the player dies any pending rewards are cancelled.

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

**Reward_#_B_ID** *uint16*: ID of flag containing value to be applied mathematically. If not specified then ``B_Value`` is used instead.

**Reward_#_B_Value** *int16*: default value to be applied mathematically if flag B has not been set on the player or if ``B_ID`` is zero.

**Reward_#_Operation** *enum* (``Addition``, ``Assign``, ``Division``, ``Modulo``, ``Multiplication``, ``Subtraction``, ``Random_Inclusive``, ``Random_Exclusive``): For example, using the Addition operation would set A to the value of A + B.

``Random_Inclusive`` operation: Set flag A to random number between the value of A and B. For example if A is 1 and B is 3 the random number could be 1, 2, or 3.

``Random_Exclusive`` operation: Set flag A to random number between the value of A and B, excluding B. For example if A is 1 and B is 3 the random number could be 1 or 2. If the value of A and B are the same then the exclusion rule is ignored.

Flag_Short
``````````

**Reward_#_Type** *enum* (``Flag_Short``)

**Reward_#_ID** *uint16*: ID of flag to modify.

**Reward_#_Value** *int16*: Modify flag's current value with this short value.

**Reward_#_Modification** *enum* (``Assign``, ``Decrement``, ``Increment``): Set value, subtract value, or add value.

Flag_Short_Random
`````````````````

**Reward_#_Type** *enum* (``Flag_Short_Random``)

**Reward_#_ID** *uint16*: ID of flag to modify.

**Reward_#_Min_Value** *int16*: Minimum short value to modify flag's current value by.

**Reward_#_Max_Value** *int16*: Maximum short value to modify flag's current value by.

**Reward_#_Modification** *enum* (``Assign``, ``Decrement``, ``Increment``): Set value, subtract value, or add value.

Non-flags
---------

Achievement
```````````

**Reward_#_Type** *enum* (``Achievement``)

**Reward_#_ID** *string*: ID of achievement to grant. Only specific achievements can be granted as a reward.

Airdrop
````````

**Reward_#_Type** *enum* (``Airdrop``)

**Reward_#_Use_Random_Airdrop_Node** *bool*: If true, call in airdrop at a random airdrop node placed in the level editor.

**Reward_#_Cargo** *GUID or uint16*: Optional spawn table ID overriding which items to drop.

**Reward_#_Spawnpoint** *string*: Location to call in the airdrop, using the spawnpoint name as set in the nodes level editor.

Currency
````````

Refer to :ref:`Currency <doc_assets_currency>` documentation.

**Reward_#_Type** *enum* (``Currency``)

**Reward_#_GUID** *string*: GUID of currency asset.

**Reward_#_Value** *int*: Amount of currency to reward.

Cutscene Mode
`````````````

Not as exciting as it sounds. While active, the first-person viewmodel is hidden and certain item actions like shooting are disabled. It's saved/loaded, but resets on death.

**Reward_#_Type** *enum* (``Cutscene_Mode``)

**Reward_#_Value** *bool*: Whether cutscene mode should currently be active.

.. _doc_npc_asset_rewards:effect:

Effect
```````

**Reward_#_Type** *enum* (``Effect``)

**Reward_#_GUID** :ref:`Asset Pointer <doc_data_assetptr>`: :ref:`Effect Asset<doc_assets_effect>` to spawn.

**Reward_#_Spawnpoint** *string*: Location to spawn the effect, using the spawnpoint name as set in the nodes level editor. For example, ``Liberator_Jet``.

**Reward_#_AtPlayerPosition** *bool*: If true, spawn the effect at the target player's position.

**Reward_#_IsReliable** *bool*: If true, multiplayer will ensure the effect is replicated. If false, it won't be retransmitted if the packet is lost. Defaults to true.

**Reward_#_RelevantDistance** *float*: If set, overrides the default multiplayer relevant distance of 128 meters. Defaults to -1.

**Reward_#_OnlyRelevantToInstigator** *bool*: If true, only the player triggering this reward will see the effect. Defaults to false. Takes priority over ``RelevantDistance`` if set.

.. _doc_npc_asset_rewards:event:

Event
`````

**Reward_#_Type** *enum* (``Event``)

**Reward_#_ID** *string*: ID of event to broadcast. This can be used by c# plugins with the ``NPCEventManager`` class, or Unity events with the :ref:`NPC Global Event component <doc_assets_mod_hooks:npc_global_event_hook>`. For example, when an event with ID "Fireworks" is broadcast all of the components with event ID "Fireworks" will have their corresponding Unity event triggered as well, in this case perhaps to spawn a fireworks effect.

**Reward_#_Replicate** *bool*: If true, event is triggered on clients as well as the server. Defaults to true. If false, event is only triggered on authority (singleplayer/server).

**Reward_#_InstigatorOnly** *bool*: If true, event is run only for the player triggering the reward. Defaults to false. Takes priority over ``Replicate``. In multiplayer this means the event is only broadcast for the triggering client, not the server.

Experience
``````````

**Reward_#_Type** *enum* (``Experience``)

**Reward_#_Value** *int*: Amount of experience to reward.

Item
````

**Reward_#_Type** *enum* (``Item``)

**Reward_#_ID** *uint16*: ID of item to reward.

**Reward_#_Amount** *int*: Amount of item to reward.

**Reward_#_Auto_Equip** *bool*: If true, the item should be automatically equipped by the player (if possible). Auto-equipping isn't possible if another item in the same slot is already equipped. Defaults to false.

**Reward_#_Ammo** *byte*: Override for the amount of ammuntion that should be loaded in the item reward.

**Reward_#_Barrel** *uint16*: Override for the barrel attachment that should be attached to the item reward.

**Reward_#_Grip** *uint16*: Override for the grip attachment that should be attached to the item reward.

**Reward_#_Magazine** *uint16*: Override for the magazine attachment that should be attached to the item reward.

**Reward_#_Origin** :ref:`doc_data_eitemorigin`: Set the item origin. For example, setting the origin to ``Admin`` will cause items to spawn at full quality. Defaults to ``Craft``.

**Reward_#_Sight** *uint16*: Override for the sight attachment that should be attached to the item reward.

**Reward_#_Tactical** *uint16*: Override for the tactical attachment that should be attached to the item reward.

Item_Random
```````````

**Reward_#_Type** *enum* (``Item_Random``)

**Reward_#_ID** *uint16*: ID of spawn table that the random item reward should come from.

**Reward_#_Amount** *int*: Amount of item to reward.

**Reward_#_Auto_Equip** *bool*: If true, the item should be automatically equipped by the player (if possible). Auto-equipping isn't possible if another item in the same slot is already equipped. Defaults to false.

**Reward_#_Origin** :ref:`doc_data_eitemorigin`: Set the item origin. For example, setting the origin to ``Admin`` will cause items to spawn at full quality. Defaults to ``Craft``.

Hint
````

**Reward_#_Type** *enum* (``Hint``)

**Reward_#_Text** :ref:`doc_data_richtext`: Alternative to localization file for debug text. Otherwise, translated text from **Reward_#** in the localization file is used.

**Reward_#_Duration** *float*: Duration of the hint, in seconds. Defaults to 2 seconds.

Player Life Food
````````````````

**Reward_#_Type** *enum* (``Player_Life_Food``)

**Reward_#_Value** *int*: Amount of food to add. Can be negative to decrease food.

Player Life Health
``````````````````

**Reward_#_Type** *enum* (``Player_Life_Health``)

**Reward_#_Value** *int*: Amount of health to add. Can be negative to decrease health.

Player Life Stamina
```````````````````

**Reward_#_Type** *enum* (``Player_Life_Stamina``)

**Reward_#_Value** *int*: Amount of stamina/energy to add. Can be negative to decrease stamina level.

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

**Reward_#_ID** *string* Override the player's default spawn location, using the ID of a spawnpoint node or the name of a map location node, as set in the level editor. For example, ``Liberator_Jet``. Saved and loaded between sessions. If empty, the override is removed and the default spawns are used. The ``SetNpcSpawnId`` admin command is useful for testing this.

.. hint:: On the Buak map, the player can talk with Kira to claim a room in the Factory using this reward type.

Quest
`````

**Reward_#_Type** *enum* (``Quest``)

**Reward_#_ID** *uint16*: Quest ID to give as a reward.

Reputation
``````````

**Reward_#_Type** *enum* (``Reputation``)

**Reward_#_Value** *int*: Amount of reputation to reward.

Rewards List Asset
``````````````````

**Reward_#_Type** *enum* (``Rewards_List_Asset``)

**Reward_#_GUID** :ref:`Asset Pointer <doc_data_assetptr>`: :ref:`Rewards List<doc_npc_asset_rewards_list>` to grant directly, or :ref:`Spawn Table <doc_assets_spawn>` to resolve into one.

Teleport
````````

**Reward_#_Type** *enum* (``Teleport``)

**Reward_#_Spawnpoint** *string*: Location to teleport the player to as a reward, using the ID of a spawnpoint node as set in the level editor. For example, ``Liberator_Jet``.

Vehicle
```````

**Reward_#_Type** *enum* (``Vehicle``)

**Reward_#_ID** : ID of Vehicle to be given.

**Reward_#_Spawnpoint** *string*: Location to spawn the vehicle in as a reward, using the ID of a spawnpoint node as set in the level editor. For example, ``Liberator_Jet``. If an ID is not provided, the vehicle will spawn above the NPC.

**Reward_#_PaintColor** *color*: If set, overrides color of spawned vehicle. Vehicle redirector asset's ``SpawnPaintColor`` and vehicle asset's ``DefaultPaintColors`` are bypassed.

Zombie
``````

Respawns zombie(s) at named Spawnpoint nodes. If insufficient dead zombies are available to respawn, alive zombies are converted to the appropriate type and teleported.

.. note:: Spawnpoints must be within a navmesh.

**Reward_#_Type** *enum* (``Zombie``)

**Reward_#_Zombie** *enum*: Which "type" of zombie to spawn, the same list as zombie kills condition. To-do: move to its own page.

**Reward_#_Spawnpoint** *string*: Where to spawn the zombies, using the name as set in the nodes level editor. When multiple nodes share a name each zombie is spawned at a random node.

**Reward_#_LevelTableOverride** *int*: Unique ID of a zombie type shown in the level editor. If set, the zombie spawned will use that type. Defaults to -1.

**Reward_#_SpawnQuantity** *int*: Amount of zombies to spawn.

**Reward_#_CooldownId** *string*: If set, only spawn if a named global cooldown (shared between all players) has passed.

**Reward_#_CooldownDuration** *float*: Seconds since CooldownId last ran before this reward can spawn zombies again.

Localization
------------

**Reward_#**: Name of the reward as it appears in user interfaces.
