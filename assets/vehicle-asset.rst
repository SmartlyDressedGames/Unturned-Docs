.. _doc_assets_vehicle:

Vehicle Assets
==============

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Vehicle``)

**Rarity** *enum* (``Common``, ``Uncommon``, ``Rare``, ``Epic``, ``Legendary``, ``Mythical``): Rarity of the vehicle, as text shown in menus and colors used for highlights. Defaults to ``Common`` rarity.

**Engine** *enum* (``Blimp``, ``Boat``, ``Car``, ``Helicopter``, ``Plane``, ``Train``): Defaults to ``Car``. Some properties will only be usable depending on the ``Engine`` enumerator used, or may behave differently.

**ID** *uint16*: Must be a unique identifier.

Vehicle Properties
------------------

**Bicycle** *flag*: Player character should use a bicycling animation.

**Bicycle_Anim_Speed** *float*: Multiplier on the speed of the bicycling animation.

**Buildable_Placement_Rule** *enum* (``None``, ``AlwaysAllow``, ``Block``): Overrides how barricades can be attached to the vehicle. Defaults to ``None``, i.e., no override.

  - ``None``: Vehicle does not override placement. This means, by default, that barricades can be placed on the vehicle unless the barricade sets ``Allow_Placement_On_Vehicle`` to false. (e.g., beds and sentry guns) Note that gameplay config ``Bypass_Buildable_Mobility``, if true, takes priority.
  - ``AlwaysAllow``: Vehicle allows any barricade to be placed on it, regardless of the barricade's ``Allow_Placement_On_Vehicle`` setting. The legacy option for this was the ``Supports_Mobile_Buildables`` flag. Vanilla trains originally used this option, but it was exploited to move beds into tunnel walls.
  - ``Block``: Vehicle prevents any barricade from being placed on it. Note that gameplay config ``Bypass_Buildable_Mobility``, if true, takes priority.

**Bypass_Hash_Verification** *flag*: Disable hash verification check, and allow for mismatched files.

**Bypass_ID_Limit** *flag*: Allows for using an ``ID`` value within the range reserved for official content.

**Cam_Driver_Offset** *float*: The vertical offset for the driver's first-person camera, in meters. This is additive with the value of ``Cam_Passenger_Offset``.

**Cam_Follow_Distance** *float*: The distance behind the player the third-person camera should be placed at, in meters. Defaults to 5.5.

**Cam_Passenger_Offset** *float*: The vertical offset for any passenger's (including the driver's) first-person camera, in meters.

**Can_Be_Locked** *bool*: Whether or not the vehicle can be locked a player. Defaults to true.

**Crawler** *flag*: *deprecated* Disables the ``Wheel_#`` GameObjects from turning when steering by setting the default value of ``Num_Steering_Tires`` to 0. This property has no effect if ``Num_Steering_Tires`` has been manually set.

.. note:: Replaced by the ``WheelConfigurations`` propery.

.. deprecated:: 3.23.4.0

**Drops_Table_ID** *uint16*: ID of the item spawn table to use when the vehicle is destroyed. Defaults to 962.

**Drops_Min** *uint8*: Minimum amount of item drops to spawn when the vehicle is destroyed. Defaults to 3.

**Drops_Max** *uint8*: Maximum amount of item drops to spawn when the vehicle is destroyed. Defaults to 7.

**Exit** *float*: Distance away from the vehicle to teleport when exiting. Defaults to 2.

**Has_Clip_Prefab** *bool*: Whether or not the vehicle has a Clip.prefab. If the vehicle should use the same prefab on the server as on the client, set to false. For example, most official content uses ``Has_Clip_Prefab false``. Defaults to true.

**Has_Horn** *bool*: Whether or not the vehicle should have a horn. Defaults to true when the vehicle either has a ``Horn`` AudioClip, or the ``HornAudioClip`` property has been set to a valid path. Otherwise, defaults to false.

**HornAudioClip** :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`: AudioClip to play when using the horn.

**IgnitionAudioClip** :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`: AudioClip to play when after entering the driver's seat.

