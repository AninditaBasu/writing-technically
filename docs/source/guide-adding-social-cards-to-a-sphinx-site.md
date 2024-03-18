---
myst:
  html_meta:
    "canonical": "https://writing-technically.readthedocs.io/en/latest/guide-adding-social-cards-to-a-sphinx-site.html"
    "description": "No need to override any layouts.html template. Use meta tags in Markdown and ReStructured Text files, and backslash to escape colons."
    "title": "How to add social media cards to the pages on a Sphinx site"
    "twitter:description": "No need to override any layouts.html template. Use meta tags in Markdown and ReStructured Text files, and backslash to escape colons."
    "twitter:title": "How to add social media cards to the pages on a Sphinx site"
    "twitter:image": "https://writing-technically.readthedocs.io/en/latest/_static/wordcloud.jpg"
    "twitter:card": "summary_large_image"
    "twitter:creator": "@anindita_basu"
    "twitter:site": "@anindita_basu"
    "og:locale": "en_US"
    "og:site_name": "Writing technically"
    "og:url": "https://writing-technically.readthedocs.io/en/latest/guide-adding-social-cards-to-a-sphinx-site.html"
    "og:type": "article"
    "og:title": "How to add social media cards to the pages on a Sphinx site"
    "og:description": "Instructions for adding page meta content in Markdown and ReStructured text files for a Sphinx site"
    "og:image": "https://writing-technically.readthedocs.io/en/latest/_static/wordcloud.jpg"
    "author": "Anindita Basu"
---

# Adding social media cards to a Sphinx site

<hr/>
<p style="font-weight:bold;font-size:75%;color:orange">25 July 2022</p>

Social cards are for defining the heading, short description, and image of your webpage when it's shared on social media. These details are picked from the `<meta>` tag of the rendered `HTML` content.

```{admonition} TL;DR
In `RST` files, use the backslash (`\`) to escape the colon (`:`) in the meta names of the social cards.
```

How the `HTML` is created in Sphinx is determined by the templates of the theme you're using. Does this mean you'll need to write overrides for templates? No! You only need to specify the info as a `meta` info in the `RST` or `MD` file itself. You do this by using front matter.

It took me a while to figure this one out. I couldn't find any posts that had this solution, so I'm writing it down.

Well, I did find two posts, and both talked about overriding the `HTML` template, but that's not really needed. You only need to get your front matter right. (This brings me to the topic for another blog post that I'll need to write now: _Front matter in ReStructured Text_. I don't know why people keep saying front matter doesn't work with ReStructured Text, because it so does.)

Here is how you add meta information that can be read by social media sites.

## Steps

1. Insert the following front matter as the very first item in your content file. The matter should be placed right at the beginning of the file.

  ````{eval-rst}
  .. tabs::

     .. tab:: Markdown files

        It's assumed you're using `myst_parser` to write in Markdown in Sphinx (because the following code snippet is tested for `myst_parser`).
      
        .. code-block:: 
      
            ---
            myst:
              html_meta:
                "description": "This is the description"
                "title": "Title"
                "twitter:description": "This is the description"
                "twitter:title": "Title"
            ---
      
     .. tab:: ReStructured Text files

        Use the backslash (```\```) to escape the colon (```:```) in the meta names of the social cards.
      
        .. code:: 
      
           .. meta::
              :description: This is the description
              :title: Title
              :twitter\:description: This is the description
              :twitter\:title: Title
      
  ````

2. Transform the file to `HTML` and look at the page source to verify that the meta information is added.

## Results

The front matter is rendered in `HTML` like this:

```html
<meta content="This is the description" name="description" />
<meta content="Title" name="title" />
<meta content="This is the description" name="twitter:description" />
<meta content="Title" name="twitter:title" />
```

<hr/>

