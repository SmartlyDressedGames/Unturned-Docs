# Weather Asset

Overrides the built-in snow and rain weather with custom events. This is feature is a work-in-progress.

Random weather can be scheduled to occur naturally on a map with the `Weather_Types` property of the [Level Asset](LevelAsset.md).

This is an [Asset v2](AssetsV2.md) class.

## How to test?

When a GUID is passed to the weather command it will start a custom weather event, and 0 can be used to end it.

	/weather 819982d7a2b6453488a8c4c5d9efe67f

## Properties Reference

`Fade_In_Duration` *float*: seconds between weather event starting and reaching full intensity.

`Fade_Out_Duration` *float*: seconds between weather event ending and reaching zero intensity.

`Ambient_Audio_Clip` [Master Bundle Pointer](MasterBundlePtr.md): audio clip to play globally. Volume matches intensity.

`Override_Fog` *bool*: should fog configured in the lighting be overridden?

`Override_Atmospheric_Fog` *bool*: should fog affect the skybox?

`Dawn`, `Midday`, `Dusk` and `Midnight`: refer to the Time of Day section.

`Effects` *array*: refer to Effects section.

`Stamina_Per_Second` *float*: stamina +/- buff.

`Health_Per_Second` *float*: health +/- buff.

`Food_Per_Second` *float*: food +/- buff.

`Water_Per_Second` *float*: water +/- buff.

`Virus_Per_Second` *float*: virus +/- buff.

## Time of Day Properties

Each of the four main times of day can override certain properties.

`Fog_Color` *color*: distance-based fog. Optionally overrides the skybox color.

`Fog_Density` *float*: [0, 1] similar to fog intensity in ambiance volume.

## Effect Properties

Multiple effects can be instantiated while the weather is active.

`Prefab` [Master Bundle Pointer](MasterBundlePtr.md): game object with a particle system. PlayOnAwake should be disabled. For effects tied to the view it may be helpful to change the culling mode to Always Simulate.

`Emission_Exponent` *float*: power applied to weather intensity multiplied by default constant rate over time.

`Pitch` *float*: x-axis rotation when `Rotate_Yaw_With_Wind` is enabled.

`Translate_With_View` *bool*: should position in world-space match the camera? The built-in snow and rain move with the view. Position is zeroed when false. May be useful for transition effects like dust blowing into the map signaling the start of a sandstorm.

`Rotate_Yaw_With_Wind` *bool*: should y-axis rotation match the wind direction? The built-in snow and rain rotate with wind.

## NPC Conditions

The weather status condition tests the state of the global weather. This condition is supported by visibility.

`Type` Weather_Status

`Logic` Equal or Not_Equal

`GUID` *string*: weather asset GUID to test.

`Value` *enum*: Active, Transitioning_In, Fully_Transitioned_In, Transitioning_Out, Fully_Transitioned_Out, or Transitioning

The weather blend alpha condition compares the current intensity to a value. For example, an NPC could sell umbrellas while rain is greater than 50% (0.5) blended in. This condition is supported by visibility, but is more expensive for visibility than the state condition because each listening object is updated when the intensity changes by 1% (0.01).

`Type` Weather_Blend_Alpha

`Logic` Less_Than or Greater_Than

`GUID` *string*: weather asset GUID to test.

`Value` *float*: [0, 1] weather intensity.