**LockMouse** *flag*: First-person camera movement is locked while driving. This is useful for ``Engine Plane`` and ``Engine Helicopter``, as a player's mouse movement while in first-person can be used to steer the vehicle.

**Num_Steering_Tires** *int32*: *deprecated* Total number of tires that should turn when steering. Defaults to 2 when using ``Engine Car``, to 1 when using any other ``Engine`` enumerator, or to 0 if the ``Crawler`` property has been set.

.. note:: Replaced by the ``WheelConfigurations`` propery.

.. deprecated:: 3.23.4.0

**Pitch_Drive** *float*: Multiplier on the pitch of the engine audio while driving. Defaults to 0.03 when using ``Engine Helicopter``, or to 0.1 when using ``Engine Blimp``. For other ``Engine`` enumerators, it defaults to 0.025 if the audio clip is named "Engine_Large", or to 0.075 if the audio clip is named "Engine_Small".

**Pitch_Idle** *float*: Multiplier on the pitch of the engine audio while idle. Defaults to 0.625 if the audio clip is named "Engine_Large, or to 0.75 if the audio clip is named "Engine_Small".

**Reclined** *flag*: Player character should use a reclined idle animation.

**Should_Spawn_Seat_Capsules** *bool*: If true, capsule colliders will be attached to the ``Seat`` GameObject in order to prevent players from clipping into the ground. This is useful for vehicles that do not have a roof. Defaults to false.

**Steering_Tire_#** *int32*: *deprecated* Set a ``Wheel_#`` GameObject as a steering tire, which will visibly turn when steering. By default, a number of steering tires equal to the value of ``Num_Steering_Tires`` will be automatically set. These will start at ``Steering_Tire_0 0`` (corresponding to ``Wheel_0``), and increment upwards.

.. note:: Replaced by the ``WheelConfigurations`` propery.

.. deprecated:: 3.23.4.0

**Tire_ID** *uint16*: ID of the item that should given when a tire is manually removed with a :ref:`ToolAsset <doc_item_asset_tire>` that has ``Mode Remove``, and can also be manually attached to the vehicle if the specified item ID is for a :ref:`ToolAsset <doc_item_asset_tire>` with ``Mode Add``. Defaults to 1451.

**Trunk_Storage_X** *byte*: Number of columns (horizontal storage space). Defaults to 0.

**Trunk_Storage_Y** *byte*: Number of rows (vertical storage space). Defaults to 0.

**Valid_Speed_Down** *float*: Configuring this will override the sanity check for reversing speed, in m/s (meters per second). Defaults to 25 when using ``Engine Car``, to 25 when using ``Engine Boat``, or to 100 otherwise.

**Valid_Speed_Horizontal** *float*: Configuring this will override the sanity check for horizontal speed. This value is multiplied by PlayerInput.RATE (0.08), and then squared. Defaults to ``(Speed_Max * 0.125)^2`` when using ``Engine Helicopter`` or ``Engine Blimp``, or to ``(Speed_Max * 0.1)^2`` otherwise. This property is useful for vehicles with speed that the server cannot predict, such as force-applying Unity components.

**Valid_Speed_Up** *float*: Configuring this will override the sanity check for forward speed, in m/s (meters per second). Defaults to 12.5 when using ``Engine Car``, to 3.25 when using ``Engine Boat``, or to 100 otherwise.

**Zip** *flag*: Player character should use a handlebar idle animation.

Paint
`````

.. _doc_assets_vehicle:paintablesections:

**PaintableSections** :ref:`list of PaintableSection dictionaries <doc_assets_vehicle:paintablesection_dictionary>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If set, the vehicle can be painted with a :ref:`Vehicle Paint Tool <doc_item_asset_vehicle_paint_tool>`. Each section's material's ``_PaintColor`` property is set to the vehicle's paint color.

.. _doc_assets_vehicle:defaultpaintcolors:

