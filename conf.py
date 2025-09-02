# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Zuban'
copyright = '2025, info (at) zubanls.com'
author = 'David Halter'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.md', 'venv/**']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
html_logo = "logo.svg"
html_favicon = 'logo.svg'

html_theme_options = {
    'github_user': 'zubanls',
    'github_repo': 'zuban-docs',
    'github_banner': True,  # Shows "Fork me on GitHub" banner
    'github_button': False,  # Shows GitHub button in sidebar
}
