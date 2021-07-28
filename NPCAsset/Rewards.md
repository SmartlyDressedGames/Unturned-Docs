Rewards
=======

Rewards can be granted by NPC assets, interactable objects, and item blueprints.

**Rewards**: Total number of rewards.

**Reward\_#\_Type** *enum*

Flags
-----

### Flag_Bool

**Reward\_#\_Type** *enum* (`Flag_Bool`)

**Reward\_#\_ID** *uint16*: ID of flag to set.

**Reward\_#\_Value** *bool*: Set flag to boolean value, of either "True" or "False".

### Flag_Math

**Reward\_#\_Type** *enum* (`Flag_Math`)

**Reward\_#\_A\_ID** *uint16*: ID of flag to apply math to.

**Reward\_#\_B\_ID** *uint16*: ID of flag containing value to be applied mathematically.

**Reward\_#\_Operation** *enum* (`Addition`, `Assign`, `Division`, `Multiplication`, `Subtraction`): For example, using the Addition operation would set A to the value of A + B.

### Flag_Short

**Reward\_#\_Type** *enum* (`Flag_Short`)

**Reward\_#\_ID** *uint16*: ID of flag to modify.

**Reward\_#\_Value** *int*: Modify flag's current value with this short value.

**Reward\_#\_Modification** *enum* (`Assign`, `Decrement`, `Increment`): Set value, subtract value, or add value.

### Flag_Short_Random

**Reward\_#\_Type** *enum* (`Flag_Short_Random`)

**Reward\_#\_ID** *uint16*: ID of flag to modify.

**Reward\_#\_Min\_Value** *int*: Minimum short value to modify flag's current value by.

**Reward\_#\_Max\_Value** *int*: Maximum short value to modify flag's current value by.

**Reward\_#\_Modification** *enum* (`Assign`, `Decrement`, `Increment`): Set value, subtract value, or add value.

Non-flags
---------

### Achievement

**Reward\_#\_Type** *enum* (`Achievement`)

**Reward\_#\_ID** *string*: ID of achievement to grant. Only specific achievements can be granted as a reward.

### Currency

Refer to [Currency](/Currency.md) documentation.

**Reward\_#\_Type** *enum* (`Currency`)

**Reward\_#\_GUID** *string*: GUID of currency asset.

**Reward\_#\_Value** *int*: Amount of currency to reward.

### Event

**Reward\_#\_Type** *enum* (`Event`)

**Reward\_#\_ID** *string*: ID of event to broadcast. This can be used by c# plugins with the `NPCEventManager` class, or Unity events with the [NPC Global Event component](../ModHooks.md#npc-global-event-hook). For example, when an event with ID "Fireworks" is broadcast all of the components with event ID "Fireworks" will have their corresponding Unity event triggered as well, in this case perhaps to spawn a fireworks effect.

### Experience

**Reward\_#\_Type** *enum* (`Experience`)

**Reward\_#\_Value** *int*: Amount of experience to reward.

### Item

**Reward\_#\_Type** *enum* (`Item`)

**Reward\_#\_ID** *uint16*: ID of item to reward.

**Reward\_#\_Amount** *int*: Amount of item to reward.

**Reward\_#\_Auto\_Equip** *bool*: Item should be automatically equipped by the player.

**Reward\_#\_Ammo** *byte*: Override for the amount of ammuntion that should be loaded in the item reward.

**Reward\_#\_Barrel** *uint16*: Override for the barrel attachment that should be attached to the item reward.

**Reward\_#\_Grip** *uint16*: Override for the grip attachment that should be attached to the item reward.

**Reward\_#\_Magazine** *uint16*: Override for the magazine attachment that should be attached to the item reward.

**Reward\_#\_Sight** *uint16*: Override for the sight attachment that should be attached to the item reward.

**Reward\_#\_Tactical** *uint16*: Override for the tactical attachment that should be attached to the item reward.

### Item_Random

**Reward\_#\_Type** *enum* (`Item_Random`)

**Reward\_#\_ID** *uint16*: ID of spawn table that the random item reward should come from.

**Reward\_#\_Amount** *int*: Amount of item to reward.

**Reward\_#\_Auto\_Equip** *bool*: Item should be automatically equipped by the player.

### Hint

**Reward\_#\_Type** *enum* (`Hint`)

**Reward\_#\_Text** *string*: Text to display as a hint.

**Reward\_#\_Duration** *float*: Duration of the hint, in seconds. Defaults to 2 seconds.

### Quest

**Reward\_#\_Type** *enum* (`Quest`)

**Reward\_#\_ID** *uint16*: Quest ID to give as a reward.

### Reputation

**Reward\_#\_Type** *enum* (`Reputation`)

**Reward\_#\_Value** *int*: Amount of reputation to reward.

### Teleport

**Reward\_#\_Type** *enum* (`Teleport`)

**Reward\_#\_Spawnpoint** *string*: Location to teleport the player to as a reward, using the spawnpoint name as set in the Devkit level editor. For example, `Liberator_Jet`.

### Vehicle

**Reward\_#\_Type** *enum* (`Vehicle`)

**Reward\_#\_Spawnpoint** *string*: Location to teleport the player to as a reward, using the spawnpoint name as set in the Devkit level editor. For example, `Liberator_Jet`.

Localization
------------

**Reward_#**: Name of the reward as it appears in user interfaces.