**DefaultPaintColors** :ref:`list of colors <doc_data_color>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

List of random colors to pick from when spawning a new vehicle. Can be overridden by a :ref:`Vehicle Redirector<doc_asset_vehicle_redirector>`'s :ref:`LoadPaintColor <doc_asset_vehicle_redirector:loadpaintcolor>` and :ref:`LoadPaintColor <doc_asset_vehicle_redirector:spawnpaintcolor>` properties.

Handling
````````

**Air_Steer_Min** *float*: The angle to turn when moving slowly, when using ``Engine Plane``. Defaults to the value of ``Steer_Min``.

**Air_Steer_Max** *float*: The angle to turn when moving quickly, when using ``Engine Plane``. Defaults to the value of ``Steer_Max``.

**Air_Turn_Responsiveness** *float*: Sensitivity on steering while airborne, when using ``Engine Plane``. Defaults to 2.

**Brake** *float*: The amount of braking force to apply.

**Center_Of_Mass_X** *float*: Overrides the vehicle's center of mass on the 𝘟-axis, when using ``Override_Center_Of_Mass true``.

**Center_Of_Mass_Y** *float*: Overrides the vehicle's center of mass on the 𝘠-axis, when using ``Override_Center_Of_Mass true``.

**Center_Of_Mass_Z** *float*: Overrides the vehicle's center of mass on the 𝘡-axis, when using ``Override_Center_Of_Mass true``.

**Lift** *float*: The amount of upwards lift force to apply, when using ``Engine Plane``.

**Override_Center_Of_Mass** *bool*: If true, override the vehicle's center of mass with the values from the ``Center_Of_Mass_#`` Vector3 properties. This allows for modifying a vehicle's center of gravity without needing to move the ``Cog`` GameObject in Unity.

**Physics_Profile** :ref:`GUID <doc_data_guid>`: GUID of a :ref:`VehiclePhysicsProfileAsset <doc_assets_vehicle_physics_profile>` to use. Using a vehicle physics profile is optional. Defaults to ``47258d0dcad14cb8be26e24c1ef3449e`` when using ``Engine Boat``, to ``6b91a94f01b6472eaca31d9420ec2367`` when using ``Engine Car``, to ``bb9f9f0204c4462ca7d976b87d1336d4`` when using ``Engine Helicopter``, or to ``93a47d6d40454335b4784e803628ac54`` when using ``Engine Plane``.

**Sleds** *flag*: Tires should easily roll. For example, most planes will use this property.

**Speed_Min** *float*: The vehicle's maximum reversing speed, in m/s (meters per second). In-game, a vehicle's speed is displayed as either kph (kilometers per hour) or mph (miles per hour). For example, a vehicle that uses ``Speed_Min -7`` will have a maximum reversing speed of 25.2 kph (15.66 mph).

**Speed_Max** *float*: The vehicle's maximum forward speed, in m/s (meters per second). For all ``Engine`` enumerators except for the ``Train`` enumerator, this value is multiplied by 1.25 because the vehicle adjusts wheel torque trying to match a specific speed. For example, a vehicle that uses ``Speed_Max 12.5`` and is using ``Engine Car`` will have a maximum forward speed of 56.25 kph (34.95 mph).

**Steer_Min** *float*: The angle to turn when moving slowly.

**Steer_Max** *float*: The angle to turn when moving quickly. This value is multiplied by 0.75.

**Traction** *flag*: Tires should have traction in snowy positions.

**Wheel_Collider_Mass_Override** *float*: Override the mass of the vehicle's Wheel Collider components. This allows for quickly modifying the mass of the wheel colliders without needing to rebundle the asset in Unity. If a vehicle has realistic mass, then it may be helpful to set this value to something exceptionally high (e.g., 500). Defaults to ``null``.

Health
``````

**Bumper_Invulnerable** *flag*: The vehicle cannot be damaged by collisions (such as with other vehicles, objects, placeables, or entities).

**Bumper_Multiplier** *float*: Multiplier on the value for detecting collisions. When less than 1, the vehicle must be moving at a higher speed to enter a collision. When greater than 1, the vehicle can enter a collision while moving at a lower speed. Defaults to 1.

**Can_Repair_While_Seated** *bool*: If true, a player can repair the vehicle while also sitting in it. Defaults to false.

**Child_Explosion_Armor_Multiplier** *float*: Multiplier on the damage taken by barricades and other buildables placed on the vehicle, by explosions. Defaults to 0.2.

**Environment_Invulnerable** *flag*: This vehicle cannot be damaged by animals, zombie melee attacks, or boulders thrown by mega zombies. Zombies and animals will still pursue the vehicle, and attempt to attack any passengers directly. Other damage sources can still damage the vehicle.

**Explosions_Invulnerable** *flag*: The vehicle cannot be damaged by explosions.

**Health** *uint16*: Total health value. Defaults to 0.

**Health_Min** *uint16*: Maximum possible health to spawn with. Defaults to 0.

**Health_Max** *uint16*: Minimum possible health to spawn with. Defaults to 0.

**Invulnerable** *flag*: The vehicle cannot be damaged by lower-power :ref:`doc_item_asset_weapon` that do not have the ``Invulnerable`` flag.

**Passenger_Explosion_Armor** *float*: Multiplier on the damage taken by players sitting in the vehicle, by explosions. Defaults to 1.

**Tires_Invulnerable** *flag*: Tires cannot be damaged.

Fuel
````

**Fuel** *uint16*: Total fuel capacity. Defaults to 0.

**Fuel_Burn_Rate** *float*: The rate fuel burns at. Defaults to 2.05 when using ``Engine Car``, or to 4.2 otherwise.

**Fuel_Min** *uint16*: Minimum possible fuel to spawn with. Defaults to 0.

**Fuel_Max** *uint16*: Minimum possible fuel to spawn with. Defaults to 0.

Battery
```````

