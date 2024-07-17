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

- Content block directives can be used to add notes, warnings, tips, and other admonitions.

- Internal links should use the `:ref:` command, usually pointing towards a custom anchor.

- Properties in the asset manual pages use one of two formats. Older pages follow a `**Name** *data type*: Description` format. Depending on the data type, it may be hyperlinked instead, or may include required (or possible) values. Newer pages follow a table-based format. These formats should not be mixed on the same page, but continuing to use the legacy format on pages that have not been converted yet is acceptable.

- Images from the Unity editor should crop out any unnecessary information. This usually includes the Title Bar (which includes details such as the Unity version, project name, and window buttons), and the Toolbar.

- The `code-block` directive can be used to display example code with syntax highlighting. Common languages include `cs`, `json`, `text`, `shell`, `bat`, and `unturneddat` (alias: `unturnedasset`).

- Including links to our Unturned Wiki can be helpful. These should use the `https://unturned.wiki/` shortlink instead of `https://unturned.wiki.gg/`. Wiki articles linked to from the Unturned Documentation should have the "[Category:Pages linked from Unturned Documentation](https://unturned.wiki/wiki/Category:Pages_linked_from_Unturned_Documentation)" hidden tracking category added to them.

Building the Docs
-----------------

The documentation is written in [reStructuredText](https://www.writethedocs.org/guide/writing/reStructuredText/) and parsed/built using [Sphinx](https://github.com/sphinx-doc/sphinx).

Building requires the *Read the Docs* theme. To install it, run this command in the repository directory:

`py -m pip install -r requirements.txt`

*py runs the python interpreter. -m is short for -module and specifies the pip package installer module. -r is short for --requirement and specifies a file with a list of package names to install.*

With Python and Sphinx installed run `make html` in the root folder to create the site locally at `/_build/html/index.html`.

Editing using [Visual Studio Code](https://code.visualstudio.com/) with the [reStructuredText Extension](https://docs.restructuredtext.net/) is recommended.

The project's `requirements.txt` file is automatically generated. To update this file, install `pip-tools` and run `pip-compile requirements.in`. Important dependencies (and their versions) should be pinned in `requirements.in`.
