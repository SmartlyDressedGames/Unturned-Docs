# Game Server Login Tokens

Beginning in version 3.20.4 Unturned dedicated servers can be authenticated using a **Game Server Login Token** or **GSLT**. Verified servers may be given preferential placement on the server list.

## Creating GSLTs

You can manually create GSLTs while logged in with your Steam account here: https://steamcommunity.com/dev/managegameservers

Use Unturned's app ID `304930`, and a memo to remind you which server the token is for.

## Unturned Configuration

The GSLT can be set in one of two places depending on your preference:

- With the `Login_Token` property in each server's `Config.json` file under the `Browser` section.

OR

- Using the `GSLT` command during startup. This can be specified in the `Commands.dat` file or on the command-line.

## Automating GSLTs

Valve provides an `IGameServersService` web API for managing GSLTs. Consult their documentation here: https://partner.steamgames.com/doc/webapi/IGameServersService
