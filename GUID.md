**NOTICE:** *You are not reading the most up-to-date documentation. This file is old, and may not reflect the current modding or server capabilities. The latest documentation can be found at [Unturned Documentation](https://docs.smartlydressedgames.com/).*

*This file may be removed in the future. Refer to its more [up-to-date equivalent](https://docs.smartlydressedgames.com/en/stable/data/guid.html) instead.*

GUID
====

Globally Unique Identifiers (**GUID**s) are 32 hexadecimal digits used to identify assets. They are preferable to file names because the files can be moved without redirectors.

A useful tool for manually generating GUIDs is [guidgenerator.com](https://www.guidgenerator.com/). Note that if the GUID property is omitted from an [asset v1](/AssetsV1.md) file, then the game will automatically assign a random GUID during a successful load.

Legacy ids are 16 bits with a [0, 65535] range, whereas GUIDs are 128 bits with an unimaginably huge range. This allows them to be generated without coordination or registration between developers.