**Battery_Burn_Rate** *float*: The rate battery charge is consumed at. Defaults to 20.

**Battery_Charge_Rate** *float*: The rate battery charge is recharged at. Defaults to 20.

**Battery_Powered** *flag*: The vehicle does not use fuel. For example, this flag is useful for creating electric vehicles.

**Battery_Spawn_Charge_Multiplier** *float*: Multiplier on the battery charge a newly-spawned vehicle with a vehicle battery will have. Setting this to a number less than 1 will result in the vehicle spawning with less battery charge than normal. Defaults to 1.

**BatteryMode_Driving** *enum* (:ref:`doc_data_ebatterymode`): How the vehicle battery should behave when a player is driving it. Defaults to ``Charge``.

**BatteryMode_Empty** *enum* (:ref:`doc_data_ebatterymode`): How the vehicle battery should behave when the vehicle is empty. Defaults to ``None``.

**BatteryMode_Headlights** *enum* (:ref:`doc_data_ebatterymode`): How the vehicle battery should behave when the headlights are on. Defaults to ``Burn``.

**BatteryMode_Sirens** *enum* (:ref:`doc_data_ebatterymode`): How the vehicle battery should behave when the siren is on. Defaults to ``Burn``.

**Can_Steal_Battery** *bool*: Whether or not the vehicle battery can be removed from the vehicle by a player. Defaults to true.

**Cannot_Spawn_With_Battery** *flag*: The vehicle does not spawn with a vehicle battery.

**Default_Battery** *guid*: Battery item given to the player when a specific battery hasn't been manually installed yet. Defaults to the vanilla car battery (098b13be34a7411db7736b7f866ada69).

Stamina
```````

**Stamina_Boost** *float*: When a value is specified, this property allows for using stamina to boost. The value specified is the multiplier on the speed a vehicle can go without using a stamina boost. For example, ``Stamina_Boost 0.5`` would only let vehicle move at 50% its maximum speed normally, but using stamina to boost would it reach its maximum speed. This property is often used with ``Stamina_Powered``, but this is not required.

**Stamina_Powered** *flag*: The vehicle does not use fuel or a vehicle battery.

Explosion
`````````

**Explosion** :ref:`GUID <doc_data_guid>` or *uint16*: GUID or legacy ID of :ref:`EffectAsset <doc_assets_effect>` to play when destroyed.

**Explosion_Min_Force_X** *float*: Minimum amount of force applied on the 𝘟-axis when the vehicle explodes. Defaults to 0.

