.. _doc_server_hosting:

Server Hosting
==============

All multiplayer servers are hosted using the Unturned Dedicated Server tool (sometimes abbreviated to U3DS). This tool can either be installed and updated using Valve's `SteamCMD <https://developer.valvesoftware.com/wiki/SteamCMD>`_ tool, or (not recommended) managed through your Steam Library. Using SteamCMD is ideal and has several benefits, but is not strictly necessary. If you are not using SteamCMD, some of the documentation may not apply to you.

**Multiplatform:**

- :ref:`How to Install Server using SteamCMD <doc_server_hosting:install_with_steamcmd>`
- :ref:`How to Install Server without SteamCMD <doc_server_hosting:install_without_steamcmd>`
- :ref:`How to Configure Server <doc_server_hosting:configure_server>`
- :ref:`How to Host Curated Maps <doc_server_hosting:host_curated_maps>`
- :ref:`How to Host Over Internet <doc_server_hosting:host_over_internet>`
- :ref:`Port Forwarding <doc_servers_port_forward>`
- :ref:`Rocket <doc_servers_rocket>`
- :ref:`Login Tokens <doc_servers_gslt>`
- :ref:`Update Notifications <doc_server_update_notifications>`
- :ref:`Rules and Guidelines <doc_server_hosting_rules>`
- :ref:`Server Codes <doc_servers_server_codes>`
- :ref:`Fake IP <doc_servers_fake_ip>`
- :ref:`Bookmark Host <doc_servers_bookmark_host>`

**Windows:**

- :ref:`How to Install SteamCMD <doc_server_hosting:install_steamcmd_windows>`
- :ref:`How to Launch Server <doc_server_hosting:launch_server_windows>`
- `Video Tutorial <https://www.youtube.com/watch?v=8axVrnSLlx4>`_

**Linux:**

- :ref:`How to Install SteamCMD <doc_server_hosting:install_steamcmd_linux>`
- :ref:`How to Launch Server <doc_server_hosting:launch_server_linux>`

.. _doc_server_hosting:install_steamcmd_windows:

How to Install SteamCMD on Windows
----------------------------------

1. `Download From Here <https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip>`_
2. Extract the contents of the zip somewhere you can find it again.
3. Run ``steamcmd.exe``

Continue to: `How to Install Server using SteamCMD <How-to-Install-Server-using-SteamCMD>`_

.. _doc_server_hosting:install_steamcmd_linux:

How to Install SteamCMD on Linux
--------------------------------

Installation on Linux varies by distribution and your admin preferences, so refer to `Valve's Linux Documentation <https://developer.valvesoftware.com/wiki/SteamCMD#Linux>`_. Once downloaded, run the ``steamcmd.sh`` script.

Continue to: :ref:`How to Install Server using SteamCMD <doc_server_hosting:install_with_steamcmd>`

.. _doc_server_hosting:install_with_steamcmd:

How to Install Server using SteamCMD
------------------------------------

1. Login to Steam anonymously.

.. code-block:: bash

	login anonymous

2. Download the Unturned Dedicated Server application.

.. code-block:: bash

	app_update 1110390
	
.. tip:: This command can also be used to update the server

3. Close SteamCMD.
	
.. code-block:: bash

	quit

4. Server files have been installed in the default `app install directory <https://developer.valvesoftware.com/wiki/SteamCMD#Downloading_an_App>`_, which is ``./steamapps/common/U3DS/``.

Continue to: :ref:`How to Launch Server on Windows <doc_server_hosting:launch_server_windows>` or :ref:`How to Launch Server on Linux <doc_server_hosting:launch_server_linux>`

.. _doc_server_hosting:install_without_steamcmd:

How to Install Server without SteamCMD
--------------------------------------

The Unturned Dedicated Server tool can be installed and updated from your Steam Library. The tool is considered its own application, and is managed separately from the Unturned game itself. There are a few issues unique to those installing the Unturned Dedicated Server tool without SteamCMD, which should be considered before setting up your server.

1. It is not possible to run multiple servers at once.

2. The tool uses the same executable name as the game, which means that if the game is closed while the server is running then Steam will think the game is still running. This can cause issues such as Steam refusing to launch the game until the server as closed.

With these considerations in mind, it is recommended to install the Unturned Dedicated Server using SteamCMD instead. For those interested in installing the Unturned Dedicated Server tool without SteamCMD, navigate to your Steam Library. When using the default application filters for the Steam Library, tools (such as for launching dedicated servers) are not be visible in your Library.

