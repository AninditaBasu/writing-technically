---
myst:
  html_meta:
    "canonical": "https://writing-technically.readthedocs.io/en/latest/guide-canonical-urls-in-a-sphinx-site.html"
    "description": "Instructions for adding a link rel canonical tag to Markdown and reStructuredText files on a Sphinx site"
    "title": "How to add canonical URLs to the pages on a Sphinx site"
    "twitter:description": "Instructions for adding a link rel canonical tag to Markdown and reStructuredText files on a Sphinx site"
    "twitter:title": "How to add canonical URLs to the pages on a Sphinx site"
    "twitter:image": "https://writing-technically.readthedocs.io/en/latest/_static/wordcloud.jpg"
    "twitter:card": "summary_large_image"
    "twitter:creator": "@anindita_basu"
    "twitter:site": "@anindita_basu"
    "og:locale": "en_US"
    "og:site_name": "Writing technically"
    "og:url": "https://writing-technically.readthedocs.io/en/latest/guide-canonical-urls-in-a-sphinx-site.html"
    "og:type": "article"
    "og:title": "How to add canonical URLs to the pages on a Sphinx site"
    "og:description": "Instructions for adding a link rel canonical tag to Markdown and reStructuredText files on a Sphinx site"
    "og:image": "https://writing-technically.readthedocs.io/en/latest/_static/wordcloud.jpg"
    "author": "Anindita Basu"
---

# Adding canonical URLs to a Sphinx site

<hr/>
<p style="font-weight:bold;font-size:75%;color:orange">17 March 2024</p>

For search optimisation purposes, you might want to designate a URL as the legitimate, authoritative URL for a page. To do so for a Sphinx site, you must specify a base URL in the `conf.py` file, and then, for every page, add its URL in the front matter.

## Steps

1. In the project's `conf.py` file, specify the `html_baseurl` option for HTML output. The value of the option should be the root URL of the project. For example, for this website, the root URL is `https://writing-technically.readthedocs.io/en/latest/`. 
2. For every file, add a `canonical` tag as the very first tag in the frontmatter, as follows:
    ````{eval-rst}
       .. tabs::
       
          .. tab:: Markdown files
       
             ``"canonical": "https://writing-technically.readthedocs.io/en/latest/index.html"``
       
          .. tab:: restructuredText files
       
             ``:canonical: https://writing-technically.readthedocs.io/en/latest/index.html``
       
    ````
3. Build the site.
   
<hr/>
