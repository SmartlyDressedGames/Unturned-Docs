.. _doc_server_hosting_rules:

Server Hosting Rules
====================

Server hosts are able to customize their server in order to offer a tailored gameplay experience to their players. This often includes adding new features, disabling vanilla content, or using custom rulesets. However, all servers must adhere to the rules outlined below.

Servers that violate these rules may be temporarily or permanently banned. To report a server for rule violations, or appeal a moderation decision applied to your server, you may file a ticket with SDG Support:

* `Report a server for breaking rules <https://support.smartlydressedgames.com/hc/en-us/requests/new?ticket_form_id=12189991924500>`_
* `Appeal a server report <https://support.smartlydressedgames.com/hc/en-us/requests/new?ticket_form_id=12189992633364>`_

`View Moderation List <https://smartlydressedgames.com/UnturnedHostBans/index.html>`_

Recent changes
--------------

**2024-06-03:** Scaled back the degree to which the server list is moderated. The previous level was untenable especially when considering anyone can freely create an unlimited number of servers, and the moderation system is duct-taped on top of the otherwise unmoderated Steam server list.

**2023-10-02:** Clarified on how subscriptions interact with currency.

**2023-08-17:** Added reasoning behind flagging servers using an anycast proxy.

**2023-02-15 revisions:** Many of the rules have been revised to be clearer, with regards to what is (or isn't) currently allowed. "Consumable microtransaction" is better defined, there are a couple of new examples, and deceptive pricing has its own dedicated a section. The monetization filter section also includes more information about the filter, its purpose, and which of the four options (including a newer "Monetized" option) your server should use.

**2022-10-16 clarification:** Selling *vanilla* cosmetics, such as those available from the Stockpile or Steam Community Market, is not allowed. When offering cosmetics as a server microtransaction, the server network should should own (or have licensed) the rights to that content. Servers should not sell cosmetic content that they do not own the right to, such as vanilla cosmetics (either official, or community-contributed).

Monetization Types
------------------

Hosts are not allowed to sell access to **vanilla** premium content. This includes the Gold Upgrade benefits as well as cosmetics and/or skins, such as those available on the Stockpile or Steam Community Market.

Monetization Filter
-------------------

Players can filter the in-game server list by this field. It is not required to configure this field, but ideally it should be set to whichever value accurately describes your server's monetization practices. When configured, this field must be configured truthfully.

``Unspecified``
```````````````

The "Monetization" field in each server's Config.json file defaults to ``Unspecified``. If you are unsure what to configure your server's monetization type as, then you can leave it unspecified.

``None``
````````

Servers that are entirely unmonetized, or only offer a donation option, can use the ``None`` value.

``NonGameplay``
```````````````

Servers that only offer microtransactions that do not provide a gameplay advantage can use the ``NonGameplay`` value. For example, selling custom weapon skins and chat colors would not be a gameplay advantage.

``Monetized``
`````````````

Servers that offer *any* "pay-to-win" microtransactions (i.e., those that provide a gameplay advantage)—such as selling "kits" containing items or vehicles—should use the ``Monetized`` option.

Online Conduct
--------------

Repeated offenders of servers violating the `Steam's Online Conduct rules <https://store.steampowered.com/online_conduct>`_ will be banned.

Roleplaying Current Events
--------------------------

Simulating gameplay of current real-world tragedies is **not** allowed. For example, ongoing conflicts (such as the Russo-Ukrainian War, or Israeli-Palestinian conflict) or natural disasters.

Anycast Proxies
---------------

If you use an anycast proxy, please consider `submitting a support request here <https://support.smartlydressedgames.com/hc/en-us/requests/new>`_ to ensure it is flagged correctly. Otherwise, players will almost certainly report the server.

Anycast proxies are a great protection mechanism, but they significantly affect the ping reported in the server browser. For example, a server hosted in Australia may have a ping of 40ms for players in the region but a ping of 300ms for players in Europe. Using an anycast proxy, in this case, would report a much lower ping (e.g., ~30ms) to players around the globe and incorrectly sort the server among those with the lowest ping.

This is frustrating for players looking for low-latency servers, as they may join one with a low ping only to find it is much higher in-game. Servers using an anycast proxy are flagged to sort like they have a higher ping to avoid this problem. It was implemented as a direct response to complaints from players.

Servers using a regular proxy with ping similar to the actual in-game ping are not flagged. Only proxies with a significant ping difference are flagged.

Workshop File Copyright Infringement
------------------------------------

Mod authors can submit a notice of copyright infringement here: https://steamcommunity.com/dmca/create/

FAQ (Frequently Asked Questions)
--------------------------------

Can I report servers for admin abuse or pay-to-win features?
````````````````````````````````````````````````````````````

This is not reportable. Unfortunately, the best option is to play on a different server, or to :ref:`host your own multiplayer server <doc_server_hosting>` for you and your friends. Moderating individual community servers is not tenable at our current small scale with current tools, but may be revisited if/when it becomes feasible.

How can my server mitigate Denial of Service (DoS) attacks?
```````````````````````````````````````````````````````````

If your server is receiving DoS attacks, the :ref:`doc_servers_fake_ip` feature is a great way to protect against this behavior. It routes traffic through Steam's relay network, shielding your server's IP, and potentially reducing network latency for players.

How can I prevent people from re-uploading my Workshop files?
`````````````````````````````````````````````````````````````

Including an :ref:`doc_asset_bundle_custom_data` in your asset bundle, with the owner to your Workshop file ID, will prevent it from being loaded when copied into other Workshop files. As a last resort, if your content has been reuploaded to Steam by another user with your permission, you may consider submitting a `notice of copyright infringement <https://steamcommunity.com/dmca/create/>`_. Notices of copyright infringement are reviewed by Valve's copyright agent, and should only be submitted if you understand the legal information on their submission page.
