.. _doc_item_asset_melee:

Melee Assets
============

Melee weapons can be used as a source of damage. Melee weapons always show quality.

This inherits the :ref:`WeaponAsset <doc_item_asset_weapon>` class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Melee``)

**Useable** *enum* (``Melee``)

**Slot** *enum* (``Primary``, ``Secondary``, ``Tertiary``, ``Any``)

**ID** *uint16*: Must be a unique identifier.

Melee Asset Properties
----------------------

**Alert_Radius** *float*: The radius where zombies and animals should be alerted when attacking, measured in meters. Defaults to 8.

**AttackAudioClip** :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`: AudioClip to play when attacking.

**ImpactAudioDef** :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`: AudioClip or OneShotAudioDefinition to play upon impact.

**Light** *flag*: Provides a toggleable flashlight, and allows for using :ref:`PlayerSpotLightConfig <doc_data_playerspotlightconfig>` properties. 

**Repair** *flag*: Repairs barricades, structures, and vehicles.

**Repeated** *flag*: The melee weapon's strong attack is disabled, and its weak attack will deal damage continuously.

**Stamina** *byte*: Amount of stamina depleted with each attack. Defaults to 0.

**Strength** *float*: Multiplier on the damage dealt by strong attacks.

**Strong** *float*: Multiplier for the strong attack animation length, for when to apply damage. Defaults to 0.33.

**Weak** *float*: Multiplier for the weak attack animation length, for when to apply damage. Defaults to 0.5.