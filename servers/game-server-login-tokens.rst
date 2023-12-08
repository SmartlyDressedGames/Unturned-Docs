.. _doc_servers_gslt:

Game Server Login Tokens
========================

Unturned dedicated servers can be logged-in to Steam using a **Game Server Login Token** or **GSLT**. This provides a few benefits:

#. If using Server Codes to connect, your code will remain linked to your GSLT between sessions. Otherwise, each time you start the server you will need to send your friends the new code.
#. Servers without a GSLT are considered "anonymous" and are hidden from the Internet server list.
#. Steam tracks your Favorites and History lists by address and port, but with a GSLT it can automatically transfer them if the server details change. This should happen within approximately 24 hours. (Verified in `issue #3980 <https://github.com/SmartlyDressedGames/Unturned-3.x-Community/issues/3980>`_ thanks to CyberAndrii and joeymisfit, and on `AlliedModders <https://forums.alliedmods.net/showthread.php?p=2529549#post2529549>`_.)

Creating GSLTs
--------------

You can manually create GSLTs while logged in with your Steam account here: https://steamcommunity.com/dev/managegameservers

Use Unturned's app ID ``304930``, and a memo to remind you which server the token is for.

Unturned Configuration
----------------------

The GSLT can be set in one of two places depending on your preference:

- With the ``Login_Token`` property in each server's ``Config.json`` file under the ``Browser`` section.

OR

- Using the ``GSLT`` command during startup. This can be specified in the ``Commands.dat`` file or on the command-line.

Automating GSLTs
----------------

Valve provides an ``IGameServersService`` web API for managing GSLTs. Consult their documentation here: https://partner.steamgames.com/doc/webapi/IGameServersService
