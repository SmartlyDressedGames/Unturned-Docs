.. _doc_item_asset_gun:

Gun Assets
==========

The ItemGunAsset class is used for ranged weapons (or "guns"), which can be used by players to deal damage. Some examples of vanilla ranged weapons include the `Eaglefire <https://wiki.smartlydressedgames.com/wiki/Eaglefire>`_ and `Crossbow <https://wiki.smartlydressedgames.com/wiki/Crossbow>`_.

Unity Asset Bundle Contents
---------------------------

.. figure:: /assets/img/UnityExampleGun.png

	An example of a gun being set up in the Unity editor.

To get started, either follow the steps to begin creating a custom item from the :ref:`introduction <doc_item_asset_intro>`, or duplicate the contents of a prepackaged example asset.

Item (Prefab)
`````````````

Open the "Item" Prefab, and add six child GameObjects named "Barrel", "Grip", "Sight", "Tactical", "Magazine", and "Eject". Most custom guns will want to have these six child GameObjects, although they are not strictly required.

The "Barrel", "Grip", "Sight", "Tactical", and "Magazine" GameObjects will determine the location of attachments on your gun. The "Sight" GameObject also determines where the camera will be positioned when aiming down sights. Shells are emitted from the "Eject" GameObject.

If an "View" GameObject is added, the camera will use its position when aiming down sights if a sight attachment has not been attached to the gun.

When a gun can accept more than one type of magazine caliber, it may be desirable to have the position of the magazine attachment depend on its caliber ID. Add a child to the "Magazine" GameObject, named "Caliber_#". For example, adding "Caliber_1" would cause magazine attachments using caliber ID 1 to use that position instead of the "Magazine" GameObject's position.

Additional Setup for Bows
:::::::::::::::::::::::::

.. figure:: /assets/img/UnityExampleCrossbow.png

	An example of a crossbow being set up in the Unity editor.

Bows require additional GameObjects to simulate the drawing of the bowstring. Note that bowstrings are only simulated from the first-person perspective.

Add a new child GameObject named "Rope", and set its state to inactive. The "Rope" GameObject should include a Line Renderer component. Vanilla bowstrings use a custom Material named "Rope" with the Unlit-Rope Shader, but this is not required.

Add two child GameObjects named "Left" and "Right". These GameObjects will determine the end points of the bowstring. If a third GameObject named "Rest" is included, it will be used as the middle point of the bowstring when aiming down sights.

Including a fourth GameObject named "Nock" will allow the bow to be fired without aiming down sights. Additionally, the "Rest" GameObject will act as a middle point when not aiming down sights, and the "Nock" GameObject will act as a middle point while aiming down sights.

Additional Setup for Economy Items
::::::::::::::::::::::::::::::::::

There are several child GameObjects that can be added related to skins. Custom items are ineligible to receive skins, so there is usually no reason to add these to the Prefab.

If an item has an "Icon2" GameObject included, its position and orientation will be used when generating icons of skins on this item. A GameObject named "Stat_Tracker" determines the location where stat trackers will appear on the gun, while a GameObject named "Effect" will determine the position of mythical effects on the gun.

Animations (Prefab)
```````````````````

In addition to animations used by any equippable item, guns have an additional set of animations that they can use.

Adding animations named "Aim_Start" and "Aim_Stop" will cause an animation to be played whenever the player starts or stops aiming down sights. Animations named "Attach_Start" and "Attach_Stop" will play when an attachment is attached or unattached to the gun. The "Sprint_Start" and "Sprint_Stop" animations play when the player starts and stops sprinting. The "Reload" animation is played when reloading the gun.

The "Hammer" animation is played under certain conditions where it would make sense to manually eject a cartridge from the gun. For example: after reloading an gun that had an empty magazine, or after firing a single-shot weapon (such as a bolt-action rifle or pump-action shotgun).

If a gun is configured to use the gun jamming feature, the "UnjamChamber" animation will play when a jam occurs.

