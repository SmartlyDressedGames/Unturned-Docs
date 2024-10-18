.. _doc_unity_project:

Unity Project
=============

.. warning:: This document is **not** indicative of the project source files becoming available anytime soon. While that is a longer-term goal, this document only aims to begin formalizing the development process. Also good to write this information down since it only exists inside my head at the moment.

Downloading
-----------

The project files are stored in a `Git <https://git-scm.com/>`_ repository. You can use the Git CLI to clone (download) the files, but I'd recommend using a GUI. Personally, I use `Fork <https://git-fork.com/>`_, though it has an upfront price of $60 USD at the time of writing (2024-10-18). The Git website `lists a variety of great, free GUI tools <https://git-scm.com/downloads/guis>`_ including `GitHub Desktop <https://github.com/apps/desktop>`_ and `Sourcetree <https://www.sourcetreeapp.com/>`_.

Getting Started
---------------

You'll need the same version of the Unity editor as described in :ref:`doc_getting_started:installing_unity`. You can double-check the editor version in ``ProjectSettings/ProjectVersion.txt``.

Unfortunately, Steam needs to be running, even to launch the game in the editor. This does make certain tasks like debugging multiplayer harder. Unturned 3 is very tightly integrated with the Steam API, so this requirement is unlikely to change. Certainly an important lesson for future games: Plan ahead to support swapping out platform APIs.

To run the game in the editor, open ``Assets/Game/Sources/Scenes/Setup.unity`` and click Play.

Play Mode Settings
------------------

An editor window is available from Window > Unturned > Editor Settings. Primarily it sets :ref:`options <doc_launch_options>` that are otherwise specified on the command-line.

**Auto Load Level and Auto Load Mode**: Set to a level's folder name to bypass the menu, going from the loading screen directly into singleplayer or the level editor.

**Glazier**: Overrides default :ref:`doc_glazier`.

Troubleshooting
---------------

Check Unity's log files. On Windows there's a shortcut in the project folder to the most recent log file `Unity Editor.log` as well as the containing folder `UnityEditor Logs Folder`.

File Organization
-----------------

One could argue "organization" is a misnomer in this case.

``Assets/CoreMasterBundle`` contains most of the Unity assets loaded at runtime. This is the only asset bundle exported for vanilla content.

``Assets/Game/Sources`` contains all of the source (e.g., ``.blend``) and imported (e.g., ``.fbx``) files for Unity assets exported in the asset bundle.

``Assets/Resources`` are Unity assets loaded by the ``Resources`` class. Introducing new files to this folder should be avoided if possible.

``Assets/Runtime`` contains all of the player code. Certain newer features have their own folders per-assembly-definition, but most game code is in the ``Assembly-CSharp`` folder. It would be nice to rename it, but as far as I'm aware we can't do this without breaking script references in asset bundles (as of 2024-10-18).

The ``Builds`` folder contains exported Unity players, the vanilla :ref:`"masterbundle" (asset bundle) <doc_asset_bundles>`, and - unintuitively - all of the important non-Unity files like :ref:`.dats <doc_asset_definitions>`.

This becomes clearer when remembering the overly-tight integration with Steam. Each subdirectory of ``Builds`` is a Steam depot (except CoreAssetBundle and Test). For future games we would instead automatically **copy** the files from the project output into a Steam depot structure. *sigh*

``Economy`` contains all of the icons and configuration files for the Steam Inventory Service. It's actually gotten a lot tidier since we can refactor it without affecting mods or plugins.

``IDs`` contains spreadsheets of vanilla legacy ID usage. This is hopefully obsolete after 3.24.6.0 added the Menu > Workshop > F1 > Log Asset IDs tool.

Continuous Integration
----------------------

For each commit, `Jenkins <https://www.jenkins.io/>`_ builds the project and runs tests, optionally uploading to a Steam branch.

At the time of writing (2024-10-18) the Jenkins server is locally hosted and not accessible over the Internet.

It **mostly** works with Pipelines using a script at ``Build_Scripts/Jenkinsfile.txt``.

Launching the correct version of Unity relies on ``Build_Scripts/JenkinsBootstrapper.exe`` built from ``JenkinsBootstrapper`` in the project root. It expects Unity to be installed in one of these paths:

- ``C:\UnityEditors``
- ``C:\Unity Editors``
- ``C:\Program Files\Unity\Hub\Editor``

(Yeah, sadly the development and build processes are very Windows-centric.)
