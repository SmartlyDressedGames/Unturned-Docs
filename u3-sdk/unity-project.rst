.. _doc_sdk_unity_project:

Unity Project Overview
======================

Downloading
-----------

Unturned's project files are stored using the `Git <https://git-scm.com/>`_ version control system (`VCS <https://en.wikipedia.org/wiki/Version_control>`_).

If you have the Git CLI installed, you can clone the files to your computer with this command:

``git clone https://github.com/SmartlyDressedGames/U3-SDK.git``

Getting Started
---------------

You'll need the same version of the Unity editor as described in :ref:`doc_getting_started:installing_unity`. You can double-check the editor version in ``ProjectSettings/ProjectVersion.txt``.

Steam needs to be running, and `Unturned <https://store.steampowered.com/app/304930>`_ must be installed. (Workshop mods and large binary files are loaded from the latest official release of the game.)

To run the game in the editor, open the ``GameStartup.unity`` scene and click Play.

.. tip:: We recommend closing Unity's **Hierarchy** window in-game except when you need it. Unturned's scenes contain mostly top-level game objects for optimization purposes with the drawback of slowing down the Hierarchy window. For more information, `Scenes Structure > Hierarchy depth and count <https://learn.unity.com/tutorial/unity-tips#64622ce0edbc2a32a219b25e>`_.

Editor Preferences
------------------

Unfortunately, Unturned doesn't support hot-reloading. If modifying code while Unity is open, we recommend changing **Script changes while playing** to **Recompile after playing**.

Play Mode Settings
------------------

An editor window is available from Window > Unturned > Editor Settings. Primarily it sets :ref:`options <doc_launch_options>` that are otherwise specified on the command-line.

**Auto Load Level and Auto Load Mode**: Set to a level's folder name to bypass the menu, going from the loading screen directly into singleplayer or the level editor.

**Glazier**: Overrides default :ref:`doc_glazier`.

Troubleshooting
---------------

Check Unity's log files. On Windows there's a shortcut in the project folder to the most recent log file ``Unity Editor.log`` as well as the containing folder ``UnityEditor Logs Folder``.

File Organization
-----------------

``Assets/Game/Sources`` contains all of the source (e.g., ``.blend``) and imported (e.g., ``.fbx``) files for Unity assets exported in the asset bundle.

``Assets/Resources`` are Unity assets loaded by the ``Resources`` class. Introducing new files to this folder should be avoided if possible.

``Assets/Runtime`` contains all of the player code. Certain newer features have their own folders per-assembly-definition, but most game code is in the ``Assembly-CSharp`` folder. It would be nice to rename it, but as far as I'm aware we can't do this without breaking script references in asset bundles (as of 2024-10-18).

``Assets/Runtime/Assembly-CSharp/NetGen`` is all generated networking code. It's included in Git to make the first-run process smoother.

The ``Builds`` folder contains exported Unity players.

Net Code
--------

Most gameplay requires remote procedure calls (RPCs) to function properly. Even singleplayer is essentially a one-player server. The RPC code is automatically generated, but this is still a manual step in the editor:

#. Open **Window** > **Unturned** > **Net Gen**
#. Click **Generate**
#. Tab out and back in to ensure the scripts are imported

Continuous Integration
----------------------

For each commit, we have set up `Jenkins <https://www.jenkins.io/>`_ to build the project and runs tests, optionally uploading to a Steam branch.

At the time of writing (2024-10-18) the Jenkins server is locally hosted and not accessible over the Internet.

It **mostly** works with Pipelines using a script at ``Build_Scripts/Jenkinsfile.txt``.

Launching the correct version of Unity relies on ``Build_Scripts/JenkinsBootstrapper.exe`` built from ``JenkinsBootstrapper`` in the project root. It expects Unity to be installed in one of these paths:

- ``C:\UnityEditors``
- ``C:\Unity Editors``
- ``C:\Program Files\Unity\Hub\Editor``

(Yeah, sadly the development and build processes are very Windows-centric.)
