.. _doc_steamcmd:

Using SteamCMD (Advanced Setup)
===============================

Some servers may benefit from a more advanced setup than the one provided in our :ref:`Simple Setup <doc_server_hosting:simple_setup>` guide. This page assumes you have read the full ":ref:`Setting up a Server <doc_server_hosting>`" documentation.

When hosting multiple servers at the same time, we recommend using `SteamCMD <https://developer.valvesoftware.com/wiki/SteamCMD>`_ to install the **Unturned Dedicated Server** tool rather than installing it from your Steam Library. SteamCMD is a command-line version of the Steam Client.

It is not possible to run multiple servers at once—from the same computer—*without* using SteamCMD.

Servers can be hosted on Windows and Linux operating systems. There is no support for hosting on macOS devices.

Download SteamCMD on Windows
----------------------------

Installation on Windows operating systems (such as Windows 10 or Windows 11) is very straightforward.

1. `Download <https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip>`_ SteamCMD for Windows.
2. Extract the contents of the zip to somewhere you can find it again.
3. Run ``steamcmd.exe``.

Download SteamCMD on Linux
--------------------------

Installation on Linux varies by distribution and your admin preferences. We recommend referring to `Valve's Linux Documentation <https://developer.valvesoftware.com/wiki/SteamCMD#Linux>`_. Once downloaded, run the ``steamcmd.sh`` script.

Install the Unturned Dedicated Server with SteamCMD
---------------------------------------------------

1. | Login to Steam anonymously.

.. code-block:: shell

	login anonymous

2. | Download the Unturned Dedicated Server application.

.. code-block:: shell

	app_update 1110390

.. tip:: This command can also be used to update the Unturned Dedicated Server.

3. | Close SteamCMD once the download finishes.

.. code-block:: shell

	quit

4. | In your SteamCMD folder, the server files can now be found within the default app install directory. For the Unturned Dedicated Server, this is ``.../steamapps/common/U3DS/``.

If you need additional information, consider reading the SteamCMD wiki page's "`Downloading an App <https://developer.valvesoftware.com/wiki/SteamCMD#Downloading_an_App>`_" section.

Launch a Server on Windows
--------------------------

Although old, this video guide remains fairly accurate and can supplement the reading below: https://www.youtube.com/watch?v=8axVrnSLlx4.

1. | Navigate to your server files. When using the default app install directory, these should be found at ``...\steamcmd\steamapps\common\U3DS``.

2. | Create a new text file within the U3DS directory. This file can be named anything – but for the purposes of this guide, we will call it "**MyServer**".

3. | Change the file type from a text file (.txt) to a batch script file (.bat). To do this, simply edit the file's name and replace the ``.txt`` file extension with ``.bat``. For example, "**MyServer.bat**".

.. warning::

	If the file name does not display the ``.txt`` file extension – e.g., you see "MyServer" rather than "MyServer.txt" – you need to enable the viewing of "File name extensions" in Windows.

	Click the "View" button in File Explorer and enable the "File name extensions" option. Once enabled, you can see and edit file extensions as part of file names.

	.. image:: /img/FileNameExtensions.jpg

4. | Open **MyServer.bat** in any text editor, such as Notepad.

5. | Copy-and-paste one of the following scripts into the file, depending on the type of server you are hosting:

   For an **Internet** server:

   .. code-block:: batch

		start "" "%~dp0ServerHelper.bat" +InternetServer/MyServer

   For a **LAN** server:

   .. code-block:: batch

		start "" "%~dp0ServerHelper.bat" +LanServer/MyServer

.. tip::

	In the provided scripts, "MyServer" is being used as the ServerID. Your server's savedata and configuration files will be found in a folder named after your chosen ServerID.

	**ExampleServer.bat** is an example of a LAN server. Opening it in a text editor will provide additional information that may be helpful should you need it.

6. | Save your changes to the file and close it.

7. | Double-click **MyServer.bat** to launch your server. A command-line interface should appear. Since this is the first time you have launched your server, it will need to generate your server's configuration files.

.. image:: /img/InterfaceU3DS.jpg

8. | You should see "Loading level: 100%" when the server has finished loading (and generated all necessary files). Use the ``Shutdown`` command in the command-line interface to safely save and close your server for now.

9. | Your server's configuration files can be found in a newly-created folder (named after its ServerID) within the ``...\U3DS\Servers`` directory. This is where your savedata and configuration files are stored.

.. tip::

	Refer to :ref:`Setting up a Server – Configure Server Settings <doc_server_hosting:configuration>` for guidance on customizing your server.

10. | When hosting an Internet server, refer to :ref:`Setting up a Server – Switching to an Internet Server <doc_server_hosting:internet_server>` for guidance on adding a :ref:`Game Server Login Token <doc_servers_gslt>` and using either :ref:`Fake IP <doc_servers_fake_ip>` or :ref:`Port Forwarding <doc_servers_port_forward>`.

Once configured, you can open your server by running the **MyServer.bat** script!

Launch a Server on Linux
------------------------

1. | Navigate to your server files. When using the default app install directory, these should be found at ``.../steamcmd/steamapps/common/U3DS``.

2. | Copy-and-paste one of the following commands into your Linux terminal, depending on the type of server you are hosting:

   For an **Internet** server:

   .. code-block:: batch

		./ServerHelper.sh +InternetServer/MyServer

   For a **LAN** server:

   .. code-block:: batch

		./ServerHelper.sh +LanServer/MyServer

.. tip::

	In the provided scripts, "MyServer" is being used as the ServerID. Your server's savedata and configuration files will be found in a folder named after your chosen ServerID.

	**ExampleServer.sh** is an example of a LAN server. Opening it in a text editor will provide additional information that may be helpful should you need it.

3. | You should see "Loading level: 100%" when the server has finished loading (and generated all necessary files). Use the ``Shutdown`` command in the command-line interface to safely save and close your server for now.

4. | Your server's configuration files can be found in a newly-created folder (named after its ServerID) within the ``...\U3DS\Servers`` directory. This is where your savedata and configuration files are stored.

.. tip::

	Refer to :ref:`Setting up a Server – Configure Server Settings <doc_server_hosting:configuration>` for guidance on customizing your server.

5. | When hosting an Internet server, refer to :ref:`Setting up a Server – Switching to an Internet Server <doc_server_hosting:internet_server>` for guidance on adding a :ref:`Game Server Login Token <doc_servers_gslt>` and using either :ref:`Fake IP <doc_servers_fake_ip>` or :ref:`Port Forwarding <doc_servers_port_forward>`.

Once configured, you can open your server by running the **MyServer.sh** script!

Related Topics
--------------

Some additional topics are covered elsewhere. Of particular interest:

- Install plugins through frameworks like :ref:`Rocket (LDM) <doc_servers_rocket>` or :ref:`OpenMod <doc_servers_openmod>`.
- Automate server maintenance with :ref:`Server Auto Restart <doc_server_auto_restart>` features.
- Configure a :ref:`Bookmark Host <doc_servers_bookmark_host>` so players can "Bookmark" your server.
- :ref:`Stay notified <doc_server_update_notifications>` when the Unturned Dedicated Server app has an update.
