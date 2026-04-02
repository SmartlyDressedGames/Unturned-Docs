.. _doc_item_fishing_catchable_properties:

Fishing Catchable Properties
============================

These options are specified in an item's :ref:`Fishing_Catchable<doc_item_asset_intro:fishing_catchable>` :ref:`Dictionary<doc_data_file_format>`.

**Capture_Duration** *float*: How long the player must keep the item within the cursor before it's caught. Defaults to 2 seconds.

**Escape_Duration** *float*: How long before the item gets away. Defaults to 2 seconds.

**Spring_Stiffness** *float*: Scales acceleration toward target position (without exceeding limits). Defaults to 16.

**Spring_Damping** *float*: Reduces speed toward target position. Defaults to 4.

**Min_Relocate_Interval** *float*: Minimum seconds before target position changes. Defaults to 1.5 seconds.

**Max_Relocate_Interval** *float*: Maximum seconds before target position changes. Defaults to 2 seconds.

**Max_Upward_Acceleration** *float*: Upward acceleration cannot increase beyond this limit. Defaults to 1.5.

**Max_Downward_Acceleration** *float*: Downward acceleration cannot increase beyond this limit. Defaults to 1.2.

**Max_Upward_Speed** *float*: Upward speed cannot increase beyond this limit. Defaults to 0.6.

**Max_Downward_Speed** *float*: Downward speed cannot increase beyond this limit. Defaults to 0.45.

**Upper_Restitution** *float*: How much velocity to preserve when bouncing off the top. Defaults to 0.6 (60%).

**Lower_Restitution** *float*: How much velocity to preserve when bouncing off the bottom. Defaults to 0.4 (40%).

**Min_Target_Delta** *float*: When choosing a new position, it will be at least this far away. Defaults to 0.3

**Max_Target_Delta** *float*: When choosing a new position, it will be at most this far away. Defaults to 0.4.

**Min_Target_Position** *float*: [0, 1] Minimum choosable position. Defaults to 0.1.

**Max_Target_Position** *float*: [0, 1] Maximum choosable position. Defaults to 0.9.

.. tip:: For example, the vanilla Lobster's configuration is:

	.. code-block:: unturneddat

		Fishing_Catchable
		{
			Min_Relocate_Interval 0.3
			Max_Relocate_Interval 1
			Max_Upward_Acceleration 1.3
			Max_Downward_Acceleration 1.75
			Max_Upward_Speed 0.5
			Max_Downward_Speed 1.2
			Upper_Restitution 0
			Lower_Restitution 2
			Min_Target_Delta 0.35
			Max_Target_Delta 0.4
			Min_Target_Position 0
			Max_Target_Position 0.4
			Capture_Duration 2.75
			Escape_Duration 1.25
			Spring_Stiffness 20
			Spring_Damping 4
		}