Audio Clips
```````````

In addition to the Audio Clips that can be included for equippable items, guns have an additional set of audio clips they can use.

If an Audio Clip named "Shoot" is included, it will play after the gun is fired. Including Audio Clips named "Reload" and "Hammer" will cause audio to play after reloading and hammering the gun, respectively.

An "Aim" Audio Clip can be included to have audio play after aiming down sights. For example, a longbow might want to have an the sound of the bow being drawn play. Miniguns can also include an Audio Clip named "Minigun" to have audio play while revving the minigun.

If a gun is configured to use the gun jamming feature, the "ChamberJammed" Audio Clip will play when a jam occurs.

Game Data File
--------------

Ranged weapons inherit properties from the :ref:`ItemWeaponAsset <doc_item_asset_weapon>` class. Any properties from parent classes that are required—or highly recommended—are listed in the table below.

.. list-table::
   :widths: 30 40 30
   :header-rows: 1

   * - Class
     - Property Name
     - Required Value
   * - :ref:`ItemAsset <doc_item_asset_intro>`
     - :ref:`GUID <doc_item_asset_intro:guid>`
     -
   * - :ref:`ItemAsset <doc_item_asset_intro>`
     - :ref:`ID <doc_item_asset_intro:id>`
     -
   * - :ref:`ItemAsset <doc_item_asset_intro>`
     - :ref:`Slot <doc_item_asset_intro:slot>`
     -
   * - :ref:`ItemAsset <doc_item_asset_intro>`
     - :ref:`Type <doc_item_asset_intro:type>`
     - ``Gun``
   * - :ref:`ItemAsset <doc_item_asset_intro>`
     - :ref:`Useable <doc_item_asset_intro:useable>`
     - ``Gun``
   * - :ref:`ItemWeaponAsset <doc_item_asset_intro>`
     - :ref:`Range <doc_item_asset_weapon:range>`
     -

Additionally, all ranged weapons require that the ``Action`` property has been configured. Note that ranged weapons will always show a quality value.

Properties
``````````

Ranged weapons have a significant number of properties. To make navigating these easier, they have been categorized into one of several property tables. Many of these tables contain similar properties that are often used together.

.. list-table:: Uncategorized
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`Aim_In_Duration <doc_item_asset_gun:aim_in_duration>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0.2``
   * - :ref:`Aiming_Movement_Speed_Multiplier <doc_item_asset_gun:aiming_movement_speed_multiplier>`
     - :ref:`float32 <doc_data_builtin_types>`
     - See description
   * - :ref:`Alert_Radius <doc_item_asset_gun:alert_radius>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``48``
   * - :ref:`Can_Aim_During_Sprint <doc_item_asset_gun:can_aim_during_sprint>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``false``
   * - :ref:`Gunshot_Rolloff_Distance <doc_item_asset_gun:gunshot_rolloff_distance>`
     - :ref:`float32 <doc_data_builtin_types>`
     - See description
   * - :ref:`Range_Rangefinder <doc_item_asset_gun:range_rangefinder>`
     - :ref:`float32 <doc_data_builtin_types>`
     - See description
   * - :ref:`Scale_Aim_Animation_Speed <doc_item_asset_gun:scale_aim_animation_speed>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``

.. list-table:: Calibers
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`Attachment_Caliber_# <doc_item_asset_gun:attachment_caliber_#>`
     - :ref:`uint16 <doc_data_builtin_types>`
     - See description
   * - :ref:`Attachment_Calibers <doc_item_asset_gun:attachment_calibers>`
     - :ref:`int32 <doc_data_builtin_types>`
     - See description
   * - :ref:`Caliber <doc_item_asset_gun:caliber>`
     - :ref:`uint16 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Magazine_Caliber_# <doc_item_asset_gun:magazine_caliber_#>`
     - :ref:`uint16 <doc_data_builtin_types>`
     - See description
   * - :ref:`Magazine_Calibers <doc_item_asset_gun:magazine_calibers>`
     - :ref:`int32 <doc_data_builtin_types>`
     - See description
   * - :ref:`Requires_NonZero_Attachment_Caliber <doc_item_asset_gun:requires_nonzero_attachment_caliber>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``false``

.. list-table:: Damage
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`Damage_Falloff_Max_Range <doc_item_asset_gun:damage_falloff_max_range>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Damage_Falloff_Multiplier <doc_item_asset_gun:damage_falloff_multiplier>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Damage_Falloff_Range <doc_item_asset_gun:damage_falloff_range>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Instakill_Headshots <doc_item_asset_gun:instakill_headshots>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``false``

.. list-table:: Effects
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`Explosion <doc_item_asset_gun:explosion>`
     - :ref:`doc_data_guid` or :ref:`uint16 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Muzzle <doc_item_asset_gun:muzzle>`
     - :ref:`doc_data_guid` or :ref:`uint16 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Shell <doc_item_asset_gun:shell>`
     - :ref:`doc_data_guid` or :ref:`uint16 <doc_data_builtin_types>`
     - See description

.. list-table:: Firing Mechanism
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`Action <doc_item_asset_gun:action>`
     - :ref:`EAction <doc_item_asset_gun:eaction>`
     -
   * - :ref:`Auto <doc_item_asset_gun:auto>`
     - :ref:`flag <doc_data_flag>`
     -
   * - :ref:`Bursts <doc_item_asset_gun:bursts>`
     - :ref:`int32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Fire_Delay_Seconds <doc_item_asset_gun:fire_delay_seconds>`
     - :ref:`int32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Firerate <doc_item_asset_gun:firerate>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Safety <doc_item_asset_gun:safety>`
     -  :ref:`flag <doc_data_flag>`
     -
   * - :ref:`Semi <doc_item_asset_gun:semi>`
     -  :ref:`flag <doc_data_flag>`
     -

.. list-table:: Hook Attachments
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`Barrel <doc_item_asset_gun:barrel>`
     - :ref:`uint16 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Grip <doc_item_asset_gun:grip>`
     - :ref:`uint16 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Sight <doc_item_asset_gun:sight>`
     - :ref:`uint16 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Tactical <doc_item_asset_gun:tactical>`
     - :ref:`uint16 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Hook_Barrel <doc_item_asset_gun:hook_barrel>`
     - :ref:`flag <doc_data_flag>`
     -
   * - :ref:`Hook_Grip <doc_item_asset_gun:hook_grip>`
     - :ref:`flag <doc_data_flag>`
     -
   * - :ref:`Hook_Sight <doc_item_asset_gun:hook_sight>`
     - :ref:`flag <doc_data_flag>`
     -
   * - :ref:`Hook_Tactical <doc_item_asset_gun:hook_tactical>`
     - :ref:`flag <doc_data_flag>`
     -

.. list-table:: Jamming
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`Can_Ever_Jam <doc_item_asset_gun:can_ever_jam>`
     - :ref:`flag <doc_data_flag>`
     -
   * - :ref:`Jam_Quality_Threshold <doc_item_asset_gun:jam_quality_threshold>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0.4``
   * - :ref:`Jam_Max_Chance <doc_item_asset_gun:jam_max_chance>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0.1``
   * - :ref:`Unjam_Chamber_Anim <doc_item_asset_gun:unjam_chamber_anim>`
     - :ref:`string <doc_data_builtin_types>`
     - ``UnjamChamber``

