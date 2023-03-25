.. _doc_getting_started:

Getting Started
===============

Installing the Unity Editor is required for exporting custom content into the game. Any 2019.4 LTS version should be compatible. `View Download Links <https://unity3d.com/unity/qa/lts-releases?version=2019.4>`_

Once Unity is installed a project can be created to house custom content. At this point it is recommended to import Unturned's provided source packages:

1. Inside Unity open the Assets > Import Package > Custom Package... wizard.
1. Find the Unturned installation directory.
3. Navigate to the Bundles/Sources directory.
4. Import the Project.unitypackage, and optionally the ExampleAssets.unitypackage.

Project.unitypackage
--------------------

This package contains the barebones required to export custom content:

- :ref:`Asset Bundling Tools <doc_asset_bundles>`
- Default Project Settings
- :ref:`(Optional) Mod Hooks <doc_assets_modhooks>`

ExampleAssets.unitypackage
--------------------------

This package contains vanilla content examples, and several useful prefabs:

- CoreMasterBundle directory has at least one example of each piece of vanilla content.
- Animations directory has all of the vanilla item animations for re-use.
- Assets/Resources/Characters/Preview.prefab is helpful for previewing clothes.

Note that custom content should NOT be placed into the CoreMasterBundle, instead create a separate directory.
