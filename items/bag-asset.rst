.. _doc_item_asset_bag:

Bag Assets
==========

The ItemBagAsset class is a base class that other classes are derived from. It is unusable on its own.

Game Data File
--------------

The ItemBagAsset class inherits properties from the :ref:`ItemClothingAsset <doc_item_asset_clothing>` class.

Properties
``````````

.. list-table::
   :widths: 40 40 20
   :header-rows: 1
   
   * - Property Name
     - Type
     - Default Value
   * - :ref:`Height <doc_item_asset_bag:height>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Width <doc_item_asset_bag:width>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``0``

Property Descriptions
`````````````````````

.. _doc_item_asset_bag:height:

Height :ref:`uint8 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::

Number of rows (vertical storage space).

----

.. _doc_item_asset_bag:width:

Width :ref:`uint8 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::

Number of columns (horizontal storage space).