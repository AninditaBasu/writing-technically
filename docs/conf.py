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

project = 'Writing Technically'
copyright = '2022 - 2023'
author = 'Anindita Basu, using <a href="http://www.sphinx-doc.org/">Sphinx</a> with the <a href="https://sphinx-book-theme.readthedocs.io/en/stable/index.html">Book theme</a> of the <a href="https://ebp.jupyterbook.org/">Executable Book project</a>.'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'sphinx_tabs.tabs',
    'sphinx_copybutton',
    'sphinx-favicon',
]

myst_enable_extensions = [
    "strikethrough",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# See https://sphinx-book-theme.readthedocs.io/en/stable/tutorials/get-started.html
html_theme = "sphinx_book_theme"
html_theme_options = {
    "repository_url": "https://github.com/AninditaBasu/writing-technically",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "repository_branch": "main",
    "logo_only": True,
    "home_page_in_toc": True,
    "show_navbar_depth": 2,
    "extra_navbar": "<a href='about.html'>About me</a>",
    "toc_title": "On this page",
    "show_toc_level": 3,
}
html_sidebars = {
    "**": ["sidebar-logo.html", "search-field.html", "sbt-sidebar-nav.html"]
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_title = 'Home'
html_logo = '_static/harappa_unicorn.jpg'

favicons = [
    {
        "rel": "icon",
        "static-file": "harappa_unicorn.jpg",
        "type": "image/jpg",
    },
]
