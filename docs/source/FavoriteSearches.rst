Favorite Searches
=================

The objects editor supports **Favorite Searches** which allows lists of objects to be quickly looked up.

Entering "fv:xyz" in the search bar loads xyz.txt from the game folder, and will match any of the lines in the file. Empty lines and lines starting with "//" (comments) are ignored. The .txt file extension was chosen because it is the notepad default.

For example this matches anything with "fire" in the name or Road Line Cap #1:

	// Fire related props
	Fire

	// Specific road prop
	Cap #1 Road Line

Recursive usage of filters is supported, so multiple favorite searches can be nested, or other filter types e.g. "Tunnel mb:core" includes tunnels from the vanilla objects.
