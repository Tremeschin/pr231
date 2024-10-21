from pathlib import Path
import mkdocs_gen_files

# Workaround

# from mkdocs_include_markdown_plugin import IncludeMarkdownPlugin
# IncludeMarkdownPlugin._update_watched_files = lambda self: None

# Find directories

repository_dir = Path(__file__).resolve().parent.parent
examples_dir = repository_dir/"examples"
docs_dir = repository_dir/"docs"

print("Repository at", repository_dir)

# Copy files

with mkdocs_gen_files.open("examples/basic.py", "w") as virtual:
    virtual.write((examples_dir/"basic.py").read_text())

print("Copied virtual files")
