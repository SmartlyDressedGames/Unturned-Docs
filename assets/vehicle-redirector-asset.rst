.. _doc_asset_vehicle_redirector:

Vehicle Redirector Assets
=========================

**Vehicle Redirector Assets** help consolidate legacy colored vehicle variants into a single vehicle asset.

Prior to the addition of paintable vehicles, it was common to create duplicates of a vehicle asset with the color being the only difference. One of many downsides with this approach was the increased hassle of keeping changes consistent between all of the variants, for example, when tuning physics. Vehicle redirector assets ensure compatibility with existing saves and content while merging colored vehicle variants into one unified asset.

Game Data File
--------------

.. list-table::
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`TargetVehicle <doc_asset_vehicle_redirector:targetvehicle>`
     - :ref:`Asset Pointer <doc_data_assetptr>`
     - Required
   * - :ref:`LoadPaintColor <doc_asset_vehicle_redirector:loadpaintcolor>`
     - :ref:`color <doc_data_color>`
     - N/A
   * - :ref:`SpawnPaintColor <doc_asset_vehicle_redirector:spawnpaintcolor>`
     - :ref:`color <doc_data_color>`
     - N/A

.. _doc_asset_vehicle_redirector:targetvehicle:

TargetVehicle :ref:`Asset Pointer <doc_data_assetptr>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::

Actual vehicle to use when attempting to load or spawn this asset.

.. _doc_asset_vehicle_redirector:loadpaintcolor:

LoadPaintColor :ref:`color <doc_data_color>`
::::::::::::::::::::::::::::::::::::::::::::

If set, overrides the default random paint color when loading a vehicle from a save file. Used to preserve colors of vehicles in existing saves.

.. _doc_asset_vehicle_redirector:spawnpaintcolor:

SpawnPaintColor :ref:`color <doc_data_color>`
:::::::::::::::::::::::::::::::::::::::::::::

If set, overrides the default random paint color when spawning a new vehicle. Optionally used to preserve colors of vehicles in spawn tables.
