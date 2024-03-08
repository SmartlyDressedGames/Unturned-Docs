.. _doc_item_asset_arrest_start:

Arrest Start Assets
===================

The ItemArrestStartAsset class is used for "catcher" items, which can restrain a player. Its sister item, the ":ref:`releaser <doc_item_asset_arrest_start>`", can be used to unlock restraints. Some examples of vanilla catchers include the `Handcuffs <https://wiki.smartlydressedgames.com/wiki/Handcuffs>`_ and `Cable Tie <https://wiki.smartlydressedgames.com/wiki/Cable_Tie>`_.

Game Data File
--------------

Catchers inherit properties from the :ref:`ItemAsset <doc_item_asset_intro>` class. Any properties from parent classes that are required are listed in the table below.

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
     - ``Arrest_Start``
   * - :ref:`ItemAsset <doc_item_asset_intro>`
     - :ref:`Useable <doc_item_asset_intro:useable>`
     - ``Arrest_Start``

Properties
``````````

.. list-table::
   :widths: 40 40 20
   :header-rows: 1
   
   * - Property Name
     - Type
     - Default Value
   * - :ref:`Strength <doc_item_asset_arrest_start:strength>`
     - :ref:`uint16 <doc_data_builtin_types>`
     - ``0``

Property Descriptions
`````````````````````

.. _doc_item_asset_arrest_start:strength:

Strength :ref:`uint16 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::

Number of times a player must lean in order to break free from their restraints.