**Explosion_Max_Force_X** *float*: Maximum amount of force applied on the 𝘟-axis when the vehicle explodes. Defaults to 0.

**Explosion_Min_Force_Y** *float*: Minimum amount of force applied on the 𝘠-axis when the vehicle explodes. This property must be set in order to use other ``Explosion_Min_Force_#`` properties. Defaults to 1024.

**Explosion_Max_Force_Y** *float*: Maximum amount of force applied on the 𝘠-axis when the vehicle explodes. This property must be set in order to use other ``Explosion_Max_Force_#`` properties. Defaults to 1024.

**Explosion_Min_Force_Z** *float*: Minimum amount of force applied on the 𝘡-axis when the vehicle explodes. Defaults to 0.

**Explosion_Max_Force_Z** *float*: Maximum amount of force applied on the 𝘡-axis when the vehicle explodes. Defaults to 0.

**ShouldExplosionCauseDamage** *bool*: If true, the explosion caused by the vehicle being destroyed will deal damage. Defaults to true if ``Explosion`` is specified.

**ShouldExplosionBurnMaterials** *bool*: If true, the materials of the vehicle's ``Model_#`` GameObjects will be tinted black when the vehicle is destroyed. Defaults to true if ``Explosion`` is specified.

Turret
------

**Turrets** *uint8*: Number of turrets on the vehicle. All of the other turret properties require that this property is set. Defaults to 0.

**Turret_#_Seat_Index** *uint8*: Which ``Seat_#`` GameObject the turret is usable from. Defaults to 0 (corresponding to ``Seat_0``).

**Turret_#_Item_ID** *uint16*: ID of the item usable from the turret seat. This is often used with a :ref:`GunAsset <doc_item_asset_gun>` that has the ``Turret`` property, but any item can be used.

**Turret_#_Yaw_Min** *float*: Minimum allowed rotation of the turret through the azimuth, in degrees. If this is set to -360, it can rotate leftward forever.

**Turret_#_Yaw_Max** *float*: Maximum allowed rotation of the turret through the azimuth, in degrees. If this is set to 360, it can rotate rightward forever.

**Turret_#_Pitch_Min** *float*: Minimum allowed rotation of the turret through the elevation, in degrees.

**Turret_#_Pitch_Max** *float*: Maximum allowed rotation of the turret through the elevation, in degrees.

**Turret_#_Ignore_Aim_Camera** *flag*: Disable having the camera positioned at the ``Aim`` GameObject.

Train
`````

These properties should be used with ``Engine Train``.

**Train_Car_Length** *float*: The distance between each train car on the train, in meters.

**Train_Track_Offset** *float*: The offset the train car is above the track, in meters.

**Train_Wheel_Offset** *float*: The offset between the wheels, in meters.

Economy
```````

**Shared_Skin_Lookup_ID** *uint16*: Share skins with another vehicle. Defaults to the value of ``ID``.

**Shared_Skin_Name** *string*: When generating images, the image name will contain the value of this string instead of the vehicle's file name. Often used with ``Shared_Skin_Lookup_ID``.

**Size2_Z** *float*: Orthogonal camera size for economy icons.

Localization
------------

**Name** *string*: Vehicle name in user interfaces.

.. _doc_assets_vehicle:paintablesection_dictionary:

PaintableSection Dictionary
```````````````````````````

.. list-table::
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`Path <doc_assets_vehicle:paintablesection_path>`
     - :ref:`string <doc_data_builtin_types>`
     - N/A
   * - :ref:`MaterialIndex <doc_assets_vehicle:paintablesection_materialindex>`
     - :ref:`int32 <doc_data_builtin_types>`
     - ``0``

PaintableSection Dictionary Descriptions
````````````````````````````````````````

.. _doc_assets_vehicle:paintablesection_path:

Path :ref:`string <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::

Scene hierarchy path to a Renderer component relative to the vehicle's root transform.

----

.. _doc_assets_vehicle:paintablesection_materialindex:

MaterialIndex :ref:`int32 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Index into Renderer component's Materials list. For example, 0 is the 1st material, 1 is the 2nd material, etc.
