# Jupyter Book v2 Example Website

This is an example website using [Jupyter Book](https://jupyterbook.org/) version 2.

## Installation

Ensure the necessary dependencies are installed within your Python environment:

```bash
conda install -r jupyter-book>=2.0.0 jupyter jupyterlab matplotlib numpy ghp-import 
```

## Running Locally

To build and view the book locally:

```bash
jupyter-book start
```

The site will be available at `http://localhost:3000`

The built html output will be in the `_build/` directory.

## Features

Jupyter Book supports:
- Markdown files (`.md`)
- Jupyter notebooks (`.ipynb`)
- MyST markdown (extended markdown syntax)
- Mathematical equations (LaTeX)
- Cross-references
- Jupyter cell outputs

# Publish to GitHub Pages

JupyterBook has a built-in function to set up GitHub Pages deployment:

~~~bash
jupyter book init --gh-pages
~~~

Answer the prompted questions; this will create a `.github/workflows/deploy.yml` file. Commit everything to a public GitHub repository, enable **Pages** in the repository settings set to build via **GitHub Actions**, and your site will be published automatically.

