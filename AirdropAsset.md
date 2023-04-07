**NOTICE:** *You are not reading the most up-to-date documentation. This file is old, and may not reflect the current modding or server capabilities. The latest documentation can be found at [Unturned Documentation](https://docs.smartlydressedgames.com/).*

*This file may be removed in the future. Refer to its more [up-to-date equivalent](https://docs.smartlydressedgames.com/en/stable/assets/airdrop-asset.html) instead.*

Airdrop Asset
=============

Overrides the care package model seen falling from the dropship, as well as the barricade spawned when it lands on the ground. Referenced by the [Level Asset](LevelAsset.md).

`Landed_Barricade` [Asset Pointer](AssetPtr.md): barricade item storage asset. Pivot point of the spawned barricade matches the pivot point of the care package as it hit the ground.

`Carepackage_Prefab` [Master Bundle Pointer](MasterBundlePtr.md): model to spawn falling.

This is an [Asset v2](AssetsV2.md) class.
