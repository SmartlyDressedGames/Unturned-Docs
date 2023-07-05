Vehicle Assets
==============

Vehicle Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Vehicle``)

**Rarity** *enum* (``Common``, ``Uncommon``, ``Rare``, ``Epic``, ``Legendary``, ``Mythical``): Rarity of the vehicle, as text colour in vehicle menus and used for highlights.

**ID** *uint16*: Must be a unique identifier.

**Engine** *enum* (``Car``, ``Plane``, ``Helicopter``, ``Blimp``, ``Boat``, ``Train``) Defaults to (``Car``)

Driving Properties
---------------------

**Physics_Profile** *GUID* of a Physics Profile Asset

**Speed_Min** *float* Minimum speed of the vehicle.
**Speed_Max** *float* Maximum speed of the vehicle.

**Steer_Min** *float* Minimum steering of the vehicle.
**Steer_Max** *float* Maximum steering of the vehicle.

**Air_Steer_Max** *float* Maximum steering of the aircraft.
**Air_Steer_Min** *float* Maximum steering of the aircraft.

**Air_Turn_Responsiveness** *float* Steering sensitivity of the aircraft.

**Lift** *float* Upwards force applied to vehicle
  
**Brake** *float* Determines the amount of brakin force applied to the vehicle

Override_Center_Of_Mass *bool*

	**Center_Of_Mass_x** *float*
	**Center_Of_Mass_y** *float*
	**Center_Of_Mass_z** *float* 

**Override_Center_Of_Mass** Defaults to (``3``)

**Sleds** *flag* Used for Planes for having sliding wheels.

**Traction** *flag*

Wheel_Collider_Mass_Override *float* Overrides mass set on tire collider in Unity with provided value.

Damage Properties
---------------------
  
**Invulnerable** *flag* Makes vehicle immune to all weapons (excluding explosives) with the Invulnerable property.

**Explosions_Invulnerable** *flag* Makes the vehicle immune to explosions.

**Environment_Invulnerable** *flag* Makes the vehicle immune to animals, zombies, and mega zombie boulders.

**Bumper_Invulnerable** *flag* Makes the vehicle invulnerable to collisions withs other objects.

**Tires_Invulnerable** *flag* Makes the tires of the vehicle invulnerable

**Child_Explosion_Armor_Multiplier** *float* Multiplies the explosion damage dealt to people in the vehicle by provided number.

Battery Properties
---------------------

**Cannot_Spawn_With_Battery** *flag* If present the vehicle will not spawn with a battery.

**Battery_Spawn_Charge_Multiplier** *float* Multiplies the battery charge of the vehicle with provided number. Defaults to (``1``) unless **Battery_Spawn_Charge_Multiplier** is present, in which case it defaults to (``0``).

**Battery_Burn_Rate** *float*

**Battery_Charge_Rate** *float*

**BatteryMode_Driving** *enum* (``Charge``, ``Burn``, ``None``): controls how the battery should behave when driving.

**BatteryMode_Empty** *enum* (``Charge``, ``Burn``, ``None``): controls how the battery should behave when it is empty.

**BatteryMode_Headlights** *enum* (``Charge``, ``Burn``, ``None``): controls how the battery should behave when the headlights are activated.
  
**BatteryMode_Sirens** *enum* (``Charge``, ``Burn``, ``None``): controls how the battery should behave when the siren is activated.

Fuel Properties
---------------------

**Fuel** *UInt16* Maxiumum amount of fuel the vehicle can store. Defaults to 0.

**Fuel_Min** *UInt16* Minimum amount of fuel the vehicle can spawn with. Defaults to 0.

**Fuel_Max** *UInt16* Maxiumum amount of fuel the vehicle can spawn with. Defaults to 0.

**Fuel_Burn_Rate** *float* The rate the fuel burns at. Defaults to (``2.05``) for the engine type (``Car``), (``4.2``) for other types.

