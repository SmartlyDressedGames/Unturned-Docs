Unturned Documentation
======================

These are the source files for *Unturned*'s modding documentation.

The built documentation is hosted by [Read the Docs](https://readthedocs.org/) here: https://docs.smartlydressedgames.com/

Offline Downloads
-----------------

PDF and Epub versions of the documentation can be [downloaded](https://readthedocs.org/projects/unturned/downloads/) for offline use.

Contributing
------------

Anyone can contribute towards *Unturned*'s modding documentation. This repository has three branches – **latest**, **stable**, and **old-markdown-archive** – although contributions should only be made towards the "latest" branch.

- **latest**: Always has the latest documentation, including upcoming features that might not be available on the current version of the game.

- **stable**: Occassionally updated with the additions to the "latest" branch.

- **old-markdown-archive**: Contains old documentation, in markdown files (rather than reStructuredText). This documentation does not appear on the online documentation site, and is only kept for historical purposes. Its contents may be removed in the future.

The online documentation pages are generated from .rst (reStructuredText) files. These files are stored in root, but are organized into folders based on where those files appear in the table of contents. For example, the [level-asset.rst](/assets/level-asset.rst) file is located in the "assets" folder.

### Styleguide

Most documentation files are formatted similarly. Some important notes:

- When asset properties are listed, they should generally follow a `**Name** *data type*: Description` format. Depending on the data type, it may be hyperlinked instead of italicized, or may also include required values if there is one.

- Content block directives can be used to add notes, warnings, tips, and other admonitions.

- Internal links should use the `:ref:` command.

- Images from the Unity editor should crop out any unnecessary information. This usually includes the Title Bar (which includes details such as the Unity version, project name, and window buttons), and the Toolbar.

Building the Docs
-----------------

The documentation is written in [reStructuredText](https://www.writethedocs.org/guide/writing/reStructuredText/) and parsed/built using [Sphinx](https://github.com/sphinx-doc/sphinx).

Building requires the *Read the Docs* theme. To install it, run this command in the repository directory:

`py -m pip install -r requirements.txt`

*py runs the python interpreter. -m is short for -module and specifies the pip package installer module. -r is short for --requirement and specifies a file with a list of package names to install.*

With Python and Sphinx installed run `make html` in the root folder to create the site locally at `/_build/html/index.html`.

Editing using [Visual Studio Code](https://code.visualstudio.com/) with the [reStructuredText Extension](https://docs.restructuredtext.net/) is recommended.