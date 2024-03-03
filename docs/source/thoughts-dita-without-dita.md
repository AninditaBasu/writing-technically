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
<p style="font-weight:bold;font-size:75%;color:orange">03 March 2024</p>

The value proposition of DITA hinges around these three things, mainly:
-  Enforcing a structure automatically, through strict topic typing
-  Reusing content at the topic, block, and element level, by means of direct references or keys
-  Generating profile-targetted content, by using attributes that can filter content at the topic, block, and element level

Are these things possible without DITA?

Assuming a docs-as-code pipeline where the content is written in plain text and transformed through a static site generator (SSG), here's a comparison table for two SSGs that I am familiar with:

| DITA feature | Sphinx                                                                                                                                                                              | MkDocs |
|---- |-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| ---- | 
| Enforcing a structure | No                                                                                                                                                                                  | No |
| Reusing content | Yes, through variables and includes                                                                                                                                                 | Yes, through variables and includes |
| Generating filtered content | Yes, through the `tag` object in `conf.py` together with the `include` directive in content, and `-t`flag in `makefile` (but the implementation isn't documented well and is buggy) | Yes, through the `extra` key in `mkdocs.yml` together with `if` blocks in content |

If this table had had columns for other SSGs too, I suspect that the row values would've been similar. 

If strict enforcement of a structure is not a requirement, DITA is not needed.

However, one of the tenets that technical writers live by is _consistency_. Consistency that's enforced through topic structures and writing guidelines.  A laissez-faire style of writing, that's a stream of consciousness spilling over on to the page and taking a rambling, meandering walk through the concepts and steps, is the stuff that a techwriter's nightmares are made of. 

![The Scream by Edvard Munch at the National Gallery of Norway uploaded to https://commons.wikimedia.org/w/index.php?curid=69541493 by ColdCreation in public domain on 8 Jan 2019](images/the_scream.jpg)

DITA is a language as well as an architecture.  It puts people in a straightjacket and that, at the end of the day, seems to be its USP. Not content reuse, not conditional profiling, but automatic enforcement of topic typing.

<hr/>
