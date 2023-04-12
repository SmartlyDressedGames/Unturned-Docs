**NOTICE:** *You are not reading the most up-to-date documentation. This file is old, and may not reflect the current modding or server capabilities. The latest documentation can be found at [Unturned Documentation](https://docs.smartlydressedgames.com/).*

*This file may be removed in the future. Refer to its more [up-to-date equivalent](https://docs.smartlydressedgames.com/en/stable/servers/game-server-login-tokens.html) instead.*

Game Server Login Tokens
========================

Beginning in version 3.20.4.0 Unturned dedicated servers can be authenticated using a **Game Server Login Token** or **GSLT**. After version 3.21.31.0 anonymous servers (without GSLT) are hidden from the internet server list.
After version 3.22.20.0 GSLT is required for direct connection (Internet servers only LAN servers work without).

Creating GSLTs
--------------

You can manually create GSLTs while logged in with your Steam account here: https://steamcommunity.com/dev/managegameservers

Use Unturned's app ID `304930`, and a memo to remind you which server the token is for.

Unturned Configuration
----------------------

The GSLT can be set in one of two places depending on your preference:

- With the `Login_Token` property in each server's `Config.json` file under the `Browser` section.

OR

- Using the `GSLT` command during startup. This can be specified in the `Commands.dat` file or on the command-line.

Automating GSLTs
----------------

Valve provides an `IGameServersService` web API for managing GSLTs. Consult their documentation here: https://partner.steamgames.com/doc/webapi/IGameServersService
