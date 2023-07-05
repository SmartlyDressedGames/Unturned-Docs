Vehicle Assets
==============

Vehicle Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Vehicle``)

**Rarity** *enum* (``Common``, ``Uncommon``, ``Rare``, ``Epic``, ``Legendary``, ``Mythical``): Rarity of the vehicle, as text colour in vehicle menus and used for highlights.

**ID** *uint16*: Must be a unique identifier.

**Engine** *enum* (``Car``, ``Plane``, ``Helicopter``, ``Blimp``, ``Boat``, ``Train``): Defaults to ``Car``

Driving Properties
---------------------

**Physics_Profile** *GUID* of a Physics Profile Asset.

**Speed_Min** *float* Minimum speed of the vehicle. Defaults to ``0.0``.

**Speed_Max** *float* Maximum speed of the vehicle. Provided value gets multiplied by 1.25 if the ``Engine`` type is ``Train``. Defaults to ``0.0``

**Steer_Min** *float* Minimum steering of the vehicle. Defaults to ``0.0``.

**Steer_Max** *float* Maximum steering of the vehicle. Defaults to ``0.0``.

**Air_Steer_Min** *float* Minimum steering of the aircraft. Defaults to ``0.0``. If not present it will use the value of ``Steer_Min``

**Air_Steer_Max** *float* Maximum steering of the aircraft. Defaults to ``0.0``. If not present it will use the value of ``Steer_Max``

**Air_Turn_Responsiveness** *float* Steering sensitivity of the aircraft. Defaults to ``2.0``

**Lift** *float* Upwards force applied to vehicle
  
**Brake** *float* Determines the amount of brakin force applied to the vehicle

**Override_Center_Of_Mass** *bool*

**Center_Of_Mass_x** *float*

**Center_Of_Mass_y** *float*

**Center_Of_Mass_z** *float* 

**Override_Center_Of_Mass** *bool* Defaults to ``false``.

**Sleds** *flag* Used for having sliding wheels on planes and other types of vehicles where this effect is desired.

**Traction** *flag* Changes the wheels physics for ice and off-road.

**Wheel_Collider_Mass_Override** *float* Overrides mass set on tire collider in Unity with provided value.

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

**Battery_Spawn_Charge_Multiplier** *float* Multiplies the battery charge of the vehicle with provided number. Defaults to ``1.0`` unless ``Battery_Spawn_Charge_Multiplier`` is present, in which case it defaults to ``0.0``.

**Battery_Burn_Rate** *float* Rate of the battery consumption. Defaults to ``20.0``.

**Battery_Charge_Rate** *float* Rate of the battery charge. Defaults to ``20.0``.

**BatteryMode_Driving** *enum* (``Charge``, ``Burn``, ``None``): controls how the battery should behave when driving.

**BatteryMode_Empty** *enum* (``Charge``, ``Burn``, ``None``): controls how the battery should behave when it is empty.

**BatteryMode_Headlights** *enum* (``Charge``, ``Burn``, ``None``): controls how the battery should behave when the headlights are activated.
  
**BatteryMode_Sirens** *enum* (``Charge``, ``Burn``, ``None``): controls how the battery should behave when the siren is activated.

**Can_Steal_Battery** *bool* Specifies wether or not the battery can be stolen from the vehicle.

Fuel Properties
---------------------

**Fuel** *UInt16* Maxiumum amount of fuel the vehicle can store. Defaults to ``0.0``.

**Fuel_Min** *UInt16* Minimum amount of fuel the vehicle can spawn with. Defaults to ``0.0``.

**Fuel_Max** *UInt16* Maxiumum amount of fuel the vehicle can spawn with. Defaults to ``0.0``.

**Fuel_Burn_Rate** *float* The rate the fuel burns at. Defaults to ``2.05`` for the ``Engine`` type ``Car``, ``4.2`` for other types.

Health Properties
---------------------

**Health** *UInt16* Maximum amount of health the vehicle can have. Defaults to ``0``.

**Health_Min** *UInt16* Minimum health that the vehicle can spawn with. Defaults to ``0``.

**Health_Max** *UInt16* Maximum health that the vehicle can spawn with. Defaults to ``0``.

Explosion Properties
---------------------

**Explosion** *ID/GUID* of the effect to use when destroyed.

**Explosion_Min_Force_X** *float* Minimum amount of force applied to the vehicle on the X axis when the vehicle explodes. Defaults to ``0.0``.

**Explosion_Min_Force_Y** *float* Minimum amount of force applied to the vehicle on the Y axis when the vehicle explodes. Defaults to ``1024.0``.

**Explosion_Min_Force_Z** *float* Minimum amount of force applied to the vehicle on the Z axis when the vehicle explodes. Defaults to ``0.0``.

**Explosion_Max_Force_X** *float* Maximum amount of force applied to the vehicle on the X axis when the vehicle explodes. Defaults to ``0.0``.

**Explosion_Max_Force_Y** *float* Maximum amount of force applied to the vehicle on the Y axis when the vehicle explodes. Defaults to ``1024.0``.

**Explosion_Max_Force_Z** *float* Maximum amount of force applied to the vehicle on the Z axis when the vehicle explodes. Defaults to ``0.0``.

**ShouldExplosionCauseDamage** *bool* If ``true`` the explosion caused by the vehicle will deal damage. Defaults to ``true``

**ShouldExplosionBurnMaterials** *bool* If ``true`` the materials of the Model_X gameobjects in unity will turn black when the vehicle explodes. Defaults to ``true``


Turret Properties
---------------------

**Turrets** *UInt8* Number of Turrets on a vehicle.

