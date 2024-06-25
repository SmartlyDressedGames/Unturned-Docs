.. _doc_asset_redirector:

Redirector Assets
=================

**Redirector Assets** are a special asset type only used when resolving asset references (GUIDs and legacy IDs). When an asset reference points to a redirector, the asset system instead returns the asset pointed to by the redirector.

.. note:: Most features do not save the resolved asset, instead they save the original asset reference. This means, for example, that redirecting some objects and re-saving a level will save the original object references, not the redirected objects.

Game Data File
--------------

.. list-table::
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`AssetCategory <doc_asset_redirector:assetcategory>`
     - :ref:`enum <doc_data_builtin_types>`
     - ``None``
   * - :ref:`TargetAsset <doc_asset_redirector:targetasset>`
     - :ref:`GUID <doc_data_guid>`
     - Required

.. _doc_asset_redirector:assetcategory:

AssetCategory :ref:`enum <doc_data_builtin_types>` ``None``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If set, a legacy ID can be redirected as well. For example, a redirector with legacy ID of ``4`` and ``AssetCategory Item`` would be found when using ``/give 4``.

.. _doc_asset_redirector:targetasset:

TargetAsset :ref:`GUID <doc_data_guid>`
:::::::::::::::::::::::::::::::::::::::

GUID of actual asset to use when an asset reference points to the redirector asset.