.. list-table:: Magazine Attachments
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`Allow_Magazine_Change <doc_item_asset_gun:allow_magazine_change>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - :ref:`Ammo_Max <doc_item_asset_gun:ammo_max>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Ammo_Min <doc_item_asset_gun:ammo_min>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Ammo_Per_Shot <doc_item_asset_gun:ammo_per_shot>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Delete_Empty_Magazines <doc_item_asset_gun:delete_empty_magazines>`
     - :ref:`flag <doc_data_flag>`
     - *deprecated*
   * - :ref:`Hammer_Time <doc_item_asset_gun:hammer_time>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Infinite_Ammo <doc_item_asset_gun:infinite_ammo>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``false``
   * - :ref:`Magazine <doc_item_asset_gun:magazine>`
     - :ref:`uint16 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Magazine_Replacement_#_ID <doc_item_asset_gun:magazine_replacement_#_id>`
     - :ref:`uint16 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Magazine_Replacement_#_Map <doc_item_asset_gun:magazine_replacement_#_map>`
     - :ref:`string <doc_data_builtin_types>`
     -
   * - :ref:`Magazine_Replacements <doc_item_asset_gun:magazine_replacements>`
     - :ref:`int32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Reload_Time <doc_item_asset_gun:reload_time>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Replace <doc_item_asset_gun:replace>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Should_Delete_Empty_Magazines <doc_item_asset_gun:should_delete_empty_magazines>`
     - :ref:`bool <doc_data_builtin_types>`
     - See description
   * - :ref:`Unplace <doc_item_asset_gun:unplace>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``

.. list-table:: Projectiles (Ballistic System)
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`Ballistic_Drop <doc_item_asset_gun:ballistic_drop>`
     - :ref:`float32 <doc_data_builtin_types>`
     - *deprecated*
   * - :ref:`Ballistic_Steps <doc_item_asset_gun:ballistic_steps>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - See description
   * - :ref:`Ballistic_Travel <doc_item_asset_gun:ballistic_travel>`
     - :ref:`float32 <doc_data_builtin_types>`
     - See description
   * - :ref:`Bullet_Gravity_Multiplier <doc_item_asset_gun:bullet_gravity_multiplier>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``4``

.. list-table:: Projectiles (Physics System)
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`Ballistic_Force <doc_item_asset_gun:ballistic_force>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0.002``
   * - :ref:`Projectile_Explosion_Launch_Speed <doc_item_asset_gun:projectile_explosion_launch_speed>`
     - :ref:`float32 <doc_data_builtin_types>`
     - See description
   * - :ref:`Projectile_Lifespan <doc_item_asset_gun:projectile_lifespan>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``30``
   * - :ref:`Projectile_Penetrate_Buildables <doc_item_asset_gun:projectile_penetrate_buildables>`
     - :ref:`flag <doc_data_builtin_types>`
     -

.. list-table:: Recoil
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`Aiming_Recoil_Multiplier <doc_item_asset_gun:aiming_recoil_multiplier>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Recoil_Crouch <doc_item_asset_gun:recoil_crouch>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0.85``
   * - :ref:`Recoil_Max_X <doc_item_asset_gun:recoil_max_x>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Recoil_Max_Y <doc_item_asset_gun:recoil_max_y>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Recoil_Min_X <doc_item_asset_gun:recoil_min_x>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Recoil_Min_Y <doc_item_asset_gun:recoil_min_y>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Recoil_Prone <doc_item_asset_gun:recoil_prone>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0.7``
   * - :ref:`Recoil_Sprint <doc_item_asset_gun:recoil_sprint>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1.25``
   * - :ref:`Recoil_Swimming <doc_item_asset_gun:recoil_swimming>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1.1``
   * - :ref:`Recover_X <doc_item_asset_gun:recover_x>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Recover_Y <doc_item_asset_gun:recover_y>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``

.. list-table:: Shake
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`Shake_Max_X <doc_item_asset_gun:shake_max_x>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Shake_Min_X <doc_item_asset_gun:shake_min_x>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Shake_Max_Y <doc_item_asset_gun:shake_max_y>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Shake_Min_Y <doc_item_asset_gun:shake_min_y>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Shake_Max_Z <doc_item_asset_gun:shake_max_z>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Shake_Min_Z <doc_item_asset_gun:shake_min_z>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``

.. list-table:: Spread
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`Spread_Aim <doc_item_asset_gun:spread_aim>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Spread_Angle_Degrees <doc_item_asset_gun:spread_angle_degrees>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Spread_Crouch <doc_item_asset_gun:spread_crouch>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0.85``
   * - :ref:`Spread_Hip <doc_item_asset_gun:spread_hip>`
     - :ref:`float32 <doc_data_builtin_types>`
     - *deprecated*
   * - :ref:`Spread_Prone <doc_item_asset_gun:spread_prone>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0.7``
   * - :ref:`Spread_Sprint <doc_item_asset_gun:spread_sprint>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1.25``
   * - :ref:`Spread_Swimming <doc_item_asset_gun:spread_swimming>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1.1``

.. _doc_item_asset_gun:eaction:

EAction Enumeration
```````````````````

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Named Value
     - Description
   * - ``Trigger``
     - Corresponds to the "Trigger" action. Uses the ballistic projectile system.
   * - ``Bolt``
     - Corresponds to the "Bolt" action. Uses the ballistic projectile system.
   * - ``Pump``
     - Corresponds to the "Pump" action. Uses the ballistic projectile system.
   * - ``Rail``
     - Corresponds to the "Rail" action. Uses the ballistic projectile system.
   * - ``String``
     - Corresponds to the "String" action. Uses the ballistic projectile system.
   * - ``Break``
     - Corresponds to the "Break" action. Uses the ballistic projectile system.
   * - ``Rocket``
     - Corresponds to the "Rocket" action. Uses the physics projectile system.
   * - ``Minigun``
     - Corresponds to the "Minigun" action. Uses the ballistic projectile system.

