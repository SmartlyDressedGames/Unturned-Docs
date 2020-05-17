# Vehicle Data

**Vehicles** in _Unturned_ consist of the 6 different engine types, Car, Plane, Helicopter, Blimp, Boat, and Train. Many properties of the different engine types are shared between them, however, some are specific to each engine type, and are categorized as such below.

- [Non-specific Data](#Non-specific-Properties)
  - [Battery Properties](#Battery-Properties)
  - [Driving Properties](#Driving-Properties)
  - [Fuel](#Fuel)
  - [Health](#Health)
  - [Explosion](#Explosion)
  - [Turret Properties](#Turret-Properties)
  - [Damage Properties](#Damage-Properties)
  - [Bicycle Properties](#Bicycle-Properties)
  - [Misc](#Misc)
- [Plane](#Plane)
- [Boat](#Boat)
- [Train](#Train)

## Non Specific Properties

---

__ID__: The item ID is used to spawn the item into the game, and is represented as an unsigned 16 bit integer (a range of 0–65535). It is recommended not to use a value less than 2,000 as those are reserved for official content. It is also recommended to avoid any ID range being used by curated content, as those are often used by modded servers and custom Workshop maps. Vehicles ID ranges do not conflict with those of Items or Objects.

__Bypass\_ID\_Limit__: Allows you to use an ID that is within the space reserved for vanilla content.

__Size2\_Z__: Controls orthogonal camera size for vehicle skin icons. Basically irrelevant since very few vehicles have skins. Defaults to `0.0`

__Shared_Skin_Name__:

__Shared_Skin_Lookup_ID__ ID of base vehicle that is being skinned. i.e. the vehicle's ID. Defaults to `ID`.

__Engine__: `Car`, `Plane`, `Helicopter`, `Blimp`, `Boat`, `Train`. Defaults to `Car`.

__Rarity__: `Common`, `Uncommon`, `Rare`, `Epic`, `Legendary`, `Mythical`. Defaults to `Common`.

### Battery Properties

__Cannot\_Spawn\_With\_Battery__: If present the vehicle will not spawn with a battery present.

__Battery\_Spawn\_Charge\_Multiplier__: Defaults to `1` unless __Battery\_Spawn\_Charge\_Multiplier__ is present, in which case the default value is `0`.

__Battery\_Burn_Rate__: Defaults to `20` unless __Battery\_Burn_Rate__ is present, in which case the default value is `0.0`.

__Battery\_Charge_Rate__: Defaults to `20` unless __Battery\_Charge_Rate__ is present, in which case the default value is `0.0`.

__BatteryMode\_Driving__: `Charge`, `Burn`, `None`.

__BatteryMode\_Empty__: `Charge`, `Burn`, `None`.

__BatteryMode\_Headlights__: `Charge`, `Burn`, `None`.

__BatteryMode\_Sirens__: `Charge`, `Burn`, `None`.

### Driving Properties

__Speed\_Min__: Maximum reverse speed in Meters per Second.

__Speed\_Max__: Maximum forward speed in Meters per Second. If the `Engine` is not `Train`, the speed is multiplied by `1.25`

__Steer\_Min__: Steering angle at the lowest possible speed.

__Steer\_Max__: Steering angle at the highest possible speed.

__Brake__: Determines the amount of braking force applied to the vehicle.

__Override_Center_Of_Mass__: Defaults to `false`. 

    Override_Center_Of_Mass_x
    Override_Center_Of_Mass_y
    Override_Center_Of_Mass_z

__Wheel_Collider_Mass_Override__: Overrides the setting of your wheel colliders mass to provided value. Should default to `3`

__Physics_Profile__: Physics Profile GUID. [Documentation can be found here](VehiclePhysicsProfile.md)

__Traction__: Changes the wheels physics on ice and off-road.

__Sleds__: Makes the wheels slide easier. For use on planes where this effect is desired.

### Fuel

__Fuel\_Min__: Minimum fuel that the vehicle can spawn with.

__Fuel\_Max__: Maximum fuel that the vehicle can spawn with.

__Fuel__: Maximum amount of fuel the vehicle can hold.

__Fuel\_Burn\_Rate__: The rate fuel burns at. Set to 2.05 for Car, 4.2 for others by default.

### Health

__Health__: Health of the vehicle. Vehicle spawns with this health by default.

__Health\_Min__: Minimum health that the vehicle can spawn with.

__Health\_Max__: Maximum health that the vehicle can spawn with.

### Explosion

__Explosion__: ID of the explosion effect to use when destroyed.

__Explosion_Min_Force_Y__: Defaults to `(00, 1024, 0.0)`. To set this property, include any of the below with a value.

    Explosion_Min_Force_Y_x
    Explosion_Min_Force_Y_y
    Explosion_Min_Force_Y_z

__Explosion_Max_Force_Y__: Defaults to `(00, 1024, 0.0)`. To set this property, include any of the below with a value. Any unspecified values are set to defaults

    Explosion_Max_Force_Y_x
    Explosion_Max_Force_Y_y
    Explosion_Max_Force_Y_z

### Turret Properties

__Turrets__: `x` Specifies the number of turrets on the vehicle.

__Turret\_`x`\_Seat_Index\_`y`__: Specifies which `Seat_y` the turret will use. `x` stands for the index of the turret (goes from 0,1,2...)

__Turret\_`x`\_Item\_ID__: Specifies the ID of the turret weapon (IT IS ADVISED that the turret gun has Turret in it's .dat)

__Turret\_`x`\_Yaw_Min__: Yaw determines turret rotation. `_Min` decides for the left side (Keep number lower than -180 if you want a forever spinny boi)

__Turret\_`x`\_Yaw_Max__: Determines turret rotation to the right side. (Keep number higher than 180 if you want a forever spinny boi) -360 and 360 make forever spinny boi

__Turret\_`x`\_Pitch_Min__: Specifies how high the Pitch of the turret can go. ↑ (This is called elevation)

__Turret\_`x`\_Pitch_Max__: Specifies how low the Pitch of the turret can go. ↓ (This is called depression)

__Turret\_`x`\_Ignore_Aim_Camera__: Use this if you want the turret control view to be from the seated player's perspective.

__Turret\_`x`\_Aim\_Offset__: Offsets the Aim on the Y axis.

### Damage Properties

__Invulnerable__: Makes vehicle immune to all weapons (but not explosives) without the __Invulnerable__ property.

__Explosions_Invulnerable__: Makes the vehicle immune to explosions.

__Environment_Invulnerable__: Makes the vehicle immune to zombies, animals, and thrown mega zombie boulders.

__Bumper_Invulnerable__: Makes vehicle invulnerable to collisions to damages caused by collisions with other objects.

__Tires_Invulnerable__: Makes tires Invulnerable.

__Child_Explosion_Armor_Multiplier__: Multiplies explosion damage dealt to people in the vehicle by provided number.

### Bicycle Properties

__Bicycle_Anim_Speed__: The speed at which the bicycle pedals spin.

__Stamina_Boost__: If present the vehicle will receive a boost when shift is pressed.

__Stamina_Powered__: If present the vehicle will use stamina for power.

### Misc.

__Pitch\_Idle__: Changes the pitch of the engine audio at idle. If your audio clip is named Engine_Large or Engine_Medium this is preset to .75 and .625

__Pitch\_Drive__: Changes the pitch of the engine audio while driving. If your audio clip is named Engine_Large or Engine_Medium this is preset to .075 and .025

__Exit__: Exit distance from vehicle.

__Cam_Follow_Distance__: Camera distance from player while in vehicle. Defaults to `5.5` unless __Cam_Follow_Distance__ is present, in which case the default value is `0.0`.


__Cam_Driver_Offset__:  Offsets the position of the drivers first person camera by set amount.

__Cam_Passenger_Offset__: Offsets the position of the passengers first person camera by set amount.

__Bumper_Multiplier__: Multiplies bumper damage

__Passenger_Explosion_Armor__: Defaults to `0.0`

__Can_Be_Locked__: If present it will not be possible to lock the vehicle.

__Trunk_Storage_X__: Width of trunk storage.

__Trunk_Storage_Y__: Height of trunk storage.

__Drops_Table_ID__: Defaults to `518`.

__Drops_Min__: Defaults to `3`.

__Drops_Max__: Defaults to `7`.

__Tire_ID__: ID of the item used to attach a tire. Defaults to `1451`.

__Num_Steering_Tires__: Steers tires 1 through n; with n being the number of tire models. If `crawler` is present the value defaults to 0. If `Engine` is car, this defaults to 2, otherwise, the default is 1.

__Zip__: Handlebar related property.

__Bicycle__: Tells unturned to use bicycle animations.

__Reclined__: Uses the slightly different drivers reclined animation.

__Crawler__: Locks wheel turning.

__LockMouse__: Locks the mouse to the forward position so the driver cannot move their view.

__Center_Of_Mass__: You apparently can manually specify this, though why you'd bother is beyond me.

__Bypass_Hash_Verification__: Bypasses hash-based file verification.

__Bypass_Buildable_Mobility__: Allows you to place beds on a vehicle.

__Supports_Mobile_Buildables__:

__Can_Repair_While_Seated__: `false`, `true` Allows passengers of the vehicle to repair it. Defaults to `false`.

## Plane

---

__Air_Turn_Responsiveness__: Defaults to `2`.

__Air_Steer_Min__:

__Air_Steer_Max__:

__Lift__: Upwards force applied to the vehicle


## Boat

---

## Train

---

__Train\_Track\_Offset__: Defaults to `0.0`.

__Train\_Wheel\_Offset__: Defaults to `0.0`.

__Train\_Car\_Length__: Defaults to `0.0`.
