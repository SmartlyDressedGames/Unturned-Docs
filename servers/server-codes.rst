.. _doc_servers_server_codes:

Server Codes
============

A **Server Code** is a randomly generated, 17-digit numeric code assigned to your server. Your friends can join your multiplayer server by inputting its **Server Code** in the Connect Directly menu without you needing to :ref:`port forward <doc_servers_port_forward>`.

You can find your Server Code in the Server Console after your server finishes loading. Run the ``CopyServerCode`` command from the Server Console to easily copy that code to your clipboard.

Limitations
-----------

The primary downside of Server Codes is their incompatibility with the pre-joining server info screen (which displays things like the server name, installed mods, current players, and other details). The info screen uses Steam's A2S protocol, which can only be queried by IP, so joining by Server Code enters the server immediately instead. You can enable :ref:`Fake IP<doc_servers_fake_ip>` to work around this limitation.

Your server's Server Code will change each time your server restarts. You can assign a :ref:`Game Server Login Token <doc_servers_gslt>` to keep your Server Code linked between sessions.

How does it work?
-----------------

Connecting by Server Code utilizes `Steam Datagram Relay (SDR) <https://partner.steamgames.com/doc/features/multiplayer/steamdatagramrelay>`_. To quote that page:

	*Relaying the traffic protects your servers and players from DoS attack, because IP addresses are never revealed. All traffic you receive is authenticated, encrypted, and rate-limited. Furthermore, for a surprisingly high number of players, we can also find a faster route through our network, which actually improves player ping times.*
