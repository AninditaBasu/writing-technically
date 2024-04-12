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

# DITA tags cheatsheet

<hr/>
<p style="font-weight:bold;font-size:75%;color:orange">11 April 2024</p>

DITA tags are semantic. The name of the tag is a clue to what that tag contains. For example, it's self-evident that the following tag (called `draft-comment`) is meant for holding review notes by an editor, SME, or writer.

`<draft-comment>Where are these values defined? In config.xml or categories.xml?</draft-comment>`

In the [previous lesson](courses-dita-authoring-tags.md), you learnt that not all tags can be used in all topic types. Hold that thought while you become familiar with some tags. Oftentimes, DITA gives you a choice of more than one tag. In such cases, choose a tag based on the meaning inherent in the content that you're tagging.

```{admonition} tagging != formatting

   Remember to use tags for their purpose and not for how their content is rendered (formatted, displayed, shown) in the output (`.html`, `.pdf`, or other).
   
   DITA does contain formatting tags such as `<b>` and `<i>`, but orgs didn't adopt DITA because of formatting.  Orgs adopt DITA, _inter alia_, because they want content to be marked up uniformly by everyone according to the meaning inherent in the content. No one looks at soe content and goes, "That means italics". The only meaning that an `<i>` tag can provide is this:
   
   ![Kiipsaare Lighthouse on the Harilaid peninsula on the island of Saaremaa, Estonia, in the territory of Vilsandi National Park](images/lighthouse_estonia.jpg)

```

The following sections describe some tags that'll find yourself using very often while writing in DITA.

## Lists

The tag to use depends on the kind of list you're writing.

