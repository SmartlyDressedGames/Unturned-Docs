.. _doc_assets_vehicle:

Vehicle Assets
==============

The **VehicleAsset** class is used by vehicles. These can be driven by players, have support for gun turrets, can function as a storage container for items, and more.

Game Data File
--------------

The ``GUID`` and ``Type`` properties are required by all vehicle assets. Many vehicle assets will want to include ``Engine`` and ``Rarity`` as well. The ``ID`` property used to be required, but this is no longer necessary.

Any properties from parent classes that are required—or recommended—are listed in the table below.

.. list-table::
   :widths: 30 40 30
   :header-rows: 1

   * - Class
     - Property Name
     - Required Value
   * - :ref:`Asset <doc_assets_vehicle>`
     - :ref:`GUID <doc_assets_vehicle:guid>`
     -
   * - :ref:`Asset <doc_assets_vehicle>`
     - :ref:`ID <doc_assets_vehicle:id>`
     -
   * - :ref:`Asset <doc_assets_vehicle>`
     - :ref:`Type <doc_assets_vehicle:type>`
     - ``Vehicle``
   * - :ref:`VehicleAsset <doc_assets_vehicle>`
     - :ref:`Engine <doc_assets_vehicle:engine>`
     -

Properties
``````````

.. list-table:: Uncategorized
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`AdditionalTransparentSections <doc_assets_vehicle:additionaltransparentsections>`
     - :ref:`list of strings <doc_data_builtin_types>`
     -
   * - :ref:`Bicycle <doc_assets_vehicle:bicycle>`
     - :ref:`flag <doc_data_flag>`
     -
   * - :ref:`Bicycle_Anim_Speed <doc_assets_vehicle:bicycle_anim_speed>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Buildable_Placement_Rule <doc_assets_vehicle:buildable_placement_rule>`
     - :ref:`EVehicleBuildablePlacementRule <doc_assets_vehicle:evehiclebuildableplacementrule>`
     - ``None``
   * - :ref:`Bypass_Hash_Verification <doc_assets_vehicle:bypass_hash_verification>`
     - :ref:`flag <doc_data_flag>`
     -
   * - :ref:`Cam_Driver_Offset <doc_assets_vehicle:cam_driver_offset>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Cam_Follow_Distance <doc_assets_vehicle:cam_follow_distance>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``5.5``
   * - :ref:`Cam_Passenger_Offset <doc_assets_vehicle:cam_passenger_offset>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Can_Be_Locked <doc_assets_vehicle:can_be_locked>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - :ref:`Crawler <doc_assets_vehicle:crawler>`
     - :ref:`flag <doc_data_flag>`
     - *deprecated*
   * - :ref:`Drops_Max <doc_assets_vehicle:drops_max>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``7``
   * - :ref:`Drops_Min <doc_assets_vehicle:drops_min>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``3``
   * - :ref:`Drops_Table_ID <doc_assets_vehicle:drops_table_id>`
     - :ref:`uint16 <doc_data_builtin_types>`
     - ``962``
   * - :ref:`Engine <doc_assets_vehicle:engine>`
     - :ref:`EEngine <doc_assets_vehicle:eengine>`
     - ``Car``
   * - :ref:`Exit <doc_assets_vehicle:exit>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``2``
   * - :ref:`GUID <doc_assets_vehicle:guid>`
     - :ref:`doc_data_guid`
     -
   * - :ref:`Has_Clip_Prefab <doc_assets_vehicle:has_clip_prefab>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - :ref:`Has_Horn <doc_assets_vehicle:has_horn>`
     - :ref:`bool <doc_data_builtin_types>`
     - See description
   * - :ref:`HornAudioClip <doc_assets_vehicle:hornaudioclip>`
     - :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`
     -
   * - :ref:`ID <doc_assets_vehicle:id>`
     - :ref:`uint16 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`IgnitionAudioClip <doc_assets_vehicle:ignitionaudioclip>`
     - :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`
     -
   * - :ref:`LockMouse <doc_assets_vehicle:lockmouse>`
     - :ref:`flag <doc_data_flag>`
     -
   * - :ref:`Num_Steering_Tires <doc_assets_vehicle:num_steering_tires>`
     - :ref:`int32 <doc_data_builtin_types>`
     - *deprecated*
   * - :ref:`Rarity <doc_assets_vehicle:rarity>`
     - :ref:`doc_data_eitemrarity`
     - ``Common``
   * - :ref:`Reclined <doc_assets_vehicle:reclined>`
     - :ref:`flag <doc_data_flag>`
     -
   * - :ref:`Should_Spawn_Seat_Capsules <doc_assets_vehicle:should_spawn_seat_capsules>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``false``
   * - :ref:`Steering_Tire_# <doc_assets_vehicle:steering_tire_#>`
     - :ref:`int32 <doc_data_builtin_types>`
     - *deprecated*
   * - :ref:`Tire_ID <doc_assets_vehicle:tire_id>`
     - :ref:`uint16 <doc_data_builtin_types>`
     - ``1451``
   * - :ref:`Trunk_Storage_X <doc_assets_vehicle:trunk_storage_x>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Trunk_Storage_Y <doc_assets_vehicle:trunk_storage_y>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Valid_Speed_Down <doc_assets_vehicle:valid_speed_down>`
     - :ref:`float32 <doc_data_builtin_types>`
     -
   * - :ref:`Valid_Speed_Horizontal <doc_assets_vehicle:valid_speed_horizontal>`
     - :ref:`float32 <doc_data_builtin_types>`
     -
   * - :ref:`Valid_Speed_Up <doc_assets_vehicle:valid_speed_up>`
     - :ref:`float32 <doc_data_builtin_types>`
     -
   * - :ref:`Zip <doc_assets_vehicle:zip>`
     - :ref:`flag <doc_data_flag>`
     -

.. list-table:: Handling
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`Air_Steer_Max <doc_assets_vehicle:air_steer_max>`
     - :ref:`float32 <doc_data_builtin_types>`
     - See description
   * - :ref:`Air_Steer_Min <doc_assets_vehicle:air_steer_min>`
     - :ref:`float32 <doc_data_builtin_types>`
     - See description
   * - :ref:`Air_Turn_Responsiveness <doc_assets_vehicle:air_turn_responsiveness>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``2``
   * - :ref:`Brake <doc_assets_vehicle:brake>`
     - :ref:`float32 <doc_data_builtin_types>`
     -
   * - :ref:`Center_Of_Mass <doc_assets_vehicle:center_of_mass>`
     - :ref:`vector3 <doc_data_vector3>`
     -
   * - :ref:`Carjack_Force_Multiplier <doc_assets_vehicle:carjack_force_multiplier>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1.0``
   * - :ref:`Engine_Force_Multiplier <doc_assets_vehicle:engine_force_multiplier>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1.0``
   * - :ref:`Lift <doc_assets_vehicle:lift>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Override_Center_Of_Mass <doc_assets_vehicle:override_center_of_mass>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``false``
   * - :ref:`Physics_Profile <doc_assets_vehicle:physics_profile>`
     - :ref:`GUID <doc_data_guid>`
     - See description
   * - :ref:`RollAngularVelocityDamping <doc_assets_vehicle:rollangularvelocitydamping>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``-1.0``
   * - :ref:`Sleds <doc_assets_vehicle:sleds>`
     - :ref:`flag <doc_data_flag>`
     -
   * - :ref:`Speed_Max <doc_assets_vehicle:speed_max>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Speed_Min <doc_assets_vehicle:speed_min>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Steer_Max <doc_assets_vehicle:steer_max>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Steer_Min <doc_assets_vehicle:steer_min>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Steering_Angle_Turn_Speed <doc_assets_vehicle:steering_angle_turn_speed>`
     - :ref:`float32 <doc_data_builtin_types>`
     - See description
   * - :ref:`Steering_LeaningForceMultiplier <doc_assets_vehicle:steering_leaningforcemultiplier>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``-1.0``
   * - :ref:`Traction <doc_assets_vehicle:traction>`
     - :ref:`flag <doc_data_flag>`
     -
   * - :ref:`Wheel_Collider_Mass_Override <doc_assets_vehicle:wheel_collider_mass_override>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``null``
   * - :ref:`WheelBalancing_ForceMultiplier <doc_assets_vehicle:wheelbalancing_forcemultiplier>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``-1.0``
   * - :ref:`WheelBalancing_UprightExponent <doc_assets_vehicle:wheelbalancing_uprightexponent>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1.5``
   * - :ref:`WheelConfigurations <doc_assets_vehicle:wheelconfigurations>`
     - :ref:`list of VehicleWheelConfiguration <doc_assets_vehicle:vehiclewheelconfiguration_dictionary>`
     -

.. list-table:: Engine RPM and Gears
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`EngineIdleRPM <doc_assets_vehicle:engineidlerpm>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1000.0``
   * - :ref:`EngineMaxRPM <doc_assets_vehicle:enginemaxrpm>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``7000.0``
   * - :ref:`EngineMaxTorque <doc_assets_vehicle:enginemaxtorque>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1.0``
   * - :ref:`EngineRPM_DecreaseRate <doc_assets_vehicle:enginerpm_decreaserate>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``10000.0``
   * - :ref:`EngineRPM_IncreaseRate <doc_assets_vehicle:enginerpm_increaserate>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``10000.0``
   * - :ref:`ForwardGearRatios <doc_assets_vehicle:forwardgearratios>`
     - :ref:`list of float32 <doc_data_builtin_types>`
     -
   * - :ref:`GearShift_DownThresholdRPM <doc_assets_vehicle:gearshift_downthresholdrpm>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1500.0``
   * - :ref:`GearShift_Duration <doc_assets_vehicle:gearshift_duration>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0.5``
   * - :ref:`GearShift_Interval <doc_assets_vehicle:gearshift_interval>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1.0``
   * - :ref:`GearShift_UpThresholdRPM <doc_assets_vehicle:gearshift_upthresholdrpm>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``5500.0``
   * - :ref:`GearShift_VisibleInHUD <doc_assets_vehicle:gearshift_visibleinhud>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - :ref:`ReverseGearRatio <doc_assets_vehicle:reversegearratio>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1.0``

