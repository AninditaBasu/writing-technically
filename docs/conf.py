# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'Writing, Technically'
copyright = '2022, Anindita Basu'
author = 'Anindita Basu'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'recommonmark',
    'sphinx_copybutton',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

#support markdown .md files
from recommonmark.parser import CommonMarkParser
source_parsers = {
    '.md': CommonMarkParser,
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# See https://bashtage.github.io/sphinx-material/index.html
html_theme = 'sphinx_material'
# Material theme options (see theme.conf at https://github.com/bashtage/sphinx-material for more information)
html_theme_options = {
    'base_url': 'https://writing-technically.readthedocs.io/',
    'repo_url': 'https://github.com/AninditaBasu/writing-technically',
    'repo_name': 'writing-technically',
    'html_minify': True,
    'css_minify': True,
    'nav_title': 'Writing, Technically',
    'globaltoc_depth': 2,
    'globaltoc_collapse': False,
    'color_primary': 'grey',
    'color_accent': 'orange'
}
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_title = 'Blog home'
html_last_updated_fmt = '%d %B %Y'
html_logo = '_static/s_1_600.jpg'

favicons = [
    {
        "rel": "icon",
        "static-file": "s_1_600.jpg",
        "type": "image/jpg",
    },
]