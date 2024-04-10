# Configuration file for the Sphinx documentation builder.
#
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys, os

# -- Project information

project = "Unturned"
copyright = "2023, Smartly Dressed Games"
author = "Smartly Dressed Games"

release = "0.1"
version = "0.1.0"

# -- General configuration
sys.path.append(os.path.abspath("_extensions")) # also find extensions within this directory
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel', # create explicit targets for all sections in the form of {path/to/page}:{title-of-section}
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxext.opengraph', # OpenGraph support (e.g., URLs posted onto our Discourse forum will appear as OneBox embeds)
    'sphinx_rtd_theme', # "Read the Docs Sphinx Theme" https://sphinx-rtd-theme.readthedocs.io/en/stable/index.html
    # -- Locally-installed modules
    'unturned_lexer',
]

autosectionlabel_prefix_document = True # make sure explicit target is unique

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# RTD theme options are documented here: https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
html_theme_options = {
    # Toc options
    'collapse_navigation': True,
}

# These folders are copied to the documentation's HTML output
html_static_path = ["_static"]

# These paths are either relative to html_static_path
# or fully qualified paths (e.g. https://...)
html_css_files = [
    'css/custom.css',
]

# -- Options for EPUB output
epub_show_urls = 'footnote'
