---
myst:
  html_meta:
    "canonical": "https://writing-technically.readthedocs.io/en/latest/courses-dita-authoring-topics-linking.html"
    "description": "A lesson that shows how to create links and relationships between topics in DITA, and contains some exercises"
    "title": "Learn to link DITA topics to each other by more than one method"
    "twitter:description": "A lesson that shows how to create links and relationships between topics in DITA, and contains some exercises"
    "twitter:title": "Learn to link DITA topics to each other by more than one method"
    "twitter:image": "https://writing-technically.readthedocs.io/en/latest/_static/wordcloud.jpg"
    "twitter:card": "summary_large_image"
    "twitter:creator": "@anindita_basu"
    "twitter:site": "@anindita_basu"
    "og:locale": "en_US"
    "og:site_name": "Writing technically"
    "og:url": "https://writing-technically.readthedocs.io/en/latest/courses-dita-authoring-topics-linking.html"
    "og:type": "article"
    "og:title": "Learn to link DITA topics to each other by more than one method"
    "og:description": "A lesson that shows how to create links and relationships between topics in DITA, and contains some exercises"
    "og:image": "https://writing-technically.readthedocs.io/en/latest/_static/wordcloud.jpg"
    "author": "Anindita Basu"
---

# DITA lesson 6: Topics, linking

<hr/>
<p style="font-weight:bold;font-size:75%;color:orange">31 May 2024</p>

By now, you know how to create topics and assemble them into a map to generate a guide. You'll recall that previous lessons stressed that DITA topics are standalone entities that should make sense on their own. However, oftentimes, a concept is linked to a task (or two), or a task needs some data that's contained in a reference topic.  DITA has more than one method to create links between topics, as you'll see in this lesson.

## Inline links (`xref`)

To create an inline link, where clicking the linked word or phrase leads you directly to a specific topic (or a section within that topic), use the `<xref>` tag, like so:

````{eval-rst}
.. code-block:: xml

    <xref href = "tides.dita"></xref>
````

Notice that in this example, nothing is contained within the `<xref>` tag itself, which has only an `href` attribute with the name of the DITA file it's linking to. How then, do you ask, will anyone know where to click, because no words are specified for the link. Well, it's because when the link is to a DITA topic (like it is in this example), the DITA output processor will automatically pick the title of the topic as the clickable link text.

You might want to override this default behaviour and provide your own text. To do so, place your text between the `<xref>` tags, like so:

````{eval-rst}
.. code-block:: xml

    <xref href = "tides.dita">the tide tables during November</xref>
````

## Related links (`related-links`)

When two files are related to each other, such that someone reading one of the files _might_ want to read the other one too, but you don't want to interrupt the flow in the topic by introducing a jump in the middle of the topic, you can specify a list of related files at the end of the topic, like so:

````{eval-rst}
.. code-block:: xml

    <related-links>
      <link href="sun.dita"></link>
      <link href="saturn.dita"></link>
    </related-links>
````

## Relationship tables (`topicref`)

Sometimes, you might not want to specify topic relationships through the `<related-links>` tag in a topic (you'll see the reasons in a subsequent lesson). How would you specify topic relationships in such cases? You do so by using a table in a map file. The table in a map file is a special kind of DITA table, and uses the `<reltable>` tag. For your writing purposes, though, think of this table like any other table with rows and columns, where every cell contains the name of a topic file, and all topics in a row are linked to each other.

Typically, relationship tables have either 2 or 3 columns. In 3-column tables, typically, column 1 contains concept files, column 2 task files, and column 3 reference files, and all files in a row link to each other. If a cell contains more than one file, the default behavious is that the files in the same cell don't link to each other; they link only to the other files in the same row.

Consider the following example:

| Column 1            | Column 2                                                 |
|---------------------|----------------------------------------------------------|
| `install.dita`      | `config_params_macos.dita`, `config_params_windows.dita` |
| `enable_admin.dita` | `user_permissions.dita`                                  |

In the output, the related links are created as follows (even though these links are not specified inside the topics themselves):

-  `install.dita` contains links to two files: `config_params_macos.dita` and `config_params_windows.dita`
-  `config_params_macos.dita` contains a link to `install.dita`
-  `config_params_windows.dita` contains a link to `install.dita`
-  `enable_admin.dita` contains a link to `user_permissions.dita`
-  `user_permissions.dita` contains a link to `enable_admin.dita`

Each cell in a `<reltable>` tag contains `<topicref>` elements, like this:

````{eval-rst}
.. code-block:: xml

    <reltable>
      <relheader>
       <relcolspec type="concept">
       <relcolspec type="task">
       <relcolspec type="reference">
      </relheader>
      <relrow>
       <relcell><topicref href="A.dita"/></relcell>
       <relcell><topicref href="B.dita"/><topicref href="C.dita"/></relcell>
       <relcell><topicref href="D.dita"/><topicref href="E.dita"/></relcell>
      </relrow>
     </reltable>
````

Again, remember that you don't need to memorise all of these tags; your authoring tool will aid you in inserting topic references. Just be aware of the different methods of inserting links in your topics.

## Recap

-  In topics:
    - `<xref>` is for inline links; the title of the linked topic is automatically treated as the link text.
    -  `<related-links>` is for specifying a linked list at the end of the file.
-  In maps, `<reltable>` is used for specifying topic links. All files in a row link to each other but files in the same cell in that row don't link to each other.


##  Exercise

Use XMLMind Editor to do the following assignments. Feel free to play around with tags.

1.  Download the sample files for this lesson ([DITA lesson 6 sample files](_static/dita_lesson6_sampleFiles.zip)) and extract them to your computer.
1.  Open the `pens_and_printers.ditamap` file and generate an HTML output (**Map** > **Convert document** > **Convert to XHTML**).
1.  Open the topic called `Refilling a fountain pen` and scroll down to the end of the page to the `Related information` section. Notice the broken links. Can you tell:
    -  Why the links are here? (Answer: It's because a relationship has been defined through a `reltable` element in the `pens_and_printers.ditamap` file.)
    -  Why are the links broken? (Answer: It's because the linked files are not on the ToC. Unless a file is in the ToC in the map, it is not transformed to an output. Notice that the two broken link files, `c_fill_mechanism_pens.dita` and `r_ink_pen_printer.dita` are not on the ToC in the `pens_and_printers.ditamap` file.)
1.  Put the `c_fill_mechanism_pens.dita` and `r_ink_pen_printer.dita` files on the ToC. However, ensure that they are not 'visible' when the output is generated. To do so, use the `toc` attribute of the `topicref` element, like so: `<topicref href="r_ink_pen_printer.dita" toc="no"/>`.
1.  Generate an output and see that the links in the `Related information` section of the `Refilling a fountain pen` topic are no longer broken.
1.  Open the map file that you created in the previous lesson, and insert a relationship table. Then, generate an output and see the results.
1.  Open any of the topics that you created in the previous lessons, and insert a `<related-links>` tag in it. Return to the map file, generate an output, and see the results.

## What next?

The next few lessons show you how to single-source.

<hr/>

```{include} courses-dita-authoring-toc.md
```
   
<hr/>

```{include} courses-dita-authoring-bugs.md
```

<hr/>
