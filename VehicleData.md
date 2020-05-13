# Vehicle Data

**Vehicles** in _Unturned_ consist of the 6 different engine types, Car, Plane, Helicopter, Blimp, Boat, and Train. Many properties of the different engine types are shared between them, however, some are specific to each engine type, and are categorized as such below.

- [Non-specific Data](#Non-specific-Data)
  - [Battery Settings](#Battery-Settings)
- [Car](#Car)
- [Plane](#Plane)
- [Helicopter](#Helicopter)
- [Blimp](#Blimp)
- [Boat](#Boat)
- [Train](#Train)

## Non Specific data

---

__ID__: The item ID is used to spawn the item into the game, and is represented as an unsigned 16 bit integer (a range of 0–65535). It is recommended not to use a value less than 2,000 as those are reserved for official content. It is also recommended to avoid any ID range being used by curated content, as those are often used by modded servers and custom Workshop maps. Vehicles ID ranges do not conflict with those of Items or Objects.

__Bypass\_ID\_Limit__: Allows you to use an ID that is within the space reserved for vanilla content.

__Size2\_Z__: Controls orthagonal camera size for vehicle skin icons. Basically irrelevant since very few vehicles have skins.

__Shared_Skin_Name__:

Shared_Skin_Lookup_ID

__Engine__: `Car`, `Plane`, `Helicopter`, `Blimp`, `Boat`, `Train`. Defaults to Car.

__Rarity__: `Common`, `Uncommon`, `Rare`, `Epic`, `Legendary`, `Mythical`. Defaults to common. 

__Zip__: Handlebar related property.

__Bicycle__: Tells unturned to use bycicle animations.

__Reclined__: Uses the slightly different drivers reclined animation.

__Crawler__: Locks wheel turning.

__LockMouse__: Locks the mouse to the forward position so the driver cannot move their view.

__Traction__: Changes the wheels physics on ice and offroad.

__Sleds__: Makes the wheels slide easier. For us on plane wheels where this effect is desired.

### Battery-Settings

__Cannot\_Spawn\_With\_Battery__: If present the vehicle will not spawn with a battery present.

__Battery\_Spawn\_Charge\_Multiplier__ Defaults to 1.

__Battery\_Burn_Rate__: Defaults to 20.

__Battery\_Charge_Rate__: Defaults to 20.

__BatteryMode\_Driving__: `Charge`, `Burn`, `None`.

__BatteryMode\_Empty__:

__BatteryMode\_Headlights__:

__BatteryMode\_Sirens__:

__Fuel\_Burn\_Rate__: The rate fuel burns at. Set to 2.05 for Car, 4.2 for others by default.

__Pitch\_Idle__: Changes the pitch of the engine audio at idle. If your audio clip is named Engine_Large or Engine_Medium this is preset to .75 and .625

__Pitch\_Drive__: Changes the pitch of the engine audio while driving. If your audio clip is named Engine_Large or Engine_Medium this is preset to .075 and .025

__Speed\_Min__: Maximum reverse speed in Meters per Second.

__Speed\_Max__: Maximum forward speed in Meters per Second.

Steer\_Min

Steer\_Max

Brake

Fuel\_Min

Fuel\_Max

Fuel

Health\_Min:

Health\_Min:

__Explosion__: ID of the explosion effect to use when destroyed.

Explosion_Min_Force_Y:

Explosion_Max_Force_Y:

Exit:

__Cam_Follow_Distance__:

Cam_Driver_Offset:

__Cam_Passenger_Offset__: Offsets the position of the passengers first person camera by set amount.

Bumper_Multiplier:

__Passenger_Explosion_Armor__: `0.0`

__Turrets__: `0`

__Turret\_`x`\_Seat_Index\_`y`__

Turret\_`x`\_Item\_ID z

Turret\_`x`\_Yaw_Min

Turret\_`x`\_Yaw_Max

Turret\_`x`\_Pitch_Min

Turret\_`x`\_Pitch_Max

Turret\_`x`\_Ignore_Aim_Camera

Turret\_`x`\_Aim\_Offset

Invulnerable

Explosions_Invulnerable

Environment_Invulnerable

Bumper_Invulnerable

__Tires_Invulnerable__: Makes tires undestroyable 

Child_Explosion_Armor_Multiplier

__Bicycle_Anim_Speed__: The speed at which the bicycle pedals spin.

Stamina_Boost

Stamina_Powered

Supports_Mobile_Buildables

Can_Be_Locked

Trunk_Storage_X

Trunk_Storage_Y

Drops_Table_ID

Drops_Min

Drops_Max

Tire_ID

__Num_Steering_Tires__:

Override_Center_Of_Mass

__Wheel_Collider_Mass_Override__: 

__Center_Of_Mass__

__Physics_Profile__: Physics Profile GUID. [Documentation can be found here](VehiclePhysicsProfile.md)

__Bypass_Hash_Verification__

__Bypass_Buildable_Mobility__: Allows you to place beds on a vehicle.

## Car

---

## Plane

---

Air_Turn_Responsiveness

Air_Steer_Min

Air_Steer_Max

__Lift__:

## Helicopter

---

## Blimp

---

## Boat

---

## Train

---

__Train\_Track\_Offset__:

__Train\_Wheel\_Offset__:

__Train\_Car\_Length__:
