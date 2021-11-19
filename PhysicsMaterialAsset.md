# Physics Material Asset

Work-in-progress feature to allow custom physics effects rather than hardcoding them.

The `PhysicsMaterialAsset` type associates gameplay properties and effects with custom Unity "physic" materials. For example if none of the built-in physics materials has appropriate effects for the surface of Mars, a custom Unity physics material named "MarsDirt" could be created. Then a physics material asset with `UnityName` set to "MarsDirt" and `Fallback` of 33650ff924b34f8d9c5a0fd97418cd3e (built-in gravel) could add custom effects for the Martian surfaces.

The `PhysicsMaterialExtensionAsset` type can be used to insert custom properties into built-in physics materials. For example if a custom laser gun should leave burn marks on the hit surface rather than bullet holes, an extension asset can set the `Base` property to a built-in physics material to add custom effects.

This is an [Asset v2](AssetsV2.md) class.

## Properties

`UnityName` *string* or `UnityNames` *string array*: names of Unity "physic" materials to associate with this asset. Not set by extension assets. Multiple names can be specified as an array because the old built-in physics materials had several variants for special cases that should now be handled by these assets.

`Fallback` [Asset Pointer](AssetPtr.md): to a different physics material asset. Fallbacks are used when a property is not set. For example the snow physics material does not have a bullet casing bounce audio clip, so the gravel fallback is used instead.

`Base` [Asset Pointer](AssetPtr.md): to a physics material asset to extend. Properties from the extension asset will be appended to the base asset.

`AudioDefs` *dictionary*: pairs of key/name and [Master Bundle Pointer](MasterBundlePtr.md) to OneShotAudioDefinition. For example the `ParticleSystemCollisionAudio` component `MaterialPropertyName` is referring to these keys. Official properties include BipedLand, FootstepWalk, FootstepRun, BulletCasingBounce, ShotgunShellBounce, and BulletImpact.