To install the tool from your Steam Library either search for "Unturned Dedicated Server" via the search filter, or enable the "Tools" application type filter so that tools are visible. Select the "Unturned Dedicated Server" application in your Steam Library, and click the "Install" button.

To navigate to the server files install directory:
#. Right-click Unturned Dedicated Server in your Steam Library
#. Select Properties... > Local Files > Browse...

The rest of the documentation assumes that the Unturned Dedicated Server tool was downloaded with SteamCMD, rather than through your Steam Library, so some of the documentation may differ slightly.

Continue to: :ref:`How to Launch Server on Windows <doc_server_hosting:launch_server_windows>` or :ref:`How to Launch Server on Linux <doc_server_hosting:launch_server_linux>`

.. _doc_server_hosting:launch_server_windows:

How to Launch Server on Windows
-------------------------------

1. Navigate to the ``...\SteamCMD\steamapps\common\U3DS`` directory.

2. Create a new text file by right-clicking an empty space within the U3DS directory, and selecting New > Text Document. This will create a new text file called "New Text Document.txt".

   1. **If the file name does not display the** ``.txt`` **file extension, then you need to enable the viewing of "File name extensions".**

   2. At the top of the File Explorer window, navigate to the View tab on the ribbon.


   3. In the Show/hide section of options, ensure that the "File name extensions" box is checked.

	.. image:: img/FileNameExtensions.jpg

   4. File extensions should now be displayed at the end of file names.

3. Rename the "New Text Document.txt" file, and change it from a text file (.txt) to a batch script file (.bat). For example, "Tutorial.bat".

4. Right-click on the batch script (``Tutorial.bat``) and select Edit. This will open the batch file in your default text editor, although any text editor (e.g., Notepad, WordPad, Notepad++) can be used.

5. Add the script that will start your server when the batch script is ran.

   a. For an Internet server, copy-and-paste the following text into the file: ``start "" "%~dp0ServerHelper.bat" +InternetServer/MyServer``
	
   b. For a LAN server, copy-and-paste the following text into the file: ``start "" "%~dp0ServerHelper.bat" +LanServer/MyServer``

   In this example "MyServer" is used as the ServerID for savedata and configuration purposes; you may choose to replace "MyServer" with a different name. For an example batch script, open the built-in ``ExampleServer.bat`` file in a text editor.

6. Save your changes to the file, and close the file.

7. Double-click the batch script to launch the server. A command-line interface should appear. Because this is the first time we have ran the batch file, it is going to generate a bunch of necessary server files.

.. image:: img/InterfaceU3DS.jpg

8. When the command-line interface stops outputting new lines of text, it has finished loading (and finished generating all necessary files). You can safely close the server by executing (typing, and then pressing the "↵ Enter" key on your keyboard) the following command on the command-line interface: ``shutdown``

9. The batch script has created a new file directory located in ``...\U3DS\Servers``, called "MyServer". This directory is where all the savedata and configuration files are kept. Changing the ``MyServer`` ServerID (from step 5) in the batch script to a different name will allow for keeping savedata separate across multiple servers, and for running multiple servers at once.

10. (optional) For your server to be visible on the in-game Internet server list you will need to set a :ref:`Login Token <doc_servers_gslt>` and configure :ref:`Fake IP <doc_servers_fake_ip>` or :ref:`Port Forwarding <doc_servers_port_forward>`.

.. _doc_server_hosting:launch_server_linux:

How to Launch Server on Linux
-----------------------------

1. Navigate to the ``.../SteamCMD/steamapps/common\U3DS`` directory.

2. To create our server, we need to execute a command.

   a. For an Internet server run the following command: ``./ServerHelper.sh +InternetServer/MyServer``

   b. For a LAN server run the following command: ``./ServerHelper.sh +LanServer/MyServer``

   In this example "MyServer" is used as the ServerID for savedata and configuration purposes; you may choose to replace "MyServer" with a different name. For an example script, open the built-in ``ExampleServer.sh`` file in a text editor.
3. You can safely close the server by executing (typing, and then pressing the "↵ Enter" key on your keyboard) the following command on the command-line interface: ``shutdown``

