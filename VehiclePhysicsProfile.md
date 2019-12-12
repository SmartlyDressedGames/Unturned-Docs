Vehicle Physics Profile
=======================

This asset exists to tune vehicle physics in bulk without rebuilding asset bundles, and exposes more control than the individual vehicle assets.

One of the goals introducing profiles is to improve the handling of vanilla wheeled vehicles. Feel free to experiment with the default profile, and propose changes to it.

How to test?
------------

In 3.19.18.0 the __reload__ command was introduced which can be used to reload specific assets or directories of assets while playing. Simply reload the physics profile and then respawn a vehicle. For example to reload the default profile:

	/reload 6b91a94f01b6472eaca31d9420ec2367

How are vehicles assigned a profile?
------------------------------------

Individual vehicle assets can specify a profile by setting __Physics_Profile__ to the GUID.

If a profile is not set, and the vehicle prefab's root rigidbody has a mass of 1.0, and the wheel colliders also have masses of 1.0, the default profile at Bundles/Assets/VehiclePhysicsProfiles/DefaultProfile.asset is used.

Asset Properties Reference
--------------------------

__Root_Mass__: If set, overrides vehicle rigidbody's mass.

__Root_Mass_Multiplier__: If set, multiplies vehicle rigidbody's mass.

__Root_Drag_Multiplier__: If set, multiplies vehicle rigidbody's positional drag force.

__Root_Angular_Drag_Multiplier__: If set, multiplies vehicle rigidbody's angular drag force.

__Wheel_Mass__: If set, overrides wheel collider mass. Ignored if vehicle asset has Wheel_Collider_Mass_Override set.

__Wheel_Mass_Multiplier__: If set, multiplies wheel collider mass.

__Wheel_Damping_Rate__: If set, override wheel collider damping rate. Lower values accelerate faster.

__Wheel_Suspension_Force__: If set, overrides wheel collider suspension force.

__Wheel_Suspension_Damper__: If set, overrides wheel collider suspension damper.

__Wheel_Stiffness_Traction_Multiplier__: Wheel collider stiffness multiplier when driving in snow. Default: 0.25

__Wheel_Friction_Sideways__ and __Wheel_Friction_Forward__:

* _Extremum_Slip_: If set, overrides friction curve extremum slip.

* _Extremum_Value_: If set, overrides friction curve extremum value.

* _Asymptote_Slip_: If set, overrides friction curve asymptote slip.

* _Asymptote_Value_: If set, overrides friction curve asymptote value.

* _Stiffness_: If set, overrides friction curve stiffness. Multiplies the extremum and asymptote values. Sideways default is 1.0 and forward default is 2.0.

__Motor_Torque_Multiplier__: Multiplies wheel collider motor torque which is usually driven by vehicle speed.

__Motor_Torque_Clamp_Multiplier__: Multiplies wheel collider motor torque when exceeding maximum speed. Default: 0.5

__Brake_Torque_Multiplier__: Multiplies wheel collider brake torque.

__Brake_Torque_Traction_Multiplier__: Multiplies wheel collider brake torque when driving in snow. Default: 0.5

__Wheel_Drive_Model__: <code>Front</code>, <code>Rear</code> or <code>All</code>. By default all cars are rear-wheel drive, but in the real world cars are front-wheel drive. This discrepency is due to a poor understanding of cars when they were added to the game in 2014.

__Wheel_Brake_Model__: <code>Front</code>, <code>Rear</code> or <code>All</code>. Modern cars have all-wheel breaking, which is the default.
