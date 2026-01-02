---
myst:
  html_meta:
    "canonical": "https://writing-technically.readthedocs.io/en/latest/guides-remote-ghpages-theme.html"
    "description": "Instructions for creating a theme for GitHub Pages"
    "title": "How to create a GitHub Pages theme"
    "twitter:description": "Instructions for creating a theme for GitHub Pages"
    "twitter:title": "How to create a GitHub Pages theme"
    "twitter:image": "https://writing-technically.readthedocs.io/en/latest/_static/wordcloud.jpg"
    "twitter:card": "summary_large_image"
    "twitter:creator": "@anindita_basu"
    "twitter:site": "@anindita_basu"
    "og:locale": "en_US"
    "og:site_name": "Writing technically"
    "og:url": "https://writing-technically.readthedocs.io/en/latest/guides-remote-ghpages-theme.html"
    "og:type": "article"
    "og:title": "How to create a GitHub Pages theme"
    "og:description": "Instructions for creating a theme for GitHub Pages"
    "og:image": "https://writing-technically.readthedocs.io/en/latest/_static/wordcloud.jpg"
    "author": "Anindita Basu"
---

# Creating a theme for GitHub Pages

<hr/>
<p style="font-weight:bold;font-size:75%;color:orange">02 January 2025</p>

For the times when none of the available themes appeal to you, and you craft your own. And then think about putting it out to the world as a shareable `remote-theme` because, who knows, someone else out there might also be unhappy with the selection on offer, see yours, like it, and use it.

## Steps

1. Create a public GitHub repo with the following structure:
   ```{code-block} text
   |- _layouts
   |  |- default.html
   |- assets
   |  |- style.css
   _config.yml
   LICENSE
   README.md
   ```
2. Make sure your `_config.yml` file has at least a title and a description, like so:
   ```{code-block} text
   title: The name of your theme
   description: A sentence or two describing your theme.
   ``` 
3. In the `README.md` file, ask people to call your theme by creating a `_config.yml` file in their own repos, and using the following code snippet to reference your theme:
   ```{code-block} yaml
   remote_theme: yourGitHubName/yourRepoName
   plugins:
     - jekyll-remote-theme
   ```
4. Check in the files. You're done.
   
<hr/>
