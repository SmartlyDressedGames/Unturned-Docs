.. _doc_servers_gslt:

Game Server Login Tokens
========================

Beginning in version 3.20.4.0 Unturned dedicated servers can be authenticated using a **Game Server Login Token** or **GSLT**. After version 3.21.31.0 anonymous servers (without GSLT) are hidden from the internet server list.

An additional benefit of using GSLTs is the automatic transfer of favorites and history if the server address changes. This should happen within approximately 24 hours. (Verified in `issue #3980 <https://github.com/SmartlyDressedGames/Unturned-3.x-Community/issues/3980>`_ and on `AlliedModders <https://forums.alliedmods.net/showthread.php?p=2529549#post2529549>`_, thanks to CyberAndrii and joeymisfit.)

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
