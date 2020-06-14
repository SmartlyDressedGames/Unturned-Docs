# Mod Hooks

## Overview

Script Components can be added to Game Objects in Unity and exported in Asset Bundles _IF_ they match a script in the base game code. These intentionally exportable scripts are referred to as __Mod Hooks__. They can be imported into a Unity project from the Project.unitypackage, and added to game objects inside the Unturned components menu. Each script makes several Events available which can drive other component properties like visibility or play an animation.

Each script documents its purpose and members within its *.cs file.

Originally proposed and coined by VitaxaRusModding in this GitHub issue: [Link](https://github.com/SmartlyDressedGames/Unturned-3.x-Community/issues/435)

## Event Listeners

### Collision Event Hook

Events for player overlaps with a trigger collider. Primarily useful for server-side objects as collisions are not triggered by other players client-side, but this limitation may be resolved in the future.

### Interactable Object Binary State Event Hook (IOBS)

(IOBS for short) are any prop placed from the level editor which can have F pressed on them to open, close, turn on/off, etc. This hook can be added to any GameObject within an IOBS to trigger events during state changes, and even control the IOBS from client and server side.

### Text Chat Event Hook

Event when a text chat message passes certain filters such as channel, within a radius, and containing a secret phrase. Only fired on the server.

### Vehicle Event Hook

Events for driver entering and exiting the vehicle. These events are fired on server and client.

### Weather Event Hook

Events for day, night, full moon, and weather. These events are fired on server and client.

### Custom Weather Event Hook

Events for a specific custom [Weather Asset](WeatherAsset.md). Any map can have an unlimited number of weather types and weather listeners.

## Event Instigators

### Client Text Chat Messenger

#### Notice:
`Allow_Client_Messages` & `Allow_Client_Commands` must be explicitly enabled in `Config.json` for servers.

Allows Unity events to request a text chat message be sent on behalf of the client. For example, to execute a command.


### Server Text Chat Messenger

#### Notice:
`Allow_Server_Messages` & `Allow_Server_Commands` must be explicitly enabled in `Config.json` for servers.

Allows Unity events to broadcast messages from the server. Icons and rich text are optional. Can also execute commands that are not available (yet) to NPCs like changing the weather or triggering an airdrop.
