# Command-line arguments

Unity's built-in command-line arguments take priority over *Unturned*'s equivalents. Some of the more relevant Unity arguments are mentioned below, but the rest can be found in the [Unity User Manual](https://docs.unity3d.com/Manual/CommandLineArguments.html).

Some command-line arguments are primarily intended for use with the Unturned Dedicated Server app.

**-AggressiveGC**: Force frequent garbage collection.

**-batchmode**: Run in batch mode.

**+connect**: Connect to a server, in the format of `+connect <ip address>:<port>`.

**-ConstNetEvents**: Debug whether plugins are writing to the network buffers.

**force-d3d11-bltblt-mode=**: Fallback to using the Windows 7-style BltBlt model for D3D11, instead of DXGI Flip Model Swapchain. This will hurt performance, but may fix some instances of crashing related to D3D11.

**-force-glcore**: Force OpenGL.

**-FullscreenMode=**: Window mode override.

**-GameSense**: GameSense integration.

**-Glazier=** *enum* (`IMGUI`): Use the legacy IMGUI rather than the default uGUI.

**-h** *int*: Alias of `-height`.

**-height** *int*: Override in-game resolution height.

**-HostPlayerLimit=** *int*: Clamps max number of players to this number. Useful for hosting providers.

**-LegacyConsole**: Use the legacy console rather than the default threaded console.

**-LogAssemblyResolve**: Log when the resolution of an assembly fails. Useful when working with non-Rocket plugins.

**-NetTransport=** *enum* (`SteamNetworking`, `SteamNetworkingSockets`): SteamNetworkingSockets was used to enable the [ISteamNetworkingSockets](https://partner.steamgames.com/doc/api/ISteamNetworkingSockets) networking API, but this has since become default. SteamNetworking can be used to revert to the older, deprecated [ISteamNetworking](https://partner.steamgames.com/doc/api/ISteamNetworking) networking API.

**-NoDefaultLog**: Disables log file creation unless a plugin calls setLogFilePath.

**-NoDeferAssets**: Disable the deferring of loading vehicles and level objects until map load time, and instead load on startup.

**-nographics**: Do not initialize the graphics device when running in batch mode.

**-OfflineOnly**: Disables requests to the internet. For LAN servers, it skips the Steam backend connection and uses locally-cached Workshop items.

**-RazerChroma**: Enable Razer Chroma integration on compatible devices.

**-RefreshRate=**: Monitor refresh rate override.

**-SNS_AllowWithoutAuth**: Allow Steam Networking Sockets connection without authentication. This was originally added as a potential workaround for a OpenSSL regression that has since been fixed by Steam.

**-SkipAssets**: Disable loading asset bundles and Workshop content. This is useful for quickly iterating on serverside code.

**-ui_scale**: UI scale override. A common usage is to set UI scale back to its default scaling, with `-ui_scale 1`.

**-ValidateAssets**: Perform [additional health checks](AssetValidation.md) on assets during start-up.

**-w** *int*: Alias of `-width`.

**-width** *int*: Override in-game resolution width.
