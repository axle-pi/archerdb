import os
import sys

project = 'ArcherDB'
author = 'Matt Dillon'
version = ''
release = '1.0.0'
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
pygments_style = 'sphinx'
html_theme = 'alabaster'
html_static_path = ['_static']
html_logo = '../_static/logo_only.svg'
html_theme_options = {
    'github_user': 'axle-pi',
    'github_repo': 'archerdb',
}

sys.path.insert(0, os.path.abspath('../..'))
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel'
]
