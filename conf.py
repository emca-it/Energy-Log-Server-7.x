from __future__ import division, print_function, unicode_literals
from datetime import datetime
from recommonmark.parser import CommonMarkParser

extensions = [#"sphinxcontrib.video", 
    ]
templates_path = ['templates', '_templates', '.templates']
source_suffix = ['.rst', '.md']
source_parsers = {
            '.md': CommonMarkParser,
        }
master_doc = 'index'
project = u'Energy-Log-Server-7.x'
copyright = str(datetime.now().year)+', EMCA Software'
author = 'EMCA-IT'
version = 'latest'
release = 'latest'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'sphinx_rtd_theme'
htmlhelp_basename = 'energy-log-server-7x'
latex_documents = [
    (master_doc, 'energy-log-server-7x.tex', u'Energy-Log-Server-7.x Documentation',
     u'', 'manual'),
]