Health Properties
---------------------

**Health** *UInt16* Maximum amount of health the vehicle can have. Defaults to 0.

**Health_Min** *UInt16* Minimum health that the vehicle can spawn with. Defaults to 0.

**Health_Max** *UInt16* Maximum health that the vehicle can spawn with. Defaults to 0.

Explosion Properties
---------------------

**Explosion** *ID/GUID* of the effect to use when destroyed.

Miscellanious Properties
---------------------

**Pitch_Idle** *float* Changes the pitch of the engine audio at idle. If your audio clip is named Engine_Large it defaults to 0.625. If your audio clip is named Engine_Small it defaults to 0.75.

**Pitch_Drive** *float* Changes the pitch of the engine audio while driving. If your Engine type is Helicopter it defaults to 0.03. If your Engine type is Blimp it defaults to 0.1. If your Engine type is Blimp it defaults to 0.1. On every other Engine type it defaults to 0.025 for audio clips named "Engine_Large" and 0.025 for audio clips named "Engine_Small"

**Exit** *float* Exit distance from vehicle. Defaults to 2

**Cam_Follow_Distance** *float* Camera distance from player while in vehicle. Defaults to 5.5 unless Cam_Follow_Distance is present, in which case it defaults to 0.

**Bumper_Multiplier** *float* Multiplies bumper damage by provided amount.

**Can_Be_Locked** *flag*

**Trunk_Storage_X** *UInt8* Width of vehicle inventory. Defaults to 0.

**Trunk_Storage_Y** *UInt8* Height of vehicle inventory. Defaults to 0.

**Drops_Table_ID** *ID* of the Spawntable to spawn when the vehicle is destroyed. Defaults to 962.

**Drops_Min** *UInt8* Minimum amount of items to spawn when the vehicle is destroyed. Defaults to 3.

**Drops_Max** *UInt8* Maximum amount of items to spawn when the vehicle is destroyed. Defaults to 7.

**Tire_ID** *ID* of the item thats used to attach a tire. Defaults to 1451.

**Num_Steering_Tires** *Int32* Steers tires 1 through n; with n being the number of tire models. If (``crawler``) is present the value defaults to 0.

**Steering_Tire** ???

**Bicycle_Anim_Speed** *float* The speed at which the bicycle pedals spin.

**Stamina_Boost** *float* The speed that 

**Stamina_Powered** *flag* If present the vehicle will get a speed boost when shift is pressed.

**Battery_Powered** *flag* If present the vehicle will be powered by the battery. Useful on electric vehicles.

**Supports_Mobile_Buildables** *flag* Specifies wether or not you can place barricades on the vehicle.

**Should_Spawn_Seat_Capsules** *bool* If true, capsule colliders get attached to the Seat to prevent players from clipping into the ground. Should be used on vehicles with no roof.

**Can_Steal_Battery** *bool* Specifies wether or not the battery can be stolen from the vehicle.

**Train_Track_Offset** *float*

**Train_Wheel_Offset** *float*

**Train_Car_Length** *float*

**Bypass_Hash_Verification** *flag*

**Can_Repair_While_Seated** *bool*

**Valid_Speed_Up** *float*

**Valid_Speed_Down** *float*

**Valid_Speed_Horizontal** *float*

**Bypass_ID_Limit** *flag*

**Has_Clip_Prefab** *bool*

**Shared_Skin_Lookup_ID *ushort*

**Shared_Skin_Name *string*

**Size2_Z *float*

**Zip** *flag*

**Bicycle** *flag*

**Reclined** *flag*

**LockMouse** *flag*

**Crawler** *flag* If present the wheel models will not turn when steering.

**Cannot_Spawn_With_Battery** *flag* If present the Vehicle will not spawn with a battery.

**Explosion_Min_Force_Y**

**Explosion_Max_Force_Y**

**Explosion_Min_Force**

**Turrets** *UInt8* Number of Turrets on a vehicle