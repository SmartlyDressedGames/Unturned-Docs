Command-line arguments
======================

Game options
------------

Some command-line arguments are primarily intended for use with the Unturned Dedicated Server app.

**+connect**: Connect to a server, in the format of `+connect <ip address>:<port>`.

**-FullscreenMode=**: Window mode override.

**-FallbackGizmos**: Use 3D Unity line renderer component for debug visualization rather than pixel-perfect lines. Performance with these is lower than the default, so only intended for cases where the default is unimplemented.

**-FrameRateLimit=** *int*: Overrides the frame rate limit specified in the display menu. Negative values disable the limit. Useful if game is running at thousands of FPS on the loading screen and overheats.

**-GameSense**: GameSense integration.

**-Glazier=** *enum* (`IMGUI`): Use the legacy IMGUI rather than the default uGUI.

**-h** *int*: Alias of `-height`.

**-height** *int*: Override in-game resolution height.

**-Holiday=** *enum* (`AprilFools`, `Christmas`, `Halloween`, `HW`, `XMAS`): Override the active holiday.

**-HostPlayerLimit=** *int*: Clamps max number of players to this number. Useful for hosting providers.

**-LegacyConsole**: Use the legacy console rather than the default threaded console.

**-LogAssemblyResolve**: Log when the resolution of an assembly fails. Useful when working with non-Rocket plugins.

**-NetTransport=** *enum* (`SteamNetworking`, `SteamNetworkingSockets`): SteamNetworkingSockets was used to enable the [ISteamNetworkingSockets](https://partner.steamgames.com/doc/api/ISteamNetworkingSockets) networking API, but this has since become default. SteamNetworking can be used to revert to the older, deprecated [ISteamNetworking](https://partner.steamgames.com/doc/api/ISteamNetworking) networking API.

**-NoDefaultLog**: Disables log file creation unless a plugin calls setLogFilePath.

**-NoDeferAssets**: Disable the deferring of loading vehicles and level objects until map load time, and instead load on startup.

**-NoSteamTextFiltering**: Disable Steam text filter, and instead revert to the old naïve filter.

**-NoWorkshopSubscriptions**: Disable loading of all Steam Workshop subscriptions. This can be helpful when troubleshooting issues.

**-OfflineOnly**: Disables requests to the internet. For LAN servers, it skips the Steam backend connection and uses locally-cached Workshop items.

**-RazerChroma**: Enable Razer Chroma integration on compatible devices.

**-RefreshRate=**: Monitor refresh rate override.

**-SkipAssets**: Disable loading asset bundles and Workshop content. This is useful for quickly iterating on serverside code.

**-ui_scale**: UI scale override. A common usage is to set UI scale back to its default scaling, with `-ui_scale 1`.

**-ValidateAssets**: Perform [additional health checks](AssetValidation.md) on assets during start-up.

**-w** *int*: Alias of `-width`.

**-width** *int*: Override in-game resolution width.

Unity options
-------------

Unity's built-in command-line arguments take priority over *Unturned*'s equivalents. Some of the more relevant Unity arguments are mentioned below, but the rest can be found in the [Unity User Manual](https://docs.unity3d.com/2019.4/Documentation/Manual/CommandLineArguments.html).

**-batchmode**: Run in batch mode.

**-force-glcore**: Force OpenGL.

**-force-vulkan**: Force Vulkan.

**-nographics**: Do not initialize the graphics device when running in batch mode.
