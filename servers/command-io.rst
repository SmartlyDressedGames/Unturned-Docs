.. _doc_servers_command_io:

Command IO
==========

By default Unturned executes commands from console input, and logs information to console output. This can be overridden however, for example to interact with an external process or remote console.

To replace the vanilla implementation:

1. Create a class that implements the ICommandInputOutput interface.
2. Get the CommandWindow singleton from Dedicator.commandWindow.
3. Pass instance to CommandWindow.setIOHandler.
4. (Optional) Specify ``-NoDefaultConsole`` on the command-line to disable vanilla console.
