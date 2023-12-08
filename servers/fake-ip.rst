.. _doc_servers_fake_ip:

Fake IP
=======

Using a Steam **Fake IP** allows players to join your server by IP address without :ref:`port forwarding <doc_servers_port_forward>`.

One benefit of Fake IP over :ref:`Server Codes <doc_servers_server_codes>` is compatibility with the pre-joining server info screen. The info screen uses Steam's A2S protocol, which can only be queried by IP, so joining by Server Code enters the server immediately.

To enable Fake IP, change ``Use_FakeIP`` from ``false`` to ``true`` in your server's ``Config.json`` file.

After startup, you can run the ``CopyFakeIP`` command from the server console to copy the IP and port to your clipboard. Pasting this into the Host field of the Connect menu automatically moves the port to the Port field.