Property Descriptions
`````````````````````

.. _doc_item_asset_gun:action:

Action :ref:`EAction <doc_item_asset_gun:eaction>`
::::::::::::::::::::::::::::::::::::::::::::::::::

The value of this property determines how the weapon functions when used, including whether it uses *ballistic projectiles*, or *physics projectiles*. Different properties are available to the weapon depending on the value of this property.

Although most action mechanisms utilize ballistic projectiles, the ``Rocket`` action mechanism uses physics projectiles instead. Additionally, any projectiles from these weapons (e.g., the `Rocket Launcher <https://wiki.smartlydressedgames.com/wiki/Rocket_Launcher>`_) are explosive.

To fire a weapon with the  ``String`` action mechanism, a player must be aiming down sights – unless a "Nock" GameObject has been added during its Unity setup.

----

.. _doc_item_asset_gun:aim_in_duration:

Aim_In_Duration :ref:`float32 <doc_data_builtin_types>` ``0.2``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

How long it takes to fully aim down sights, in seconds.

----

.. _doc_item_asset_gun:aiming_movement_speed_multiplier:

Aiming_Movement_Speed_Multiplier :ref:`float32 <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on the player's movement speed while aiming down sights. Defaults to ``0.75`` when ``Can_Aim_During_Sprint`` is ``false``. Otherwise, defaults to ``1``.

----

.. _doc_item_asset_gun:aiming_recoil_multiplier:

Aiming_Recoil_Multiplier :ref:`float32 <doc_data_builtin_types>` ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on recoil magnitude while aiming down sights.

----

.. _doc_item_asset_gun:alert_radius:

Alert_Radius :ref:`float32 <doc_data_builtin_types>` ``48``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

The radius of the alert generated by ranged weapons when they are fired. Zombies or animals caught within this radius are alerted. This radius is measured in meters.

----

.. _doc_item_asset_gun:allow_magazine_change:

Allow_Magazine_Change :ref:`bool <doc_data_builtin_types>` ``true``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

When ``false``, the magazine cannot be removed, replaced, or reloaded. This functions similar to a few other properties, such as ``Hook_Barrel`` or ``Hook_Grip`` when determing valid hook attachment slots.

----

.. _doc_item_asset_gun:ammo_max:

Ammo_Max :ref:`uint8 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::

Maximum amount of ammo to randomly generate in the magazine attachment that was attached to the weapon by default.

----

.. _doc_item_asset_gun:ammo_min:

Ammo_Min :ref:`uint8 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::

Minimum amount of ammo to randomly generate in the magazine attachment that was attached to the weapon by default.

----

.. _doc_item_asset_gun:ammo_per_shot:

Ammo_Per_Shot :ref:`uint8 <doc_data_builtin_types>` ``1``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Number of ammunition consumed per shot. For example, a value of ``3`` would consume three ammo every time the weapon is fired, while a value of ``0`` would allow for the weapon to have infinite ammo.

----

.. _doc_item_asset_gun:attachment_caliber_#:

Attachment_Caliber_# :ref:`uint16 <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Legacy ID of a caliber to check for hook attachment compatibility. This property is used in conjunction with ``Attachment_Calibers``, which determines how many instances of this property should be read by the game.

When this property is unset, it will default to ``0``. When the ``Attachment_Calibers`` property is not greater than ``0``, this property will default to the value of any ``Magazine_Caliber_#`` properties.

For example, a valid configuration for a ranged weapon's calibers could be:

.. code-block:: unturned

  Attachment_Calibers 2
  Attachment_Caliber_0 1
  Attachment_Caliber_1 9

  Magazine_Calibers 3
  Magazine_Caliber_0 1
  Magazine_Caliber_1 4
  Magazine_Caliber_2 9

This would allow the ranged weapon to use hook attachments with caliber IDs of 1 or 9, and to use magazine attachments with caliber IDs of 1, 4, or 9.

----

.. _doc_item_asset_gun:attachment_calibers:

Attachment_Calibers :ref:`int32 <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Set the length of the array containing the calibers for hook attachment compatibility. This property is used in conjunction with the ``Attachment_Caliber_#`` property, and the value of ``Attachment_Calibers`` should be equal to the number of instances of ``Attachment_Caliber_#``.

When this property is not greater than ``0`` – it will default to the value of ``Magazine_Calibers``, and the ``Attachment_Caliber_#`` property can no longer be customized.

To use this property, ``Magazine_Calibers`` must be configured.

----

.. _doc_item_asset_gun:auto:

Auto :ref:`flag <doc_data_flag>`
::::::::::::::::::::::::::::::::

The weapon has an automatic firing mode.

----

.. _doc_item_asset_gun:ballistic_drop:

Ballistic_Drop :ref:`float32 <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::

.. deprecated:: 3.23.7.0
   Use ``Bullet_Gravity_Multiplier`` instead.

Existing values are automatically converted if ``Bullet_Gravity_Multiplier`` has not been configured. The conversion is logged during :ref:`doc_asset_validation`.

----

.. _doc_item_asset_gun:ballistic_force:

Ballistic_Force :ref:`float32 <doc_data_builtin_types>` ``0.002``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

