.. _doc_assets_airdrop:

Airdrop Assets
==============

Overrides the care package model seen falling from the dropship, as well as the barricade spawned when it lands on the ground. Referenced by the :ref:`Level Asset <doc_assets_level>`.

``Type`` *string*: ``SDG.Unturned.AirdropAsset``

``Landed_Barricade`` :ref:`Asset Pointer <doc_data_assetptr>`: Barricade item storage asset. Pivot point of the spawned barricade matches the pivot point of the care package as it hit the ground.

``Carepackage_Prefab`` :ref:`Master Bundle Pointer <doc_data_masterbundleptr>`: Model to spawn falling.
