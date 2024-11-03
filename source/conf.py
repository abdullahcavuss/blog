# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


project = 'Blog'
copyright = '2024, Abdullah CAVUS'
author = 'Abdullah CAVUS'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']

templates_path = ['_templates']
exclude_patterns = []

language = 'tr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
## conf.py

# These folders are copied to the documentation's HTML output
html_static_path = ['_static']


# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': True,
    'analytics_id': 'G-FHLWHCPSG0',
    'display_version': True,
    'style_external_links': True,
    'prev_next_buttons_location': 'both',
    'navigation_depth': 4,
    'collapse_navigation': False,
}
html_css_files = ["custom.css"]

html_logo = 'favicon.jpeg'
