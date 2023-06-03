.. _doc_item_asset_tool:

Tool Assets
===========

Tools are a type of useable. The specific function of a tool significantly depends on the ``Useable`` property.

This inherits the :ref:`ItemAsset <doc_item_asset_intro>` class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Tool``): When intending to use a child class, refer to that class's documentation instead for the proper enumerator to use.

**Useable** *enum* (``Carjack``, ``Carlockpick``, ``Housing_Planner``, ``Walkie_Talkie``): When using the ``Carjack`` enumerator, the tool can be used on vehicles to launch them upwards into the air. When using ``Carlockpick``, the tool can be used once on any locked vehicle in order to forcefully unlock it. When using ``Housing_Planner``, the tool can be used to quickly access :ref:`structure pieces <doc_item_asset_structure>` from the player's own inventory. When using ``Walkie_Talkie``, the tool can be used to have long-distance voice chat communications with other players.

**ID** *uint16*: Must be a unique identifier.

Tool Asset Properties
---------------------

Tools have no unique asset properties. Instead, refer to ``Useable`` for relevant configuration options. Refer to parent classes for additional properties.