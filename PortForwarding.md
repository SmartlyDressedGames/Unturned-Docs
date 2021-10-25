Port Forwarding
===============

When hosting a server on a home network __port forwarding__ is required in order to direct traffic to the host computer. One way to think of it is that when there are multiple devices (e.g. computers and phones) connected to the LAN, the outside internet does not know which device is the Unturned server. In this case port forwarding specifies which LAN device is the host.

Two pieces of information: the port range and local device address are required prior to port forwarding, and are described in detail below.

Port Range
----------

Each Unturned server uses two consecutive ports while running. The first is used for game traffic and for server list queries, and the second for communicating with the Steam backend services.

By default 27015 and 27016 are used. Setting a different value with the `Port` command uses that value, value + 1. Recommended `Port` command settings are 27015 for the first server, 27017 for the second server, 27019 for the third server, so on and so forth.

Local Device Address
--------------------

Forwarding the ports directs them to a LAN address, i.e. the computer hosting the server. To determine the local IP on Windows:

1. Press Windows + R to open the Run dialog.
2. Type `cmd` and press enter.
3. Type `ipconfig` in the command prompt and press enter.
4. Find the `Wireless LAN adapter Wi-Fi` or `Ethernet adapter Ethernet` header.
5. Look for the `IPv4 Address` value and make note of it. This is the local address to forward the ports to. It likely looks something like `192.168.0.6`.

How to Forward Ports
--------------------

Instructions vary by router, but should be doable from the web browser without any extra tools or software. This third-party website has a thorough list of routers with simple steps for each model: https://portforward.com/router.htm

In general the steps are along the lines of:

1. Connect to router via web browser.
2. Login with home admin credentials.
3. Find Port Forwarding menu.
4. Find the option to add a new rule.
5. Name the new rule something related to Unturned for reference.
6. Input 27015 as the starting port(s) and 27016 as the ending port(s).

	On some routers it might not be possible to input multiple ports within a single rule. In that case multiple rules can be setup; one for each of the ports.
7. Enable TCP and UDP protocols.
8. Set destination internal IP to the local host address.
9. Save the new rule.
