---
myst:
  html_meta:
    "canonical": "https://writing-technically.readthedocs.io/en/latest/guide-setting-up-a-sphinx-site.html"
    "description": "Instructions for creating a Sphinx site and deploying it to GitHub, GitLab, and Read The Docs"
    "title": "How to create and deploy a Sphinx site"
    "twitter:description": "Creating a Sphinx site and deploying it to GitHub, GitLab, and Read The Docs. You need Python, but you don't need to know Python."
    "twitter:title": "How to create and deploy a Sphinx site"
    "twitter:image": "https://writing-technically.readthedocs.io/en/latest/_static/wordcloud.jpg"
    "twitter:card": "summary_large_image"
    "twitter:creator": "@anindita_basu"
    "twitter:site": "@anindita_basu"
    "og:locale": "en_US"
    "og:site_name": "Writing technically"
    "og:url": "https://writing-technically.readthedocs.io/en/latest/guide-setting-up-a-sphinx-site.html"
    "og:type": "article"
    "og:title": "How to create and deploy a Sphinx site"
    "og:description": "Creating a Sphinx site and deploying it to GitHub, GitLab, and Read The Docs. You need Python, but you don't need to know Python."
    "og:image": "https://writing-technically.readthedocs.io/en/latest/_static/wordcloud.jpg"
    "author": "Anindita Basu"
---

# How to set up a Sphinx site

<hr/>
<p style="font-weight:bold;font-size:75%;color:orange">19 July 2022 (last updated: 4 March 2023)</p>

Sphinx is a static site generator that uses Python to convert `RST` and `MD` files to `HTML`.

To set up a Sphinx site, these are the steps:

1. Build a site locally.
2. Deploy the site for public consumption.
3. Personalise the site.
4. Publicise the site.

The entire process takes about 50 minutes or longer.

## Build a site locally

```{admonition} Estimated time

   -  Prerequisites: 15 minutes
   -  Steps: 5 minutes

```

### Prerequisites

- Python 3.0 or later. To see if you have Python installed somewhere on your computer, open the command prompt, type `python`, and press Enter.
- Sphinx 5.0 or later. To see if your computer has Sphinx, at the command prompt, type `sphinx-build --version`, and press Enter.

### Steps

1. On your computer, create a directory.
2. Open a Python terminal and use the `cd` command to go to this directory you just created.
3. Create a text file called `README.rst`. Optionally, add a line or two in this file.
4. Run the `sphinx-quickstart docs` command and, at the prompts, specify the following inputs. Some files and folders are created.
   -   Separate source and build directories (y/n) [n]: Type `y` and press Enter.
   -   Project name: Type the name of your site and press Enter.
   -   Author name(s): Type your name and press Enter.
   -   Project release [ ]: Press Enter.
   -   Project language [en]: Press Enter.
   
   The following files and folders are created:
   ```
        docs
        ├── build
        ├── make.bat
        ├── Makefile
        └── source
           ├── conf.py
           ├── index.rst
           ├── _static
           └── _templates
   ```
5. Run the following command: `sphinx-build -b html docs/source/ docs/build/html`.
   `HTML` content is generated from the `source/index.rst` file and other files, and placed in the `build` folder.
6. In a browser, open the `build/index.html` file. This is the home page of your website.

## Deploy the site for public consumption

So that everyone in the world can see your site, push your files to your favourite deployment-solution provider.

### Deploy through GitLab

You ask GitLab to build the site for you and make it available through Pages. To do so, you first host your source on a GitLab repository, and then use a `.gitlab-ci.yml` file as a CI/CD file for GitLab to build and serve the site.

```{admonition} Estimated time

   5 minutes
   
```

1. Sign in to GitLab and create a repository.    
2. Add a `.gitlab-ci.yml` file, at the root of the repository, with the following matter:
    ```
    stages:
      - deploy
    
    pages:
      stage: deploy
      image: python:3.9-slim
      before_script:
        - apt-get update && apt-get install make     --no-install-recommends -y
        - python -m pip install sphinx
      script:
        - cd docs && make html
      after_script:
        - mv docs/build/html/ ./public/
      artifacts:
        paths:
        - public
      rules:
        - if: $CI_COMMIT_REF_NAME == "main"
    ```
3. Push the entire `docs` directory (minus the `docs/build` directory) from your computer to the `main` branch of the GitLab repository. This is what your repository should look like:
   ```
        docs
        ├── make.bat
        ├── Makefile
        └── source
           ├── conf.py
           ├── index.rst
           ├── _static
           └── _templates
        .gitlab-ci.yml
        README.rst
   ```
6. Wait for the build to complete, after which your site is available at `<your-user-name>.gitlab.io/<your-repo-name>`.

### Deploy through GitHub

You have two options for doing this.

