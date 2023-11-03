.. _doc_getting_started:

Getting Started
===============

Installing the Unity Editor is required for exporting custom content into the game. Most 2021.3 LTS version should be compatible; Unturned currently uses 2021.3.29f1. `View Download Links <https://unity.com/releases/editor/qa/lts-releases?version=2021.3>`_

Once Unity is installed, a project can be created to house custom content. At this point, it is recommended to import Unturned's provided Unity packages.

Unity Packages
--------------

Unturned provides multiple Unity packages with the base installation of the game. These packages include examples that can be referenced when creating custom content, and provide the tools necessary to export content from Unity.

These Unity packages are located in the ``.../Unturned/Extras/Sources`` directory, and are regularly updated alongside any major updates to the game.

#. Open your Unity project.
#. Select **Assets > Import Package > Custom Package...** from the toolbar.
#. In the file browser, navigate to the ``.../Unturned/Extras/Sources`` directory.
#. Import the ``Project.unitypackage`` file; importing the ``ExampleAssets.unitypackage`` file is optional.

When importing a Unity package, all of the items in the package will be installed by default. You may deselect any items that you do not want to import.

Project.unitypackage
````````````````````

This package contains the bare-bones required to export custom content:

- Default Project Settings
- :ref:`Asset Bundling Tools <doc_asset_bundles>`
- :ref:`Mod Hooks <doc_assets_mod_hooks>` (optional)

ExampleAssets.unitypackage
``````````````````````````

This package contains vanilla content examples, and several useful prefabs:

- ``CoreMasterBundle`` directory has an example of each type of vanilla asset.
- ``Game/Sources/Animations`` directory has all of the vanilla item animations.
- ``Resources/Characters/Preview.prefab`` is helpful for previewing clothes.

.. warning:: Custom content should not be placed into the CoreMasterBundle directory. Instead, create a separate directory to house your custom content.