The amount of force that should be applied to the *physics projectile*, measured in Newtons. It may be helpful to read Unity's `Rigidbody.AddForce documentation <https://docs.unity3d.com/ScriptReference/Rigidbody.AddForce.html>`_ to better understand physics projectiles.

Properties used by physics projectiles (such as ``Ballistic_Force``) cannot be used alongside properties intended for ballistic projectiles (such as ``Ballistic_Travel`` or ``Bullet_Gravity_Multiplier``).

----

.. _doc_item_asset_gun:ballistic_steps:

Ballistic_Steps :ref:`uint8 <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::

Lifespan of *ballistic projectiles*. A higher value relative to ``Ballistic_Travel`` will result in less muzzle velocity. Must be a value greater than ``0``.

Defaults to ``Range ÷ Ballistic_Travel``, rounded up to the nearest integer.

To avoid a mismatch between the weapon's max range and its manual ballistic range, it is recommend to only configure ``Ballistic_Steps`` or ``Ballistic_Travel`` (or neither) – no both.

----

.. _doc_item_asset_gun:ballistic_travel:

Ballistic_Travel :ref:`float32 <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Travel speed of *ballistic projectiles*. A higher value relative to ``Ballistic_Steps`` will result in more muzzle velocity. Must be a value greater than ``0.1``.

Defaults to ``10``. If ``Ballistic_Steps`` is specified and greater than ``0``, and ``Ballistic_Travel`` is not specified, then ``Ballistic_Travel`` defaults to ``Range ÷ Ballistic_Steps``.

To avoid a mismatch between the weapon's max range and its manual ballistic range, it is recommend to only configure ``Ballistic_Travel`` or ``Ballistic_Steps`` (or neither) – no both.

----

.. _doc_item_asset_gun:barrel:

Barrel :ref:`uint16 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::

Legacy ID of a barrel attachment that should be attached by default. The ``Hook_Barrel`` flag is not required to use this property.

----

.. _doc_item_asset_gun:bullet_gravity_multiplier:

Bullet_Gravity_Multiplier :ref:`float32 <doc_data_builtin_types>` ``4``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier for gravity's acceleration. This property is available to *ballistic projectile* weapons. Setting this value to ``1`` allows for more realistic bullet drop.

.. note:: This defaults to ``4`` because *Unturned*'s maximum engagement distance is rather short, but this distance may be raised in the future if/when network improvements are made to the game. Gravity defaults to 9.81 m/s², or can be configured in the :ref:`doc_mapping_config`.

----

.. _doc_item_asset_gun:bursts:

Bursts :ref:`int32 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::

When a value greater than ``0`` is provided, the weapon has a burst firing mode. A number of shots equal to this value is fired when using this mode.

----

.. _doc_item_asset_gun:caliber:

Caliber :ref:`uint16 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::

Legacy ID of the caliber to check for hook attachment and magazine attachment compatibility. To add compatibility for multiple calibers, or to configure hook attachment and magazine attachment compatibility separately, use the ``Magazine_Calibers`` and ``Attachment_Calibers`` properties instead.

----

.. _doc_item_asset_gun:can_aim_during_sprint:

Can_Aim_During_Sprint :ref:`bool <doc_data_builtin_types>` ``false``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

When ``true``, the player can sprint while aiming down sights.

----

.. _doc_item_asset_gun:can_ever_jam:

Can_Ever_Jam :ref:`flag <doc_data_flag>`
::::::::::::::::::::::::::::::::::::::::

When this flag is included, the weapon can jam. Weapons have a chance of jamming once their quality drops below a certain threshold. Starting from the initial threshold, the chance of jamming on each shot is blended between between 0% and a specified max chance.

The "ChamberJammed" Audio Clip is played when a jam occurs, as well as the animation "UnjamChamber" if present.

For an example, refer to ``.../Guns/Cobra_Jam/Cobra_Jam.dat`` in the game files.

----

.. _doc_item_asset_gun:damage_falloff_max_range:

Damage_Falloff_Max_Range :ref:`float32 <doc_data_builtin_types>` ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Percentage of maximum range where damage stops decreasing. For example, a max falloff range value of ``0.6`` with a range of ``200`` means damage stops dropping off after 120 meters.

----

.. _doc_item_asset_gun:damage_falloff_multiplier:

Damage_Falloff_Multiplier :ref:`float32 <doc_data_builtin_types>` ``1``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Percentage of damage to apply at maximum range. For example, a falloff multiplier value of ``0.25`` with a damage value of ``40`` means 10 damage will be dealt at maximum range.

----

.. _doc_item_asset_gun:damage_falloff_range:

Damage_Falloff_Range :ref:`float32 <doc_data_builtin_types>` ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Percentage of maximum range where damage begins decreasing. For example, a falloff range value of ``0.3`` with a range value of ``200`` means damage begins dropping off after 60 meters.

----

.. _doc_item_asset_gun:delete_empty_magazines:

Delete_Empty_Magazines :ref:`flag <doc_data_flag>`
::::::::::::::::::::::::::::::::::::::::::::::::::

.. deprecated:: 3.30.3.0
   Use ``Should_Delete_Empty_Magazines`` instead.

When this flag is included, the attached magazine attachment is deleted when fully depleted.

----

.. _doc_item_asset_gun:explosion:

Explosion :ref:`doc_data_guid` or :ref:`uint16 <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

GUID or legacy ID of the effect that should be used for explosions caused by ``Action Rocket`` projectiles.

----

.. _doc_item_asset_gun:fire_delay_seconds:

Fire_Delay_Seconds :ref:`int32 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Delay before the weapon is actually fired, in seconds.

----

.. _doc_item_asset_gun:firerate:

Firerate :ref:`uint8 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::