Unordered list
: A list where the order of the items in not important and where each item is, typically, rendered with a bullet in the output.  The tag for an unordered list is `<ul>`, which cannot hold any content of its own except for one or more `<li>` tags where each `<li>` tag hold a list item.

  ````{eval-rst}
  .. tabs::

     .. tab:: DITA code
     
        .. code:: none
        
            <ul>
              <li> </li>
              <li> </li>
            </ul>
            
     .. tab:: Sample text
        
        -  Gold        
        -  Frankincense        
        -  Myrrh

     .. tab:: DITA-tagged sample text
     
        .. code:: none
        
            <ul>
              <li>Gold</li>
              <li>Frankincese</li>
              <li>Myrrh</li>
            </ul>

     .. tab:: Similar tags
     
        ``<steps-unordered>``
        
        See Procedures_.

  ````
  A ``<ul>`` tag can be used in the ``<concept>`` and ``<reference>`` topic types. It can also be used in the ``<task>`` topic type but, for task topics, also look at the tags that are listed in [Procedures](#procedures). 

Ordered list
: A list where the order of the items matters. Each item is rendered with a number, incremented by 1.  The tag for an ordered list is `<ol>`, which cannot hold any content of its own except for one or more `<li>` tags where each `<li>` tag hold a list item.

  ````{eval-rst}
  .. tabs::

     .. tab:: DITA code
     
        .. code:: none

            <ol>
              <li> </li>
              <li> </li>
            </ol>

     .. tab:: Sample text
        
        1.  Gold        
        2.  Frankincense        
        3.  Myrrh

     .. tab:: DITA-tagged sample text
     
        .. code:: none

            <ol>
              <li>Gold</li>
              <li>Frankincese</li>
              <li>Myrrh</li>
            </ol>

     .. tab:: Similar tags
     
        ``<steps>``
        
        See Procedures_.

  ````
  A ``<ul>`` tag can be used in the ``<concept>`` and ``<reference>`` topic types. It can also be used in the ``<task>`` topic type but if you find yourself using an `<ol>` in a task topic, pause. And ask yourself if the semantics of the content need a tag that's listed in [Procedures](#procedures). 

Definition list
: A list where each item contains two parts: a term and its definition. The parent tag for a definition list is `<dl>`, which cannot hold any content of its own except for one or more `<dlentry>` tags, where each `<dlentry>` tag holds a term (in a `<dt>`) and its definition (in a `<dd>`).

  ````{eval-rst}
  .. tabs::

     .. tab:: DITA code
     
        .. code:: none        
            
            <dl>
              <dlentry>
                <dt> </dt>
                <dd> </dd>
              </dlentry>
            </dl>
     
     .. tab:: Sample text
        
        Gold
            A precious yellow metallic element, highly malleable and ductile, and not subject to oxidation or corrosion.        
        Frankincense
            An aromatic gum resin from various Asian and African trees of the genus Boswellia, especially B. carteri, used chiefly for burning as incense in religious or ceremonial practices, in perfumery, and in pharmaceutical and fumigating preparations.        
        Myrrh
            An aromatic resinous exudation from certain plants of the genus Myrrhis, especially M. odorata, a small spiny tree: used for incense, perfume, etc.

     .. tab:: DITA-tagged sample text
     
        .. code:: none

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
        
        .. code:: none        
        
            <parml>
              <plentry>
                <pt> </pt>
                <pd> </pd>
               </plentry>
            </parml>
    
  ````
  A ``<dl>`` tag can be used in the ``<concept>``, ``<reference>``, and ``<task>`` topic types, but because it is for definition lists, which are in the nature of referential information, the best use of the ``<dl>`` tag is in the ``<reference>`` topic type.
  
  To decide whether to use ``<dl>`` or ``<parml>``, think of the nature of the content. If it's a series of argument for a command, the content is more in the nature of a parameter list than a definition list.

More list tags
: DITA has a few more tags for other kinds of lists, such as glossaries. You'll see them when you see them.

## Images

DITA has one tag for images; it's called `<image>` and has the following syntax: 

`<image href="remington.jpg"></image>`

In this example, the source of the image is a file called `filename.jpg`, which is specified through the `href` attribute.

The `<image>` tag can't contain anything except two optional child tags:

-  `<alt>`, for alternate text. Always a good writing practise to use this tag even though it's optional.
-  `<longdescref>`, for a reference to a file that contains a description of the image. The reference could be to a local file or to an external URL.

If you need the image to have a title, you put it inside a `<fig>` tag, like so:

```
<fig>
  <title>Tools of the Trade</title>
  <image href="remington.jpg">
    <alt>A picture of a Remington typewriter</alt>
    <longdescref href="https://www.britannica.com/technology/Remington"
              format="html"
              scope="external"/>
  </image>
</fig>
```

DITA being XML, it's also entirely possible to write your images as code, by using the `<svg-container>` tag to define a scalable vector graphic (SVG). This course doesn't cover DITA SVGs.

```{admonition} What about videos?

   DITA has an `<object>` tag that's similar to the HTML `<object>` tag. Put your videos in `<object>`.
```

## Tables

Just like there's more than one tag for lists, so it is for DITA tables too. But in all probability, you'll be using the `<table>` tag the most often.

Here's a comparison table of the table tags that can be used in concept, task, and reference topics.

|               | `<table>`                            | `<simpletable>` | `<choicetable>` |
|---------------|--------------------------------------|------|------|
| Header row    | Yes                                  | Yes | Yes |
| Header column | Yes                                  | Yes | Yes |
| Merge cells   | Yes                                  | No   | No   |
| Title         | Yes                                  | No   | No   |
| Where used    | `<concept>`, `<task>`, `<reference>` | `<concept>`, `<task>`, `<reference>` | `<task>` |

The `<table>` tag supports more accessibility features than the other two.

## Procedures

## Links

## Code


For a complete list, take a look at the [DITA language specification](https://docs.oasis-open.org/dita/v1.2/os/spec/language_reference.html#language_reference). Again, remember that you don't need to memorise these tags; just be aware, broadly, of what's available and where they can be used. In the [next lesson](xxx.md), you'll learn write some topics with these tags.

##  Summary


##  Exercise



<hr/>

```{include} courses-dita-authoring-toc.md
```
   
<hr/>
