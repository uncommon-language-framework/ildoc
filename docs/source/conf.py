# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'ULR IL'
copyright = '2024, Carl Furtado'
author = 'Carl Furtado'

release = 'latest'

# -- General configuration

extensions = [
    'myst_parser',
    'sphinx_rtd_theme'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
