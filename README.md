Unturned Documentation
======================

These are the source files for *Unturned*'s modding documentation.

The built documentation is hosted by [Read the Docs](https://readthedocs.org/) here: https://docs.smartlydressedgames.com/

Offline Downloads
-----------------

PDF, ePub, and zipped HTML versions of the documentation can be [downloaded](https://readthedocs.org/projects/unturned/downloads/) for offline use.

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

This section explains how to build a local copy of the documentation. Our documentation is written in [reStructuredText](https://www.writethedocs.org/guide/writing/reStructuredText/), and converted to HTML through [Sphinx](https://github.com/sphinx-doc/sphinx).

When building locally, we recommend using [Visual Studio Code](https://code.visualstudio.com/). Install the [Esbonio extension](https://docs.esbon.io/en/latest/index.html) by Swyddfa, and the [reStructuredText extension](https://docs.restructuredtext.net/) by LeXtudio Inc. You can find the full documentation for those extensions on their websites.

The version of Python used by the project is noted in the `.readthedocs.yaml` file. When building, you should use the same version of Python as used by the documentation. If you have multiple versions of Python installed, you may need to manually specify the version that should be used when running commands.

Before you can build the documentation, you will need to download all of its dependencies. From the repository's directory, run the following command:

```shell
py -m pip install -r requirements.txt
```

<small>*`py` runs the python interpreter, and can be used to specify the python version that should be used. `-m pip install` is used to select the pip package installer module. `-r requirements.txt` will install dependencies pinned in the specified requirements file.*</small>

With the project installed, run `make html` in the root folder. This will create the documentation locally at `/_build/html/index.html`. If you installed Esbonio correctly, you can preview how the documentation would look with the site's theme as well.

The project's `requirements.txt` file is automatically generated. If you need to add or update dependencies, these should be pinned in `requirements.in` instead. Run the following command (available from `pip-tools`) to generate a new requirements file afterwards:

```shell
pip-compile requirements.in
```
