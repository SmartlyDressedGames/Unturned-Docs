Mod Hooks
=========

Overview
--------

Script Components can be added to Game Objects in Unity and exported in Asset Bundles _IF_ they match a script in the base game code. These intentionally exportable scripts are referred to as __Mod Hooks__. They can be imported into a Unity project from the Project.unitypackage, and added to game objects inside the Unturned components menu. Each script makes several Events available which can drive other component properties like visibility or play an animation.

Each script documents its purpose and members within its *.cs file.

Originally proposed and coined by VitaxaRusModding in this GitHub issue: [Link](https://github.com/SmartlyDressedGames/Unturned-3.x-Community/issues/435)

Collision Event Hook
--------------------

Events for player overlaps with a trigger collider. Primarily useful for server-side objects as collisions are not triggered by other players client-side, but this limitation may be resolved in the future.

Interactable Object Binary State Event Hook
-------------------------------------------

(IOBS for short) are any prop placed from the level editor which can have F pressed on them to open, close, turn on/off, etc. This hook can be added to any GameObject within an IOBS to trigger events during state changes, and even control the IOBS from client and server side.

Text Chat Event Hook
--------------------

Event when a text chat message passes certain filters such as channel, within a radius, and containing a secret phrase. Only fired on the server.

Vehicle Event Hook
------------------

Events for driver entering and exiting the vehicle. These events are fired on server and client.

Weather Event Hook
------------------

Events for day, night, full moon, and weather. These events are fired on server and client.
