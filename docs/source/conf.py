# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Writing Technically'
copyright = '2022 - 2024, Anindita Basu'
author = 'Anindita Basu, using <a href="http://www.sphinx-doc.org/">Sphinx</a> with the <a href="https://sphinx-book-theme.readthedocs.io/en/stable/index.html">Book theme</a> of the <a href="https://ebp.jupyterbook.org/">Executable Book project</a>.<p>This site uses no tracking code or site analytics. Neither does it use any cookies, as far as I know. Because it is on the free plan of the ReadTheDocs hosting service, you might see some ads on the sidebar at the left.</p>'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx_tabs.tabs',
    'sphinx_copybutton',
    'sphinx_togglebutton',
    'sphinx_favicon'
]

myst_enable_extensions = [
    'deflist',
    'strikethrough'
]

# Add any paths that contain templates here, relative to this directory.
#templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_theme_options = {
    "repository_url": "https://github.com/AninditaBasu/writing-technically",
    "use_repository_button": False,
    "use_issues_button": False,
    "use_edit_page_button": False,
    "use_download_button": False,
    "repository_branch": "main",
    "home_page_in_toc": True,
    "show_navbar_depth": 2,
    "extra_footer": "<a href='about.html'>About me</a>",
    "toc_title": "On this page",
    "show_toc_level": 3,
}
html_sidebars = {
    "**": ["navbar-logo.html", "search-field.html", "sbt-sidebar-nav.html"]
}
html_baseurl = "https://writing-technically.readthedocs.io/en/latest/"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_title = 'Home'
html_logo = '_static/wordcloud.jpg'

favicons = [
    {
        "rel": "icon",
        "static-file": "wordcloud.jpg",
        "type": "image/jpg",
    },
]