The value of this property affects the minimum number of ticks between the firing of consecutive shots. A higher ``Firerate`` value will cause the weapon to have a slower rate of a fire. The weapon's rate of fire can be calculated with ``50 ÷ (Firerate + 1)``, as the rounds per second.

----

.. _doc_item_asset_gun:grip:

Grip :ref:`uint16 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::

Legacy ID of a grip attachment that should be attached by default. The ``Hook_Grip`` flag is not required to use this property.

----

.. _doc_item_asset_gun:gunshot_rolloff_distance:

Gunshot_Rolloff_Distance :ref:`float32 <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Distance over which the gunshot audio rolls off until it is completely inaudible, in meters. Defaults to ``16`` when using ``Action String``; defaults to ``64`` when using ``Action Rocket``; otherwise, defaults to ``512``.

----

.. _doc_item_asset_gun:hammer_time:

Hammer_Time :ref:`float32 <doc_data_builtin_types>` ``1``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on the time it takes to pull back the hammer a ranged weapon after firing. This does not affect the actual animation speed, but the cooldown before the player can perform other actions (such as shooting) again. Values less than ``1`` have no effect.

----

.. _doc_item_asset_gun:hook_barrel:

Hook_Barrel :ref:`flag <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::

When this flag is included, the ranged weapon has a barrel attachment slot.

----

.. _doc_item_asset_gun:hook_grip:

Hook_Grip :ref:`flag <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::

When this flag is included, the ranged weapon has a grip attachment slot.

----

.. _doc_item_asset_gun:hook_sight:

Hook_Sight :ref:`flag <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::

When this flag is included, the ranged weapon has a sight attachment slot.

----

.. _doc_item_asset_gun:hook_tactical:

Hook_Tactical :ref:`flag <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::

When this flag is included, the ranged weapon has a tactical attachment slot.

----

.. _doc_item_asset_gun:infinite_ammo:

Infinite_Ammo :ref:`bool <doc_data_builtin_types>` ``false``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

When ``true``, ammunition is not depleted from the magazine attachment. This allows for the weapon to have infinite ammo, so long as a magazine attachment with a number of rounds remaining equal to ``Ammo_Per_Shot`` is attached.

----

.. _doc_item_asset_gun:instakill_headshots:

Instakill_Headshots :ref:`bool <doc_data_builtin_types>` ``false``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If ``true``, a player that is headshot with this weapon is instantly killed. This does not affect zombies, unless the world's difficulty configuration has the ``Weapons_Use_Player_Damage`` setting enabled.

----

.. _doc_item_asset_gun:jam_max_chance:

Jam_Max_Chance :ref:`float32 <doc_data_builtin_types>` ``0.1``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Decimal-to-percent chance for jamming to occur. This property requires ``Can_Ever_Jam``.

----

.. _doc_item_asset_gun:jam_quality_threshold:

Jam_Quality_Threshold :ref:`float32 <doc_data_builtin_types>` ``0.4``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

The maximum threshold for when jamming can occur. This value is a decimal-to-percent representation of the item's quality value. For example, a threshold of ``0.4`` allows jamming to start occuring at 40% item quality. This property requires ``Can_Ever_Jam``.

----

.. _doc_item_asset_gun:magazine:

Magazine :ref:`uint16 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::

Legacy ID of a magazine attachment that should be attached by default.

----

.. _doc_item_asset_gun:magazine_caliber_#:

Magazine_Caliber_# :ref:`uint16 <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Legacy ID of a caliber to check for magazine attachment compatibility. This property is used in conjunction with ``Magazine_Calibers``, which determines how many instances of this property should be read by the game.

When this property is unset, it will default to ``0``. When the ``Magazine_Calibers`` property is not greater than ``0``, this property will default to the value of ``Caliber``.

----

.. _doc_item_asset_gun:magazine_calibers:

Magazine_Calibers :ref:`int32 <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::

Set the length of the array containing the calibers for magazine attachment compatibility. This property is used in conjunction with the ``Magazine_Caliber_#`` property, and the value of ``Magazine_Calibers`` should be equal to the number of instances of ``Magazine_Caliber_#``.

When this property is not greater than ``0`` – it will default to ``1``, and the ``Magazine_Caliber_#`` property can no longer be customized.

This property is often used alongside ``Attachment_Calibers``, but this is optional.

----

.. _doc_item_asset_gun:magazine_replacement_#_id:

Magazine_Replacement_#_ID :ref:`uint16 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Legacy ID of a magazine attachment that should be used as an alternative default when certain condition(s) are met. This property is used in conjunction with ``Magazine_Replacements``, which determines how many instances of this property should be read by the game.

----

.. _doc_item_asset_gun:magazine_replacement_#_map:

Magazine_Replacement_#_Map :ref:`string <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

This value should be the name of a map. When the weapon spawns on this map, this condition has been met. This property requires ``Magazine_Replacement_#_ID``.

----

.. _doc_item_asset_gun:magazine_replacements:

Magazine_Replacements :ref:`int <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

``Magazine_Replacements`` and its related properties are used to add alternative magazine attachments that should be used as the weapon's default when certain condition(s) are met.

This value sets the length of the array containing any alternative default magazine attachments. This property is used in conjunction with the ``Magazine_Replacement_#_ID`` property, and the value of ``Magazine_Replacements`` should be equal to the number of instances of ``Magazine_Replacement_#_ID``.

----

.. _doc_item_asset_gun:muzzle:

Muzzle :ref:`doc_data_guid` or :ref:`uint16 <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

GUID or legacy ID of the effect to play after shooting. This is emitted from the ranged weapon's "Barrel" GameObject.

