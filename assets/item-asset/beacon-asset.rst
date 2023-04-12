.. _doc_item_asset_beacon:

Beacon Assets
=============

Beacons are a placeable zombie horde spawners. Placing the beacon will start a horde event, which can be completed by killing a certain number of zombies without letting the beacon be destroyed.

This inherits the :ref:`BarricadeAsset <doc_item_asset_barricade>` class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Beacon``)

**Useable** *enum* (``Barricade``)

**Build** *enum* (``Beacon``)

**ID** *uint16*: Must be a unique identifier.

Beacon Asset Properties
-----------------------

**Wave** *uint16*: Number of zombies that must be killed to complete the beacon. If there are not enough zombies in the area for the horde event to be completed, zombies will respawn continuously. The final zombie spawned by a horde event is guaranteed to be a Mega Zombie. Defaults to 0.

**Rewards** *byte*: Number of items to drop upon successfully completing the beacon. When using ``Enable_Participant_Scaling true``, the number of rewards will scale based on the number of participants. Defaults to 0.

**Reward_ID** *uint16*: Legacy ID of the spawn table to use for the rewarded items. Defaults to 0.

**Enable_Participant_Scaling** *bool*: Whether or not zombie health, and rewards dropped, should scale based on the number of players. Zombie health scales linearly, which can be represented by ``(Initial Participants) × 1.5``. Reward scaling has diminishing returns, with an equivalent formula being ``7 * sqrt(Initial Participants)``. Defaults to true.
