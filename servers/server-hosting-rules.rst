.. _doc_server_hosting_rules:

Server Hosting Rules
====================

Servers that violate these rules may be temporarily or permanently banned. To report a server for rule violations, or appeal a moderation decision applied to your server, you may file a ticket with SDG Support:

* `Report a server for breaking rules <https://support.smartlydressedgames.com/hc/en-us/requests/new?ticket_form_id=12189991924500>`_
* `Appeal a server report <https://support.smartlydressedgames.com/hc/en-us/requests/new?ticket_form_id=12189992633364>`_

`View Moderation List <https://smartlydressedgames.com/UnturnedHostBans/index.html>`_

Recent changes
--------------

**2023-08-17:** Added reasoning behind flagging servers using an anycast proxy.

**2023-02-15 revisions:** Many of the rules have been revised to be clearer, with regards to what is (or isn't) currently allowed. "Consumable microtransaction" is better defined, there are a couple of new examples, and deceptive pricing has its own dedicated a section. The monetization filter section also includes more information about the filter, its purpose, and which of the four options (including a newer "Monetized" option) your server should use.

**2022-10-16 clarification:** Selling *vanilla* cosmetics, such as those available from the Stockpile or Steam Community Market, is not allowed. When offering cosmetics as a server microtransaction, the server network should should own (or have licensed) the rights to that content. Servers should not sell cosmetic content that they do not own the right to, such as vanilla cosmetics (either official, or community-contributed).

Monetization Types
------------------

Warnings for breaking the monetization rules first began being sent out on May 28, 2021. The monetization rules have now been in full effect since June 11, 2021.

Hosts are allowed to sell permanent benefits and monthly subscriptions. Consumable microtransactions are **not** allowed. A consumable microtransaction is anything that can be permanently consumed, lost, stolen, or destroyed. If it cannot be permanently lost, then it is not considered a consumable.

Examples
--------

This section will provide *examples* of allowed/banned monetization options. It is not an exhaustive list of every possible monetization strategy.

Examples of allowed monetization:
`````````````````````````````````

- Accepting donations.
- Selling permanent or monthly subscription access to play on the server(s).
- Selling ranks, unlocks, benefits, etc. available permanently, or for the duration of the monthly subscription. Timers or cooldowns are fine.
- Selling reusable "kits"—which are reusable permanently, or for the duration of the monthly subscription—containing in-game items. Timers or cooldowns are fine.
- Selling **custom** cosmetics like custom skins, name tags, chat colors, etc. available permanently or for the duration of the monthly subscription.
- Selling services or commissions, for example a modder taking commissions for new content that gets added to the server for all players.

Examples of banned monetization:
````````````````````````````````

- Selling individual in-game items like weapons, ammunition, supplies, bases, etc. that can be permanently lost, stolen, or destroyed.
- Selling individual in-game vehicles that can be permanently lost, stolen, or destroyed.
- Selling experience points.
- Selling currency.
- Selling ranks, kits, unlocks, benefits, etc. which stack with themselves as a loophole.
- Selling copies of **vanilla** cosmetics, such as those available on the Stockpile or Steam Community Market.

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

Deceptive Pricing
-----------------

Fictitious and deceptive pricing is not allowed. For example: lying that a discount is nearly expired, or pretending the price is discounted when it has never been at the listed full price. We would strongly advise following `Steam's discounting rules <https://partner.steamgames.com/doc/marketing/discounts>`_ to help avoid breaking any real-world laws.

Online Conduct
--------------

Repeated offenders of `Steam's rules and guidelines <https://support.steampowered.com/kb_article.php?ref=4045-USHJ-3810>`_ will be banned.

Anycast Proxies
---------------

If you use an anycast proxy, please consider `submitting a support request here <https://support.smartlydressedgames.com/hc/en-us/requests/new>`_ to ensure it is flagged correctly. Otherwise, players will almost certainly report the server.

Anycast proxies are a great protection mechanism, but they significantly affect the ping reported in the server browser. For example, a server hosted in Australia may have a ping of 40ms for players in the region but a ping of 300ms for players in Europe. Using an anycast proxy, in this case, would report a much lower ping (e.g., ~30ms) to players around the globe and incorrectly sort the server among those with the lowest ping.

This is frustrating for players looking for low-latency servers, as they may join one with a low ping only to find it is much higher in-game. Servers using an anycast proxy are flagged to sort like they have a higher ping to avoid this problem. It was implemented as a direct response to complaints from players.

Servers using a regular proxy with ping similar to the actual in-game ping are not flagged. Only proxies with a significant ping difference are flagged.

Workshop File Copyright Infringement
------------------------------------

Mod authors can submit a notice of copyright infringement here: https://steamcommunity.com/dmca/create/

If you have submitted a notice of copyright infringement against a server host, please notify Smartly Dressed Games by email as well. We will keep a record of the server's workshop file usage. If there is a pattern of copyright infringement we will ban the server.
