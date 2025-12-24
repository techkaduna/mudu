# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys

sys.path.insert(0, os.path.abspath(".."))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "mudu"
copyright = "2025, Kolawole Andrew"
author = "Kolawole Andrew"
release = "1.1.500"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # "sphinx.ext.viewcode",
    # "sphinx.ext.viewcode",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.todo",
    "sphinx.ext.napoleon",
    "autoapi.extension",
]

autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "private-members": False,
    "show-inheritance": True,
    "inherited-members": True,
}

# Autodoc setting
autodoc_inherit_docstrings = True

# Autosummary settings
autosummary_generate = True

# AutoAPI settings
autoapi_type = "python"
autoapi_dirs = ["../mudu"]
autoapi_add_toctree_entry = True
autoapi_keep_files = True
autoapi_generate_api_docs = True

# Napoleon settings
napoleon_google_docstring = True
napoloen_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_use_admonition_for_note = False
napoleon_use_param = True
napoleon_use_rtype = True

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "navigation": 4,
    "collapse_navigation": False,
    "sticky_navigation": True,
}
html_static_path = ["_static"]


def setup(app):
    app.add_css_file("custom.css")


html_logo = "_static/logo.png"

latex_engine = "pdflatex"
latex_elements = {
    "papersize": "a4paper",
    "pointsize": "11pt",
    "preamble": r"""
    \usepackage{amsmath}
    \usepackage{amssymb}
    \setcounter{tocdepth}{2}
    """,
}

latex_documents = [
    (
        "index",
        "mudu.tex",
        "mudu documentation",
        "Kolawole Andrew",
        "manual",
    ),
]
