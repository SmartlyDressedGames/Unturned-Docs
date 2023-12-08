.. _doc_servers_fake_ip:

Fake IP
=======

Using a Steam **Fake IP** allows players to join your server by IP address without :ref:`port forwarding <doc_servers_port_forward>`.

Unlike :ref:`Server Codes <doc_servers_server_codes>`, a server using Fake IP can be visible on the Internet server list (still without port forwarding) as long as you set a :ref:`Login Token <doc_servers_gslt>`.

To enable Fake IP, change ``Use_FakeIP`` from ``false`` to ``true`` in your server's ``Config.json`` file.

After startup, you can run the ``CopyFakeIP`` command from the server console to copy the IP and port to your clipboard. Pasting this into the Host field of the Connect menu automatically moves the port to the Port field.

Connecting by Fake IP utilizes `Steam Datagram Relay (SDR) <https://partner.steamgames.com/doc/features/multiplayer/steamdatagramrelay>`_. To quote that page: "Relaying the traffic protects your servers and players from DoS attack, because IP addresses are never revealed. All traffic you receive is authenticated, encrypted, and rate-limited. Furthermore, for a surprisingly high number of players, we can also find a faster route through our network, which actually improves player ping times."

The downside of Fake IP as opposed to port forwarding is that the address and port will change after every restart, so, for example, a domain name cannot be used without custom scripts.
