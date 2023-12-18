# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Aplikacja wspomagająca naukę na egzamin inżynierski (Platforma E-learningowa)'
copyright = '2023, DOMINIKA BRYŁA, PIOTR RUDEK, KINGA KANIK'
author = 'DOMINIKA BRYŁA, PIOTR RUDEK, KINGA KANIK'
release = 'v1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'pl'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

import os
import sys
sys.path.insert(0, os.path.abspath('../../'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'StudiumApp.settings'
import django
django.setup()


extensions = [
    'sphinx.ext.autodoc',
]