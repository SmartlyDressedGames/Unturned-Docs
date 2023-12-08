.. _doc_servers_server_codes:

Server Codes
============

By default, your friends can join your server using its **Server Code** in the Connect menu without :ref:`port forwarding <doc_servers_port_forward>`.

The downside of Server Codes is they are incompatible with the pre-joining server info screen. The info screen uses Steam's A2S protocol, which can only be queried by IP, so joining by Server Code enters the server immediately. You can also enable :ref:`Fake IP<doc_servers_fake_ip>` to work around this limitation.

After startup, you can run the ``CopyServerCode`` command from the server console to copy the code to your clipboard.

.. note:: Without a :ref:`Login Token <doc_servers_gslt>` the Server Code will change each time your server restarts.
