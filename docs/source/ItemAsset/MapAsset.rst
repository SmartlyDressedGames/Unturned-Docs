Map Assets
==========

Maps and compasses provide the player with additional UI information for as long as they are in the player's inventory. They can neither be held nor equipped.

This inherits the `ItemAsset <README.rst>`_ class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to `GUID <GUID.rst>`_ documentation.

**Type** *enum* (``Map``, ``Compass``)

**ID** *uint16*: Must be a unique identifier.

Map Asset Properties
--------------------

**Enables_Map** *flag*: Provides access to a satellite map display.

**Enables_Chart** *flag*: Provides access to a chart map display.

**Enables_Compass** *flag*: Provides a compass HUD, and the ability to set visible waypoints on the map display.