**Turret_X_Seat_Index** *UInt8* Turret_X_Seat_Index ``0`` is the driver seat, ``1`` is seat 2, etc.

**Turret_X_Item_ID** *UInt16* Specifies the ID of the turret weapon. It is advised that the weapon has ``Turret`` in its .dat.

**Turret_X_Yaw_Min** *float* Determines turret rotation to the left side. (-180 > ``y`` for no rotation constriction).

**Turret_X_Yaw_Max** *float* Determines turret rotation to the left side. (180 < ``y`` for no rotation constriction).

**Turret_X_Pitch_Min** *float* Determines how high the pitch of the turret can go

**Turret_X_Pitch_Max** *float* Determines how low the pitch of the turret can go

**Turret_X_Ignore_Aim_Camera** *flag* Used for having the turret control view be viewed from the seated perspective (instead of the ``Aim`` gameobject).

**Turret_X_Aim_Offset** *float* Offsets the Aim on the Y axis.


Train Properties
---------------------

**Train_Track_Offset** *float* Defaults to ``0.0``

**Train_Wheel_Offset** *float* Defaults to ``0.0``

**Train_Car_Length** *float* Defaults to ``0.0``

Bicycle Properties
---------------------

**Bicycle** *flag* Tells unturned to use bicycle animations.

**Bicycle_Anim_Speed** *float* The speed at which the bicycle pedals spin.

**Stamina_Boost** *float* The speed that

**Stamina_Powered** *flag* If present the vehicle will get a speed boost when shift is pressed.

Miscellanious Properties
---------------------

**Pitch_Idle** *float* Changes the pitch of the engine audio at idle. If your audio clip is named Engine_Large it defaults to 0.625. If your audio clip is named Engine_Small it defaults to 0.75.

**Pitch_Drive** *float* Changes the pitch of the engine audio while driving. If ``Engine`` type is ``Helicopter`` it defaults to ``0.03``. If ``Engine`` type is ``Blimp`` it defaults to ``0.1``. On ``Engine`` types ``Car``, ``Plane``, ``Boat``, ``Train`` it defaults to ``0.025`` for audio clips named "Engine_Large", and 0.025 for audio clips named "Engine_Small"

**Exit** *float* Exit distance from vehicle. Defaults to ``2.0``

**Cam_Follow_Distance** *float* Camera distance from player while in vehicle. Defaults to 5.5 unless Cam_Follow_Distance is present, in which case it defaults to ``0.0``.

**Bumper_Multiplier** *float* Multiplies bumper damage by provided amount. Defaults to ``1.0``.

**Can_Be_Locked** *flag* Specifies wether or not the vehicle can be locked.

**Trunk_Storage_X** *UInt8* Width of vehicle inventory. Defaults to ``0``.

**Trunk_Storage_Y** *UInt8* Height of vehicle inventory. Defaults to ``0``.

**Drops_Table_ID** *ID* of the Spawntable to spawn when the vehicle is destroyed. Defaults to ``962``.

**Drops_Min** *UInt8* Minimum amount of items to spawn when the vehicle is destroyed. Defaults to ``3``.

**Drops_Max** *UInt8* Maximum amount of items to spawn when the vehicle is destroyed. Defaults to ``7``.

**Num_Steering_Tires** *Int32* Steers tires 1 through n; with n being the number of tire models. If ``Crawler`` is present the value defaults to ``0``. Defaults to 2 with ``Engine`` type ``Car``. Useful for vehicles where more than 2 wheels steer

**Steering_Tire_X** *Int32* X being the tire you want to steer (2 and 3 (usually for 4 steering Tires) on seperate lines) and ``Int32`` being the Wheel_``Y`` you want to steer in unity.

**Battery_Powered** *flag* If present the vehicle will be powered by the battery. Useful on electric vehicles.

**Supports_Mobile_Buildables** *flag* Specifies wether or not you can place barricades on the vehicle.

**Should_Spawn_Seat_Capsules** *bool* If ``true``, capsule colliders get attached to the Seat to prevent players from clipping into the ground. Should be used on vehicles with no roof.

**Bypass_Hash_Verification** *flag* Bypasses hash-based file verification.

**Can_Repair_While_Seated** *bool* If ``true`` allows passengers of the vehicle to repair the vehicle.

**Valid_Speed_Up** *float* Defaults to 12.5 with ``Engine`` type ``Car``, 3.25 with ``Engine`` type ``Boat``, and 100 with other types.

**Valid_Speed_Down** *float* Defaults to 25 with ``Engine`` type ``Car`` and ``Boat``, and 100 with other types.

**Valid_Speed_Horizontal** *float* Value gets multiplied with PlayerInput.RATE = 0.08 (???)

**Bypass_ID_Limit** *flag* Used for bypassing the ID limit set by vanilla vehicles (``ID`` < 200).

**Has_Clip_Prefab** *bool* Should be ``false``.

**Zip** *flag* Handlebar related property. Used on vanilla Quad, Snowmobile, Dirtbike, and Jetski.

**Reclined** *flag* Alternative reclined sitting animation for driver.

**LockMouse** *flag* If present the driver will not be able to move their view.

**Crawler** *flag* If present the wheel models will not turn when steering.


Skin Properties
---------------------

**Shared_Skin_Lookup_ID** *UInt16* ID of the vehicle that the skin applies to. Defaults to the vehicles ``ID``.

**Shared_Skin_Name** *string* funky skin stuff

**Size2_Z** *float* Controls orthogonal camera size for vehicle skin icons. Defaults to ``0.0``.