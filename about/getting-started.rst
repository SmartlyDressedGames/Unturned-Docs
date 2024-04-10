.. _doc_getting_started:

Getting Started
===============

To get started with creating mods for *Unturned*, certain tools need to be downloaded first. This article provides a walkthrough for downloading these tools.

Installing Unturned
-------------------

*Unturned* must be downloaded in order to create and upload mods. The game can be downloaded from `Steam <https://store.steampowered.com/app/304930/>`_. If you are using SteamCMD, its app ID is ``304930``.

Not only do the game files include tools necessary for creating custom content, but the game's official assets can also be used as an example when creating your own items, objects, or other assets.

Installing Unity
----------------

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

Other Tools
-----------

Modders will need a few more tools on hand to create custom content.

Text editors
````````````

A text editor (e.g., Notepad) or a code editor (e.g., Notepad++ or Visual Studio Code) is required to write the game data files used by assets. Code editors often include other useful tools, such as being able to search-and-replace content across multiple files at once.

We *do not* recommend using a word processor, as these can add unwanted characters when not used properly.

If you are unsure what you should use, Notepad comes installed on all Windows systems by default, and lacks any additional tools or features that (while helpful) may be confusing for an inexperienced user.

Image editing software
``````````````````````

To create custom textures for your modded content – such as for new shirts or pants, materials for custom objects, or 2D effects – you will need an image editing software that supports transparency. Some free image editors include Paint.NET, GIMP, and Krita.

Blender
```````

A 3D modeling tool such as Blender is required to create custom models (and animations). Blender is the same tool we use for *Unturned*, although it is not strictly required.