import os
import sys

project = 'ArcherDB'
author = 'Matt Dillon'
version = ''
release = '0.0.2'
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
pygments_style = 'sphinx'
html_theme = 'alabaster'
html_static_path = ['_static']
html_logo = '../_static/logo_only.svg'

sys.path.insert(0, os.path.abspath('../..'))
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel'
]
