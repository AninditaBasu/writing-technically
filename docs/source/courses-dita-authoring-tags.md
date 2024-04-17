---
myst:
  html_meta:
    "canonical": "https://writing-technically.readthedocs.io/en/latest/courses-dita-authoring-tags.html"
    "description": "A lesson that explains common DITA tags and contains some exercises"
    "title": "Learn about tagging in DITA"
    "twitter:description": "A lesson that explains common DITA tags and contains some exercises"
    "twitter:title": "Learn about tagging in DITA"
    "twitter:image": "https://writing-technically.readthedocs.io/en/latest/_static/wordcloud.jpg"
    "twitter:card": "summary_large_image"
    "twitter:creator": "@anindita_basu"
    "twitter:site": "@anindita_basu"
    "og:locale": "en_US"
    "og:site_name": "Writing technically"
    "og:url": "https://writing-technically.readthedocs.io/en/latest/courses-dita-authoring-tags.html"
    "og:type": "article"
    "og:title": "Learn about tagging in DITA"
    "og:description": "A lesson that explains common DITA tags and contains some exercises"
    "og:image": "https://writing-technically.readthedocs.io/en/latest/_static/wordcloud.jpg"
    "author": "Anindita Basu"
---

# Tagging in DITA

<hr/>
<p style="font-weight:bold;font-size:75%;color:orange">9 April 2024</p>

In the [previous lesson](courses-dita-authoring-infotype.md), you learnt about arranging information into discrete buckets called topic types. In this lesson, you'll learn how to move that information to the DITA vocabulary.

DITA is a markup language, which means that all content in DITA is marked up (or, labelled with) tags. Because DITA tags are almost always semantic, the name of the tag itself is a clue to its purpose and function.

![DITA tag cloud](/images/dita_tags.png)

For example, consider the following text: `The Adventures of Tom Sawyer`

This text can be marked up with a tag called `<title>` in the following manner:

````{eval-rst}
.. code-block:: xml

    <title>The Adventures of Tom Sawyer</title>
````

DITA has a finite set of tags, and has strict rules about which tags can be used where. Every topic type has its own set of tags. Some tags can be used in all topic types; some can't and are specific to only certain topic types. For example, the tag called `<steps>` can be used only in a `<task>` topic type, while the tag called `<section>` can be used in both `<concept>` and `<reference>` topic types, but not in the `<task>` topic type.

Further, some tags can contain child tags and sometimes, the parent tag can hold content independently (along with child tags and their content) but sometimes, the only thing that a parent tag can hold is child tags. Here's an example for each of these two cases.

````{eval-rst}
.. tabs::

   .. tab:: Parent tag can hold content by itself

      .. code-block:: xml

          <note>The value in the <varname>outputdir</varname> field 
          should include the complete file path.</note>
      
      In this example, the ``<note>`` tag contains some text and also contains another tag called ``<varname>``.

   .. tab:: Parent tag can't

      .. code-block:: xml

          <step><cmd>In Windows Explorer, go to the Sphinx 
          installation directory.</cmd></step>
      
      In this example, the parent tag called ``<step>`` can't hold anything by itself; it can hold only a child tag called ``<cmd>`` that holds the text.

````

Every DITA topic must have the following two tags as an essential requirement:

-  The tag for the topic type. These tags are eponymous: `<concept>`, `<task>`, and `<reference>`.
-  A `<title>` tag that immediately follows the topic-type tag.

Therefore, all the following three examples are valid DITA files.

````{eval-rst}
.. tabs::

   .. tab:: Concept

      .. code-block:: xml
      
          <concept id = "some_ID">
          
          <title>The adventures</title>
          
          </concept>

   .. tab:: Task

      .. code-block:: xml
      
          <task id = "some_ID">
      
          <title>Adventuring</title>
      
          </task>

   .. tab:: Reference

      .. code-block:: xml
      
          <reference id = "some_ID">
      
          <title>Adventure chronology</title>
      
          </reference>

````

However, you and I live in the real world. Most of the time. In the real world, all DITA authoring tools will almost always insert (automatically, without being asked) a _body_ tag after that first essential `<title>` tag.

![Sculpture at Notre Dame of Saint Denis holding his head](/images/saint_denis.jpg)

Therefore, in the usual tech-writer life, a minimally valid DITA topic looks like this:

````{eval-rst}
.. tabs::

   .. tab:: Concept

      .. code-block:: xml
      
          <concept id = "some_ID">
          
          <title>The adventures</title>
          
          <conbody>
          ...
          Why do I exist?
          ...
          </conbody>
          
          </concept>

   .. tab:: Task

      .. code-block:: xml
      
          <task id = "some_ID">
      
          <title>Adventuring</title>
          
          <taskbody>
          ...
          How do I exist?
          ...
          </taskbody>
                
          </task>

   .. tab:: Reference

      .. code-block:: xml
      
          <reference id = "some_ID">
      
          <title>Adventure chronology</title>
          
          <refbody>
          ...
          What are the existential milestones?
          ...
          </refbody>
                
          </reference>

````

You don't have to memorise either the tag names or the places where they can be used. DITA is an authoring system that's used by very large enterprises, which will always make available some kind of XML authoring tool to its writers. All of these DITA authoring tools have in-built validations that make it ~~impossible~~ very difficult for you to mark up content with an invalid tag. The important thing for a writer is to decide which topic type to use, and then to take the help of the authoring tool to insert tags as needed. 

For the curious, however, here's an indicative list of tags that these topic types can contain. It's not a complete list.

````{eval-rst}
.. tabs::

   .. tab:: Concept

      .. code-block:: xml
      
          <concept> *
	          <title>  </title> *
	          <titlealts>  </titealts>
	          <shortdesc>  </shortdesc>
	          <conbody>
		          <dl> | <parml> | <div> | <fig> | 
		          <syntaxdiagram> | <imagemap> | <image> | 
		          <note> | <ol> | <p> | <pre> | <codeblock> | 
		          <msgblock> | <screen> | <simpletable> | 
		          <sl> | <table> | <ul> | <section> |
	          </conbody>
	          <related-links>  </related-links>
          </concept> *


   .. tab:: Task

      .. code-block:: xml
      
          <task> *
	          <title>  </title> *
	          <titlealts>  </titealts>
	          <shortdesc>  </shortdesc>
	          <taskbody>
		          <prereq>  </prereq>
		          <context>  </context>
		          <steps>
		                <step><cmd>  </cmd></step>		     
		          </steps>
		          <result>  </result> 
		          <postreq>  </postreq> 
	          </taskbody>
	          <related-links>  </related-links>
          </task> *

   .. tab:: Reference

      .. code-block:: xml
      
          <reference> *
	          <title>  </title> *
	          <titlealts>  </titealts>
	          <shortdesc>  </shortdesc>
	          <refbody>
		          <section> | <example> | <dl> | <parml> | 
		          <div> | <fig> | <syntaxdiagram> | <imagemap> | 
		          <image> | <note> | <ol> | <p> | <pre> | 
		          <codeblock> | <msgblock> | <screen> | <simpletable> | 
		          <sl> | <table> | <ul> | 
	          </refbody>
	          <related-links>  </related-links>
          </reference> *

````

Every tag has a name, for example, `shortdesc` or `title`. Every tag also has several attributes that describe the tag. You can think of attributes as tag-metadata; they contain information about, and for, the tag. 

```{admonition} ID required for topic type

   Every topic-type tag must always have an `id` attribute. 
   
   So, `<concept></concept>` will always fail a validation check; `<concept id="_some_value_"></concept>` will pass.

```

A tag can have more than one attribute.  Every attribute has a name  and a value. Here's an example of a `link` tag that has an attribute named `href` (with the value being `pqr.dita`) and an attribute named `scope` (whose value is `local`).

````{eval-rst}
.. code-block:: xml

    <link scope="local" href="pqr.dita">
````

In the [next lesson](courses-dita-authoring-tags-cheatsheet.md), you'll learn about a few DITA tags that are often used for marking up lists, tables, images, steps, and such other things that are used by technical writers.

##  Recap

-  Every topic type has a finite set of tags that can be used in a very specific order.
-  Only one tag is an essential tag in every topic type. This tag is the `<title>` tag that immediately follows the tag for the topic type.
-  Some tags are exclusive to certain topic types; some tags can be used in more than one topic type.
-  Tags can contain other tags but this is unidirectional; no parent tag can ever be contained by any tag that can become its child tag.
-  Tags can have one or more attributes, where each attribute is like a key-value pair.

<hr/>

```{include} courses-dita-authoring-toc.md
```
   
<hr/>
