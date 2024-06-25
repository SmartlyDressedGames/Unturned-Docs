.. _doc_assets_vehicle_physics_profile:

Vehicle Physics Profile Assets
==============================

This asset exists to tune vehicle physics in bulk without rebuilding asset bundles, and exposes more control than the individual vehicle assets.

One of the goals introducing profiles is to improve the handling of vanilla wheeled vehicles. Feel free to experiment with the default profile, and propose changes to it.

How to test?
------------

In 3.19.18.0 the **reload** command was introduced which can be used to reload specific assets or directories of assets while playing. Simply reload the physics profile and then respawn a vehicle. For example to reload the default profile:

.. code-block:: shell

	/reload 6b91a94f01b6472eaca31d9420ec2367

How are vehicles assigned a profile?
------------------------------------

Individual vehicle assets can specify a profile by setting **Physics_Profile** to the GUID.

If a profile is not set, and the vehicle prefab's root rigidbody has a mass of 1.0, and the wheel colliders also have masses of 1.0, the default profile at Bundles/Assets/VehiclePhysicsProfiles/DefaultProfile.asset is used.

Asset Properties Reference
--------------------------

**Type** *string*: ``SDG.Unturned.VehiclePhysicsProfileAsset``

**Root_Mass**: If set, overrides vehicle rigidbody's mass.

**Root_Mass_Multiplier**: If set, multiplies vehicle rigidbody's mass.

**Root_Drag_Multiplier**: If set, multiplies vehicle rigidbody's positional drag force.

**Root_Angular_Drag_Multiplier**: If set, multiplies vehicle rigidbody's angular drag force.

**Carjack_Force_Multiplier**: If set, multiplies carjack item's force applied.

**Wheel_Mass**: If set, overrides wheel collider mass. Ignored if vehicle asset has Wheel_Collider_Mass_Override set.

**Wheel_Mass_Multiplier**: If set, multiplies wheel collider mass.

**Wheel_Damping_Rate**: If set, override wheel collider damping rate. Lower values accelerate faster.

**Wheel_Suspension_Force**: If set, overrides wheel collider suspension force.

**Wheel_Suspension_Damper**: If set, overrides wheel collider suspension damper.

**Wheel_Stiffness_Traction_Multiplier**: Wheel collider stiffness multiplier when driving in snow. Default: 0.25

**Wheel_Friction_Sideways** and **Wheel_Friction_Forward**:

* **Extremum_Slip**: If set, overrides friction curve extremum slip.

* **Extremum_Value**: If set, overrides friction curve extremum value.

* **Asymptote_Slip**: If set, overrides friction curve asymptote slip.

* **Asymptote_Value**: If set, overrides friction curve asymptote value.

* **Stiffness**: If set, overrides friction curve stiffness. Multiplies the extremum and asymptote values. Sideways default is 1.0 and forward default is 2.0.

**Motor_Torque_Multiplier**: Multiplies wheel collider motor torque which is usually driven by vehicle speed.

**Motor_Torque_Clamp_Multiplier**: Multiplies wheel collider motor torque when exceeding maximum speed. Default: 0.5

**Brake_Torque_Multiplier**: Multiplies wheel collider brake torque.

**Brake_Torque_Traction_Multiplier**: Multiplies wheel collider brake torque when driving in snow. Default: 0.5

**Wheel_Drive_Model**: ``Front``, ``Rear`` or ``All``. By default all cars are rear-wheel drive, but in the real world cars are front-wheel drive. This discrepancy is due to a poor understanding of cars when they were added to the game in 2014.

**Wheel_Brake_Model**: ``Front``, ``Rear`` or ``All``. Modern cars have all-wheel breaking, which is the default.
