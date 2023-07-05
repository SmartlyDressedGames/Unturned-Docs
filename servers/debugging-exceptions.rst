.. _doc_debugging_exceptions:

Debugging Exceptions
====================

In release builds it can be difficult to narrow down exactly what's causing an exception. Thanks to `DiFFoZ post here <https://github.com/SmartlyDressedGames/Unturned-3.x-Community/issues/3979#issuecomment-1620788082>`_ for sharing a technique to find the line number, summarized here for posterity:

#. Unity logs an IL offset in square brackets to the ``Player.log`` file. This is not included in the stack trace sent to the game for the ``Client.log`` file unfortunately. For example 0x003db in this log:

	.. code-block:: text

		at SDG.Unturned.ResourceSpawnpoint..ctor (System.Byte newType, System.UInt16 newID, System.Guid newGuid, UnityEngine.Vector3 newPoint, System.Boolean newGenerated, SDG.Unturned.NetId netId) [0x003db] in <08e91a6d9e1d4bd5bf2e982fa4148205>:0
		                                                                                                                                                                                              ^^^^^^^^^

#. Open the related assembly (in this case ``Assembly-CSharp.dll``) in a c# decompiler like DnSpy or ILSpy.
#. In ILSpy use ``Search`` (Ctrl+Shift+F) to find the method from the stack trace.
#. Change display mode to ``IL with C#``.
#. Find related line, ``IL_03db`` in the 0x003db example case.
