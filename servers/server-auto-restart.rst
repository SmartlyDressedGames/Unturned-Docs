.. _doc_server_auto_restart:

Server Auto Restart
===================

Server maintenance can be somewhat automated without plugins, by utilizing a couple features from your server's Config.json file.

Scheduled Maintenance
---------------------

We recommend restarting your server once every 24 hours, as much of the game's older code still uses single-precision floating point time.

There are three settings for scheduled shutdowns:

#. | **Enable_Scheduled_Shutdown**: When ``true``, the server will shutdown at a specified time.

#. | **Scheduled_Shutdown_Time**: Local time for when the server will shutdown.

#. | **Scheduled_Shutdown_Warnings**: Players will be notified via a chat broadcast at these times before the scheduled shutdown. For example, 30:00 will broadcast in chat 30 minutes before the shutdown.

Checking for Updates
--------------------

Your server can monitor for updates, and shutdown when one is detected. Three settings are important when checking for updates:

#. | **Enable_Update_Shutdown**: When ``true``, the server will monitor for updates.

#. | **Update_Steam_Beta_Name**: Defaults to ``public``, but can be set to ``preview`` for servers running on the preview branch.

#. | **Update_Shutdown_Warnings**: After an update is detected, the server will wait for the longest of these durations to notify players before shutdown. For example, if the longest time is 2:30, the server will broadcast in chat 2 minutes and 30 seconds before the shutdown.

Practical Application
---------------------

These options are most useful in conjunction with a script that updates and restarts the server in a loop. For example, this Windows .bat script can be placed in the steamcmd folder to infinitely update and restart the server:

.. code-block:: bat
    :linenos:
    
    @echo off
    rem @ suppresses echo command from being echoed, and then disables echoing in this script.

    rem This is a label for use with "goto". The script will return to this label to update and restart the server.
    :loop

    rem %~dp0 expands to the path to this script's directory, allowing it to be called from a different working directory.
    rem The "/wait" option pauses our script until steamcmd is finished.
    rem Start steamcmd, download latest version of Unturned Dedicated Server, then close cleanly.
    echo Updating...
    start "" /wait "%~dp0steamcmd.exe" +login anonymous +app_update 1110390 +quit

    echo Finished update! Launching server...
    start "" /wait "%~dp0steamapps\common\U3DS\Unturned.exe" -batchmode -nographics +InternetServer/MyServer

    echo Server has exited. Restarting after timeout...
    echo:
    echo Press CTRL+C and then Y during this timeout to cancel restart.
    timeout 10

    rem Return to the "loop" label to update and restart the server.
    goto loop

Here's a similar example for Linux, tested on Ubuntu. Note that the U3DS install path may be different depending how steamcmd was installed and whether ``+force_install_dir`` was specified, but typically one of these locations:

1. ``~/.steam/steam/steamapps/common/U3DS``
2. ``~/Steam/steamapps/common/U3DS``

As such, it may be helpful to create a symbolic link to the U3DS directory:

``ln -s ~/.steam/steam/steamapps/common/U3DS ~/U3DS``

OR

``ln -s ~/Steam/steamapps/common/U3DS ~/U3DS``

This example script assumes the symbolic link exists at ``~/U3DS``.

1. Save script as ``MyServer.sh`` in your home directory (e.g., ``nano ~/MyServer.sh``):

.. code-block:: sh
	:linenos:

	#! /usr/bin/bash
	while true; do
		echo Updating...
		steamcmd +login anonymous +app_update 1110390 -validate +quit

		echo Finished update! Launching server...
		cd ~/U3DS
		source ServerHelper.sh +InternetServer/MyServer

		echo Server has exited. Restarting after timeout...
		echo Press Ctrl+C during this timeout to cancel restart.
		read -t 10
	done

2. Open a screen to run the server in with ``screen -S MyServer``.
3. Run script with ``bash MyServer.sh``.
4. If everything's working OK, press ``Ctrl + A`` then ``D`` to detach, leaving the script running.
5. You can re-attach to the screen with ``screen -r MyServer``.
