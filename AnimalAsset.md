**GUID** *32-digit hexadecimal*: Refer to [GUID](/GUID.md) documentation.

**Type** *enum* (`Animal`)

**ID** *uint16*: Must be a unique identifier.

Animal Properties
-----------------

**Health** *uint16*: Total health value.

**Regen** *float*: How often health should be regenerated, in seconds. After the specified amount of time passes, the animal regains 1 health. Defaults to 10 seconds.

**Damage** *byte*: Damage dealt to the player per attack.

**Behaviour** *enum* (`Defense`, `Offense`, `Ignore`): AI behavior type. Defense AI will run away when alerted, Offense AI will attack when alerted, and Ignore AI will run away when attacked.

**Speed_Run** *float*: Running speed in m/s.

**Speed_Walk** *float*: Walking speed in m/s.

**Horizontal\_Attack\_Range** *float*: Maximum attack range on the horizontal plane. Defaults to 2.25 meters.

**Horizontal\_Vehicle\_Attack\_Range** *float*: Maximum attack range on the horizontal plane, when the target is inside a vehicle. Defaults to 4.4 meters squared.

**Vertical\_Attack\_Range** *float*: Maximum vertical attack range. Defaults to 2 meters.

**Roars** *int*: Total number of roar sounds in Unity. A roar sound is played when the animal attacks.

**Panics** *int*: Total number of panic sounds in Unity. A panic sound is played when the animal is startled.

**Attack\_Anim\_Variants** *int*: Total number of attack animations in Unity. Defaults to 1.

**Eat\_Anim\_Variants** *int*: Total number of eat animations in Unity. Defaults to 1.

**Glance\_Anim\_Variants** *int*: Total number of glance animations in Unity. Defaults to 2.

**Startle\_Anim\_Variants** *int*: Total number of startle animations in Unity. Defaults to 1.

**Should\_Play\_Anims\_On\_Dedicated\_Server** *bool*: Defaults to false.

Drops
-----

**Reward_ID** *uint16*: ID of the item spawn table to use.

**Reward_XP** *uint*: Amount of experience to reward.

**Reward_Min** *byte*: Minimum amount of item drops to reward. Defaults to 3.

**Reward_Max** *byte*: Maximum amount of item drops to reward. Defaults to 4.

**Meat** *uint16*: ID of item to spawn when animal is killed. Deprecated in favor of Reward_ID.

**Pelt** *uint16*: ID of item to spawn when animal is killed. Deprecated in favor of Reward_ID.

Localization
------------

**Name** *string*: Animal name in user interfaces.
