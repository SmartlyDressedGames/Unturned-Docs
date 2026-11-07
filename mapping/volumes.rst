.. _doc_mapping_volumes:

Level Volumes
=============

Volumes are box or sphere-shaped areas placed within the level editor. Each changes gameplay, visuals, audio, or state when a player is within its bounds.

**Shape** *enum* (``Box``, ``Sphere``): Shape of the volume. This setting only appears on volumes that support both shapes.

**Falloff** *float*: Distance inward from the edge before the volume reaches full intensity. Both ambiance and oxygen volumes support this setting.

Gameplay
--------

Deadzone
````````

Gives players radiation via lowering their virus / infection stats. Can be counteracted when they wear protective clothing.

**Deadzone Type** *enum* (``Default Radiation``, ``Full Suit Radiation``): Protection level that players need. Default radition will require a gasmask with filters. Full suit radiation requires a gasmask an full body suit.

**Damage per Second (Unprotected)** *float*: Damage dealt each second to players without protection. Defaults to ``0``.

**Damage per Second (Protected)** *float*: Damage dealt each second to players who have protection. Defaults to ``0``.

**Radiation per Second** *float*: Radiation (virus/infection) damage dealt each second to players without protection.

**Mask Filter Degradation per Second** *float*: How fast an equipped gasm ask filter loses quality. Defaults to ``0.4``.

Horde Purchase
``````````````
Area where players can buy an item in Horde mode. This level mode has been deprecated.

**Item ID** *uint16*: Legacy ID of the item to sell.

**Cost** *uint32*: Price of the item.

Kill
````

Instantly kills entities that enter the volume.

**Kill Players** *bool*: Kill players. Defaults to ``true``.

**Kill Zombies** *bool*: Kill zombies. Defaults to ``true``.

**Kill Animals** *bool*: Kill animals. Defaults to ``true``.

**Kill Vehicles** *bool*: Destroy vehicles. Defaults to ``false``.

**Death Cause** *enum*: Death cause reported for killed players, for example in the death message. Defaults to ``BURNING``.

No Structures
`````````````

Stops structures from being placed inside the volume.

Oxygen
``````

Overrides whether players can breathe inside the volume.

**Is Breathable** *bool*: If true, players can breathe within the volume. If false, oxygen is depleted. Defaults to ``true``.

Safezone
````````

Protected zone where hostile actions are restricted.

**No Weapons** *bool*: Players inside cannot use weapon items. Defaults to ``true``.

**No Buildables** *bool*: Players cannot place barricades or structures inside. Defaults to ``true``.

**No Incoming Damage** *bool*: Players inside cannot take damage, unless the source bypasses safezones. Defaults to ``true``.

Teleporter Entrance
```````````````````

Teleports players who enter the volume to a Teleporter Exit with a matching ID.

**Pair ID** *string*: ID of the Teleporter Exit to send players to.

Teleporter Exit
```````````````

Exit for Teleporter Entrance volumes.

**ID** *string*: ID that Teleporter Entrances use to find this exit.

Underground Whitelist
`````````````````````

Designates areas where players are allowed to be when below the terrain surface. This is only applied when enabled in the :ref:`Level Config <doc_mapping_config>`. When outside of a whitelist volume, the player will be teleported to the surface.

Arena Mode Compactor
````````````````````

Sphere only. Sets the starting circle in Arena mode. When the map has more than one of these, one is picked at random each round.

NPCs
----