.. list-table:: Engine Sound
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`EngineSound <doc_assets_vehicle:enginesound>`
     - :ref:`RpmEngineSoundConfiguration <doc_assets_vehicle:rpmenginesoundconfiguration_dictionary>`
     -
   * - :ref:`EngineSound_Type <doc_assets_vehicle:enginesound_type>`
     - :ref:`EVehicleEngineSoundType <doc_assets_vehicle:evehicleenginesoundtype>`
     - ``Legacy``
   * - :ref:`Pitch_Drive <doc_assets_vehicle:pitch_drive>`
     - :ref:`float32 <doc_data_builtin_types>`
     -
   * - :ref:`Pitch_Idle <doc_assets_vehicle:pitch_idle>`
     - :ref:`float32 <doc_data_builtin_types>`
     -

.. list-table:: Health and Armor
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`Bumper_Multiplier <doc_assets_vehicle:bumper_multiplier>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1.0``
   * - :ref:`Bumper_Invulnerable <doc_assets_vehicle:bumper_invulnerable>`
     - :ref:`flag <doc_data_flag>`
     -
   * - :ref:`Can_Repair_While_Seated <doc_assets_vehicle:can_repair_while_seated>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``false``
   * - :ref:`Child_Explosion_Armor_Multiplier <doc_assets_vehicle:child_explosion_armor_multiplier>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0.2``
   * - :ref:`Environment_Invulnerable <doc_assets_vehicle:environment_invulnerable>`
     - :ref:`flag <doc_data_flag>`
     -
   * - :ref:`Explosions_Invulnerable <doc_assets_vehicle:explosions_invulnerable>`
     - :ref:`flag <doc_data_flag>`
     -
   * - :ref:`Health <doc_assets_vehicle:health>`
     - :ref:`uint16 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Health_Max <doc_assets_vehicle:health_max>`
     - :ref:`uint16 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Health_Min <doc_assets_vehicle:health_min>`
     - :ref:`uint16 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Invulnerable <doc_assets_vehicle:invulnerable>`
     - :ref:`flag <doc_data_flag>`
     -
   * - :ref:`Passenger_Explosion_Armor <doc_assets_vehicle:passenger_explosion_armor>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Tires_Invulnerable <doc_assets_vehicle:tires_invulnerable>`
     - :ref:`flag <doc_data_flag>`
     -

.. list-table:: Fuel
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`Fuel <doc_assets_vehicle:fuel>`
     - :ref:`uint16 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Fuel_Burn_Rate <doc_assets_vehicle:fuel_burn_rate>`
     - :ref:`float32 <doc_data_builtin_types>`
     - See description
   * - :ref:`Fuel_Min <doc_assets_vehicle:fuel_min>`
     - :ref:`uint16 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Fuel_Max <doc_assets_vehicle:fuel_max>`
     - :ref:`uint16 <doc_data_builtin_types>`
     - ``0``

.. list-table:: Battery
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`Battery_Burn_Rate <doc_assets_vehicle:battery_burn_rate>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``20``
   * - :ref:`Battery_Charge_Rate <doc_assets_vehicle:battery_charge_rate>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``20``
   * - :ref:`Battery_Powered <doc_assets_vehicle:battery_powered>`
     - :ref:`flag <doc_data_flag>`
     -
   * - :ref:`Battery_Spawn_Charge_Multiplier <doc_assets_vehicle:battery_spawn_charge_multiplier>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`BatteryMode_Driving <doc_assets_vehicle:batterymode_driving>`
     - :ref:`doc_data_ebatterymode`
     - ``Charge``
   * - :ref:`BatteryMode_Empty <doc_assets_vehicle:batterymode_empty>`
     - :ref:`doc_data_ebatterymode`
     - ``None``
   * - :ref:`BatteryMode_Headlights <doc_assets_vehicle:batterymode_headlights>`
     - :ref:`doc_data_ebatterymode`
     - ``Burn``
   * - :ref:`BatteryMode_Sirens <doc_assets_vehicle:batterymode_sirens>`
     - :ref:`doc_data_ebatterymode`
     - ``Burn``
   * - :ref:`Can_Steal_Battery <doc_assets_vehicle:can_steal_battery>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - :ref:`Cannot_Spawn_With_Battery <doc_assets_vehicle:cannot_spawn_with_battery>`
     - :ref:`flag <doc_data_flag>`
     -
   * - :ref:`Default_Battery <doc_assets_vehicle:default_battery>`
     - :ref:`doc_data_guid`
     - ``098b13be34a7411db7736b7f866ada69``

.. list-table:: Stamina
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`Stamina_Boost <doc_assets_vehicle:stamina_boost>`
     - :ref:`float32 <doc_data_builtin_types>`
     -
   * - :ref:`Stamina_Powered <doc_assets_vehicle:stamina_powered>`
     - :ref:`flag <doc_data_flag>`
     -

.. list-table:: Paintability
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`DefaultPaintColor_Configuration <doc_assets_vehicle:defaultpaintcolor_configuration>`
     - :ref:`VehicleRandomPaintColorConfiguration <doc_assets_vehicle:vehiclerandompaintcolorconfiguration_dictionary>`
     -
   * - :ref:`DefaultPaintColor_Mode <doc_assets_vehicle:defaultpaintcolor_mode>`
     - :ref:`EVehicleDefaultPaintColorMode <doc_assets_vehicle:evehicledefaultpaintcolormode>`
     - See description
   * - :ref:`DefaultPaintColors <doc_assets_vehicle:defaultpaintcolors>`
     - :ref:`list of colors <doc_data_color>`
     -
   * - :ref:`IsPaintable <doc_assets_vehicle:ispaintable>`
     - :ref:`bool <doc_data_builtin_types>`
     -
   * - :ref:`PaintableSections <doc_assets_vehicle:paintablesections>`
     - :ref:`list of PaintableVehicleSection <doc_assets_vehicle:paintablevehiclesection_dictionary>`
     -

.. list-table:: Explosion
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`Explosion <doc_assets_vehicle:explosion>`
     - :ref:`GUID <doc_data_guid>` or :ref:`uint16 <doc_data_builtin_types>`
     -
   * - :ref:`Explosion_Force_Multiplier <doc_assets_vehicle:explosion_force_multiplier>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1.0``
   * - :ref:`Explosion_Max_Force <doc_assets_vehicle:explosion_max_force>`
     - :ref:`vector3 <doc_data_vector3>`
     - ``(0, 1024, 0)``
   * - :ref:`Explosion_Min_Force <doc_assets_vehicle:explosion_min_force>`
     - :ref:`vector3 <doc_data_vector3>`
     - ``(0, 1024, 0)``
   * - :ref:`ShouldExplosionBurnMaterials <doc_assets_vehicle:shouldexplosionburnmaterials>`
     - :ref:`bool <doc_data_builtin_types>`
     - See description
   * - :ref:`ShouldExplosionCauseDamage <doc_assets_vehicle:shouldexplosioncausedamage>`
     - :ref:`bool <doc_data_builtin_types>`
     - See description

.. list-table:: Turret
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`Turret_#_Ignore_Aim_Camera <doc_assets_vehicle:turret_ignore_aim_camera>`
     - :ref:`flag <doc_data_flag>`
     -
   * - :ref:`Turret_#_Item_ID <doc_assets_vehicle:turret_item_id>`
     - :ref:`uint16 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Turret_#_Pitch_Max <doc_assets_vehicle:turret_pitch_max>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Turret_#_Pitch_Min <doc_assets_vehicle:turret_pitch_min>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Turret_#_Seat_Index <doc_assets_vehicle:turret_seat_index>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Turret_#_Yaw_Max <doc_assets_vehicle:turret_yaw_max>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Turret_#_Yaw_Min <doc_assets_vehicle:turret_yaw_min>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Turrets <doc_assets_vehicle:turrets>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``0``

.. list-table:: Train
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`Train_Car_Length <doc_assets_vehicle:train_car_length>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Train_Track_Offset <doc_assets_vehicle:train_track_offset>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Train_Wheel_Offset <doc_assets_vehicle:train_wheel_offset>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``

