import os

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.ifconfig",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    'sphinx_demo.extension'
]
if os.getenv("SPELLCHECK"):
    extensions += ("sphinxcontrib.spelling",)
    spelling_show_suggestions = True
    spelling_lang = "en_US"

source_suffix = ".rst"
master_doc = "index"
project = "project"
year = 2020
author = "demo"
copyright = "{0}, {1}".format(year, author)
version = release = "0.1.0"

pygments_style = "trac"
templates_path = ["."]
extlinks = {}
# on_rtd is whether we are on readthedocs.org
on_rtd = os.environ.get("READTHEDOCS", None) == "True"

if not on_rtd:  # only set the theme if we"re building docs locally
    html_theme = "sphinx_rtd_theme"

html_use_smartypants = True
html_last_updated_fmt = "%b %d, %Y"
html_split_index = False
html_sidebars = {"**": ["searchbox.html", "globaltoc.html", "sourcelink.html"]}
html_short_title = "%s-%s" % (project, version)

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = True

autoapi_dirs = ["../sphinx_demo"]


html_css_files = ["style.css", "other.css"]


html_theme_options = {"nosidebar": True}

numfig = True
todo_include_todos = True
nitpicky = True


# Latex


latex_docclass = {"howto": "article", "manual": "article"}

numfig_format = {"container": "Cont. %s", 'original': 'Original %s'}
