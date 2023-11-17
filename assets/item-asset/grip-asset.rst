.. _doc_item_asset_grip:

Grip Assets
===========

Grip attachments are inventory items that can be attached to ranged weapons.

This inherits the :ref:`CaliberAsset <doc_item_asset_caliber>` class.

Game Data File
--------------

Item Asset Properties
`````````````````````

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Grip``)

**ID** *uint16*: Must be a unique identifier.

Grip Asset Properties
`````````````````````

.. list-table::
   :widths: 40 40 20
   :header-rows: 1
   
   * - Property Name
     - Type
     - Default Value
   * - :ref:`Bipod <doc_item_asset_grip_property_bipod>`
     - :ref:`flag <doc_data_flag>`
     - n/a

Property Descriptions
`````````````````````

.. _doc_item_asset_grip_property_bipod:

Bipod :ref:`flag <doc_data_flag>`
::::::::::::::::::::::::::::::::::::::::::

Stat-changing properties should only take place while prone.