:orphan:

.. _doc_dat_editing_code:

Dat Editing Code
================

This document aims to clarify some of the thought process behind the "editable" and "metadata" additions to the ``UnturnedDat`` module.

We'll refer to ``DatValue``, ``DatDictionary``, and ``DatList`` as the "data classes." They were marked public in the first version of the ``UnturnedDat`` module. They have been kept public for backwards compatibility with user code, but use of ``IDatValue``, ``IDatDictionary``, and ``IDatList`` should be preferred where possible. This will allow us to more easily maintain compatibility if additional changes are necessary.

When parsing with metadata is enabled, the data classes are wrapped/proxied in ``*WithMetadata`` classes, and the ``*WithMetadata`` classes are inserted into the document hierarchy. Initially these were a subclass of the data class, but we wanted to keep the inheritance hierarchy shallow especially when adding the ``Editable*`` classes.

Along with editing support, we intend to use metadata for more descriptive asset parsing errors in the future.

Why not store metadata in data classes directly? We didn't want to introduce any overhead for players running without the ``-ParseAssetMetadata`` command-line flag. Also, not all nodes have metadata (only nodes created by the parser have metadata).

The ``IEditable*`` interfaces allow user code to modify documents while mostly preserving comments, white space, file layout, and line numbering.

``IEditable`` types wrap/proxy data similar to metadata. They store additional info like comment overrides, preferred line numbers, margins, and insertion order. This preserves any parsed metadata rather than clobbering it.

Edits modifying parsed data wrap ``*WithMetadata`` classes, whereas edits **adding** data wrap the data classes directly.

.. warning:: Comments are associated with the node following them. If a comment isn't associated with a node (separated by empty lines) it will be lost (currently). We could *potentially* work around this by adding a "FloatingComment" node type, but it's low priority.
