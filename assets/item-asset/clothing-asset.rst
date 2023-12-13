.. _doc_item_asset_clothing:

Clothing Assets
===============

Clothing can be worn by players and zombies. Clothing items always show quality.

This inherits the :ref:`ItemAsset <doc_item_asset_intro>` class.

Clothing Asset Properties
-------------------------

**Armor** *float*: Multiplier on damage received. Defaults to 1.

**Armor_Explosion** *float*: Multiplier on damage received from area-of-effect explosions. Defaults to the value used for Armor.

**Destroy_Clothing_Colliders** *bool*: If false, colliders are not destroyed when the clothing is attached to the character. For example equipped vanilla clothes do not have any colliders, but some mods (e.g., armor with hitbox) may have relied on child colliders not being destroyed. Defaults to true.

**Falling_Damage_Multiplier** *float*: Multiplier on damage received from falling. Defaults to 1.

**Prevents_Falling_Broken_Bones** *bool*: If true on any worn clothing item, bones never break when falling. Defaults to false.

**Priority_Over_Cosmetic** *bool*: If set, overrides the default cosmetic override behavior. By default, night vision goggles and headlamps take priority over cosmetics in the same slot. If true, the in-game item is shown rather than a cosmetic in the same slot.

**Proof_Water** *flag*: Specified if it should exhibit the waterproof property. Only applicable to backpacks and glasses. When waterproof glasses are worn, the player will not have their screen blurred while underwater. When a waterproof backpack and waterproof glasses are worn together, the player's oxygen will deplete at a greatly reduced rate when underwater.

**Proof_Fire** *flag*: Specified if it should exhibit the fireproof property. Only applicable to shirts and pants. When a fireproof shirt and fireproof pants are worn together, the player will be immune to fire damage.

**Proof_Radiation** *flag*: Specified if it should exhibit the radiation-proof property. Only applicable to pants, shirts, and masks. When a radiation-proof mask is worn, the player will not be damaged by standard deadzones. When radiation-proof pants, a radiation-proof shirt, and a radiation-proof mask are worn together, the player will not be damaged by full-suit deadzones. The protection only lasts for as long as the radiation-proof mask's item quality remains greater than 0%. The mask's quality will deplete over time while inside of a deadzone. :ref:`Radiation filters <doc_item_asset_filter>` can be used to replenish a radiation-proof mask's quality.

**Skin_Override** *string*: Optional name of a renderer that should use the player's skin material. For example, to create a miniature version of the player sitting on their shoulder.

**Mirror_Left_Handed_Model** *bool*: Clothing should be mirrored when the player is left-handed. Only applicable to vests, backpacks, masks, glasses, and hats. Defaults to true.

**Movement_Speed_Multiplier** *float*: Multiplier on movement speed. Defaults to 1.

**Hair_Visible** *bool*: Hair should be visible. Defaults to true.

**Beard_Visible** *bool*: Facial hair should be visible. Defaults to true.

**Visible_On_Ragdoll** *bool*: Should be visible on ragdolls. Defaults to true.

**WearAudio** :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`: AudioClip or OneShotAudioDefinition to play upon wearing.