Dedicated Workshop Update Monitor
=================================

When hosting a server with content from the [Steam Workshop](https://steamcommunity.com/app/304930/workshop/) it may be desirable to restart the server when updates are released by creators. In particular, maps have their own version numbers which the server list uses to test compatibility before players connect.

By default the game monitors for changes to the hosted map. When a change is detected it notifies players via chat and shuts down the server after a timer. This can be overridden however, for example to notify players with a custom modal prompt and perform a custom restart process.

To replace the vanilla implementation:

1. Create a class that implements the IDedicatedWorkshopUpdateMonitor interface, or create a subclass of DedicatedWorkshopUpdateMonitor and override as-needed.
2. Bind the DedicatedWorkshopUpdateMonitorFactory.onCreateForLevel event and return the custom instance.
