Unturned Documentation
======================

These are the source files for *Unturned*'s modding documentation.

The built documentation is hosted by [Read the Docs](https://readthedocs.org/) here: https://docs.smartlydressedgames.com/

Contributing
------------

Anyone can contribute towards *Unturned*'s modding documentation. This repository has three branches – **latest**, **stable**, and **old-markdown-archive** – although contributions should only be made towards the "latest" branch.

- **latest**: Always has the latest documentation, including upcoming features that might not be available on the current version of the game.

- **stable**: Occassionally updated with the additions to the "latest" branch.

- **old-markdown-archive**: Contains old documentation, in markdown files (rather than reStructuredText). This documentation does not appear on the online documentation site, and is only kept for historical purposes. Its contents may be removed in the future.

The online documentation pages are generated from .rst (reStructuredText) files. These files are stored in root, but are organized into folders based on where those files appear in the table of contents. For example, the [level-asset.rst](/assets/level-asset.rst) file is located in the "assets" folder.

### Styleguide

Most documentation files are formatted similarly.

Building the Docs
-----------------

The documentation is written in [reStructuredText](https://www.writethedocs.org/guide/writing/reStructuredText/) and parsed/built using [Sphinx](https://github.com/sphinx-doc/sphinx).

With Python and Sphinx installed run `make html` in the root folder to create the site locally at `/_build/html/index.html`.

Editing using [Visual Studio Code](https://code.visualstudio.com/) with the [reStructuredText Extension](https://docs.restructuredtext.net/) is recommended.