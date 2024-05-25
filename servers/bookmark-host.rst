.. _doc_servers_bookmark_host:

Bookmark Host
=============

Configuring the **Bookmark Host** property along with a :ref:`Login Token <doc_servers_gslt>` enables the bookmark button, allowing players to find your server even after an IP or port change.

By default the game supports Steam's built-in Favorites and History server lists. These lists remember your server by the combination of IPv4 address and port, so if your address or port change the link is broken. Steam mitigates this if you have a :ref:`GSLT <doc_servers_gslt>` assigned by automatically updating the saved address, but this doesn't happen in realtime. These lists also aren't compatible with the newer :ref:`Fake IP<doc_servers_fake_ip>` feature.

Considering the trend toward Fake IP, a replacement was necessary, not to mention a popular request from server hosts. Thankfully, with GSLTs in widespread use now and providing a stable persistent ID, the client can save custom per-server bookmark data. The intention is to make bookmarks a better alternative to the legacy favorites/history lists, including proper support for IPv6 at some point. At the time of writing (2024-05-24) the client doesn't save history using the bookmark host property yet, but it should be added once more hosts opt-in.

To enable bookmarking, set ``BookmarkHost`` in your server's ``Config.json`` file to one of these formats:

1. A DNS entry with an ``A`` record pointing to your server's public IP. For example, if you own the "example.com" domain you could add an A record "myunturnedserver" pointing at your game server IP and set ``BookmarkHost`` to "myunturnedserver.example.com". In this case the client will save your server's current port number, so the IP address can change but the port can't. If your server doesn't have a static public IP you could use dynamic DNS to update the DNS record periodically. Note that this option is inapplicable for servers using Fake IP because both the IP and port are randomly assigned after each restart.

2. The URL of a custom web API to return the address, and optionally the port. Clients perform a GET request if ``BookmarkHost`` begins with "http://" or "https://". The response should be plain text. Examples of valid responses include:

    - 127.0.0.1
    - 127.0.0.1:27015
    - myunturnedserver.example.com
    - myunturnedserver.example.com:27015

  The hosts of Pandahut have generously shared an example implementation consisting of a server plugin which updates the latest server address on a custom backend, and a web request handler to serve the latest address to clients. Note that we don't necessarily recommend using this program as-is, it's just an example: `BookmarkHostPlugin by PandahutMushy <https://github.com/PandahutMushy/BookmarkHostPlugin>`_