.. list-table:: Economy
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`Shared_Skin_Lookup_ID <doc_assets_vehicle:shared_skin_lookup_id>`
     - :ref:`doc_data_guid` or :ref:`uint16 <doc_data_builtin_types>`
     - See description
   * - :ref:`Shared_Skin_Name <doc_assets_vehicle:shared_skin_name>`
     - :ref:`string <doc_data_builtin_types>`
     -
   * - :ref:`Size2_Z <doc_assets_vehicle:size2_z>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``

.. _doc_assets_vehicle:eengine:

EEngine Enumeration
```````````````````

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Named Value
     - Description
   * - ``Car``
     - This vehicle is part of the Car category.
   * - ``Plane``
     - This vehicle is part of the Plane category.
   * - ``Blimp``
     - This vehicle is part of the Blimp category.
   * - ``Boat``
     - This vehicle is part of the Boat category.
   * - ``Train``
     - This vehicle is part of the Train category.

.. _doc_assets_vehicle:evehiclebuildableplacementrule:

EVehicleBuildablePlacementRule Enumeration
``````````````````````````````````````````

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Named Value
     - Description
   * - ``None``
     - Vehicle does not override placement. This means that barricades can be attached *unless* the barricade sets :ref:`Allow_Placement_On_Vehicle <doc_item_asset_barricade>` to ``false`` (e.g., beds and sentry guns are often set to ``false``).
   * - ``AlwaysAllow``
     - Vehicle allows any barricade to be placed on it, regardless of the barricade's :ref:`Allow_Placement_On_Vehicle <doc_item_asset_barricade>` setting. Trains used to use this option, but it can be exploited to move beds into out-of-bounds areas (e.g., into other objects).
   * - ``Block``
     - Vehicle prevents any barricade form being placed on it.

.. _doc_assets_vehicle:evehicledefaultpaintcolormode:

EVehicleDefaultPaintColorMode
`````````````````````````````

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Named Value
     - Description
   * - ``None``
     - Not configured.
   * - ``List``
     - Pick from the :ref:`DefaultPaintColors <doc_assets_vehicle:defaultpaintcolors>` list.
   * - ``RandomHueOrGrayscale``
     - Pick a random HSV using :ref:`DefaultPaintColor_Configuration <doc_assets_vehicle:defaultpaintcolor_configuration>`.

.. _doc_assets_vehicle:evehicleenginesoundtype:

EVehicleEngineSoundType Enumeration
```````````````````````````````````

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Named Value
     - Description
   * - ``Legacy``
     - Default.
   * - ``EngineRPMSimple``
     - Set pitch and volume of a single clip according to engine RPM.

.. _doc_assets_vehicle:paintablevehiclesection_dictionary:

PaintableVehicleSection Dictionary
``````````````````````````````````

.. list-table::
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`Path <doc_assets_vehicle:paintablevehiclesection_path>`
     - :ref:`string <doc_data_builtin_types>`
     -
   * - :ref:`MaterialIndex <doc_assets_vehicle:paintablevehiclesection_materialindex>`
     - :ref:`int32 <doc_data_builtin_types>`
     - ``0``

.. _doc_assets_vehicle:rpmenginesoundconfiguration_dictionary:

RpmEngineSoundConfiguration Dictionary
``````````````````````````````````````

.. list-table::
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`IdlePitch <doc_assets_vehicle:rpmenginesoundconfiguration_idlepitch>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0.0``
   * - :ref:`IdleVolume <doc_assets_vehicle:rpmenginesoundconfiguration_idlevolume>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0.0``
   * - :ref:`MaxPitch <doc_assets_vehicle:rpmenginesoundconfiguration_maxpitch>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0.0``
   * - :ref:`MaxVolume <doc_assets_vehicle:rpmenginesoundconfiguration_maxvolume>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0.0``

.. _doc_assets_vehicle:vehiclerandompaintcolorconfiguration_dictionary:

VehicleRandomPaintColorConfiguration Dictionary
```````````````````````````````````````````````

.. list-table::
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`MinSaturation <doc_assets_vehicle:vehiclerandompaintcolorconfiguration_minsaturation>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0.0``
   * - :ref:`MaxSaturation <doc_assets_vehicle:vehiclerandompaintcolorconfiguration_maxsaturation>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0.0``
   * - :ref:`MinValue <doc_assets_vehicle:vehiclerandompaintcolorconfiguration_minvalue>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0.0``
   * - :ref:`MaxValue <doc_assets_vehicle:vehiclerandompaintcolorconfiguration_maxvalue>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0.0``
   * - :ref:`GrayscaleChance <doc_assets_vehicle:vehiclerandompaintcolorconfiguration_grayscalechance>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0.0``

.. _doc_assets_vehicle:vehiclewheelconfiguration_dictionary:

VehicleWheelConfiguration Dictionary
````````````````````````````````````

.. list-table::
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`CopyColliderRpmIndex <doc_assets_vehicle:wheelconfiguration_copycolliderrpmindex>`
     - :ref:`int32 <doc_data_builtin_types>`
     - ``-1``
   * - :ref:`IsColliderPowered <doc_assets_vehicle:vehiclewheelconfiguration_iscolliderpowered>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``false``
   * - :ref:`IsColliderSteered <doc_assets_vehicle:vehiclewheelconfiguration_iscollidersteered>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``false``
   * - :ref:`IsModelSteered <doc_assets_vehicle:vehiclewheelconfiguration_ismodelsteered>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``false``
   * - :ref:`ModelPath <doc_assets_vehicle:vehiclewheelconfiguration_modelpath>`
     - :ref:`string <doc_data_builtin_types>`
     -
   * - :ref:`ModelRadius <doc_assets_vehicle:wheelconfiguration_modelradius>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``-1.0``
   * - :ref:`ModelUseColliderPose <doc_assets_vehicle:vehiclewheelconfiguration_modelusecolliderpose>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``false``
   * - :ref:`WheelColliderPath <doc_assets_vehicle:vehiclewheelconfiguration_wheelcolliderpath>`
     - :ref:`string <doc_data_builtin_types>`
     -

Property Descriptions
`````````````````````

.. _doc_assets_vehicle:additionaltransparentsections:

AdditionalTransparentSections :ref:`list of strings <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Scene hierarchy paths relative to the vehicle's root transform to register as needing transparent sorting. Their render queue is periodically updated according to whether their pivot point is underwater.

----

.. _doc_assets_vehicle:air_steer_max:

Air_Steer_Max :ref:`float32 <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::

The angle to turn when moving quickly, when using ``Engine Plane``. Defaults to the value of ``Steer_Max``.

----

.. _doc_assets_vehicle:air_steer_min:

Air_Steer_Min :ref:`float32 <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::

The angle to turn when moving slowly, when using ``Engine Plane``. Defaults to the value of ``Steer_Min``.

----

.. _doc_assets_vehicle:air_turn_responsiveness:

Air_Turn_Responsiveness :ref:`float32 <doc_data_builtin_types>` ``2``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Sensitivity on steering while airborne, when using ``Engine Plane``.

----

.. _doc_assets_vehicle:battery_burn_rate:

Battery_Burn_Rate :ref:`float32 <doc_data_builtin_types>` ``20``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

This controls the rate at which battery charge decreases per second.

----

.. _doc_assets_vehicle:battery_charge_rate:

Battery_Charge_Rate :ref:`float32 <doc_data_builtin_types>` ``20``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

This controls the rate at which battery charge increases per second.

----

.. _doc_assets_vehicle:battery_powered:

Battery_Powered :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::::::::::::

The vehicle does not use fuel. For example, this flag is useful for creating electric vehicles.

----

.. _doc_assets_vehicle:battery_spawn_charge_multiplier:

Battery_Spawn_Charge_Multiplier :ref:`float32 <doc_data_builtin_types>` ``1``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Battery charge on a newly-spawned vehicle is multiplied by this [0, 1] number. Setting this to a number less than ``1`` will result in the vehicle spawning with less battery charge than normal.

----

.. _doc_assets_vehicle:batterymode_driving:

BatteryMode_Driving :ref:`doc_data_ebatterymode` ``Charge``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

How the vehicle battery should behave when a player is driving it.

----

.. _doc_assets_vehicle:batterymode_empty:

BatteryMode_Empty :ref:`doc_data_ebatterymode` ``None``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

How the vehicle battery should behave when the vehicle is empty.

----

.. _doc_assets_vehicle:batterymode_headlights:

BatteryMode_Headlights :ref:`doc_data_ebatterymode` ``Burn``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

How the vehicle battery should behave when the headlights are on.

----

.. _doc_assets_vehicle:batterymode_sirens:

BatteryMode_Sirens :ref:`doc_data_ebatterymode` ``Burn``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

How the vehicle battery should behave when the siren is on.

----

.. _doc_assets_vehicle:bicycle:

Bicycle :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::::

Player character should use a bicycling animation.

----

.. _doc_assets_vehicle:bicycle_anim_speed:

Bicycle_Anim_Speed :ref:`float32 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on the speed of the bicycling animation.

