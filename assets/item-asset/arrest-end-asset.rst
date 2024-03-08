.. _doc_item_asset_arrest_end:

Arrest End Assets
=================

The ItemArrestEndAsset class is used for "releaser" items, which can remove a corresponding ":ref:`catcher <doc_item_asset_arrest_start>`" item that is restraining a player. An example of a vanilla releaser is the `Handcuffs Key <https://wiki.smartlydressedgames.com/wiki/Handcuffs_Key>`_.

Game Data File
--------------

Releasers inherit properties from the :ref:`ItemAsset <doc_item_asset_intro>` class. Any properties from parent classes that are required are listed in the table below.

.. list-table::
   :widths: 30 40 30
   :header-rows: 1
   
   * - Class
     - Property Name
     - Required Value
   * - :ref:`ItemAsset <doc_item_asset_intro>`
     - :ref:`GUID <doc_item_asset_intro:guid>`
     - 
   * - :ref:`ItemAsset <doc_item_asset_intro>`
     - :ref:`ID <doc_item_asset_intro:id>`
     - 
   * - :ref:`ItemAsset <doc_item_asset_intro>`
     - :ref:`Type <doc_item_asset_intro:type>`
     - ``Arrest_End``
   * - :ref:`ItemAsset <doc_item_asset_intro>`
     - :ref:`Useable <doc_item_asset_intro:useable>`
     - ``Arrest_End``

Properties
``````````

.. list-table::
   :widths: 40 40 20
   :header-rows: 1
   
   * - Property Name
     - Type
     - Default Value
   * - :ref:`Recover <doc_item_asset_arrest_end:recover>`
     - :ref:`uint16 <doc_data_builtin_types>`
     - ``0``

Property Descriptions
`````````````````````

.. _doc_item_asset_arrest_end:recover:

Recover :ref:`uint16 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::

Legacy ID of a corresponding :ref:`catcher <doc_item_asset_arrest_start>` item that can be unlocked with this item.