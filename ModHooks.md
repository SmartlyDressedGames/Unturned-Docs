# Mod Hooks

## Overview

Script Components can be added to Game Objects in Unity and exported in Asset Bundles _IF_ they match a script in the base game code. These intentionally exportable scripts are referred to as __Mod Hooks__. They can be imported into a Unity project from the Project.unitypackage, and added to game objects inside the Unturned components menu. Each script makes several Events available which can drive other component properties like visibility or play an animation.

Each script documents its purpose and members within its *.cs file.

Originally proposed and coined by VitaxaRusModding in this GitHub issue: [Link](https://github.com/SmartlyDressedGames/Unturned-3.x-Community/issues/435)

## Event Listeners

### Activation Event Hook

Events when a component or game object are enabled and disabled. Useful for extending toggleable actions in the base game.

### Binary Random Component

When triggered will invoke one of two events depending on percentage probability. For example with a probability of 0.05 the OnTrue event will be invoked 5% of the time, and OnFalse will be invoked the remaining 95% of times.

### Collision Event Hook

Events for player overlaps with a trigger collider. Primarily useful for server-side objects as collisions are not triggered by other players client-side, but this limitation may be resolved in the future.

### Destroy Event Hook

Event when a component or game object is removed from the scene.

### Interactable Object Binary State Event Hook (IOBS)

(IOBS for short) are any prop placed from the level editor which can have F pressed on them to open, close, turn on/off, etc. This hook can be added to any GameObject within an IOBS to trigger events during state changes, and even control the IOBS from client and server side.

### NPC Global Event Hook

Event triggered when corresponding [NPC Event reward](NPCAsset/Rewards.md#event) type is triggered. For example, when any NPC Event with ID "Fireworks" is broadcast all of the components with event ID "Fireworks" will have their corresponding Unity event triggered as well, in this case perhaps to spawn a fireworks effect.

### Text Chat Event Hook

Event when a text chat message passes certain filters such as channel, within a radius, and containing a secret phrase. Only fired on the server.

### Timer Event Hook

Allows events to set or cancel a timer, and triggers an event when the timer expires.

### Useable Gun Event Hook

Events for EquipableItem prefab. Supersedes VehicleTurretEventHook. These events are fired on server and client.

### Vehicle Event Hook

Events for driver entering and exiting the vehicle. These events are fired on server and client.

### Vehicle Turret Event Hook

Events for Turret_# GameObjects in the vehicle when guns are used. These events are fired on server and client.

### Weather Event Hook

Events for day, night, full moon, and weather. These events are fired on server and client.

### Custom Weather Event Hook

Events for a specific custom [Weather Asset](WeatherAsset.md). Any map can have an unlimited number of weather types and weather listeners.

## Event Instigators

### Client Text Chat Messenger

Allows Unity events to request a text chat message be sent on behalf of the client. For example, to execute a command.

The `UnityEvents.Allow_Client_Messages` and/or `UnityEvents.Allow_Client_Commands` settings must be enabled in the server `Config.json` file before these can be triggered. This ensures hosts are aware of their usage. Singleplayer defaults to enabled.

### Server Text Chat Messenger

Allows Unity events to broadcast messages from the server. Icons and rich text are optional. Can also execute commands that are not available (yet) to NPCs like changing the weather or triggering an airdrop.

The `UnityEvents.Allow_Server_Messages` and/or `UnityEvents.Allow_Server_Commands` settings must be enabled in the server `Config.json` file before these can be triggered. This ensures hosts are aware of their usage. Singleplayer defaults to enabled.

### Effect Spawner

Allows Unity events to spawn effect assets. When the `AuthorityOnly` field is enabled only the server will spawn effects and replicate them to clients.

## Misc

### Fall Damage Override

Allows any game object to override the fall damage when a character lands on it or one of its descendants.
