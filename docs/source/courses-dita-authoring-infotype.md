---
myst:
  html_meta:
    "canonical": "https://writing-technically.readthedocs.io/en/latest/courses-dita-authoring-infotype.html"
    "description": "A lesson that explains information typing in DITA and contains some exercises"
    "title": "Learn about information typing in DITA"
    "twitter:description": "A lesson that explains information typing in DITA and contains some exercises"
    "twitter:title": "Learn about information typing in DITA"
    "twitter:image": "https://writing-technically.readthedocs.io/en/latest/_static/wordcloud.jpg"
    "twitter:card": "summary_large_image"
    "twitter:creator": "@anindita_basu"
    "twitter:site": "@anindita_basu"
    "og:locale": "en_US"
    "og:site_name": "Writing technically"
    "og:url": "https://writing-technically.readthedocs.io/en/latest/courses-dita-authoring-infotype.html"
    "og:type": "article"
    "og:title": "Learn about information typing in DITA"
    "og:description": "A lesson that explains information typing in DITA and contains some exercises"
    "og:image": "https://writing-technically.readthedocs.io/en/latest/_static/wordcloud.jpg"
    "author": "Anindita Basu"
---

# Information typing in DITA

<hr/>
<p style="font-weight:bold;font-size:75%;color:orange">9 April 2024</p>

As a technical writer, you probably know that a lot of your time is spent not on the actual writing, but in gathering information and in thinking how to present that information in a manner that helps your readers.

You don't write novels, stories, poems, or thrillers. What you write is not read by people at leisure for pleasure; what you write is read by people who're looking for very specific types of information and are very definitely _not_ at leisure.

```{admonition} Definition

   The process of sorting information into specific categories is called information typing. 
```

DITA architecture has something called topic types, which you can think of as blocks that:

-  Are built in a specific way, based on a standard model
-  Answer one - and only one - type of question

DITA has several topic types; this course focusses on the following three topic types: concept, task, and reference.

Concept
: Explanations and descriptions about things.  Concept topics answer questions such as "What is this about", "Why does it behave the way it does" or "Where does it fit into the overall scheme of things?"
```{image} images/rodin_thinker.jpg
:alt: The Thinker by Auguste Rodin the Musée Rodin in Paris uploaded to https://commons.wikimedia.org/w/index.php?curid=94532194 by CrisNYCa - Own work, CC BY-SA 4.0
:align: center
```

Task
: The steps that are needed to achieve a specific goal or result.  Task topics answer the question "How do I do this?"
```{image} images/Quit_India_Movement_2017_stamp8.jpg
:alt: A commemorative postage stamp on 1942 FREEDOM MOVEMENT with the slogan Do or Die issued by the Government of India, licensed under the Government Open Data License - India (GODL)
:align: center
```

Reference
: A collection of values, data, code snippets, or any information that are needed when doing a task but don't need to be remembered or internalised. Reference topics answer questions such as "What are the system settings", "What are the default parameter values", or "What were the arguments for that command again?"
```{image} images/dictionary.jpg
:alt: A multi-volume Latin dictionary by Egidio Forcellini at https://commons.wikimedia.org/w/index.php?curid=462068 by Dr. Marcus Gossler - Own work, CC BY-SA 3.0
:align: center
```

<p>&nbsp;</p>

Every DITA topic is a stand-alone topic that's answering a very specific question. If you think of a DITA topic as a web page on a documentation portal, think of every page as an independent entity that's capable of being read and understood in isolation, independent of other pages on that documentation portal. The DITA writing paradigm is not a linear paradigm with Previous and Next content; the DITA sea is choppy and DITA topics are meant to stand alone.

The exercise at the end of this lesson is meant for providing some practise in chopping information into topic types.

## Recap

-  DITA information types are standalone entities that answer just one question.
-  The concept topic-type is for explanations.
-  The task topic-type is for procedures.
-  The reference topic-type is for data. 

##  Exercise

Writing in DITA is about segragating content into topic types. To get some practise into this task, look at the following books and chunk its content into one or more blocks of _concept_, _task_, and _reference_. Use any text editor that you like.

-  [Astrolabe Treatise](_static/chaucer_astrolabe_treatise.pdf)
-  [Knitting, Crochet, and Netting](_static/knitting_crochet_netting.pdf)

Or, if you'd rather do things from scratch, how about this: Imagine that you've been asked to produce documentation for a musical instrument called _shehnai_. Think of what all you'll write, and note down these section names or titles of the parts of your document (which, effectively, means that you're creating an outline or a table of contents for your document). Think of the questions that these parts are going to answer. Then, label these parts as _concept_, _task_, and _reference_. Again, use any text editor that you're comfortable with.

![Stamp from India showing the legendary Bismillah Khan](/images/bismillah_khan.jpg)

<hr/>

Lessons:

```{include} courses-dita-authoring-toc.md
```

<hr/>
