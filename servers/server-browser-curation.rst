.. _doc_server_browser_curation:

Server Browser Curation
=======================

This feature allows anyone to create and share lists of "rules" that filter or label servers in the server browser. Lists can be shared through the Steam Workshop as :ref:`Server Browser Curation Assets <doc_asset_server_browser_curation>`, or automatically downloaded from a URL on the Internet.

If you're a server host, suppose you want to prevent bad actors from copying your server details. Your first rule would ``Allow`` your genuine servers, for example, matching by ``ServerID`` ("server code"). Your second rule could then ``Deny`` servers with a regex that matches your server network's branding.

- :ref:`Examples <doc_server_browser_curation:examples>`
- :ref:`FAQ (Frequently Asked Questions)<doc_server_browser_curation:faq>`

Properties
----------

Name :ref:`string <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::

Your display name in the user interface. For example, a server network might display as "MyNetwork Verified Servers", or someone creating a list of high-quality well-moderated hosts might choose "MyName's Recommendations".

IconURL :ref:`string <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::

Optional URL of a 32x32 image to display in the user interface. For example, a server network might use the same icon they use in the server browser.

Labels :ref:`list of dictionaries <doc_data_file_format>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Labels applied by rules are defined here. Each has the following properties:

**Name** :ref:`string <doc_data_builtin_types>`: Name used to refer to this label from a rule.


**Text** :ref:`string <doc_data_builtin_types>`: Rich text displayed in the server browser.

For example, defining two labels:

.. code-block:: unturneddat
	:linenos:

	Labels
	[
		{
			Name Verified
			Text <color=green>MyNetwork Verified</color>
		}
		{
			Name Fake
			Text <color=red>MyNetwork Imposter</color>
		}
	]

Rules :ref:`list of dictionaries <doc_data_file_format>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Rules are processed from top to bottom. Each has the following properties:

**Action** *enum* (``Label``, ``Allow``, ``Deny``): ``Label`` applies a label and continues processing rules, whereas ``Allow`` and ``Deny`` both stop rule processing. ``Deny`` blocks the server, either hiding it or moving it to the bottom depending on the player's settings.

.. note:: ``Allow`` and ``Deny`` **can** apply labels as well. The only difference is that ``Label`` action doesn't affect whether server is allowed or denied.

**Inverted** *bool*: If true, negate whether this rule matches. i.e., binary NOT.

**Description** *string*: Text shown in the rules list user interface and in the tooltip for servers moved to the bottom of the list. Please use this to document *why* your rule exists!

**Label** *string*: Name of a label to apply.

**Type** *enum* (``Name``, ``IPv4``, ``ServerID``): Determines which server data this rule matches against.

	- **Name**: Match server's name using one or more `regular expression (regex) <https://en.wikipedia.org/wiki/Regular_expression>`_. Refer to **Regex** or **Regexes** property.
	- **IPv4**: Match server's public IP using one or more `CIDR addresses <https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation>`_. Refer to **Filter** or **Filters** property.
	- **ServerID**: Match server's ID (also referred to as "server code" or Steam ID). Refer to **Value** or **Values** property.

**Regex** *string* or **Regexes** *list of string*: The rule matches if any of the regexes match the server name. (binary OR)

One quick way to test a regex is to prefix it with "regex:" in the server browser name filter to search by regex. There are also a variety of helpful, free regex creation tools online.

For example, matching any server with "MyNetwork" in the name: ``Regex (?i)(MyNetwork)`` (``(?i)`` enables case-insensitive matching)

**Filter** or **Filters**: The rule matches if any of the rules match the server IPv4 address. (binary OR)

IPv4 address with optional subnet mask and optional port number or range. Here's an example list with explanations:

.. code-block:: unturneddat
	:linenos:

	Filters
	[
		// Matches any port on this IP address.
		10.8.0.1

		// Matches port 27015.
		10.8.0.1:27015

		// Matches ports 27015 through 27030 (inclusive).
		10.8.0.1:27015-27030

		// Matches any port on IP addresses in the range 192.168.1.0 through 192.168.1.255.
		192.168.1.0/24
	]

**Value** *uint64* or **Values** *list of uint64*: The rule matches if any of the Steam IDs match the server's Steam ID. (binary OR)

From the server console you can copy the server ID with "CopyServerCode". From the in-game server lobby screen you can copy it to the clipboard by pressing PageDown.

.. _doc_server_browser_curation:examples:

Examples
--------

Here's a hypothetical verification list for the "NelsonNet" network:

.. code-block:: unturneddat
	:linenos:

	Name NelsonNet Verification Example
	IconURL https://cdn.smartlydressedgames.com/ShareX/2024/12/ExampleIcon.png

	Labels
	[
		{
			Name Verified
			Text <color=#708fbd>NelsonNet Official</color>
		}
	]

	Rules
	[
		{
			Action Allow
			Description Verify NelsonNet's Steam IDs
			Label Verified
			Type ServerID
			Values
			[
				85568392932910946
			]
		}
		{
			Action Deny
			Description Hide fake NelsonNet servers (case-insensitive check for "NelsonNet" in the name)
			Type Name
			Regex (?i)(NelsonNet)
		}
	]

For an example of adding a curator by web URL, here's the link for that list: ``https://cdn.smartlydressedgames.com/ShareX/2024/12/ExampleCurationList.txt``

.. _doc_server_browser_curation:faq:

FAQ (Frequently Asked Questions)
--------------------------------

How can I find the details for someone else's server?
:::::::::::::::::::::::::::::::::::::::::::::::::::::

Pressing the **"Clipboard Debug"** hotkey (default **PageDown**) on the server lobby screen copies a variety of public information about the server to your clipboard. For example:

.. figure:: /img/ServerInfoScreen.png

	An example server.

Pressing the key on this server copies the following information to the clipboard:

.. code-block:: text
	:linenos:

	Name: Nelson's PEI Server
	Description:
	Thumbnail:
	Address: 192.168.48.73
	Connection Port: 27016
	Query Port: 27015
	SteamId: 85568392932910946 (k_EAccountTypeGameServer)
	Ping: 1ms
	0 workshop file(s):

Relevant details being:

- Name (line 1) can be used in a **Name** rule.
- Address (line 4) can be used in an **IPv4** rule.
- SteamId (line 7) can be used in a **ServerID** rule.

How do I create a regular expression (regex)?
:::::::::::::::::::::::::::::::::::::::::::::

As a starting point, ``(?i)(your text here)`` matches "your text here" (without quotes) `case-insensitively <https://en.wikipedia.org/wiki/Case_sensitivity>`_. It would also match "Your Text Here" or "yOuR tExT hErE", but not "yourtexthere".

For more advanced uses, we'd recommend using an online tool. At the time of writing (2025-02-07) these are top search results for "regex tool":

#. https://regex101.com/
#. https://regexr.com/
#. https://regex-generator.olafneumann.org/
#. https://www.regextester.com/


