import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "stubfiles"))


project = "Spike V3"
html_theme = "sphinx_rtd_theme"

extensions = ["sphinx.ext.apidoc", "sphinx_toolbox.wikipedia"]

apidoc_modules = [
    {"path": "../stubfiles", "destination": "api/"},
]
apidoc_automodule_options = {
    "members",
    "show-inheritance",
    "undoc-members",
}
apidoc_separate_modules = True

autodoc_order_members = "groupwise"

master_doc = "api/modules"

html_extra_path = ["index.html"]
