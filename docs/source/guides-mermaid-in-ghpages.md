---
myst:
  html_meta:
    "canonical": "https://writing-technically.readthedocs.io/en/latest/guides-mermaid-in-ghpages.html"
    "description": "Instructions for displaying Mermaid charts on GitHub Pages"
    "title": "How to display a Mermaid diagram on GitHub Pages"
    "twitter:description": "Instructions for displaying Mermaid charts on GitHub Pages"
    "twitter:title": "How to display a Mermaid diagram on GitHub Pages"
    "twitter:image": "https://writing-technically.readthedocs.io/en/latest/_static/wordcloud.jpg"
    "twitter:card": "summary_large_image"
    "twitter:creator": "@anindita_basu"
    "twitter:site": "@anindita_basu"
    "og:locale": "en_US"
    "og:site_name": "Writing technically"
    "og:url": "https://writing-technically.readthedocs.io/en/latest/guides-mermaid-in-ghpages.html"
    "og:type": "article"
    "og:title": "How to display a Mermaid diagram on GitHub Pages"
    "og:description": "Instructions for displaying Mermaid charts on GitHub Pages"
    "og:image": "https://writing-technically.readthedocs.io/en/latest/_static/wordcloud.jpg"
    "author": "Anindita Basu"
---

# Displaying Mermaid diagrams on GitHub Pages

<hr/>
<p style="font-weight:bold;font-size:75%;color:orange">04 January 2026</p>

Mermaid charts show up fine in GitHub README files and other Markdown files when viewed inside their GitHub repos. The charts don't show up when the same files are published to GitHub Pages sites.

## Steps

The following steps are relevant only if you use your own CSS files for your GitHub Pages site. If you're using a theme, the steps are different (and not documented here).

1. In the `_config.yml` file of your repo, add the following code block:
   ```{code-block} text
   kramdown:
     input: GFM
     syntax_highlighter_opts:
       disable: true
   ```
2. Create an `assets/js/mermaid-fix.js` file with the following content:
   ```{code-block} text
   document.addEventListener("DOMContentLoaded", () => {
     document.querySelectorAll("pre > code.language-mermaid").forEach(block => {
       const parent = block.parentElement;
       const container = document.createElement("div");
       container.className = "mermaid";
       container.textContent = block.textContent;
       parent.replaceWith(container);
     });
   });
   ``` 
3. In all of the template files that are used by your Markdown files, add the following code in the `<head>`:
   ```{code-block} text
     <script src="{{ '/assets/js/mermaid-fix.js' | relative_url }}"></script>

     <script type="module">
       import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
     mermaid.initialize({ startOnLoad: true, theme: "default" });
     </script>
   ```
4. Check in the files. After the GitHub Pages build is over, you should be able to see a rendered version of your Mermaid diagram.
   
<hr/>
