.. _doc_item_asset_vehicle_lockpick_tool:

Vehicle Lockpick Tool Assets
=============================

Vehicle lockpick tools are created from the ItemVehicleLockpickToolAsset class. They are useables for unlocking a vehicle.

This inherits the :ref:`ToolAsset <doc_item_asset_tool>` class.

Vehicle Lockpick Tool Asset Properties
--------------------------------------

**FailureProbability** *float*: Normalized percentage chance of lockpicking failing. Defaults to zero. The "Use_Failure" animation is played instead of "Use" if lockpicking fails.

**FailureEffect** :ref:`doc_data_assetptr`: Effect to play when lockpicking fails.
