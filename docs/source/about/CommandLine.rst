.. _doc_commandline:

Command-line arguments
======================

You can add command-line arguments within Steam:
1. Right-click Unturned in your Steam Library
2. Select Properties... > General
3. Find the Launch Options field
4. Type options separated by spaces. For example "-FallbackGizmos -Width=1920 -Height=1080" will enable the FallbackGizmos flag, set Width to 1920 and set Height to 1080.

Game options
------------

Some command-line arguments are primarily intended for use with the Unturned Dedicated Server app.

**+connect**: Connect to a server, in the format of ``+connect <ip address>:<port>``.

**-DisableCullingVolumes**: Disable object culling distance overrides. Please refer to :ref:`Manual Object Culling <doc_mapping_culling>` for more details.

**-DisableLightLODs**: Disable fadeout of dynamic lights. Could be useful for high-quality screenshots.

**-FullscreenMode=**: Window mode override.

**-FallbackGizmos**: Use 3D Unity line renderer component for debug visualization rather than pixel-perfect lines. Performance with these is lower than the default, so only intended for cases where the default is unimplemented.

**-FarClipDistance** *float*: [16.0, 2048.0] overrides the maximum draw distance in the graphics menu. By default the lowest max draw distance is 614.4 meters which is slightly higher than the network distance of 512.0 meters. Useful for players who are willing to gain performance at a significant gameplay disadvantage.

**-ForceTrustClient**: Disables movement validation (e.g., position difference between ticks matches speed) for vehicles. Using this is not recommended! It is easier for cheaters to fly cars with movement limits disabled. This flag should eventually be removed when(/if) vehicle movement is made server authoritative.

**-FrameRateLimit=** *int*: Overrides the frame rate limit specified in the display menu. Negative values disable the limit. Useful if game is running at thousands of FPS on the loading screen and overheats.

**-GameSense**: GameSense integration.

**-Glazier=** *enum* (``IMGUI``): Use the legacy IMGUI rather than the default uGUI.

**-h** *int*: Alias of ``-height``.

**-height** *int*: Override in-game resolution height.

**-Holiday=** *enum* (``AprilFools``, ``Christmas``, ``Halloween``, ``HW``, ``Valentines``, ``XMAS``): Override the active holiday.

**-HostPlayerLimit=** *int*: Clamps max number of players to this number. Useful for hosting providers.

**-LegacyConsole**: Use the legacy console rather than the default threaded console.

**-LogAssemblyResolve**: Log when the resolution of an assembly fails. Useful when working with non-Rocket plugins.

**-LogLevelBatchingTextureAtlasExclusions**: Please refer to :ref:`Level Batching <doc_mapping_batching>` for more details.

**-NetTransport=** *enum* (``SteamNetworking``, ``SteamNetworkingSockets``): SteamNetworkingSockets was used to enable the `ISteamNetworkingSockets <https://partner.steamgames.com/doc/api/ISteamNetworkingSockets>`_ networking API, but this has since become default. SteamNetworking can be used to revert to the older, deprecated `ISteamNetworking <https://partner.steamgames.com/doc/api/ISteamNetworking>`_ networking API.

**-NoDefaultLog**: Disables log file creation unless a plugin calls setLogFilePath.

**-NoDeferAssets**: Disable the deferring of loading vehicles and level objects until map load time, and instead load on startup.

**-NoSteamTextFiltering**: Disable Steam text filter, and instead revert to the old naïve filter.

**-NoWorkshopSubscriptions**: Disable loading of all Steam Workshop subscriptions. This can be helpful when troubleshooting issues.

**-OfflineOnly**: Disables requests to the internet. For LAN servers, it skips the Steam backend connection and uses locally-cached Workshop items.

**-PreviewLevelBatchingTextureAtlas**: Please refer to :ref:`Level Batching <doc_mapping_batching>` for more details.

**-RazerChroma**: Enable Razer Chroma integration on compatible devices.

**-RefreshRate=**: Monitor refresh rate override.

**-SkipAssets**: Disable loading asset bundles and Workshop content. This is useful for quickly iterating on serverside code.

**-ui_scale**: UI scale override. A common usage is to set UI scale back to its default scaling, with ``-ui_scale 1``.

**-UseLevelBatching** *bool*: Overrides whether level batching can be enabled. Per-level support for level batching is still required. For example ``-UseLevelBatching=false`` disables it. Please refer to :ref:`Level Batching <doc_mapping_batching>` for more details.

**-ValidateAssets**: Perform :ref:`additional health checks <doc_asset_validation>` on assets during start-up.

**-ValidateLevelBatchingUVs**: Please refer to :ref:`Level Batching <doc_mapping_batching>` for more details.

**-w** *int*: Alias of ``-width``.

**-width** *int*: Override in-game resolution width.

Unity options
-------------

Unity's built-in command-line arguments take priority over *Unturned*'s equivalents. Some of the more relevant Unity arguments are mentioned below, but the rest can be found in the `Unity User Manual <https://docs.unity3d.com/2019.4/Documentation/Manual/PlayerCommandLineArguments.html>`_.

**-batchmode**: Run in batch mode.

**-force-glcore**: Force OpenGL.

**-force-vulkan**: Force Vulkan.

**-nographics**: Do not initialize the graphics device when running in batch mode.