----

.. _doc_assets_vehicle:brake:

Brake :ref:`float32 <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::

The amount of braking force to apply.

----

.. _doc_assets_vehicle:buildable_placement_rule:

Buildable_Placement_Rule :ref:`EVehicleBuildablePlacementRule <doc_assets_vehicle:evehiclebuildableplacementrule>` ``None``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

This property overrides how barricades can be attached to the vehicle. View the :ref:`EVehicleBuildablePlacementRule <doc_assets_vehicle:evehiclebuildableplacementrule>` documentation for more information about the behavior of each option. Note that the ``Bypass_Buildable_Mobility`` gameplay config option, when ``true``, will always take priority over this property.

The ``Supports_Mobile_Buildables`` flag predates this property, and has since been deprecated. Its behavior can be replicated by using this property with the ``AlwaysAllow`` value instead.

----

.. _doc_assets_vehicle:bumper_invulnerable:

Bumper_Invulnerable :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::::::::::::::::

The vehicle cannot be damaged by collisions (such as with other vehicles, objects, placeables, or entities).

----

.. _doc_assets_vehicle:bumper_multiplier:

Bumper_Multiplier :ref:`float32 <doc_data_builtin_types>` ``1.0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on the value for detecting collisions. When less than 1, the vehicle must be moving at a higher speed to enter a collision. When greater than 1, the vehicle can enter a collision while moving at a lower speed.

----

.. _doc_assets_vehicle:bypass_hash_verification:

Bypass_Hash_Verification :ref:`flag <doc_data_flag>`
::::::::::::::::::::::::::::::::::::::::::::::::::::

Disable hash verification check, and allow for mismatched files.

----

.. _doc_assets_vehicle:cam_driver_offset:

Cam_Driver_Offset :ref:`float32 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

The vertical offset for the driver's first-person camera, in meters. This is additive with the value of ``Cam_Passenger_Offset``.

----

.. _doc_assets_vehicle:cam_follow_distance:

Cam_Follow_Distance :ref:`float32 <doc_data_builtin_types>` ``5.5``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

The distance behind the player the third-person camera should be placed at, in meters.

----

.. _doc_assets_vehicle:cam_passenger_offset:

Cam_Passenger_Offset :ref:`float32 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

The vertical offset for any passenger's (including the driver's) first-person camera, in meters.

----

.. _doc_assets_vehicle:can_be_locked:

Can_Be_Locked :ref:`bool <doc_data_builtin_types>` ``true``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Whether or not the vehicle can be locked by a player.

----

.. _doc_assets_vehicle:can_repair_while_seated:

Can_Repair_While_Seated :ref:`bool <doc_data_builtin_types>` ``false``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

When ``true``, this vehicle can be repaired by seated players.

----

.. _doc_assets_vehicle:can_steal_battery:

Can_Steal_Battery :ref:`bool <doc_data_builtin_types>` ``true``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Whether or not the vehicle battery can be removed from the vehicle by a player.

----

.. _doc_assets_vehicle:cannot_spawn_with_battery:

Cannot_Spawn_With_Battery :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::

The vehicle does not spawn with a vehicle battery.

----

.. _doc_assets_vehicle:carjack_force_multiplier:

Carjack_Force_Multiplier :ref:`float32 <doc_data_builtin_types>` ``1.0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

This is a multiplier on the force applied when using a `Carjack <https://unturned.wiki/Carjack>`_ on this vehicle. It is recommended that this property scales based on your vehicle's mass.

Although this property was originally intended for modded vehicles, many official vehicles use this property as well. If you are creating a custom vehicle and using one of the example assets provided as a template (or have a mass that is similar to official content), you will likely want to use a value of ``2`` for this property.

The mass of official vehicles may be revisited in the future, to make collisions feel more reasonable. If this happens, the recommended value could be increased again.

----

.. _doc_assets_vehicle:center_of_mass:

Center_Of_Mass :ref:`vector3 <doc_data_vector3>`
::::::::::::::::::::::::::::::::::::::::::::::::

Overrides the vehicle's center of mass on the 𝘟\-, 𝘠\-, and 𝘡-axis, when using ``Override_Center_Of_Mass true``. This allows for modifying a vehicle's center of gravity without needing to move the "Cog" GameObject in Unity.

For example:

.. code-block:: unturneddat
  :linenos:

  Override_Center_Of_Mass true
  Center_Of_Mass (0, -50, 0)

----

.. _doc_assets_vehicle:child_explosion_armor_multiplier:

Child_Explosion_Armor_Multiplier :ref:`float32 <doc_data_builtin_types>` ``0.2``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

This is a multiplier on the damage that barricades (and other buildables) placed on the vehicle receive, when damaged by explosions.

----

.. _doc_assets_vehicle:crawler:

Crawler :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::::

.. deprecated:: 3.23.4.0
	Replaced by the ``WheelConfigurations`` property.

Disables the ``Wheel_#`` GameObjects from turning when steering by setting the default value of ``Num_Steering_Tires`` to ``0``. This property has no effect if ``Num_Steering_Tires`` has been manually set.

----

.. _doc_assets_vehicle:default_battery:

Default_Battery :ref:`doc_data_guid` ``098b13be34a7411db7736b7f866ada69``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Battery item given to the player when a specific battery hasn't been manually installed yet. Defaults to the `Vehicle Battery <unturned.wiki/Vehicle_Battery>`_ used by official vehicles.

----

.. _doc_assets_vehicle:defaultpaintcolor_configuration:

DefaultPaintColor_Configuration :ref:`VehicleRandomPaintColorConfiguration <doc_assets_vehicle:vehiclerandompaintcolorconfiguration_dictionary>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Determines the potential colors of a newly-spawned vehicle. Can be overridden by a :ref:`Vehicle Redirector <doc_asset_vehicle_redirector>`'s :ref:`LoadPaintColor <doc_asset_vehicle_redirector:loadpaintcolor>` and :ref:`LoadPaintColor <doc_asset_vehicle_redirector:spawnpaintcolor>` properties.

This property is used with ``DefaultPaintColor_Mode RandomHueOrGrayscale``. For example:

.. code-block:: unturneddat
	:linenos:

	DefaultPaintColor_Mode RandomHueOrGrayscale
	DefaultPaintColor_Configuration
	{
		MinSaturation 0.15
		MaxSaturation 0.7
		MinValue 0.15
		MaxValue 0.9
		GrayscaleChance 0.1
	}

----

.. _doc_assets_vehicle:defaultpaintcolor_mode:

DefaultPaintColor_Mode :ref:`EVehicleDefaultPaintColorMode <doc_assets_vehicle:evehicledefaultpaintcolormode>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

This property controls the mode that should be used when randomly picking a paint color for a newly-spawned vehicle. Defaults to ``List`` if :ref:`DefaultPaintColors <doc_assets_vehicle:defaultpaintcolors>` has been configured. Otherwise, defaults to ``None``. This can be manually set to ``RandomHueOrGrayscale`` to pick a random HSV.

----

.. _doc_assets_vehicle:defaultpaintcolors:

