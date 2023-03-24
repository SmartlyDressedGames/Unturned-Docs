.. _doc_data_guid:

GUID
====

Globally Unique Identifiers (**GUIDs**) are 32 hexadecimal digits used to identify assets. They are preferable to file names because the files can be moved without redirectors.

A useful tool for manually generating GUIDs is `guidgenerator.com <https://www.guidgenerator.com/>`_. Note that if the GUID property is omitted from an :ref:`asset v1 <doc_assets_v1>` file, then the game will automatically assign a random GUID during a successful load.

Legacy ids are 16 bits with a [0, 65535] range, whereas GUIDs are 128 bits with an unimaginably huge range. This allows them to be generated without coordination or registration between developers.
