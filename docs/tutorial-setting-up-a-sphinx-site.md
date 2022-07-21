# How to set up a Sphinx site

<hr/>
<span style="font-weight:bold;font-size:75%;color:orange">19 July 2022</span>

Sphinx is a static site generator that uses Python to convert `RST` and `MD` files to `HTML`.

To set up a Sphinx site, these are the steps:

1. [Build a site locally](#build-a-site-locally).
2. [Personalise the site](#personalise-the-site).
3. [Deploy the site for the public](#deploy-the-site-for-the-public).

The entire process takes about 50 minutes or longer.

![Pink flowers in a blue boat-shaped glass bowl atop a chessboard table](_static/chess_flowers.jpg)

## Build a site locally

<div class="admonition note" name="html-admonition" style="padding: 10px">
<p class="title">Estimated time: 15 minutes</p>
<ul><li>Steps 1 and 2, ~10 minutes</li>
    <li>Steps 3 and 4, ~1 minute</li>
    <li>Step 5, ~2 minutes</li>
    <li>Step 6, ~1 minute</li>
    <li>Step 7, ~1 minute</li></ul>
</div>

1. Install Python.
2. Install Sphinx.
3. In a new directory, create a file called README.rst.
4. Open a Python terminal and go to this directory you just created.
5. Run the `sphinx-quickstart docs` command and, at the prompts, specify the following inputs:
    1. Separate source and build directories (y/n) [n]: Type `n` and press Enter.
    2. Project name: Type the name of your site and press Enter.
    3. Author name(s): Type your name and press Enter.
    4. Project release [ ]: Press Enter.
    5. Project language [en]: Press Enter.
    Some files and folders are created.
6. Go to the `docs` directory (`cd docs`) and run the following command: `.\make html`.
7. In your system file explorer, go to the `_build` > `html` directory and look for a file called `index.html`. This is the home page of your site. Open it.

The `_build` directory contains all the files that are needed for a website. Deploy the contents of this directory to a hosting provider of your choice.

<hr/>

## Personalise the site

Because the site is about you, not about Sphinx.

### Change the theme

The default theme of Sphinx docs is `alabaster`, which is a bit insipid. Find a theme that's more you.

<div class="admonition note" name="html-admonition" style="padding: 10px">
<p class="title">Estimated time: ~12 minutes or longer</p>
<ul><li>Step 1, ~1 minute</li>
    <li>Step 2, ~1 minute</li>
    <li>Step 3, 10 minutes or longer</li></ul>
</div>

1. Install the theme by running a `pip install` command.
2. Edit the `html_theme` parameter in `conf.py`. The default Sphinx value is `alabaster`. Read the documentation of the theme of your choice to see what this value should be changed to.
3. In the same `conf.py` file, specify the options for HTML output. The theme documentation should have this information.

### Write in Markdown (instead of ReStructured Text)

Because some people (like me) find Markdown much more easy to handle than the recalcitrant child that ReStructured Text can often become.

Sphinx knows how to change `RST` file to `HTML`, and will do so without prompting. It also knows how to change `MD` files to `HTML`, but needs to be told specially (through the `conf.py` file) to do so.

<div class="admonition note" name="html-admonition" style="padding: 10px">
<p class="title">Estimated time: ~6 minutes</p>
<ul><li>Step 1, ~1 minute</li>
    <li>Step 2, ~5 minutes</li></ul>
</div>

1. Install `recommonmark` by running a `pip install` command.
2. Edit the `conf.py` file at two places, as follows.
    - Specify `recommonmark` as an extension, like this:
       ```
      # Add any Sphinx extension module names here, as strings. They can be
      # extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
      # ones.
        extensions = [
           'recommonmark',
       ]
       ```
    -  Enable the conversion of `MD` files to `HTML` through Sphinx by including the following code block: 
       ```python
       #support Markdown .md files
       from recommonmark.parser import CommonMarkParser
       source_parsers = {
       '.md': CommonMarkParser,
       }
       ```
 
<hr/>

## Deploy the site for the public

So that everyone in the world can see your site, push your files to your favourite deployment-solution provider.

### Deploy to GitHub

You have two ways of doing this.

**Option 1: Upload the built HTML files**

In this method, you build the files locally, and upload only the output to the cloud. The source files are, thus, not connected to the output files.

<div class="admonition note" name="html-admonition" style="padding: 10px">
<p class="title">Estimated time: ~4 minutes</p>
<ul><li>Step 1, ~1 minute</li>
    <li>Step 2, ~2 minutes</li>
    <li>Step 3, ~1 minute</li></ul>
</div>

1. Create a GitHub repository.
2. Push the contents of the `docs/_build` directory to the `main` branch of your GitHub repository.
3. Enable GitHub Pages.

**Option 2: Ask GitHub to build the HTML files**

In this method, you upload the source files to the cloud, and let GitHub generate the output. Therefore, the source files are always the same as the output files.

<div class="admonition note" name="html-admonition" style="padding: 10px">
<p class="title">Estimated time: ~8 minutes</p>
<ul><li>Step 1, ~1 minute</li>
    <li>Step 2, ~2 minutes</li>
    <li>Step 3, ~2 minutes</li>
    <li>Step 4, ~2 minutes</li>
    <li>Step 5, ~1 minute</li></ul>
</div>

1. Create a GitHub repository.
2. Push the contents of the `docs` directory (minus the `docs/_build`) directory to the `main` branch of your GitHub repository.
3. Add a `requirements.txt` file, at the root of your project, that lists all the Python modules you installed (through the `pip` command) for your site.
4. Add a `.github/workflows/sphinx.yml` file, at the root of your project, that contains the following matter:
    ```
    name: Sphinx build
    
    on: push
    
    jobs:
      build:
        runs-on: ubuntu-latest
        steps:
        - uses: actions/checkout@v3
        - name: Build HTML
          uses: ammaraskar/sphinx-action@0.4
        - name: Upload artifacts
          uses: actions/upload-artifact@v3
          with:
            name: html-docs
            path: docs/build/html/
        - name: Deploy
          uses: peaceiris/actions-gh-pages@v3
          if: github.ref == 'refs/heads/main'
          with:
            github_token: ${{ secrets.GITHUB_TOKEN }}
            publish_dir: docs/build/html
    ```
    This script uses a GitHub Action to build the files.
5. Enable GitHub pages and wait for the build to complete, after which your site is available at _your-name/github-repo-name/index.html_.

### Deploy to Read The Docs

You have only one option, which is that of asking Read The Docs to build the site for you. To do so, you first host your source on a publicly available Git repository (or some other version control system), and then use a `YAML` file as the build script.

<div class="admonition note" name="html-admonition" style="padding: 10px">
<p class="title">Estimated time: ~10 minutes</p>
<ul><li>Step 1, ~1 minute</li>
    <li>Step 2, ~2 minutes</li>
    <li>Step 3, ~2 minutes</li>
    <li>Step 4, ~2 minutes</li>
    <li>Step 5, ~3 minutes</li></ul>
</div>

1. Create a GitHub, GitLab, or BitBucket repository and push the contents of the `docs` directory (minus the `docs/_build`) directory to the `main` branch of your repository.
2. Add a `requirements.txt` file, at the root of your project, that lists all the Python modules you installed (through the `pip` command) for your site.
3. Add a `.readthedocs.yml` file, at the root of your project, that contains the following matter:
    ```
   # .readthedocs.yaml
   # Read the Docs configuration file
   # See https://docs.readthedocs.io/en/stable/config-file/v2.html for details
   
   # Required
   version: 2

   # Set the version of Python and other tools you might need
   build:
     os: ubuntu-20.04
     tools:
       python: "3.8"
   
   # Build documentation in the docs/ directory with Sphinx
   sphinx:
     configuration: docs/conf.py
   
   # Optionally declare the Python requirements required to build your docs
   python:
      install:
      - requirements: requirements.txt
    ```
4. Go to Read The Docs and import this repository as a project.
5. Wait for the build to complete, after which your site is available at _your-project-name.readthedocs.io/en/latest/index.html_.