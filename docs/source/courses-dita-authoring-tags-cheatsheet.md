---
myst:
  html_meta:
    "canonical": "https://writing-technically.readthedocs.io/en/latest/courses-dita-authoring-tags-cheatsheet.html"
    "description": "A lesson that explains how to pick a DITA tag when more than one tag is available for the purpose"
    "title": "Learn about choosing tags in DITA"
    "twitter:description": "A lesson that explains how to pick a DITA tag when more than one tag is available for the purpose"
    "twitter:title": "Learn about choosing tags in DITA"
    "twitter:image": "https://writing-technically.readthedocs.io/en/latest/_static/wordcloud.jpg"
    "twitter:card": "summary_large_image"
    "twitter:creator": "@anindita_basu"
    "twitter:site": "@anindita_basu"
    "og:locale": "en_US"
    "og:site_name": "Writing technically"
    "og:url": "https://writing-technically.readthedocs.io/en/latest/courses-dita-authoring-tags-cheatsheet.html"
    "og:type": "article"
    "og:title": "Learn about choosing tags in DITA"
    "og:description": "A lesson that explains how to pick a DITA tag when more than one tag is available for the purpose"
    "og:image": "https://writing-technically.readthedocs.io/en/latest/_static/wordcloud.jpg"
    "author": "Anindita Basu"
---

# DITA lesson 3: Tags, cheatsheet

<hr/>
<p style="font-weight:bold;font-size:75%;color:orange">11 April 2024</p>

DITA tags are semantic. The name of the tag is a clue to what that tag contains. For example, it's self-evident that the following tag (called `draft-comment`) is meant for holding review notes by an editor, SME, or writer.

````{eval-rst}
.. code-block:: xml

    <draft-comment>Where are these values defined? 
        In config.xml or categories.xml?</draft-comment>
````

In the [previous lesson](courses-dita-authoring-tags.md), you learnt that not all tags can be used in all topic types. Hold that thought while you become familiar with some tags. Oftentimes, DITA gives you a choice of more than one tag. In such cases, choose a tag based on the meaning inherent in the content that you're tagging.

```{admonition} DITA tagging != formatting

   DITA taging is about the type of content ("_This is a note._" "_These sentences form a paragraph._" "_This information belongs to a table._") rather than the appearance of the content ("_Underline this word._" "_Italicise this phrase._" "_Make this word look bold and strong._")
   
   DITA does contain formatting tags such as `<b>` and `<i>`, but orgs didn't adopt DITA because of formatting.  Orgs adopt DITA, _inter alia_, because they want content to be marked up uniformly by all writers. And, no writer can look at some content and go, "_This information is [italics](words-italics.md)_".   

```

## Lists

The tag to use depends on the kind of list you're writing.