----

.. _doc_item_asset_gun:projectile_explosion_launch_speed:

Projectile_Explosion_Launch_Speed :ref:`float32 <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Players caught within the area-of-effect explosion caused by a *physics projectile* weapon are launched at this speed. For example, this can be used to create velocity-related items like "rocket-jumping" mods. Defaults to ``Player_Damage × 0.1``.

----

.. _doc_item_asset_gun:projectile_lifespan:

Projectile_Lifespan :ref:`float32 <doc_data_builtin_types>` ``30``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Lifespan of *physics projectiles*, in seconds. After this much time elapses, the projectile despawns.

----

.. _doc_item_asset_gun:projectile_penetrate_buildables:

Projectile_Penetrate_Buildables :ref:`flag <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

The area-of-effect explosions caused by *physics projectiles* penetrate through buildables when this flag is set.

----

.. _doc_item_asset_gun:range_rangefinder:

Range_Rangefinder :ref:`float32 <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Overrides the maximum distance displayed when using a "Rangefinder" tactical attachment on this weapon. For example, it may be useful to set this property when using ``Action Rocket``, as explosive projectiles use ``Range`` to determine the explosion radius rather than the maximum range of the weapon. Defaults to the value of the ``Range`` property.

----

.. _doc_item_asset_gun:recoil_crouch:

Recoil_Crouch :ref:`float32 <doc_data_builtin_types>` ``0.85``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on camera recoil while crouched.

----

.. _doc_item_asset_gun:recoil_max_x:

Recoil_Max_X :ref:`float32 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Maximum horizontal camera recoil in degrees. This property is used in conjunction with ``Recoil_Min_Y``.

----

.. _doc_item_asset_gun:recoil_max_y:

Recoil_Max_Y :ref:`float32 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Maximum vertical camera recoil in degrees. This property is used in conjunction with ``Recoil_Min_X``.

----

.. _doc_item_asset_gun:recoil_min_x:

Recoil_Min_X :ref:`float32 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Minimum horizontal camera recoil in degrees. This property is used in conjunction with ``Recoil_Max_X``.

----

.. _doc_item_asset_gun:recoil_min_y:

Recoil_Min_Y :ref:`float32 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Minimum vertical camera recoil in degrees. This property is used in conjunction with ``Recoil_Max_Y``.

----

.. _doc_item_asset_gun:recoil_prone:

Recoil_Prone :ref:`float32 <doc_data_builtin_types>` ``0.7``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on camera recoil while prone.

----

.. _doc_item_asset_gun:recoil_sprint:

Recoil_Sprint :ref:`float32 <doc_data_builtin_types>` ``1.25``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on camera recoil while sprinting. This property is not relevant unless ``Can_Aim_During_Sprint`` has been set to ``true``.

----

.. _doc_item_asset_gun:recoil_swimming:

Recoil_Swimming :ref:`float32 <doc_data_builtin_types>` ``1.1``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on camera recoil while swimming.

----

.. _doc_item_asset_gun:recover_x:

Recover_X :ref:`float32 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on camera degrees to be counter-animated horizontally over the next 250 milliseconds.

----

.. _doc_item_asset_gun:recover_y:

Recover_Y :ref:`float32 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on camera degrees to be counter-animated vertically over the next 250 milliseconds.

----

.. _doc_item_asset_gun:reload_time:

Reload_Time :ref:`float32 <doc_data_builtin_types>` ``1``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on time it takes to finish reloading the ranged weapon. This does not affect the actual animation speed, but the cooldown before the player can perform other actions (such as shooting) again. Values less than ``1`` have no effect.

----

.. _doc_item_asset_gun:replace:

Replace :ref:`float32 <doc_data_builtin_types>` ``1``
:::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier of the reload animation length before the magazine is respawned. This does not affect the actual animation speed, but the cooldown before the player can perform other actions (such as shooting) again. Values less than ``0.01`` have no effect.

----

.. _doc_item_asset_gun:requires_nonzero_attachment_caliber:

Requires_NonZero_Attachment_Caliber :ref:`bool <doc_data_builtin_types>` ``false``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If ``true``, attachments must specify at least one non-zero (``0``) caliber ID to be compatible. For example, this can be used to make most vanilla attachments (like the Tactical Laser, Dot Sight, and Vertical Grip) incompatible with this weapon.

----

.. _doc_item_asset_gun:safety:

Safety :ref:`flag <doc_data_flag>`
::::::::::::::::::::::::::::::::::

The weapon has a safety firing mode.

----

.. _doc_item_asset_gun:scale_aim_animation_speed:

Scale_Aim_Animation_Speed :ref:`bool <doc_data_builtin_types>` ``true``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

When true, the length of the "Aim_Start" and "Aim_Stop" animations are scaled to match ``Aim_In_Duration`` (with modifiers).

----

.. _doc_item_asset_gun:semi:

Semi :ref:`flag <doc_data_flag>`
::::::::::::::::::::::::::::::::

The weapon has a semi-automatic firing mode.

----

.. _doc_item_asset_gun:shake_max_x:

Shake_Max_X :ref:`float32 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Maximum 𝘟-axis model shake caused from firing the weapon.

----

.. _doc_item_asset_gun:shake_min_x:

Shake_Min_X :ref:`float32 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Minimum 𝘟-axis model shake caused from firing the weapon.

----

.. _doc_item_asset_gun:shake_max_y:

Shake_Max_Y :ref:`float32 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Maximum 𝘠-axis model shake caused from firing the weapon.

----

.. _doc_item_asset_gun:shake_min_y:

Shake_Min_Y :ref:`float32 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Minimum 𝘠-axis model shake caused from firing the weapon.

----

.. _doc_item_asset_gun:shake_max_z:

Shake_Max_Z :ref:`float32 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Maximum 𝘡-axis model shake caused from firing the weapon.

----

.. _doc_item_asset_gun:shake_min_z:

Shake_Min_Z :ref:`float32 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Minimum 𝘡-axis model shake caused from firing the weapon.

----

.. _doc_item_asset_gun:shell:

Shell :ref:`doc_data_guid` or :ref:`uint16 <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

GUID or legacy ID of the effect to play after shooting, emitted from the ranged weapon's "Eject" GameObject. Defaults to ``33`` when using either ``Action Pump`` or ``Action Break``; defaults to ``1`` when using any other ``Action`` key-value pair except for ``Action Rail``; otherwise, defaults to ``0``.

----

.. _doc_item_asset_gun:should_delete_empty_magazines:

Should_Delete_Empty_Magazines :ref:`bool <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Overrides how empty magazines are handled by the action item mode. When set to ``true``, empty magazine attachments are deleted when completely emptied. The default behavior depends on the configuration of the ``Action`` property.

Defaults to ``true`` when using one of the following ``Action`` enumerators: ``Break``, ``Pump``, ``Rail``, ``Rocket``, or ``String``. Otherwise, defaults to ``false``.

----

.. _doc_item_asset_gun:sight:

Sight :ref:`uint16 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::

Legacy ID of a sight attachment that should be attached by default. The ``Hook_Sight`` flag is not required to use this property.

----

.. _doc_item_asset_gun:spread_aim:

Spread_Aim :ref:`float32 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on the bullet spread while aiming down sights. This is multiplied by the ``Spread_Angle_Degrees`` value.

----

.. _doc_item_asset_gun:spread_angle_degrees:

Spread_Angle_Degrees :ref:`float32 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Bullet angle of deviation away from the aiming direction. For example, ``15`` means the shot could hit up to 15 degrees away from the center of the crosshair, whereas ``0`` will always hit the center of the crosshair. All other spread values are multipliers for this.

----

.. _doc_item_asset_gun:spread_crouch:

Spread_Crouch :ref:`float32 <doc_data_builtin_types>` ``0.85``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on the bullet spread while crouched.

----

.. _doc_item_asset_gun:spread_hip:

Spread_Hip :ref:`float32 <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::

.. deprecated:: 3.22.20.0
   Use ``Spread_Angle_Degrees`` instead.

Maintained for backwards compatibility. Running the game with the ``-ValidateAssets`` :ref:`launch option <doc_launch_options>` will log the equivalent ``Spread_Angle_Degrees`` value.

----

.. _doc_item_asset_gun:spread_prone:

Spread_Prone :ref:`float32 <doc_data_builtin_types>` ``0.7``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on the bullet spread while prone.

----

.. _doc_item_asset_gun:spread_sprint:

Spread_Sprint :ref:`float32 <doc_data_builtin_types>` ``1.25``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on the bullet spread while sprinting.

----

.. _doc_item_asset_gun:spread_swimming:

Spread_Swimming :ref:`float32 <doc_data_builtin_types>` ``1.1``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on the bullet spread while swimming.

----

.. _doc_item_asset_gun:tactical:

Tactical :ref:`uint16 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::

Legacy ID of a tactical attachment that should be attached by default. The ``Hook_Tactical`` flag is not required to use this property.

----

.. _doc_item_asset_gun:turret:

Turret :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::::::::::::

This weapon should be treated as a vehicular turret. This flag affects the player's first-person viewmodel while the weapon is held.

----

.. _doc_item_asset_gun:unjam_chamber_anim:

Unjam_Chamber_Anim :ref:`string <doc_data_builtin_types>` ``UnjamChamber``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Name of an animation clip to play when unjamming the weapon. This property requires ``Can_Ever_Jam``.

----

.. _doc_item_asset_gun:unplace:

Unplace :ref:`float32 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier of the reload animation length before the magazine is despawned. This does not affect the actual animation speed, but the cooldown before the player can perform other actions (such as shooting) again.

NPC Rewards
-----------

Gun assets can use quest rewards. For example, every time the ranged weapon is fired an item could be spawned in the player's inventory. Alternatively, shooting the ranged weapon may be required to complete a quest. For more information, refer to the :ref:`Rewards <doc_npc_asset_rewards>` documentation.

These rewards are prefixed with ``Shoot_Quest_``. For example, ``Shoot_Quest_Rewards 1``.

Understanding Projectile Systems
--------------------------------

All ranged weapons utilize one of two projectile systems: the *ballistic projectile system*, or the *physics projectile system*. This is determined based on the :ref:`Action <doc_item_asset_gun:action>` the weapon has been configured to use, although most weapons use the ballistic projectile system.

Ballistic projectiles use a deterministic simulation. Their travel time, bullet drop, and other characteristics can be configured with properties such as :ref:`Ballistic_Travel <doc_item_asset_gun:ballistic_travel>` and :ref:`Bullet_Gravity_Multiplier <doc_item_asset_gun:bullet_gravity_multiplier>`. When the ballistics game mechanic is disabled, these weapons function as hitscan instead.

Physics projectiles use Unity's physics simulation. Unlike ballistic projectiles, these are not deterministic. Additionally, physics projectiles cause area-of-effect explosions upon impact. The characteristics of physics projectiles can be configured with properties such as :ref:`Ballistic_Force <doc_item_asset_gun:ballistic_force>` and :ref:`Projectile_Explosion_Launch_Speed <doc_item_asset_gun:projectile_explosion_launch_speed>`.
