Server Hosting
==============

All multiplayer servers are hosted using the Unturned Dedicated Server tool, which is installed and updated through Valve's [SteamCMD](https://developer.valvesoftware.com/wiki/SteamCMD) tool.

__Multiplatform:__
- [How to Configure Server](#How-to-Configure-Server)
- [How to Host Curated Maps](#How-to-Host-Curated-Maps)
- [How to Host Over Internet](#How-to-Host-Over-Internet)
- [Port Forwarding](PortForwarding.md)
- [Rocket](Rocket.md)
- [Login Tokens](GameServerLoginTokens.md)
- [Update Notifications](ServerUpdateNotifications.md)
- [Rules and Guidelines](ServerHostingRules.md)

__Windows:__
- [How to Install SteamCMD](#How-to-Install-SteamCMD-on-Windows)
- [How to Launch Server](#How-to-Launch-Server-on-Windows)
- [Video Tutorial](https://www.youtube.com/watch?v=8axVrnSLlx4)

__Linux:__
- [How to Install SteamCMD](#How-to-Install-SteamCMD-on-Linux)
- [How to Launch Server](#How-to-Launch-Server-on-Linux)

How to Install SteamCMD on Windows
----------------------------------

1. [Download From Here](https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip)
2. Extract the contents of the zip somewhere you can find it again.
3. Run `steamcmd.exe`

Continue to: [How to Install Server using SteamCMD](#How-to-Install-Server-using-SteamCMD)

How to Install SteamCMD on Linux
--------------------------------

Installation on Linux varies by distribution and your admin preferences, so refer to [Valve's Linux Documentation](https://developer.valvesoftware.com/wiki/SteamCMD#Linux). Once downloaded, run the `steamcmd.sh` script.

Continue to: [How to Install Server using SteamCMD](#How-to-Install-Server-using-SteamCMD)

How to Install Server using SteamCMD
-------------------------------------------------------

1. Login to Steam anonymously:

		login anonymous

2. Download the server:

		app_update 1110390

	_Note: this command can also be used to update the server._

3. Close SteamCMD:

		quit

4. The server files are now in the SteamCMD > steamapps > common > U3DS directory.

Continue to: [How to Launch Server on Windows](#How-to-Launch-Server-on-Windows) or [How to Launch Server on Linux](#How-to-Launch-Server-on-Linux)

How to Launch Server on Windows
-------------------------------

1. Navigate to the SteamCMD > steamapps > common > U3DS directory.
2. Right-click within the folder.
3. Select New > Text Document
4. Replace "New Text Document.txt" with "Tutorial.bat"
5. Right-click on the batch script (`Tutorial.bat`) and select Edit.
6. For an internet server insert the following text into the file:

		start "" "%~dp0ServerHelper.bat" +InternetServer/MyServer

	Alternatively, for a LAN server insert the following text into the file:

		start "" "%~dp0ServerHelper.bat" +LanServer/MyServer

	_Note: In this example MyServer is used as the ServerID for savedata and configuration purposes._

7. Save your changes.
8. Double-click the batch script to launch the server.
3. Cleanly shutdown the server once it finishes loading:

		shutdown

	Running it will have created a "MyServer" directory in U3DS > Servers. This is where all savedata and configuration files are kept. Changing the `MyServer` ServerID in the batch script can be done to run multiple servers at once, or to keep savedata separate.

For an example script open the built-in `ExampleServer.bat` file.

How to Launch Server on Linux
-----------------------------

1. Navigate to the SteamCMD > steamapps > common > U3DS directory.
2. For an internet server run the following command:

		./ServerHelper.sh +InternetServer/MyServer

	Alternatively, for a LAN server run the following command:

		./ServerHelper.sh +LanServer/MyServer

	_Note: In this example MyServer is used as the ServerID for savedata and configuration purposes._

3. Cleanly shutdown the server once it finishes loading:

		shutdown

	Running it will have created a "MyServer" directory in U3DS > Servers. This is where all savedata and configuration files are kept. Changing the `MyServer` ServerID in the launch arguments can be done to run multiple servers at once, or to keep savedata separate.

For an example script open the built-in `ExampleServer.sh` file.

How to Configure Server
-----------------------

Each individual ServerID has its own savedata and configuration.

1. Determine the ServerID. This is the name after the +InternetServer/ or +LanServer/ command.
2. Navigate to U3DS > Servers > ServerID.

Launch commands are setup in the Server > `Commands.dat` file. Each line should have one command.

Common useful commands are:

- __Map__: Specify the map to load by name, otherwise PEI is used.

	Examples:

		Map PEI
		Map Washington
		Map Russia

- __Port__: Running multiple internet servers simultaneously requires specifying different ports. Unturned will use the set port for game traffic, port + 1 for server list queries and port + 2 for the Steam backend. Recommended port values are 27015 for the first server, 27018 for the second server, so on and so forth.

	Examples:

		Port 27015
		Port 27018

- __Name__: Name of the server on the server list; set as "Unturned" by default.
- __Password__: Requires password to join server. Note that password is only SHA1 hashed, so don't use the same password anywhere else.
- __Perspective__: Can be set to "First", "Third", "Both", or "Vehicle" to change camera options.
- __Cheats__: Allows admins to invoke cheat commands like spawning items or vehicles from the chat.

Game rules, listing display, and many other options are available in the `Config.json` file. Game options mirror the in-game Play > Singleplayer > Config menu. This file deserves further documentation, but is not officially documented yet.

Steam Workshop add-ons (e.g., maps, items, vehicles) are setup in the `WorkshopDownloadConfig.json` file.
To include a Workshop file on your server:

1. Browse to its web page, for example: [Hawaii](https://steamcommunity.com/sharedfiles/filedetails/?id=1753134636)
2. Copy the file ID from the end of the URL.

		URL: https://steamcommunity.com/sharedfiles/filedetails/?id=1753134636
		ID: 1753134636

3. Insert the file ID into the File_IDs list:

		"File_IDs":
		[
			1753134636
		],

	Multiple file IDs should be separated by commas:

		"File_IDs":
		[
			1753134636,
			1702240229
		],

4. During startup the files will be updated, and any dependencies detected. Players will have the files downloaded while connecting to the server.

How to Host Curated Maps
------------------------

Curated maps are available as workshop items, so are configured in the `WorkshopDownloadConfig.json` file. During startup the Map command searches installed workshop items for a matching name.

Alphabetically sorted list of curated map file IDs:

- Athens Arena: 1454125991
- Belgium: 1727125581
- Bunker Arena: 1257784170
- California: 1905768396
- Canyon Arena: 1850209768
- Carpat: 1497352180
- Cyprus Arena: 1647991167
- Cyprus Survival: 1647986053
- Dango: 1850228333
- Easter Island: 1983200271
- Elver: 2136497468
- France: 1975500516
- Greece: 1702240229
- Hawaii: 1753134636
- Rio de Janeiro: 1821848824

How to Host Over Internet
-------------------------

Hosting a publicly-accessible internet server requires an extra step compared to a LAN server. When on a home network [Port Forwarding](PortForwarding.md) is required in order to direct traffic to the host computer.

One way to think of it is that when there are multiple devices (e.g. computers and phones) connected to the LAN, the outside internet does not know which device is the Unturned server. In this case port forwarding specifies which LAN device is the host.

For port ranges and other details: [Port Forwarding](PortForwarding.md)