4. The executed command has created a new file directory located in ``.../U3DS/Servers``, called "MyServer". This directory is where all the savedata and configuration files are kept. Changing the ``MyServer`` ServerID (from step 2) in the batch script to a different name will allow for keeping savedata separate across multiple servers, and for running multiple servers at once.

5. (optional) For your server to be visible on the in-game Internet server list you will need to set a :ref:`Login Token <doc_servers_gslt>` and configure :ref:`Fake IP <doc_servers_fake_ip>` or :ref:`Port Forwarding <doc_servers_port_forward>`.

.. _doc_server_hosting:configure_server:

How to Configure Server
-----------------------

Each individual ServerID has its own savedata and configuration.

#. Determine the ServerID. This is the name after the +InternetServer/ or +LanServer/ command.
#. Navigate to U3DS > Servers > ServerID.

Launch commands are setup in the Server > ``Commands.dat`` file. Each line should have one command.

Common useful commands are:

- **Map**: Specify the map to load by name, otherwise PEI is used.

Examples:

.. code-block:: c#

	Map PEI
	Map Washington
	Map Russia

- **Port**: Running multiple servers simultaneously requires specifying different ports. Unturned uses two consecutive ports. The first is for server list queries, and the second for in-game traffic. Recommended port values are 27015 for the first server, 27017 for the second server, 27019 for the third server, so on and so forth.

Examples:

.. code-block:: c#

		Port 27015
		Port 27017

- **Name**: Name of the server on the server list; set as "Unturned" by default.
- **Password**: Requires password to join server. Note that password is only SHA1 hashed, so don't use the same password anywhere else.
- **Perspective**: Can be set to "First", "Third", "Both", or "Vehicle" to change camera options.
- **Cheats**: Allows admins to invoke cheat commands like spawning items or vehicles from the chat.

Game rules, listing display, and many other options are available in the ``Config.json`` file. Game options mirror the in-game Play > Singleplayer > Config menu. This file deserves further documentation, but is not officially documented yet.

Steam Workshop add-ons (e.g., maps, items, vehicles, collections) are setup in the ``WorkshopDownloadConfig.json`` file.
To include a Workshop file on your server:

1. Browse to its web page, for example: `Hawaii <https://steamcommunity.com/sharedfiles/filedetails/?id=1753134636>`_
2. Copy the file ID from the end of the URL.

.. code-block:: c#

	URL: https://steamcommunity.com/sharedfiles/filedetails/?id=1753134636
	ID: 1753134636

3. Insert the file ID into the File_IDs list:

.. code-block:: c#

	"File_IDs":
	[
		1753134636
	],

Multiple file IDs should be separated by commas:

.. code-block:: c#

	"File_IDs":
	[
		1753134636,
		1702240229
	],

4. During startup the files will be updated, and any dependencies detected. Players will have the files downloaded while connecting to the server.

.. _doc_server_hosting:host_curated_maps:

How to Host Curated Maps
````````````````````````

Curated maps are available as workshop items, so are configured in the ``WorkshopDownloadConfig.json`` file. During startup the Map command searches installed workshop items for a matching name.

Alphabetically sorted list of curated map file IDs:

- A6 Polaris: 2898548949
- Athens Arena: 1454125991
- Arid: 2683620106
- Belgium: 1727125581
- Buak: 3000549606
- Bunker Arena: 1257784170
- California: 1905768396
- Canyon Arena: 1850209768
- Carpat: 1497352180
- Cyprus Arena: 1647991167
- Cyprus Survival: 1647986053
- Dango: 1850228333
- Easter Island: 1983200271
- Escalation: 3251926587
- Elver: 2136497468
- France: 1975500516
- Greece: 1702240229
- Hawaii: 1753134636
- Ireland: 1411633953
- Kuwait: 2483365750
- Rio de Janeiro: 1821848824

.. _doc_server_hosting:host_over_internet:

How to Host Over Internet
-------------------------

By default, your friends can join your server over the Internet using its :ref:`Server Code <doc_servers_server_codes>` in the Connect menu without port forwarding.

For your server to be visible on the in-game Internet server list you will need to:

#. Set a :ref:`Login Token <doc_servers_gslt>`.
#. Configure :ref:`Fake IP <doc_servers_fake_ip>` or :ref:`Port Forwarding <doc_servers_port_forward>`.

.. note:: Without a :ref:`Login Token <doc_servers_gslt>` the Server Code will change each time your server restarts.
