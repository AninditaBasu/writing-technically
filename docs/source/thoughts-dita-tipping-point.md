---
myst:
  html_meta:
    "title": "When to move from docs-as-code to DITA"
    "description": "At what point does DITA become a good alternative to docs-as-code?"
    "author": "Anindita Basu"
    "og:type": "website"
    "og:title": "When to move from docs-as-code to DITA"
    "og:description": "At what point does DITA become a good alternative to docs-as-code?"
    "og:image": "https://writing-technically.readthedocs.io/en/latest/_static/wordcloud.jpg"
    "twitter:card": "summary_large_image"
    "twitter:title": "When to move from docs-as-code to DITA"
    "twitter:description": "At what point does DITA become a good alternative to docs-as-code?"
    "twitter:image": "https://writing-technically.readthedocs.io/en/latest/_static/wordcloud.jpg"
---

# From docs-as-code to DITA

<hr/>
<p style="font-weight:bold;font-size:75%;color:orange">3 March 2024</p>

At what point does an organisation start looking at DITA as an alternative to its docs-as-code approach to documentation?

A docs-as-code writing environment is one where:
-  Content is written in plain text, such as Markdown or reStructuredText, by using a text editor such as Notepad++ or VS Code.
-  Content source is in a version controlled repository through Git or similar software.
-  Output is generated through a static site generator (SSG) such as Sphinx, MkDocs, or similar. Many of the popular SSGs are free to use commercially, and have plugins to customise the styling.  Most of these plugins have  overrides that are fairly well documented.
-  Optionally, a CI/CD process runs checks for quality.

A DITA environment is one where:
-  Content is written in a controlled language called DITA, which enforces strict information typing through XML schemas. The DITA language and architecture specifications are free to use. Writing in DITA needs an XML editor.
-  Content source can be in a version-controlled repository, or in a content management system (CMS). While systems such as Git are free to use commercially, no CMS is.
-  Output is generated through DITA or Ant commands. Documentation exists, but the process is complicated and needs significant time and expertise.
-  Optionally, a CI/CD process runs checks for quality.

Assuming a clean slate, that is, assuming there is no formal documentation system in place yet, a docs-as-code environment might take a day or two to set up. A DITA environment could take a few days or weeks.

If it's not a clean-slate case, and an organisation already has a docs-as-code system in place that's been working marvellously for the past several years, adopting a DITA environment could take months. So, when does this kind of investment in time, effort, and, possibly, vendor-provided software, become necessary?

If strict enforcement of information typing is not a requirement, [migrating to DITA is not a necessity](thoughts-dita-without-dita.md).

However, one of the tenets that technical writers live by is _consistency_. Consistency that's enforced through topic structures and writing guidelines.  A laissez-faire style of writing, where a stream of consciousness spills over on to the page and takes a rambling, meandering walk through concepts and steps, is the stuff that a technical writer's nightmares are made of. 

![The Scream by Edvard Munch at the National Gallery of Norway uploaded to https://commons.wikimedia.org/w/index.php?curid=69541493 by ColdCreation in public domain on 8 Jan 2019](images/the_scream.jpg)

DITA is a language as well as an architecture.  It puts people in a straightjacket and that, at the end of the day, seems to be its unique selling proposition. Not content reuse, not conditional profiling, but automatic enforcement of topic typing. Adopting such a system might become necessary (or, an alternative to consider) when:

-  Maintaining the docs-as-code publish pipeline becomes a significant overhead. Most SSGs work through many plugins and components, and not all of these are maintained by the SSG-providers themselves. A dedicated resource might be needed to track upgrades in these plugins and components, and ensure that builds don't break. With DITA, releases happen once in a lifetime (or, maybe twice?) Once a DITA publishing pipeline is set up for all the required outputs (HTML, PDF, webhelp, hoverhelp, whatnothelp), constant monitoring and tweaking is not needed.
    ```{admonition} However, ...

   However, when those tweaks do become essential, experience-born expertise is needed because the DITA publishing world is not well-documented at all. This means that even ChatGPT will not have helpful answers. And, expertise with SSGs isn't transferrable to a DITA world because the two worlds are very different.
    ```
-  The organisation produces documents that are an input to another organisation. DITA provides interoperability because of its standard vocabulary.
    ```{admonition} However, ...

   However, DITA is not the only system that provides such interoperability, which can also be achieved by setting up the exact same publishing process at both places, whether through docs-as-code or through a commercially available writing software.
    ```
-  The organisation acquires (or is acquired by) another organisation, and they use disparate documentation systems. The larger a writing team and the larger a documentation suite, the more a need for standard writing systems and processes.
    ```{admonition} However, ...

   However, DITA is not the only system that provides enforceable standards. Any specifications-led system, such as DocBook, can achieve the same result. It's just that DITA is a more widely used standard than others.
    ```

<hr/>
