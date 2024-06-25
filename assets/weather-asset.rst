.. _doc_assets_weather:

Weather Assets
==============

Overrides the built-in snow and rain weather with custom events. This is feature is a work-in-progress.

Random weather can be scheduled to occur naturally on a map with the ``Weather_Types`` property of the :ref:`Level Asset <doc_assets_level>`.

How to test?
------------

When a GUID is passed to the weather command it will start a custom weather event, and 0 can be used to end it.

.. code-block:: shell
	
	/weather 819982d7a2b6453488a8c4c5d9efe67f

Properties Reference
--------------------

**Type** *string*: ``SDG.Unturned.WeatherAsset``

**Volume_Mask** :ref:`u32 Mask <doc_data_bitmask>`: Only enabled while inside an ambience volume with non-zero bitwise AND result. Defaults to 0xFFFFFFFF.

**Fade_In_Duration** *float*: Seconds between weather event starting and reaching full intensity.

**Fade_Out_Duration** *float*: Seconds between weather event ending and reaching zero intensity.

**Ambient_Audio_Clip** :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`: Audio clip to play globally. Volume matches intensity.

**Override_Fog** *bool*: Should fog configured in the lighting be overridden?

**Override_Atmospheric_Fog** *bool*: Should fog affect the skybox?

**Shadow_Strength_Multiplier** *float*: Directional light shadow strength multiplier.

**Fog_Blend_Exponent** *float*: Power applied to fog blending alpha.

**Cloud_Blend_Exponent** *float*: Power applied to cloud blending alpha.

**Wind_Main** *float*: Wind zone windMain value. Will be replaced by more configurable game-specific wind eventually.

**Dawn**, **Midday**, **Dusk** and **Midnight**: Refer to the ":ref:`Time of Day <doc_assets_weather:time_of_day>`" section.

**Effects** *array*: Refer to the ":ref:`Effects <doc_assets_weather:effects>`" section.

**Stamina_Per_Second** *float*: Stamina +/- buff.

**Health_Per_Second** *float*: Health +/- buff.

**Food_Per_Second** *float*: Food +/- buff.

**Water_Per_Second** *float*: Water +/- buff.

**Virus_Per_Second** *float*: Virus +/- buff.

**Has_Lightning** *bool*: If true, lightning will be enabled for this weather type. In the future this should get cleaned up, but for now it is hardcoded for assigning a net id.

**Min_Lightning_Interval** *float*: Minimum seconds between lightning strikes.

**Max_Lightning_Interval** *float*: Maximum seconds between lightning strikes.

.. _doc_assets_weather:time_of_day:

Time of Day Properties
----------------------

Each of the four main times of day can override certain properties.

**Fog_Color** *struct*: Distance-based fog. Optionally overrides the skybox color. Refer to the ":ref:`Color <doc_assets_weather:color>`" section.

**Fog_Density** *float*: Functions similarly to fog intensity in ambiance volume. Value must be within [0, 1].

**Cloud_Color** *struct*: Inner body of cloud. Refer to the ":ref:`Color <doc_assets_weather:color>`" section.

**Cloud_Rim_Color** *struct*: Outer edge of cloud. More visible than inner color. Refer to the ":ref:`Color <doc_assets_weather:color>`" section.

**Brightness_Multiplier** *float*: All ambient lighting colors are multiplied by this.

.. _doc_assets_weather:effects:

Effect Properties
-----------------

Multiple effects can be instantiated while the weather is active.

**Prefab** :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`: Game object with a particle system. PlayOnAwake should be disabled. For effects tied to the view it may be helpful to change the culling mode to "Always Simulate".

**Emission_Exponent** *float*: Power applied to weather intensity multiplied by default constant rate over time.

**Pitch** *float*: X-axis rotation when ``Rotate_Yaw_With_Wind`` is enabled.

**Translate_With_View** *bool*: Should position in world-space match the camera? The built-in snow and rain move with the view. Position is zeroed when false. May be useful for transition effects like dust blowing into the map signaling the start of a sandstorm.

**Rotate_Yaw_With_Wind** *bool*: Should y-axis rotation match the wind direction? The built-in snow and rain rotate with wind.

.. _doc_assets_weather:color:

Color Properties
----------------

Each color can use a custom override, or a color from the level editor lighting panel. Using a level color is primarily for rain and snow backwards compatibility.

**Level_Enum** *enum*: If set, then the RGB specified are multiplied by this color.

**R**, **G**, **B** *uint8*: Color channel values.

NPC Conditions
--------------

Global weather state and current weather intensity blend can be tested through NPC conditions. Refer to :ref:`Conditions <doc_npc_asset_conditions>` documentation for documentation.