DefaultPaintColors :ref:`list of colors <doc_data_color>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

List of random colors to pick from when spawning a new vehicle. Can be overridden by a :ref:`Vehicle Redirector <doc_asset_vehicle_redirector>`'s :ref:`LoadPaintColor <doc_asset_vehicle_redirector:loadpaintcolor>` and :ref:`LoadPaintColor <doc_asset_vehicle_redirector:spawnpaintcolor>` properties.

This property is used with ``DefaultPaintColor_Mode List``. For example:

.. code-block:: unturneddat
	:linenos:

	DefaultPaintColor_Mode List
	DefaultPaintColors
	[
		"#353535" // Classic Black
		"#37658c" // Classic Blue
		"#2e642e" // Classic Green
		"#bd6e27" // Classic Orange
		"#6a466d" // Classic Purple
		"#9a2525" // Classic Red
		"#d4d4d4" // Classic White
		"#cdaa1e" // Classic Yellow
	]

----

.. _doc_assets_vehicle:drops_max:

Drops_Max :ref:`uint8 <doc_data_builtin_types>` ``7``
:::::::::::::::::::::::::::::::::::::::::::::::::::::

Maximum amount of item drops to spawn when the vehicle is destroyed.

----

.. _doc_assets_vehicle:drops_min:

Drops_Min :ref:`uint8 <doc_data_builtin_types>` ``3``
:::::::::::::::::::::::::::::::::::::::::::::::::::::

Minimum amount of item drops to spawn when the vehicle is destroyed.

----

.. _doc_assets_vehicle:drops_table_id:

Drops_Table_ID :ref:`uint16 <doc_data_builtin_types>` ``962``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

ID of the item spawn table to use when the vehicle is destroyed. The default spawn table is Destroyed_Vehicle_Default.

----

.. _doc_assets_vehicle:engine:

Engine :ref:`EEngine <doc_assets_vehicle:eengine>` ``Car``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

The ``Engine`` property determines the type of vehicle (e.g., car, plane, boat). Some vehicle properties are only usable depending on the vehicle's ``Engine``.

----

.. _doc_assets_vehicle:engine_force_multiplier:

Engine_Force_Multiplier :ref:`float32 <doc_data_builtin_types>` ``1.0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

This is a multiplier on otherwise not-yet-configurable plane/heli/boat/etc. forces. It is recommended that this property scales based on your vehicle's mass.

----

.. _doc_assets_vehicle:enginemaxtorque:

EngineMaxTorque :ref:`float32 <doc_data_builtin_types>` ``1.0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier for the amount of torque provided to the wheels. Understanding how engine RPM is translated to wheel torque is crucial for tuning the physics:

#. Engine RPM is normalized into a 0 to 1 range according to :ref:`EngineIdleRPM <doc_assets_vehicle:engineidlerpm>` and :ref:`EngineMaxRPM <doc_assets_vehicle:enginemaxrpm>`. For example, an Engine RPM of 2000 with Idle RPM of 1000 and Max RPM of 5000 would be 0.25.
#. Vehicle root needs an ``EngineCurvesComponent`` attached. This allows you to map normalized engine RPM to a normalized torque multiplier. Typically, the multiplier should be closest to 1 in the middle range (e.g., 0.3 to 0.8) and drop off toward 0 and 1.
#. Torque curve is sampled using the normalized engine RPM.
#. Sampled torque is multiplied by ``EngineMaxTorque``.
#. If changing gears, torque is zero.
#. If reversing, torque is multiplied by :ref:`ReverseGearRatio <doc_assets_vehicle:reversegearratio>`.
#. Otherwise, torque is multiplied by the active :ref:`ForwardGearRatio <doc_assets_vehicle:forwardgearratios>`.
#. Each :ref:`Powered Wheel <doc_assets_vehicle:vehiclewheelconfiguration_iscolliderpowered>` gets an equal share of the torque. To clarify, the per-wheel torque is equal to the engine output torque divided by the number of powered wheels.

----

.. _doc_assets_vehicle:enginerpm_decreaserate:

EngineRPM_DecreaseRate :ref:`float32 <doc_data_builtin_types>` ``10000.0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

How quickly engine RPM can decrease in RPM/s. For example, 1000 will take 2 seconds to go from 4000 to 2000 RPM.

.. note:: Originally, I thought this might come in handy, but in practice tuning the torque and gear ratios worked better. Kept in case it comes in useful for somebody.

----

.. _doc_assets_vehicle:enginesound:

EngineSound :ref:`RpmEngineSoundConfiguration <doc_assets_vehicle:rpmenginesoundconfiguration_dictionary>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

When :ref:`EngineSound_Type <doc_assets_vehicle:enginesound_type>` is set to ``EngineRPMSimple``, this should be set to an :ref:`RpmEngineSoundConfiguration dictionary <doc_assets_vehicle:rpmenginesoundconfiguration_dictionary>`.

----

.. _doc_assets_vehicle:enginesound_type:

EngineSound_Type :ref:`EVehicleEngineSoundType <doc_assets_vehicle:evehicleenginesoundtype>` ``Legacy``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Defaults to ``Legacy``. In that mode, ``Pitch_Idle`` and ``Pitch_Drive`` are used to control engine audio pitch.

----

.. _doc_assets_vehicle:engineidlerpm:

EngineIdleRPM :ref:`float32 <doc_data_builtin_types>` ``1000.0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Engine RPM will never drop below this value regardless of whether wheel RPM * gear ratio is lower. Otherwise, the engine wouldn't be able to start the wheels rolling from zero.

----

.. _doc_assets_vehicle:enginerpm_increaserate:

EngineRPM_IncreaseRate :ref:`float32 <doc_data_builtin_types>` ``10000.0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

How quickly engine RPM can increase in RPM/s. For example, 1000 will take 2 seconds to go from 2000 to 4000 RPM.

.. note:: Originally, I thought this might come in handy, but in practice tuning the torque and gear ratios worked better. Kept in case it comes in useful for somebody.

----

.. _doc_assets_vehicle:enginemaxrpm:

EngineMaxRPM :ref:`float32 <doc_data_builtin_types>` ``7000.0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Engine RPM will never exceed this value regardless of whether wheel RPM * gear ratio is higher. It should be kept to a reasonable value because the normalized engine RPM is used in a variety of places like sampling the torque curve and network replication.

----

.. _doc_assets_vehicle:environment_invulnerable:

Environment_Invulnerable :ref:`flag <doc_data_flag>`
::::::::::::::::::::::::::::::::::::::::::::::::::::

This vehicle cannot be damaged by animals, zombie melee attacks, or boulders thrown by mega zombies. Zombies and animals will still pursue the vehicle, and attempt to attack any passengers directly. Other damage sources can still damage the vehicle.

----

.. _doc_assets_vehicle:exit:

Exit :ref:`float <doc_data_builtin_types>` ``2``
::::::::::::::::::::::::::::::::::::::::::::::::

Distance away from the vehicle to teleport when exiting.

----

.. _doc_assets_vehicle:explosion:

Explosion :ref:`doc_data_guid` or :ref:`uint16 <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

GUID or legacy ID of :ref:`EffectAsset <doc_assets_effect>` to play when destroyed.

----

.. _doc_assets_vehicle:explosion_force_multiplier:

Explosion_Force_Multiplier :ref:`float32 <doc_data_builtin_types>` ``1.0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

This is a multiplier on the force applied when the vehicle explodes. It is recommended that this property scales based on your vehicle's mass.

Many official vehicles use this property. If you are creating a custom vehicle and using one of the example assets provided as a template (or have a mass that is similar to official content), you will likely want to use a value of ``2`` for this property.

----

.. _doc_assets_vehicle:explosion_max_force:

Explosion_Max_Force :ref:`vector3 <doc_data_vector3>` ``(0, 1024, 0)``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Maximum amount of force applied on the 𝘟\-, 𝘠\-, and 𝘡-axis, when the vehicle explodes.

----

.. _doc_assets_vehicle:explosion_min_force:

Explosion_Min_Force :ref:`vector3 <doc_data_vector3>` ``(0, 1024, 0)``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Minimum amount of force applied on the 𝘟\-, 𝘠\-, and 𝘡-axis, when the vehicle explodes.

----

.. _doc_assets_vehicle:explosions_invulnerable:

Explosions_Invulnerable :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::::::::::::::::::::

The vehicle cannot be damaged by explosions.

----

.. _doc_assets_vehicle:forwardgearratios:

ForwardGearRatios :ref:`list of float32 <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Ratio between engine RPM and wheel RPM in a given gear. For example, if the wheel RPM is 6 and the gear ratio is 5 then the engine RPM is 30.