#### Option 1. Upload the built HTML files

In this method, you build the files locally, and upload only the output to GitHub. The source files are, thus, not connected to the output files.

```{admonition} Estimated time

   5 - 7 minutes

```

1. Sign in to GitHub and create a repository.
2. In the `main` branch, create a `docs` folder.
3. In the `docs` folder, create an empty file called `.nojekyll`.
4. Push the contents of the local `docs/build` directory (which you generated through Sphinx locally) to `main/docs` of your GitHub repository.
5. Enable GitHub Pages. Specify the source to be the `main` branch and `docs` folder.
6. Wait for the build to finish. Thereafter, your site is available at `<your-user-name>/<github-repo-name>/index.html`.

#### Option 2: Ask GitHub to build the HTML files

In this method, you upload the source files to GitHub, and ask GitHub to generate the output. In this method, the output files are always in sync with the source files.

I haven't completely figured out this method yet. The GitHub build is running fine but the site deployment is going awry. After I sort it out, I'll update this page.

### Deploy through Read The Docs

You have only one option, which is that of asking Read The Docs to build the site for you. To do so, you first host your source on a publicly available Git repository, and then use a `.readthedocs.yaml` file as a CI/CD file that Read The Docs will read to build the output.

```{admonition} Estimated time

   10 minutes

```

1. Sign in to GitHub, GitLab, or BitBucket and create a repository.
    ```{margin} **What your repo should contain**
        docs
        ├── make.bat
        ├── Makefile
        └── source
           ├── conf.py
           ├── index.rst
           ├── _static
           └── _templates
        .readthedocs.yaml
        README.rst
    ```
2. Add a `.readthedocs.yaml` file, at the root of the repository, with the following matter:
    ```
    # Details are at https://docs.readthedocs.io/en/stable/config-file/v2.html
    
    # Required
    version: 2
    
    # Set the version of Python and other tools you might need
    build:
      os: ubuntu-20.04
      tools:
        python: "3.8"
    
    # Build documentation in the docs/ directory with Sphinx
    sphinx:
      configuration: docs/source/conf.py
    ```
3. Push the entire `docs` directory (minus the `docs/build` directory) from your computer to the `main` branch of the Git repository.
4. Sign in to Read The Docs and import this repository as a project.
5. Wait for the build to complete, after which your site is available at `<your-project-name>.readthedocs.io/en/latest/index.html`.

## Personalise the site

Because the site is about you.

### Add stuff

Make your changes locally, test them, and then push them to your repo.

```{admonition} Estimated time

   10 minutes or longer

```

1. Open the `index.rst` file. This file is the home page of your site. Edit it to your heart's content.
2. For every page that you want on your site, add an `RST` or `MD` file to the `docs/source` directory. Images go into the `docs/source/_static` directory.
3. For every page that you want on your site, after you've created that page, add it as a `toctree` entry to the `index.rst` file.
4. Test your changes while you work:
    1. Open a Python terminal and go to the `<your-Sphinx-directory>/docs` directory.
    2. Build the site locally by running the following command.

       ````{eval-rst}
       .. tabs::
       
          .. tab:: Windows
       
             ``.\make html``
       
          .. tab:: Unix
       
             ``make html``
       
          .. tab:: MacOS
       
             ``I don't know``
       
       ````
    3. Look at the output in the `docs/build` directory.

### Change the theme

The default theme of Sphinx docs is `alabaster`, which is a bit insipid. Find a theme that's more you.

```{admonition} Estimated time

   10 minutes or longer

```

1. If it's a third-party theme, install it by running a `pip install` command.
2. Edit the `html_theme` parameter in `conf.py`. The default Sphinx value is `alabaster`. Read the documentation of the theme of your choice to see what this value should be changed to.
3. In the same `conf.py` file, specify the options for HTML output. The theme documentation should have this information.
4. If it's a third-party theme, add a `requirements.txt` file at the root of your project (at the same level as `.readthedocs.yaml`) and add an entry for the theme package.

### Write in Markdown (instead of ReStructured Text)

Because some people (like me) find Markdown much more easy to handle than the recalcitrant child that ReStructured Text can often become.

Sphinx knows how to change `RST` file to `HTML`, and will do so without prompting. It also knows how to change `MD` files to `HTML`, but needs to be told specially (through the `conf.py` file) to do so.

```{admonition} Estimated time

   2 minutes

```

1. Add the following entry to the `conf.py` file:
    ```
    extensions = [
        'myst_parser',
    ]
    ```
2. In the `requirements.txt` file, add an entry for `myst_parser`. If you don't have a `requirements.txt` file, create one at the root of the project (at the same level as `.readthedocs.yaml`).

## Publicise the site

This part, I don't have any _gyan_, except for saying, use your best offices :)

<hr/>