NPC Overlap
```````````

Area that triggers the ``Volume_Overlap`` :ref:`NPC condition <doc_npc_asset_conditions>`. 

**ID** *string*: ID that ``Condition_#_VolumeID`` refers to.

NPC Reward
``````````

Grants a :ref:`Rewards List Asset <doc_npc_asset_rewards_list>` to players who enter the volume, if the asset's conditions are met.

**Asset GUID** :ref:`doc_data_guid`: GUID of the rewards list asset.

**Affect Vehicle Passengers** *bool*: If true, pasengers of vehicles are granted the rewards list. Defaults to ``false``.

Environment
-----------

Ambiance
````````

Overrides ambient audio, fog, lighting, and weather within the volume.

**Effect ID** :ref:`doc_data_guid` or *uint16*: :ref:`Effect Asset <doc_assets_effect>` played as ambient audio while inside.

**No Water** *bool*: Hides the water surface while inside.

**No Lighting** *bool*: Turns off level lighting while inside. Useful for dark interiors.

**Weather Mask** :ref:`Bitmask <doc_data_bitmask>`: Weather only blends in while inside if its ``Volume_Mask`` shares a bit with this mask.

**Override Fog** *enum* (``None``, ``Constant``, ``PerTimeOfDay``): Whether the volume overrides fog.

**Fog Time** *enum*: Picks which time of day the fog color and intensity fields edit when using ``PerTimeOfDay``.

**Fog Color** :ref:`color <doc_data_color>`: Color of the overridden fog.

**Fog Intensity** ``Fog_Intensity`` *float*: Strength of the overridden fog.

**Override Atmospheric Fog** *bool*: Also override atmospheric (sky) fog.

**Use Falloff** *bool*: If true, blends by distance using **Falloff**. If false, blends over time using the fade durations below.

**Priority** *int*: Volumes with higher priority override volumes with lower priority where they overlap.

**Audio Fade-In** / **Audio Fade-Out** *float*: Seconds to fade audio in and out when **Use Falloff** is off. Both default to ``2``.

**Fog Fade-In** / **Fog Fade-Out** *float*: Seconds to fade fog in and out when **Use Falloff** is off. Default to ``20`` and ``8``, respectively.

**Lighting Fade-In** / **Lighting Fade-Out** *float*: Seconds to fade lighting in and out when **Use Falloff** is off. Both default to ``4``.

Effect
``````

Box only. Spawns an :ref:`Effect Asset <doc_assets_effect>` scaled to fill the volume.

**Effect ID** :ref:`doc_data_guid` or *uint16*: Effect to spawn. GUID usage is recommended.

**Emission Rate** *float*: Multiplier for the particle system's max particles and emission rate. Defaults to ``1``.

**Audio Range** *float*: Sets the max distance of the effect's audio source. Defaults to ``1``.

Foliage
```````

Controls where foliage can be placed / baked.

**Mode** *enum* (``Additive``, ``Subtractive``): Additive volumes allow foliage to be baked inside. Subtractive volumes stop foliage from baking inside.

**Instanced Meshes** *bool*: Affects instanced mesh foliage such as grass. Defaults to ``true``.

**Resources** *bool*: Affects resource foliage such as trees and rocks. Defaults to ``true``.

**Objects** *bool*: Affects object foilage. Defaults to ``true``.

Water
`````

A body of water that players can interact with.

**Surface Visible** *bool*: Shows the water surface. Defaults to ``true``.

**Reflection Visible** *bool*: Enables planar reflections on the surface. Defaults to ``false``.

**Sea Level** *bool*: Marks this as the level's sea level volume.

**Refill Type** *enum* (``Clean``, ``Salty``, ``Dirty``): Type of water given when refilling canteens from this volume. Defaults to ``Salty``.

**Fish** :ref:`doc_data_guid`: Spawn table for fish caught in this volume. Requires ``Supports_Fishing_Volumes`` in the :ref:`Level Asset <doc_assets_level:supports_fishing_volumes>`.

**Fishing Minimum Depth Override** *float*: If set, the water at the bobber must be deeper than this to catch fish.

Miscellaneous 
-------------

Cartography (GPS/Chart)
```````````````````````

Box only. Sets the area captured for the GPS and Chart map images.

Manual Object Culling
`````````````````````

Hides the objects inside it when the player is farther away than the cull distance. See :ref:`Manual Object Culling <doc_mapping_culling>`.

**Cull Distance** *float*: Distance from the volume's center which its objects are hidden. Defaults to ``64``.

**Include Large Objects** *bool*: Also culls objects of type ``Large``, such as shipping containers. Defaults to ``false``.

Navmesh Clip
````````````

Solid volume that blocks zombie navigation.

Player Clip
```````````

Invisible solid that blocks player movement.

**Block Player** *bool*: If false, the volume no longer blocks players but will prevent buildables from being placed within it. Defaults to ``true``.