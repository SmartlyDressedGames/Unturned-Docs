.. _doc_item_asset_clothing:

Clothing Assets
===============

The ItemClothingAsset class is a base class that other classes are derived from. It is unusable on its own.

Items that use a class derived from this class are known as clothing items. Clothing can be worn by players and zombies, although they may function slightly differently between the two.

Game Data File
--------------

The ItemClothingAsset class inherits properties from the :ref:`ItemAsset <doc_item_asset_intro>` class. Clothing items will always display a quality value.

Properties
``````````

.. list-table::
   :widths: 40 40 20
   :header-rows: 1
   
   * - Property Name
     - Type
     - Default Value
   * - :ref:`Armor <doc_item_asset_clothing:armor>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Armor_Explosion <doc_item_asset_clothing:armor_explosion>`
     - :ref:`float32 <doc_data_builtin_types>`
     - See description
   * - :ref:`Beard_Visible <doc_item_asset_clothing:beard_visible>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - :ref:`Destroy_Clothing_Colliders <doc_item_asset_clothing:destroy_clothing_colliders>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - :ref:`Falling_Damage_Multiplier <doc_item_asset_clothing:falling_damage_multiplier>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Hair_Visible <doc_item_asset_clothing:hair_visible>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - :ref:`Mirror_Left_Handed_Model <doc_item_asset_clothing:mirror_left_handed_model>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - :ref:`Movement_Speed_Multiplier <doc_item_asset_clothing:movement_speed_multiplier>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Prevents_Falling_Broken_Bones <doc_item_asset_clothing:prevents_falling_broken_bones>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``false``
   * - :ref:`Priority_Over_Cosmetic <doc_item_asset_clothing:priority_over_cosmetic>`
     - :ref:`bool <doc_data_builtin_types>`
     - See description
   * - :ref:`Proof_Fire <doc_item_asset_clothing:proof_fire>`
     - :ref:`flag <doc_data_flag>`
     - 
   * - :ref:`Proof_Radiation <doc_item_asset_clothing:proof_radiation>`
     - :ref:`flag <doc_data_flag>`
     - 
   * - :ref:`Proof_Water <doc_item_asset_clothing:proof_water>`
     - :ref:`flag <doc_data_flag>`
     - 
   * - :ref:`Skin_Override <doc_item_asset_clothing:skin_override>`
     - :ref:`string <doc_data_builtin_types>`
     - 
   * - :ref:`Visible_On_Ragdoll <doc_item_asset_clothing:visible_on_ragdoll>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - :ref:`WearAudio <doc_item_asset_clothing:wear_audio>`
     - :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`
     - See description

Property Descriptions
`````````````````````

.. _doc_item_asset_clothing:armor:

Armor :ref:`float32 <doc_data_builtin_types>` ``1``
:::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on damage received to the covered body part(s). The affected body part(s) will differ depending on the child class.

----

.. _doc_item_asset_clothing:armor_explosion:

Armor_Explosion :ref:`float32 <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on the damage received from area-of-effect explosions. Defaults to the value of ``Armor``.

----

.. _doc_item_asset_clothing:beard_visible:

Beard_Visible :ref:`bool <doc_data_builtin_types>` ``true``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

When ``true``, the character's facial hair should be visible (unless disabled by some other condition).

----

.. _doc_item_asset_clothing:destroy_clothing_colliders:

Destroy_Clothing_Colliders :ref:`bool <doc_data_builtin_types>` ``true``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

When ``false``, colliders are *not* destroyed when the clothing is attached to the player character. For example, equipped vanilla clothing do not have any colliders. But some mods (e.g., armor with a hitbox) may have relied on child colliders not being destroyed.

----

.. _doc_item_asset_clothing:falling_damage_multiplier:

Falling_Damage_Multiplier :ref:`float32 <doc_data_builtin_types>` ``1``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on damage received from falling.

----

.. _doc_item_asset_clothing:hair_visible:

Hair_Visible :ref:`bool <doc_data_builtin_types>` ``true``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

When ``true``, the character's hair should be visible (unless disabled by some other condition).

----

.. _doc_item_asset_clothing:mirror_left_handed_model:

Mirror_Left_Handed_Model :ref:`bool <doc_data_builtin_types>` ``true``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Clothing should be mirrored when the player is using the left-handed setting. This property only affects 3D clothing items, being: vests, backpacks, masks, glasses, and hats.

----

.. _doc_item_asset_clothing:movement_speed_multiplier:

Movement_Speed_Multiplier :ref:`float32 <doc_data_builtin_types>` ``1``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on movement speed.


----

.. _doc_item_asset_clothing:prevents_falling_broken_bones:

Prevents_Falling_Broken_Bones :ref:`bool <doc_data_builtin_types>` ``false``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

When ``true``, the player will never receive the Broken Bones debuff from falling.

----

.. _doc_item_asset_clothing:priority_over_cosmetic:

Priority_Over_Cosmetic :ref:`bool <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

This property can be set to override the default cosmetic override behavior. The default behavior will differ depending on the asset. For most assets, cosmetics are displayed over clothing. For glasses using the ``Vision`` property, the clothing item has priority over the cosmetic.

----

.. _doc_item_asset_clothing:proof_fire:

Proof_Fire :ref:`flag <doc_data_flag>`
::::::::::::::::::::::::::::::::::::::

When this flag is included, this clothing item is considered fireproof. When a fireproof shirt and fireproof pants are worn together, the player becomes immune to fire damage. This property has no effect on other clothing types.

----

.. _doc_item_asset_clothing:proof_radiation:

Proof_Radiation :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::::::::::::

When this flag is included, this clothing item is considered radiation-proof. When a radiation-proof mask is worn, the player will not be affected by standard deadzones. When radiation-proof pants, a radiation-proof shirt, and a radiation-proof mask are all worn together, the player will not be damaged by full-suit deadzones. This protection only lasts for as long as the radiation-proof mask's item quality is greater than 0%. The mask's quality will deplete over time while inside of a deadzone, but can be replenished with :ref:`radiation filters <doc_item_asset_filter>`.

----

.. _doc_item_asset_clothing:proof_water:

Proof_Water :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::::::::

When this flag is included, this clothing item is considered waterproof. When waterproof glasses are worn, the player's screen is no longer blurred when underwater. When waterproof glasses and a waterproof backpack are worn together, the player's oxygen will deplete at a greatly reduced rate while underwater. This property has no effect on other clothing types.

----

.. _doc_item_asset_clothing:skin_override:

Skin_Override :ref:`string <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::::

Optional name of a renderer that should use the player's skin material. For example, the `Conflicting Conscience <https://unturned.wiki.gg/wiki/Conflicting_Conscience>`_ cosmetic adds miniature versions of the player sitting on their shoulder. 

----

.. _doc_item_asset_clothing:visible_on_ragdoll:

Visible_On_Ragdoll :ref:`bool <doc_data_builtin_types>` ``true``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

When ``true``, this clothing item should be visible on ragdolls.

----

.. _doc_item_asset_clothing:wear_audio:

WearAudio :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

AudioClip or OneShotAudioDefinition to play upon equipping this clothing item. Default value is dependent on the child asset. Backpacks and vests will use ``Sounds/Zipper.mp3`` by default. Otherwise, ``Sounds/Sleeve.mp3`` is used.