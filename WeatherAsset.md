# Weather Asset

Overrides the built-in snow and rain weather with custom events. This is feature is a work-in-progress.

Random weather can be scheduled to occur naturally on a map with the `Weather_Types` property of the [Level Asset](LevelAsset.md).

This is an [Asset v2](AssetsV2.md) class.

## How to test?

When a GUID is passed to the weather command it will start a custom weather event, and 0 can be used to end it.

	/weather 819982d7a2b6453488a8c4c5d9efe67f

## Properties Reference

`Volume_Mask` [u32 Mask](Bitmask.md): only enabled while inside an ambience volume with non-zero bitwise AND result. Defaults to 0xFFFFFFFF.

`Fade_In_Duration` *float*: seconds between weather event starting and reaching full intensity.

`Fade_Out_Duration` *float*: seconds between weather event ending and reaching zero intensity.

`Ambient_Audio_Clip` [Master Bundle Pointer](MasterBundlePtr.md): audio clip to play globally. Volume matches intensity.

`Override_Fog` *bool*: should fog configured in the lighting be overridden?

`Override_Atmospheric_Fog` *bool*: should fog affect the skybox?

`Shadow_Strength_Multiplier` *float*: directional light shadow strength multiplier.

`Fog_Blend_Exponent` *float*: power applied to fog blending alpha.

`Cloud_Blend_Exponent` *float*: power applied to cloud blending alpha.

`Wind_Main` *float*: wind zone windMain value. Will be replaced by more configurable game-specific wind eventually.

`Dawn`, `Midday`, `Dusk` and `Midnight`: refer to the Time of Day section.

`Effects` *array*: refer to Effects section.

`Stamina_Per_Second` *float*: stamina +/- buff.

`Health_Per_Second` *float*: health +/- buff.

`Food_Per_Second` *float*: food +/- buff.

`Water_Per_Second` *float*: water +/- buff.

`Virus_Per_Second` *float*: virus +/- buff.

`Has_Lightning` *bool*: if true, lightning will be enabled for this weather type. In the future this should get cleaned up, but for now it is hardcoded for assigning a net id.

`Min_Lightning_Interval` *float*: minimum seconds between lightning strikes.

`Max_Lightning_Interval` *float*: maximum seconds between lightning strikes.

## Time of Day Properties

Each of the four main times of day can override certain properties.

`Fog_Color` *struct*: distance-based fog. Optionally overrides the skybox color. Refer to Color section.

`Fog_Density` *float*: [0, 1] similar to fog intensity in ambiance volume.

`Cloud_Color` *struct*: inner body of cloud. Refer to Color section.

`Cloud_Rim_Color` *struct*: outer edge of cloud. More visible than inner color. Refer to Color section.

`Brightness_Multiplier` *float*: all ambient lighting colors are multiplied by this.

## Effect Properties

Multiple effects can be instantiated while the weather is active.

`Prefab` [Master Bundle Pointer](MasterBundlePtr.md): game object with a particle system. PlayOnAwake should be disabled. For effects tied to the view it may be helpful to change the culling mode to Always Simulate.

`Emission_Exponent` *float*: power applied to weather intensity multiplied by default constant rate over time.

`Pitch` *float*: x-axis rotation when `Rotate_Yaw_With_Wind` is enabled.

`Translate_With_View` *bool*: should position in world-space match the camera? The built-in snow and rain move with the view. Position is zeroed when false. May be useful for transition effects like dust blowing into the map signaling the start of a sandstorm.

`Rotate_Yaw_With_Wind` *bool*: should y-axis rotation match the wind direction? The built-in snow and rain rotate with wind.

## Color Properties

Each color can use a custom override, or a color from the level editor lighting panel. Using a level color is primarily for rain and snow backwards compatibility.

`Level_Enum` *enum*: if set then the RGB specified are multiplied by this color.
`R`, `G`, `B` *uint8*: color channel values.

## NPC Conditions

Global weather state and current weather intensity blend can be tested through NPC conditions. Refer to [Conditions.md](/NPCAsset/Conditions.md) for documentation.
