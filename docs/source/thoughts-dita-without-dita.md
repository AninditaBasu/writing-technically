---
myst:
  html_meta:
    "description": "Can docs-as-code implement the unique features of DITA"
    "title": "DITA without DITA"
    "twitter:description": "Can docs-as-code implement the unique features of DITA"
    "twitter:title": "DITA without DITA"
    "twitter:image": "https://writing-technically.readthedocs.io/en/latest/_static/wordcloud.jpg"
    "twitter:card": "summary_large_image"
    "og:type": "website"
    "og:title": "DITA without DITA"
    "og:description": "Can docs-as-code implement the unique features of DITA"
    "og:image": "https://writing-technically.readthedocs.io/en/latest/_static/wordcloud.jpg"
    "author": "Anindita Basu"
---

# DITA without DITA

<hr/>
<p style="font-weight:bold;font-size:75%;color:orange">19 February 2024</p>

The value proposition of DITA hinges around these three things, mainly:
-  Enforcing a structure automatically, through strict topic typing
-  Reusing content at the topic, block, and element level, by means of direct references or keys
-  Generating profile-targetted content, by using attributes that can filter content at the topic, block, and element level

Are these things possible without DITA?

Assuming a docs-as-code pipeline where the content is written in plain text and transformed through a static site generator (SSG), here's a comparison table for two SSGs that I am familiar with:

| DITA feature | Sphinx | MkDocs |
|---- |----| ---- | 
| Enforcing a structure | No | No |
| Reusing content | Yes, through variables and includes | Yes, through variables and includes |
| Generating filtered content | Yes, through the `tag` object in `conf.py` together with the `include` directive in content, and `-t`flag in `makefile` (but the implementation isn't documented well and is buggy) | Yes, through the `extra` key in `mkdocs.yml` together with `if` blocks in content |

If this table had had columns for other SSGs too, I suspect that the row values would've been similar. 

If strict enforcement of a structure is not a requirement, DITA is not needed. One can use the good practices of DITA even outside a DITA environment, even inside a docs-as-code environment.

When is going the DITA way a good option? [Let me count the situations](thoughts-dita-tipping-point.md).

<hr/>
