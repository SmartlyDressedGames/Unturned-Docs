# Troubleshooting

## Menus are big and overlapping

1. Right-click Unturned in your Steam Library
2. Select Properties... > General
3. Find the Launch Options field
3. Type "-ui_scale 1" without quotes

## Force OpenGL

1. Right-click Unturned in your Steam Library
2. Select Properties... > General
3. Find the Launch Options field
4. Type "-force-glcore" without quotes

## D3D11 Crash

1. Right-click Unturned in your Steam Library
2. Select Properties... > Local Files > Browse...
3. Open the Unturned_Data folder
4. Open the boot.config file in a text editor
5. Add a line with "force-d3d11-bltblt-mode=" without quotes
6. Save and close the file

## Delete Items

1. Open the in-game Steam inventory from Menu > Survivors > Inventory
2. Select any items you wish to remove and a Delete or Salvage button will show under the icon
3. Confirm the deletion

## Local Files

1. Right-click Unturned in your Steam Library
2. Select Properties... > Local Files > Browse...

## Verify

1. Right-click Unturned in your Steam Library
2. Select Properties... > Local Files
3. Click "Verify integrity of game files..."

## Crash Files

1. Right-click Unturned in your Steam Library
2. Select Properties... > Local Files > Browse...
3. Open the Logs folder
4. Attach the Client.log file to your email
5. Return to the Unturned folder
6. Open the Unity AppData folder
7. Attach the Player.log file to your email

## Unity Windows Crash Files

1. Right-click Unturned in your Steam Library
2. Select Properties... > Local Files > Browse...
3. Open the "Unity Temp" folder
4. Zip and attach the Crashes folder to your email

## Repair BattlEye

1. Right-click Unturned in your Steam Library
2. Select Properties... > Local Files > Browse...
3. Open the BattlEye folder
4. Run Uninstall_BattlEye.bat
5. Delete the BattlEye folder
6. Right-click Unturned in your Steam Library
7. Select Properties... > Local Files
8. Click "Verify integrity of game files..."

## Opt-out of Betas

1. Right-click Unturned in your Steam Library
2. Select Properties... > Betas
3. From the dropdown select "None"

## Steam Cloud

Your stored files can be found at:
`C:\Program Files (x86)\Steam\userdata\ (your steam id) \304930`

## View Workshop Files

This page lists your Steam account's Unturned file subscriptions:
https://steamcommunity.com/my/myworkshopfiles/?appid=304930&browsefilter=mysubscriptions

## Temporarily Disable All Workshop Files

Disabling loading of your Steam account's Unturned file subscriptions can be helpful to narrow down whether a problem is mod-related or not.

1. Right-click Unturned in your Steam Library
2. Select Properties... > General
3. Find the Launch Options field
4. Type "-NoWorkshopSubscriptions" without quotes
