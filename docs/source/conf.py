# Configuration file for the Sphinx documentation builder.

# -- Project information

project = "U3 Docs"
copyright = '2023, Smartly Dressed Games'
author = 'Smartly Dressed Games'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel', # create explicit targets for all sections in the form of {path/to/page}:{title-of-section}
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme', # "Read the Docs Sphinx Theme" https://sphinx-rtd-theme.readthedocs.io/en/stable/index.html
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

html_theme_options = {
    # Toc options
    'collapse_navigation': True,
}

html_show_sphinx = False # hide "Created using Sphinx" from the HTML footer

# -- Options for EPUB output
epub_show_urls = 'footnote'
