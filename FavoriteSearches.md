**NOTICE:** *You are not reading the most up-to-date documentation. This file is old, and may not reflect the current modding or server capabilities. The latest documentation can be found at [Unturned Documentation](https://docs.smartlydressedgames.com/).*

*This file may be removed in the future. Refer to its more [up-to-date equivalent](https://docs.smartlydressedgames.com/en/stable/mapping/favorite-searches.html) instead.*

Favorite Searches
=================

The objects editor supports __Favorite Searches__ which allows lists of objects to be quickly looked up.

Entering "fv:xyz" in the search bar loads xyz.txt from the game folder, and will match any of the lines in the file. Empty lines and lines starting with "//" (comments) are ignored. The .txt file extension was chosen because it is the notepad default.

For example this matches anything with "fire" in the name or Road Line Cap #1:

	// Fire related props
	Fire

	// Specific road prop
	Cap #1 Road Line

Recursive usage of filters is supported, so multiple favorite searches can be nested, or other filter types e.g. "Tunnel mb:core" includes tunnels from the vanilla objects.
