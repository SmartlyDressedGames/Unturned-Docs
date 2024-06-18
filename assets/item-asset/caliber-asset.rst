.. _doc_item_asset_caliber:

Caliber Assets
==============

The ItemCaliberAsset class is a base class that other classes are derived from. It is unusable on its own.

Game Data File
--------------

The ItemCaliberAsset class inherits properties from the :ref:`ItemAsset <doc_item_asset_intro>` class.

Properties
``````````

.. list-table::
   :widths: 40 40 20
   :header-rows: 1
   
   * - Property Name
     - Type
     - Default Value
   * - :ref:`Aiming_Movement_Speed_Multiplier <doc_item_asset_caliber:aiming_movement_speed_multiplier>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Aiming_Recoil_Multiplier <doc_item_asset_caliber:aiming_recoil_multiplier>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Aim_Duration_Multiplier <doc_item_asset_caliber:aim_duration_multiplier>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Ballistic_Damage_Multiplier <doc_item_asset_caliber:ballistic_damage_multiplier>`
     - :ref:`float32 <doc_data_builtin_types>`
     - See description
   * - :ref:`Calibers <doc_item_asset_caliber:calibers>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Caliber_# <doc_item_asset_caliber:caliber_#>`
     - :ref:`uint16 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Damage <doc_item_asset_caliber:damage>`
     - :ref:`float32 <doc_data_builtin_types>`
     - *deprecated*
   * - :ref:`Destroy_Attachment_Colliders <doc_item_asset_caliber:destroy_attachment_colliders>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - :ref:`Firerate <doc_item_asset_caliber:firerate>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Instantiated_Attachment_Name_Override <doc_item_asset_caliber:instantiated_attachment_name_override>`
     - :ref:`string <doc_data_builtin_types>`
     - See description
   * - :ref:`Paintable <doc_item_asset_caliber:paintable>`
     - :ref:`flag <doc_data_flag>`
     -
   * - :ref:`Recoil_X <doc_item_asset_caliber:recoil_x>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Recoil_Y <doc_item_asset_caliber:recoil_y>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Shake <doc_item_asset_caliber:shake>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Spread <doc_item_asset_caliber:spread>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Sway <doc_item_asset_caliber:sway>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1``

Property Descriptions
`````````````````````

.. _doc_item_asset_caliber:aiming_movement_speed_multiplier:

Aiming_Movement_Speed_Multiplier :ref:`float32 <doc_data_builtin_types>` ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on character movement speed while aiming down sights.

----

.. _doc_item_asset_caliber:aiming_recoil_multiplier:

Aiming_Recoil_Multiplier :ref:`float32 <doc_data_builtin_types>` ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on recoil magnitude while aiming down sights.

----

.. _doc_item_asset_caliber:aim_duration_multiplier:

Aim_Duration_Multiplier :ref:`float32 <doc_data_builtin_types>` ``1``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on the value of :ref:`Aim_In_Duration <doc_item_asset_gun:aim_in_duration>` property available to the :ref:`ItemGunAsset <doc_item_asset_gun>` class.

----

.. _doc_item_asset_caliber:ballistic_damage_multiplier:

Ballistic_Damage_Multiplier :ref:`float32 <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on damage. Defaults to the value of the ``Damage`` property, or ``1`` if both properties are unset.

----

.. _doc_item_asset_caliber:caliber_#:

Caliber_# :ref:`uint16 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::

Legacy ID of a caliber to check for attachment compatibility. This property is used in conjunction with ``Calibers``, which determines how many instances of this property should be read by the game.

When this property is unset, it will default to ``0``. When the ``Magazine_Calibers`` property is not greater than ``0``, this property will default to the value of ``Caliber``.

----

.. _doc_item_asset_caliber:calibers:

Calibers :ref:`uint8 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::

Set the length of the array containing the calibers for attachment compatibility. This property is used in conjunction with the ``Caliber_#`` property, and the value of ``Calibers`` should be equal to the number of instances of ``Caliber_#``.

----

.. _doc_item_asset_caliber:damage:

Damage :ref:`float32 <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::

.. deprecated:: 3.27.0.0
   Use ``Ballistic_Damage_Multiplier`` instead.

Maintained for backwards compatibility. If both this property and ``Ballistic_Damage_Multiplier`` have been set, the latter's value is used.

----

.. _doc_item_asset_caliber:destroy_attachment_colliders:

Destroy_Attachment_Colliders :ref:`bool <doc_data_builtin_types>` ``true``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

When ``false``, colliders are not destroyed when the attached ranged weapon's colliders are destroyed. This property exists for backwards compatibility with mods that may have relied on attachments having colliders, but using this property is not recommended.

.. caution:: Mods with complex colliders on their custom attachments are frequently reported as causing low performance issues for players. It is recommended that your custom attachments do not rely on having colliders.

----

.. _doc_item_asset_caliber:firerate:

Firerate :ref:`uint8 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::

The value of the attached ranged weapon's :ref:`Firerate <doc_item_asset_gun:firerate>` property is reduced by the value of this property. A larger decrease will allow for the ranged weapon to fire more often.

----

.. _doc_item_asset_caliber:instantiated_attachment_name_override:

Instantiated_Attachment_Name_Override :ref:`string <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Name to use when instantiating attachment prefab. By default, the value of ``GUID`` is used. Since Unity's built-in Animation component references GameObjects by name, this property can help share animations between items.

For example, a magazine attachment with GUID ``dbfb1d0d11ca438e9dffb95f76e61274`` will instantiate Magazine.prefab as (Gun)/Magazine/dbfb1d0d11ca438e9dffb95f76e61274 by default. With ``Instantiated_Attachment_Name_Override`` set to "Example" it would instead spawn as (Gun)/Magazine/Example.

----

.. _doc_item_asset_caliber:paintable:

Paintable :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::::::

When this flag is included, the attachment should be affected by Steam Economy skins that include support for skinning attachments.

----

.. _doc_item_asset_caliber:recoil_x:

Recoil_X :ref:`float32 <doc_data_builtin_types>` ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on horizontal recoil.

----

.. _doc_item_asset_caliber:recoil_y:

Recoil_Y :ref:`float32 <doc_data_builtin_types>` ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on vertical recoil.

----

.. _doc_item_asset_caliber:shake:

Shake :ref:`float32 <doc_data_builtin_types>` ``1``
:::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on shake.

----

.. _doc_item_asset_caliber:spread:

Spread :ref:`float32 <doc_data_builtin_types>` ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on bullet spread.

----

.. _doc_item_asset_caliber:sway:

Sway :ref:`float32 <doc_data_builtin_types>` ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on scope sway.