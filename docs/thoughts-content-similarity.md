# Identical files

<hr/>

Sometimes, we create files. Other times, we inherit files. Many a times, we share files across products and services. In all of this, what remains constantly unwaveringly unstintingly true is...bloat. Our documentation sets grow in size, and keep growing, and before long, we're staring at docs debt.

![burden](/images/burden.png)

A documentation set that I ran a scan on, for example, revealed the following numbers.

```
21754: Total number of DITA files (.dita, .ditamap)
20563: Files with only 1 commit (which means, they've never been updated)
1029: Files with 2 commits (which means, they were updated only once)
162: Files with more than 2 commits (the remainder)
```

Do we need to carry this debt on our heads? Aren't we creating our own little Hotel Californias, where docs can sign out any time they want, but they can't ever leave?

But, but, but.......how does one identify duplicate files? Doing so isn't easy at all, right?

Well, it might not be easy but it's not impossible. Also, we don't need to do everything manually. These days, we have computers  for the heavy lifting, leaving us humans free to focus on the creative aspects.

So, I explored a few content analysis libraries.

## `difflib`, a standard Python library for analysing text sequences

The `difflib` library compares sequences, where a sequence is the sentences in the text files. The similarity ratio is calculated as follows:

 `similarity_ratio = 2 * length_of_lcs / (length_of_sequence1 + length_of_sequence2)`

where,

-  `length_of_lcs` = length of the longest common subsequence
-  `length_of_sequence1` = the length of the first sequence
-  `length_of_sequence2` = the length of the second sequence
-  A subsequence is a sequence of elements that appears in the same relative order in both sequences, but not necessarily consecutively.

This was the library I explored first, and I got good enough results. But I thought I'll explore a bit more because the processing time was too long. 

## `spaCy`, a Python FOSS library for NLP

I found this library to be excellent for reporting on the grammatical aspects of text, but not so much for text comparisons. That's because the trained, free models of spaCy don't have word embeddings (and I have no intention of spending time training it with my docs).

I'll be exploring spaCy more for possible use as a machine-reviewer, before text is passed on to a human editor, but I won't be using it for text-comparison purposes.

## `nltk`, a pip-installable Python library for NLP

This library showed the most promise, and I ended up choosing this one. It has several methods for finding similar text:

-  The cosine method: I don't understand the maths behind it, or the explanations, but the it gave me okay-ish results. While word-to-word identical files were identified correctly, it didn't do as well in identifying sentences fragments that were identical.
-  The wordnet method, which takes the semantics of the words into account. I thought this would be good for identifying sentences that convey the same thing despite being worded differently. I was disappointed by the results, though.
-  The Jaccard method, which is the one that gave me the most astonishingly accurate results.The similarity ratio is calculated as follows:
    `J(A, B) = |A ∩ B| / |A ∪ B|` where	`A` and `B` are the tokenized text of the two files being compared

 This is where I stopped exploring, and started running pilots with writers. (It's working well.) 

Both `difflib` and `nltk.metrics.jaccard_distance` give good results but I chose the Jaccard method because of its accuracy and speed. Here are some numbers for speed.

|  | difflib |	jaccard |
|---|---|---|
| 797 files | 40 minutes | 30 minutes |
| 4151 files | 7 hours | 4 hours |
| 2561 files | 5 hours | 3 hours |

And, here's a screenshot of a file-pair that `jaccard` reported as being 81.82% identical (while `difflib` said 79.82%). The Jaccard score is more accurate.  

![burden](/images/almost_identical_2.png)

*(I added the underlines in these files, and highlighted some text, only for screenshot purposes. They show the differences in this part of the text.)*

## What next

Now to write up some guidelines on how to deal with files that are a 100% match, those that are 99% to 90% similar, and ones that have 89% to 90% similar content.

We work with DITA, which already has content reuse built in. All that's needed now is, armed with these results, use the reuse mechanism effectively.  Benefits?

-  Reduced file count, so: 
    -  Reduced resource consumption by machines (storage, clone time, build time)
	-  Lesser time spent by humans to update, edit, review, and maintain
-  Reduced word count, so reduced translation costs.

<hr/>