Unordered list
: A list where the order of the items in not important and where each item is, typically, rendered with a bullet in the output.  The tag for an unordered list is `<ul>`, which cannot hold any content of its own except for one or more `<li>` tags where each `<li>` tag hold a list item.

  ````{eval-rst}
  .. tabs::

     .. tab:: DITA code
     
        .. code:: xml
        
            <ul>
              <li> </li>
              <li> </li>
            </ul>
            
     .. tab:: Sample text
        
        -  Gold        
        -  Frankincense        
        -  Myrrh

     .. tab:: Tagged sample text
     
        .. code:: xml
        
            <ul>
              <li>Gold</li>
              <li>Frankincese</li>
              <li>Myrrh</li>
            </ul>

     .. tab:: Similar tags
     
        ``<steps-unordered>``

  ````
  A ``<ul>`` tag can be used in the ``<concept>`` and ``<reference>`` topic types. It can also be used in the ``<task>`` topic type but, for task topics, also look at the tags that are listed in [Procedures](#procedures). 

Ordered list
: A list where the order of the items matters. Each item is rendered with a number, incremented by 1.  The tag for an ordered list is `<ol>`, which cannot hold any content of its own except for one or more `<li>` tags where each `<li>` tag hold a list item.

  ````{eval-rst}
  .. tabs::

     .. tab:: DITA code
     
        .. code:: xml

            <ol>
              <li> </li>
              <li> </li>
            </ol>

     .. tab:: Sample text
        
        1.  Gold        
        2.  Frankincense        
        3.  Myrrh

     .. tab:: Tagged sample text
     
        .. code:: xml

            <ol>
              <li>Gold</li>
              <li>Frankincese</li>
              <li>Myrrh</li>
            </ol>

     .. tab:: Similar tags
     
        ``<steps>``

  ````
  A ``<ul>`` tag can be used in the ``<concept>`` and ``<reference>`` topic types. It can also be used in the ``<task>`` topic type but if you find yourself using an `<ol>` in a task topic, pause. And ask yourself if the semantics of the content need a tag that's listed in [Procedures](#procedures). 

Definition list
: A list where each item contains two parts: a term and its definition. The parent tag for a definition list is `<dl>`, which cannot hold any content of its own except for one or more `<dlentry>` tags, where each `<dlentry>` tag holds a term (in a `<dt>`) and its definition (in a `<dd>`). One term (`<dt>`) can have more than one definition (`<dd>`), just like in a dictionary, a word entry can have more than one meaning. 

  ````{eval-rst}
  .. tabs::

     .. tab:: DITA code
     
        .. code:: xml        
            
            <dl>
              <dlentry>
                <dt> </dt>  <!-- for the term -->
                <dd> </dd>  <!-- for the definition -->
              </dlentry>
            </dl>
     
     .. tab:: Sample text
        
        Gold
            A precious yellow metallic element, highly malleable and ductile, and not subject to oxidation or corrosion.        
        Frankincense
            An aromatic gum resin from various Asian and African trees of the genus Boswellia, especially B. carteri, used chiefly for burning as incense in religious or ceremonial practices, in perfumery, and in pharmaceutical and fumigating preparations.        
        Myrrh
            An aromatic resinous exudation from certain plants of the genus Myrrhis, especially M. odorata, a small spiny tree: used for incense, perfume, etc.

     .. tab:: Tagged sample text
     
        .. code:: xml

            <dl>
              <dlentry>
                <dt>Gold</dt>
                <dd>A precious yellow metallic element, highly malleable and ductile, and not subject to oxidation or corrosion.</dd>
              </dlentry>
              <dlentry>
                <dt>Frankincense</dt>
                <dd>An aromatic gum resin from various Asian and African trees of the genus Boswellia, especially B. carteri, used chiefly for burning as incense in religious or ceremonial practices, in perfumery, and in pharmaceutical and fumigating preparations.</dd>
              </dlentry>
              <dlentry>
                <dt>Myrrh</dt>
                <dd>An aromatic resinous exudation from certain plants of the genus Myrrhis, especially M. odorata, a small spiny tree: used for incense, perfume, etc.</dd>
              </dlentry>
            </dl>

     .. tab:: Similar tags
     
        ``<parml>``
        
        For a list of terms and definitions for the parameters on a user interface.
        
        .. code:: xml        
        
            <parml>
              <plentry>
                <pt> </pt>  <!-- for the parameter name -->
                <pd> </pd>  <!-- for the parameter description -->
               </plentry>
            </parml>
    
  ````
  A ``<dl>`` tag can be used in the ``<concept>``, ``<reference>``, and ``<task>`` topic types, but because it is for definition lists, which are in the nature of referential information, the best use of the ``<dl>`` tag is in the ``<reference>`` topic type.
  
  To decide whether to use ``<dl>`` or ``<parml>``, think of the nature of the content. If it's a series of argument for a command, the content is more in the nature of a parameter list than a definition list.

More list tags
: DITA has a few more tags for other kinds of lists, such as glossaries. You'll see them when you see them.

## Images

DITA has one tag for images; it's called `<image>` and has the following syntax: 

````{eval-rst}
.. code-block:: xml

    <image href="remington.jpg"></image>
````

In this example, the source of the image is a file called `remington.jpg`, which is specified through the `href` attribute.

The `<image>` tag can't contain anything except two optional child tags:

-  `<alt>`, for alternate text. Always a good writing practise to use this tag even though it's optional.
-  `<longdescref>`, for a reference to a file that contains a description of the image. The reference could be to a local file or to an external URL.

If you need the image to have a title, you put it inside a `<fig>` tag, like so:

````{eval-rst}
.. code-block:: xml

    <fig>
      <title>Tools of the Trade</title>
      <image href="remington.jpg">
        <alt>A picture of a Remington typewriter</alt>
        <longdescref href="https://www.britannica.com/technology/Remington"
                  format="html"
                  scope="external"/>
      </image>
    </fig>
````

DITA being XML, it's also entirely possible to write your images as code, by using the `<svg-container>` tag to define a scalable vector graphic (SVG). This course doesn't cover DITA SVGs.

```{admonition} What about videos?

   DITA has an `<object>` tag that's similar to the HTML `<object>` tag. Put your videos in `<object>`.
```

## Tables

Just like there's more than one tag for lists, similarly, there's more than one DITA tag for tables too.  Here's a comparison table of some of the table tags that can be used in concept, task, and reference topics.

|  | `<table>` | `<simpletable>` | `<choicetable>` |
|--|-----------|------|------|
| Header row | Yes  | Yes | Yes |
| Header column | Yes  | Yes | Yes |
| Merge cells | Yes  | No  | No   |
| Title | Yes | No  | No  |
| Where used | `<concept>`, `<task>`, `<reference>` | `<concept>`, `<task>`, `<reference>` | `<task>` |

The `<table>` tag supports more accessibility features than the other two.

## Procedures

The most commonly used tag is `<steps>`, which cannot hold anything other than one or more `<step>` tags.

The `<step>` tag can't hold anything in it either except for a single `<cmd>` tag. `cmd` is short for `command`. I believe the tag was named `cmd` because every sentence in a step is an imperative statement. Do this; do that.

````{eval-rst}
.. tabs::

   .. tab:: DITA code
     
      .. code:: xml        
            
           <steps>
             <step><cmd> </cmd></step>
             <step><cmd> </cmd></step>
           </steps>
     
   .. tab:: Sample text
        
      1.  Rise, brothers, rise.        
      2.  Come, let us gather our nets from the shore.        
      3.  Set our catamarans free.

   .. tab:: Tagged sample text
     
      .. code:: xml

           <steps>
            <step><cmd>Rise, brothers, rise. </cmd>
            <step><cmd>Come, let us gather our nets from the shore.</cmd>
            <step><cmd>Set our catamarans free.</cmd>
           </steps>

   .. tab:: Similar tags
     
      ``<ol>``, for ordered lists.
      
      Also, ``<steps-unordered>``, which can be used for procedures where the order of the steps is not important.
        
      Both ``<steps>`` and ``<steps-unordered>`` are valid tags for a task topic but a task topic can contain either ``<steps>`` or ``<steps-unordered>``, not both.       

````

## Links

For cross-references, through the `<link>` tag and its attributes:

The `href` attribute
: For the link destination, which can be a DITA file, a location within a file, or a URL.

The `scope` attribute
: For the degree of separation between the source and the target. Allowed values are `local`, `peer`, `external`, and `-dita-use-conref-target`.

Links can have several more attributes. You'll see them by and by.

## Code

For inline code, there's `<codeph>`; for code that spans more than one line, there's `<codeblock>`.

````{eval-rst}
.. tabs::

   .. tab:: ``codeph``
      
      DITA code:
      
      .. code:: xml 
                             
           <p>Run the following command from the terminal: <codeph>curl -d "@apitest.json" -X POST http://127.0.0.1:8000/data</codeph>.<p>
       
      Sample output:
      
      Run the following command from the terminal: ``curl -d "@apitest.json" -X POST http://127.0.0.1:8000/data``.
     
   .. tab:: ``codeblock``
        
      DITA code:
      
      .. code:: xml 
                             
           <p>The call can have more than one path parameter, 
               where each parameter is enlosed in braces.</p>
               
           <codeblock>
           GET /mandal/{id}
           GET /mandal/{id}/sukta/{sid}
           GET /verses.{format}
           </codeblock>
       
      Sample output:      
      
      The call can have more than one path parameter, where each parameter is enlosed in braces.
      
      .. code-block:: none
      
          GET /mandal/{id}
          GET /mandal/{id}/sukta/{sid}
          GET /verses.{format}

````

## Sundry

The following tags are also often encountered in techdocs.

`<shortdesc>`
: One single paragraph that contains a description of the contents of the topic.

`<section>`
: A logical unit to group (or, organise) content. Very roughly analogous to the `div` tag in HTML.

`<note>`
: A comment, explanation, cautionary advice, or warning.

`<p>`
: A paragraph.

##  Summary

For a complete list, take a look at the [DITA language specification](https://docs.oasis-open.org/dita/v1.2/os/spec/language_reference.html#language_reference). Again, remember that you don't need to memorise these tags; just be aware, broadly, of what's available and where they can be used. In the [next lesson](courses-dita-authoring-topics.md), you'll learn to write some topics with these tags.

<hr/>

```{include} courses-dita-authoring-toc.md
```
   
<hr/>
