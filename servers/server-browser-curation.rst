.. _doc_server_browser_curation:

Server Browser Curation
=======================

.. note:: We'll go into more detail on the *why* behind this feature in a blog post.

This feature allows anyone to create and share lists of "rules" that filter or label servers in the server browser. Lists can be shared through the Steam Workshop as (asset doc link), or automatically downloaded from a URL on the Internet.

If you're a server host, suppose you want to prevent bad actors from copying your server details. Your first rule would ``Allow`` your genuine servers, for example, matching by ``ServerID`` ("server code"). Your second rule could then ``Deny`` servers with a regex that matches your server network's branding.

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
