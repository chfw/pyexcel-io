# -*- coding: utf-8 -*-
DESCRIPTION = (
    'A python library to read and write structured data in csv, zipped csv ' +
    'format and to/from databases' +
    ''
)
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'pyexcel-io'
copyright = 'copyright 2015-2019 Onni Software Ltd.'
author = 'Onni Software Ltd.'
# The short X.Y version
version = '0.5.14'
# The full version, including alpha/beta/rc tags
release = '0.5.14'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [    'sphinx.ext.autodoc',    'sphinx.ext.doctest',    'sphinx.ext.intersphinx',    'sphinx.ext.viewcode',]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Extension configuration -------------------------------------------------
# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}
# TODO: html_theme not configurable upstream
html_theme = 'default'


def setup(app):
    app.add_stylesheet('theme_overrides.css')



# TODO: DESCRIPTION not configurable upstream
texinfo_documents = [
    ('index', 'pyexcel-io',
     'pyexcel-io Documentation',
     'Onni Software Ltd.', 'pyexcel-io',
     DESCRIPTION,
     'Miscellaneous'),
]
intersphinx_mapping.update({
    'pyexcel': ('http://pyexcel.readthedocs.io/en/latest/', None),
})