.. note::

	When converting vanilla cars to gear ratios, the approach I used was to calculate the gear ratio for a desired speed and engine RPM.
	Suppose you're targeting 80 kph with a wheel radius of 0.6 m:

		1. Convert 80 kph to m/s, in this case, 22.2 m/s.
		2. Calculate wheel circumference with 2 * pi * r, in this case 3.77 m.
		3. Calculate how far the vehicle would travel in a minute. 22.2 m/s * 60 s/min is 1,333.2 m/min.
		4. Divide the distance per minute by the circumference to get the wheel RPM of 353.6776.

	Supposedly (I'm still learning as I go) engines work most efficiently around the upper-middle of their RPM range. For example, 3500 RPM for an engine with 1000 idle RPM and 6000 max RPM. Using 3500 as our target engine RPM we can divide it by the wheel RPM to get a good starting point for the gear ratio tuning: 9.89.

----

.. _doc_assets_vehicle:fuel:

Fuel :ref:`uint16 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::

Total fuel capacity.

----

.. _doc_assets_vehicle:fuel_burn_rate:

Fuel_Burn_Rate :ref:`float32 <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::

This controls the rate at which fuel decreases per second. Defaults to ``2.05`` when using ``Engine Car``, or to ``4.2`` otherwise.

----

.. _doc_assets_vehicle:fuel_max:

Fuel_Max :ref:`uint16 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::

Maximum possible fuel to spawn with.

----

.. _doc_assets_vehicle:fuel_min:

Fuel_Min :ref:`uint16 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::

Minimum possible fuel to spawn with.

----

.. _doc_assets_vehicle:gearshift_downthresholdrpm:

GearShift_DownThresholdRPM :ref:`float32 <doc_data_builtin_types>` ``1500.0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

When engine RPM is below this value and a lower gear is available the car will shift gears down.

----

.. _doc_assets_vehicle:gearshift_duration:

GearShift_Duration :ref:`float32 <doc_data_builtin_types>` ``0.5``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

How long it takes to shift gears, measured in seconds. Wheels do not provide any torque for this duration.

----

.. _doc_assets_vehicle:gearshift_interval:

GearShift_Interval :ref:`float32 <doc_data_builtin_types>` ``1.0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

How long to wait since the last gear change before shifting gears, measured in seconds. It can take a moment for the engine RPM to adjust after a gear change, so without a delay the RPM would still exceed the threshold.

----

.. _doc_assets_vehicle:gearshift_upthresholdrpm:

GearShift_UpThresholdRPM :ref:`float32 <doc_data_builtin_types>` ``5500.0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

When engine RPM is above this value and a higher gear is available the car will shift gears up.

----

.. _doc_assets_vehicle:gearshift_visibleinhud:

GearShift_VisibleInHUD :ref:`bool <doc_data_builtin_types>` ``true``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If gears are configured and this is true, RPM and gear number will be shown in the user interface.

----

.. _doc_assets_vehicle:guid:

GUID :ref:`doc_data_guid`
:::::::::::::::::::::::::

Refer to :ref:`GUID <doc_data_guid>` documentation. Vehicles are required to have this property.

.. tip::

  If the GUID property has been omitted from the asset file, then the game will automatically attempt to assign a random (and unique) GUID during a successful load.

----

.. _doc_assets_vehicle:has_clip_prefab:

Has_Clip_Prefab :ref:`bool <doc_data_builtin_types>` ``true``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Whether or not the vehicle has a Clip.prefab. If the vehicle should use the same prefab on the server as on the client, set to false. For example, most official content uses ``Has_Clip_Prefab false``.

----

.. _doc_assets_vehicle:has_horn:

Has_Horn :ref:`bool <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::

Whether or not the vehicle should have a horn. Defaults to ``true`` when the vehicle either has a ``Horn`` AudioClip, or the ``HornAudioClip`` property has been set to a valid path. Otherwise, defaults to ``false``.

----

.. _doc_assets_vehicle:health:

Health :ref:`uint16 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::

Total health value.

----

.. _doc_assets_vehicle:health_max:

Health_Max :ref:`uint16 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::

Minimum possible health to spawn with.

----

.. _doc_assets_vehicle:health_min:

Health_Min :ref:`uint16 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::

Maximum possible health to spawn with.

----

.. _doc_assets_vehicle:hornaudioclip:

HornAudioClip :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

AudioClip to play when using the horn.

----

.. _doc_assets_vehicle:id:

ID :ref:`uint16 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::

Must be a unique identifier. This property used to be required by vehicles, but this is no longer necessary.

The range reserved for official content is [1, 2000).

----

.. _doc_assets_vehicle:ignitionaudioclip:

IgnitionAudioClip :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

AudioClip to play after entering the driver's seat.

----

.. _doc_assets_vehicle:invulnerable:

Invulnerable :ref:`flag <doc_data_flag>`
::::::::::::::::::::::::::::::::::::::::

The vehicle cannot be damaged by lower-power :ref:`doc_item_asset_weapon` that do not have the ``Invulnerable`` flag.

----

.. _doc_assets_vehicle:ispaintable:

IsPaintable :ref:`bool <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::

If ``true``, :ref:`Vehicle Paint Tools <doc_item_asset_vehicle_paint_tool>` can be used on this vehicle. Defaults to ``true`` if :ref:`PaintableSections <doc_assets_vehicle:paintablesections>` has been configured.

----

.. _doc_assets_vehicle:lift:

Lift :ref:`float32 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::

The amount of upwards lift force to apply, when using ``Engine Plane``.

----

.. _doc_assets_vehicle:lockmouse:

LockMouse :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::::::

First-person camera movement is locked while driving. This is useful for ``Engine Plane`` and ``Engine Helicopter``, as a player's mouse movement while in first-person can be used to steer the vehicle.

----

.. _doc_assets_vehicle:num_steering_tires:

Num_Steering_Tires :ref:`int32 <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::

.. deprecated:: 3.23.4.0
	Replaced by the ``WheelConfigurations`` property.

Total number of tires that should turn when steering. Defaults to ``2`` when using ``Engine Car``, to ``1`` when using any other ``Engine`` enumerator, or to ``0`` if the ``Crawler`` property has been set.

----

.. _doc_assets_vehicle:override_center_of_mass:

Override_Center_Of_Mass :ref:`bool <doc_data_builtin_types>` ``false``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If ``true``, overrides the vehicle's center of mass with the values from the ``Center_Of_Mass`` property. This allows for modifying a vehicle's center of gravity without needing to move the "Cog" GameObject in Unity.

----

.. _doc_assets_vehicle:paintablesections:

PaintableSections :ref:`list of PaintableVehicleSection <doc_assets_vehicle:paintablevehiclesection_dictionary>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If set, the vehicle can be painted with a :ref:`Vehicle Paint Tool <doc_item_asset_vehicle_paint_tool>`. Each section's material's ``_PaintColor`` property is set to the vehicle's paint color.

----

.. _doc_assets_vehicle:passenger_explosion_armor:

Passenger_Explosion_Armor :ref:`float32 <doc_data_builtin_types>` ``1``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on the damage taken by players sitting in the vehicle, by explosions.

----

.. _doc_assets_vehicle:physics_profile:

Physics_Profile :ref:`GUID <doc_data_guid>`
:::::::::::::::::::::::::::::::::::::::::::

GUID of a :ref:`VehiclePhysicsProfileAsset <doc_assets_vehicle_physics_profile>` to use. Physics profiles allow for increased control over vehicle settings in bulk, but are not required for anything.

There are several default profiles. These are used when the vehicle's :ref:`Engine <doc_assets_vehicle:engine>` property has been set to ``Boat``, ``Car``, ``Helicopter``, or ``Plane``, if its WheelColliders also have a mass equal to 1.0. Otherwise, nothing is used by default.

- ``Boat`` defaults to ``47258d0dcad14cb8be26e24c1ef3449e``.
- ``Car`` defaults to ``6b91a94f01b6472eaca31d9420ec2367``.
- ``Helicopter`` defaults to ``bb9f9f0204c4462ca7d976b87d1336d4``.
- ``Plane`` defaults to ``93a47d6d40454335b4784e803628ac54``.

Other vehicle types do not have a default profile.

----

.. _doc_assets_vehicle:pitch_drive:

Pitch_Drive :ref:`float32 <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on the pitch of the engine audio while driving. Defaults to ``0.03`` when using ``Engine Helicopter``, or to ``0.1`` when using ``Engine Blimp``. For other ``Engine`` enumerators, it defaults to ``0.025`` if the audio clip is named "Engine_Large", or to ``0.075`` if the audio clip is named "Engine_Small". Otherwise, defaults to ``0.05``.

----

.. _doc_assets_vehicle:pitch_idle:

Pitch_Idle :ref:`float32 <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on the pitch of the engine audio while idle. Defaults to ``0.625`` if the audio clip is named "Engine_Large", or to ``0.75`` if the audio clip is named "Engine_Small". Otherwise, defaults to ``0.5``.

----

.. _doc_assets_vehicle:rarity:

Rarity :ref:`doc_data_eitemrarity` ``Common``
:::::::::::::::::::::::::::::::::::::::::::::

Rarity of the item, as text shown in menus and colors used for highlights.

----

.. _doc_assets_vehicle:reclined:

Reclined :ref:`flag <doc_data_flag>`
::::::::::::::::::::::::::::::::::::

Player character should use a reclined idle animation.

----

.. _doc_assets_vehicle:reversegearratio:

ReverseGearRatio :ref:`float32 <doc_data_builtin_types>` ``1.0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Gear ratio to use when reversing. Please refer to :ref:`ForwardGearRatios <doc_assets_vehicle:forwardgearratios>` for more details on gear ratios.

----

.. _doc_assets_vehicle:rollangularvelocitydamping:

RollAngularVelocityDamping :ref:`float32 <doc_data_builtin_types>` ``-1.0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If greater than zero, an acceleration is applied to angular velocity on 𝘡-axis toward zero.

----

.. _doc_assets_vehicle:shared_skin_lookup_id:

Shared_Skin_Lookup_ID :ref:`doc_data_guid` or :ref:`uint16 <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

GUID or legacy ID of another vehicle, which this vehicle should share skins with. This property was used by some official vehicles (such as the `Rally Car <https://unturned.wiki/Rally_Car>`_), as each paint color used to be a separate vehicle. This is no longer necessary, but some modded vehicles may still rely on this functionality. Defaults to the value of this vehicle's configured ``GUID``.

----

.. _doc_assets_vehicle:shared_skin_name:

Shared_Skin_Name :ref:`string <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::

When generating images, the image name will contain the value of this string instead of the vehicle's file name. Often used with ``Shared_Skin_Lookup_ID``.

----

.. _doc_assets_vehicle:should_spawn_seat_capsules:

Should_Spawn_Seat_Capsules :ref:`bool <doc_data_builtin_types>` ``false``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If ``true``, capsule colliders will be attached to the ``Seat`` GameObject in order to prevent players from clipping into the ground. This is useful for vehicles that do not have a roof, such as bicycles.

----

.. _doc_assets_vehicle:shouldexplosionburnmaterials:

ShouldExplosionBurnMaterials :ref:`bool <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

When ``true``, the materials of the vehicle's ``Model_#`` GameObjects will be tinted black when the vehicle is destroyed. Defaults to ``true`` if the ``Explosion`` property is configured.

----

.. _doc_assets_vehicle:shouldexplosioncausedamage:

ShouldExplosionCauseDamage :ref:`bool <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

When ``true``, the explosion caused by the vehicle being destroyed will deal damage to nearby entities, and kill any passengers. Defaults to ``true`` if the ``Explosion`` property is configured.

----

.. _doc_assets_vehicle:size2_z:

Size2_Z :ref:`float32 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::

Orthogonal camera size for economy icons.

----

.. _doc_assets_vehicle:sleds:

Sleds :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::

Tires should easily roll. For example, most planes will want to use this property.

----

.. _doc_assets_vehicle:speed_max:

Speed_Max :ref:`float32 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::

The vehicle's maximum velocity to aim for while accelerating forward, in m/s (meters per second). For all ``Engine`` enumerators except for the ``Train`` enumerator, this value is multiplied by 1.25 because the vehicle adjusts wheel torque trying to match a specific speed. For example, a vehicle that uses ``Speed_Max 12.5`` and is using ``Engine Car`` will have a maximum forward speed of 56.25 kph (34.95 mph).

----

.. _doc_assets_vehicle:speed_min:

Speed_Min :ref:`float32 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::

The vehicle's maximum velocity to aim for while accelerating in reverse, in m/s (meters per second). In-game, a vehicle's speed is displayed as either kph (kilometers per hour) or mph (miles per hour). For example, a vehicle that uses ``Speed_Min -7`` will have a maximum reversing speed of 25.2 kph (15.66 mph).

----

.. _doc_assets_vehicle:stamina_boost:

Stamina_Boost :ref:`float32 <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::

When a value is specified, this property allows for using stamina to boost. The value specified is the multiplier on the speed a vehicle can go without using a stamina boost. For example, ``Stamina_Boost 0.5`` would only let vehicle move at 50% its maximum speed normally, but using stamina to boost would it reach its maximum speed. This property is often used with ``Stamina_Powered``, but this is not required.

----

.. _doc_assets_vehicle:stamina_powered:

Stamina_Powered :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::::::::::::

The vehicle does not use fuel or a vehicle battery.

----

.. _doc_assets_vehicle:steer_max:

Steer_Max :ref:`float32 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::

Steering angle range at target maximum speed (for the current forward/backward direction). This value is multiplied by 0.75.

----

.. _doc_assets_vehicle:steer_min:

Steer_Min :ref:`float32 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::

Steering angle range at zero speed.

----

.. _doc_assets_vehicle:steering_angle_turn_speed:

Steering_Angle_Turn_Speed :ref:`float32 <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

How quickly wheels can turn to meet player input, measured in degrees per second. Defaults to the value of ``Steer_Max * 5.0``.

----

.. _doc_assets_vehicle:steering_leaningforcemultiplier:

Steering_LeaningForceMultiplier :ref:`float32 <doc_data_builtin_types>` ``-1.0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If greater than zero, torque is applied on 𝘡-axis according to steering input for bikes and motorcycles.

----

.. _doc_assets_vehicle:steering_tire_#:

Steering_Tire_# :ref:`int32 <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::

.. deprecated:: 3.23.4.0
	Replaced by the ``WheelConfigurations`` property.

Set a ``Wheel_#`` GameObject as a steering tire, which will visibly turn when steering. By default, a number of steering tires equal to the value of ``Num_Steering_Tires`` will be automatically set. These will start at ``Steering_Tire_0 0`` (corresponding to ``Wheel_0``), and increment upwards.

----

.. _doc_assets_vehicle:tire_id:

Tire_ID :ref:`uint16 <doc_data_builtin_types>` ``1451``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::

ID of the item that should be given when a tire is manually removed with a :ref:`ToolAsset <doc_item_asset_tire>` that has ``Mode Remove``, and can also be manually attached to the vehicle if the specified item ID is for a :ref:`ToolAsset <doc_item_asset_tire>` with ``Mode Add``.

----

.. _doc_assets_vehicle:tires_invulnerable:

Tires_Invulnerable :ref:`flag <doc_data_flag>`
::::::::::::::::::::::::::::::::::::::::::::::

Tires cannot be damaged.

----

.. _doc_assets_vehicle:traction:

Traction :ref:`flag <doc_data_flag>`
::::::::::::::::::::::::::::::::::::

Tires should have traction in snowy positions.

----

.. _doc_assets_vehicle:train_car_length:

Train_Car_Length :ref:`float32 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

The distance between each train car on the train, in meters. This property is used with ``Engine Train``.

----

.. _doc_assets_vehicle:train_track_offset:

Train_Track_Offset :ref:`float32 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

The offset the train car is above the track, in meters. This property is used with ``Engine Train``.

----

.. _doc_assets_vehicle:train_wheel_offset:

Train_Wheel_Offset :ref:`float32 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

The offset between the wheels, in meters. This property is used with ``Engine Train``.

----

.. _doc_assets_vehicle:trunk_storage_x:

Trunk_Storage_X :ref:`uint8 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Number of columns (horizontal storage space).

----

.. _doc_assets_vehicle:trunk_storage_y:

Trunk_Storage_Y :ref:`uint8 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Number of rows (vertical storage space).

----

.. _doc_assets_vehicle:turret_ignore_aim_camera:

Turret_#_Ignore_Aim_Camera :ref:`flag <doc_data_flag>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::

Normally, the player's camera is positioned at the "Aim" GameObject. Including this flag will disable this feature.

----

.. _doc_assets_vehicle:turret_item_id:

Turret_#_Item_ID :ref:`uint16 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Legacy ID of the item usable from the turret seat. This is often used with a :ref:`GunAsset <doc_item_asset_gun>` that has the ``Turret`` property. However, other items can be used – although most will function in unintended ways.

----

.. _doc_assets_vehicle:turret_pitch_max:

Turret_#_Pitch_Max :ref:`float32 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Maximum allowed rotation of the turret through the elevation, in degrees.

----

.. _doc_assets_vehicle:turret_pitch_min:

Turret_#_Pitch_Min :ref:`float32 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Minimum allowed rotation of the turret through the elevation, in degrees.

----

.. _doc_assets_vehicle:turret_seat_index:

Turret_#_Seat_Index :ref:`uint8 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Index of the "Seat_#" GameObject that this turret is usable from. For example, ``0`` would correspond to "Seat_0".

----

.. _doc_assets_vehicle:turret_yaw_max:

Turret_#_Yaw_Max :ref:`float32 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Maximum allowed rotation of the turret through the azimuth, in degrees. If this is set to ``360``, it can rotate rightward forever.

----

.. _doc_assets_vehicle:turret_yaw_min:

Turret_#_Yaw_Min :ref:`float32 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Minimum allowed rotation of the turret through the azimuth, in degrees. If this is set to ``-360``, it can rotate leftward forever.

----

.. _doc_assets_vehicle:turrets:

Turrets :ref:`uint8 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::

Total number of turrets on the vehicle. All other turret-related properties require that this property has been configured.

For example, this is how the `Fighter Jet <https://unturned.wiki/Fighter_Jet>`_ is configured:

.. code-block:: unturneddat
	:linenos:

	Turrets 1
	Turret_0_Seat_Index 0
	Turret_0_Item_ID 1471
	Turret_0_Yaw_Min -135
	Turret_0_Yaw_Max 135
	Turret_0_Pitch_Min 85
	Turret_0_Pitch_Max 180
	Turret_0_Ignore_Aim_Camera

----

.. _doc_assets_vehicle:type:

Type :ref:`doc_data_eassettype`
:::::::::::::::::::::::::::::::

Designates the vehicle's class. Vehicle assets are required to have this property.

----

.. _doc_assets_vehicle:valid_speed_down:

Valid_Speed_Down :ref:`float32 <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Configuring this will override the sanity check for reversing speed, in m/s (meters per second). If reversing speed exceeds this, the movement is marked as invalid.

Defaults to ``25`` when using ``Engine Car`` or ``Engine Boat``, or to ``100`` otherwise.

----

.. _doc_assets_vehicle:valid_speed_horizontal:

Valid_Speed_Horizontal :ref:`float32 <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Configuring this will override the sanity check for horizontal speed. This value is multiplied by ``PlayerInput.RATE (0.08)``, and then squared.

Defaults to ``(Speed_Max * 0.125)^2`` when using ``Engine Helicopter`` or ``Engine Blimp``, or to ``(Speed_Max * 0.1)^2`` otherwise. This property is useful for vehicles with speed that the server cannot predict, such as force-applying Unity components.

----

.. _doc_assets_vehicle:valid_speed_up:

Valid_Speed_Up :ref:`float32 <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::

Configuring this will override the sanity check for forward speed, in m/s (meters per second). If forward speed exceeds this, the movement is marked as invalid.

Defaults to 12.5 when using ``Engine Car``, to 3.25 when using ``Engine Boat``, or to 100 otherwise.

----

.. _doc_assets_vehicle:wheel_collider_mass_override:

Wheel_Collider_Mass_Override :ref:`float32 <doc_data_builtin_types>` ``null``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Override the mass of the vehicle's WheelCollider components. This allows for quickly modifying the mass of the wheel colliders without needing to rebundle the asset in Unity. If a vehicle has realistic mass, then it may be helpful to set this value to something exceptionally high (e.g., ``500``).

----

.. _doc_assets_vehicle:wheelbalancing_forcemultiplier:

WheelBalancing_ForceMultiplier :ref:`float32 <doc_data_builtin_types>` ``-1.0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If greater than zero, torque is applied on the Z axis multiplied by this factor to align vehicle up with ground up.

.. note:: :ref:`RollAngularVelocityDamping <doc_assets_vehicle:rollangularvelocitydamping>` is critical for damping this force.

----

.. _doc_assets_vehicle:wheelbalancing_uprightexponent:

WheelBalancing_UprightExponent :ref:`float32 <doc_data_builtin_types>` ``1.5``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Exponent on the 0 to 1 factor representing how aligned the vehicle is with the ground up vector. For example, a value of 2 would apply much less force while nearly aligned with up, whereas a value of 0.5 would apply more force even while nearly aligned with up.

----

.. _doc_assets_vehicle:wheelconfigurations:

WheelConfigurations :ref:`list of VehicleWheelConfiguration <doc_assets_vehicle:vehiclewheelconfiguration_dictionary>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Controls WheelCollider components and their corresponding visual models. When converting older vehicles, enable the ``-LogVehicleWheelConfigurations`` command-line flag to output an equivalent wheel configuration.

For example, this is how the `Ambulance <https://unturned.wiki/Ambulance>`_ is configured:

.. code-block:: unturneddat
	:linenos:

	WheelConfigurations
	[
		{
			WheelColliderPath Tires/Tire_0
			IsColliderSteered true
			IsColliderPowered true
			ModelPath Wheels/Wheel_0
			ModelUseColliderPose true
		}
		{
			WheelColliderPath Tires/Tire_1
			IsColliderSteered true
			IsColliderPowered true
			ModelPath Wheels/Wheel_1
			ModelUseColliderPose true
		}
		{
			WheelColliderPath Tires/Tire_2
			IsColliderSteered false
			IsColliderPowered false
			ModelPath Wheels/Wheel_2
			ModelUseColliderPose true
		}
		{
			WheelColliderPath Tires/Tire_3
			IsColliderSteered false
			IsColliderPowered false
			ModelPath Wheels/Wheel_3
			ModelUseColliderPose true
		}
	]

----

.. _doc_assets_vehicle:zip:

Zip :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::

Player character should use a handlebar idle animation.

PaintableVehicleSection Dictionary Descriptions
```````````````````````````````````````````````

.. _doc_assets_vehicle:paintablevehiclesection_path:

Path :ref:`string <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::

Scene hierarchy path to a Renderer component relative to the vehicle's root transform.

----

.. _doc_assets_vehicle:paintablevehiclesection_materialindex:

MaterialIndex :ref:`int32 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Index into Renderer component's Materials list. For example, ``0`` is the 1st material, ``1`` is the 2nd material, and so forth.

RpmEngineSoundConfiguration Dictionary Descriptions
```````````````````````````````````````````````````

.. _doc_assets_vehicle:rpmenginesoundconfiguration_idlepitch:

IdlePitch :ref:`float32 <doc_data_builtin_types>` ``0.0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

AudioSource pitch when engine RPM is at :ref:`Idle RPM <doc_assets_vehicle:engineidlerpm>`.

----

.. _doc_assets_vehicle:rpmenginesoundconfiguration_idlevolume:

IdleVolume :ref:`float32 <doc_data_builtin_types>` ``0.0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

AudioSource volume when engine RPM is at :ref:`Idle RPM <doc_assets_vehicle:engineidlerpm>`.

----

.. _doc_assets_vehicle:rpmenginesoundconfiguration_maxpitch:

MaxPitch :ref:`float32 <doc_data_builtin_types>` ``0.0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

AudioSource pitch when engine RPM is at :ref:`Max RPM <doc_assets_vehicle:enginemaxrpm>`.

----

.. _doc_assets_vehicle:rpmenginesoundconfiguration_maxvolume:

MaxVolume :ref:`float32 <doc_data_builtin_types>` ``0.0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

AudioSource volume when engine RPM is at :ref:`Max RPM <doc_assets_vehicle:enginemaxrpm>`.

VehicleRandomPaintColorConfiguration Dictionary Descriptions
````````````````````````````````````````````````````````````

.. _doc_assets_vehicle:vehiclerandompaintcolorconfiguration_minsaturation:

MinSaturation :ref:`float32 <doc_data_builtin_types>` ``0.0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Minimum random saturation in HSV color to generate.

----

.. _doc_assets_vehicle:vehiclerandompaintcolorconfiguration_maxsaturation:

MaxSaturation :ref:`float32 <doc_data_builtin_types>` ``0.0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Maximum random saturation in HSV color to generate.

----

.. _doc_assets_vehicle:vehiclerandompaintcolorconfiguration_minvalue:

MinValue :ref:`float32 <doc_data_builtin_types>` ``0.0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Minimum value or brightness in HSV color to generate.

----

.. _doc_assets_vehicle:vehiclerandompaintcolorconfiguration_maxvalue:

MaxValue :ref:`float32 <doc_data_builtin_types>` ``0.0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Maximum value or brightness in HSV color to generate.

----

.. _doc_assets_vehicle:vehiclerandompaintcolorconfiguration_grayscalechance:

GrayscaleChance :ref:`float32 <doc_data_builtin_types>` ``0.0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

[0, 1] color will have zero saturation if random value is less than this. For example, 0.2 means 20% of vehicles will be grayscale.

VehicleWheelConfiguration Dictionary Descriptions
`````````````````````````````````````````````````

.. _doc_assets_vehicle:wheelconfiguration_copycolliderrpmindex:

CopyColliderRpmIndex :ref:`int32 <doc_data_builtin_types>` ``-1``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If set, visual-only wheels without a collider (like the back wheels of the snowmobile) can copy RPM from a wheel that does have a collider. Requires :ref:`ModelRadius <doc_assets_vehicle:wheelconfiguration_modelradius>` to also be set.

----

.. _doc_assets_vehicle:vehiclewheelconfiguration_iscolliderpowered:

IsColliderPowered :ref:`bool <doc_data_builtin_types>` ``false``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If ``true``, collider is connected to the engine and responds to player's acceleration input.

----

.. _doc_assets_vehicle:vehiclewheelconfiguration_iscollidersteered:

IsColliderSteered :ref:`bool <doc_data_builtin_types>` ``false``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If ``true``, collider's steering angle responds to player input.

----

.. _doc_assets_vehicle:vehiclewheelconfiguration_ismodelsteered:

IsModelSteered :ref:`bool <doc_data_builtin_types>` ``false``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If ``true``, model is rotated according to steering input.

Only kept for backwards compatibility. Prior to wheel configurations, only certain WheelColliders actually received steering input, while multiple models would appear to steer. For example, the APC's front 4 wheels appeared to rotate but only the front 2 actually affected physics.

----

.. _doc_assets_vehicle:vehiclewheelconfiguration_modelpath:

ModelPath :ref:`string <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::

Scene hierarchy path of visual representation of wheel relative to the vehicle's root transform.

----

.. _doc_assets_vehicle:wheelconfiguration_modelradius:

ModelRadius :ref:`float32 <doc_data_builtin_types>` ``-1.0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If greater than zero, visual-only wheels (without a collider) like the extra wheels of the Snowmobile use this radius to calculate their rolling speed.

----

.. _doc_assets_vehicle:vehiclewheelconfiguration_modelusecolliderpose:

ModelUseColliderPose :ref:`bool <doc_data_builtin_types>` ``false``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If ``true``, model ignores ``IsModelSteered`` and instead uses the wheel collider state (or an approximation when not simulating).

Prior to wheel configurations, some high-fidely modded cars used a separate set of physics constraints to animate the wheel models as if they had suspension. Constraint setups like this should be completely superseded by the ``ModelUseColliderPose`` property. The constraints were awful for performance because physics for every purely-visual wheel were simulated on every client, and even then they didn't actually match the real wheel state.

----

.. _doc_assets_vehicle:vehiclewheelconfiguration_wheelcolliderpath:

WheelColliderPath :ref:`string <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Scene hierarchy path of a WheelCollider component relative to the vehicle's root transform.

Localization
------------

**Name** *string*: Vehicle name in user interfaces.
