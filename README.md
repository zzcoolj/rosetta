# Rosetta Project
## General Information

### Development/Programming
- [Check out team work boards in Trello](https://trello.com/b/LulZRg4T/rosetta4slavic)
- Jump into hackers team: contact me!

### Algorithms research
- Read this PhD [thesis](references/73143_XU_2016_diffusion.pdf) Page 83 (P98 in pdf) - Page 89 (P104 in pdf)

### Experts analysis and crowd sourcing
- Papers to read
    - [The BAF: A Corpus of English-French Bitext](references/The%20BAF_A%20Corpus%20of%20English-French%20Bitext.pdf)
    - [Revisiting sentence alignment algorithms for alignment visualization and evaluation](references/Revisiting%20sentence%20alignment%20algorithms%20for%20alignment%20visualization%20and%20evaluation.pdf)
    - PhD [thesis](references/73143_XU_2016_diffusion.pdf) Page 87 (P102 in pdf) - Page 88 (P103 in pdf), *Evaluation metrics* and *Evaluation corpora*
- Website to check
    - [FarkasTranslations.com](http://www.farkastranslations.com/bilingual_books.php): Multi-parallel, corpora of publicly available books.
    - The [online view](http://www.farkastranslations.com/books/Twain_Mark-Tom_Sawyer-en-de-hu-nl-ca.html) of *The Adventures of Tom Sawyer* can be a baseline view of our tool. 
    (We gonna build something more than that for sure.)
- Our crowd sourcing plan
    - Why we need paragraph alignments of literary texts?
        - Used as a gold alignment for literary texts sentence/paragraph alignment algorithms evaluation. *Manual alignments constitute the most reliable references, but are quite rare.*
        - Simplify the process of literary alignment evaluation corpora generation.
        - Previous *gold references only specify alignment links*, they can not evaluate the similarity between aligned paragraphs,
        which is important for literary translation studies.
    - How?
        - Check our two-step crowd sourcing [design draft](references/two-step-crowd-sourcing-scenario-draft.pdf).
            - 0/1/2 score standards in the second step: 2 means aligned (insofar as possible — sometimes it’s truncated, but it’s not like the missing data is in a different paragraph), 
            1 means sorta aligned (includes situations where a paragraph in English is split across multiple paragraphs), and 0 means it wasn’t translated. 
            - A manual annotated example [here](references/human-annotated-score-for-exact-matching-paragraph-alignment.pdf).

### Relevant workshops and seminars
- [LaTeCH-CLfL 2019](https://sighum.wordpress.com/events/latech-clfl-2019/) 


## Timetable

### Rosetta4Slavic
- Starting date: 17 April
- Project: Translation dashboard prototype development
    - [Design draft](Rosetta4Slavic/references/Rosetta4Slavic-translation-dashboard-draft-v1.pdf)
    - [Online demo](https://zzcoolj.github.io/garage/Rosetta4Slavic/translation-dashboard/)
    - Check [Rosetta4Slavic folder](Rosetta4Slavic/) for more information about the development
- [BSNLP](http://bsnlp.cs.helsinki.fi) workshop@ACL2019 submission
    - Deadline: ~~April 26, 2019~~ **May 3, 2019**
    - LaTex writing on Overleaf

### Rosetta4Endangered
- Starting date: 22 April
- Digging into alignment algorithms
- Results analysis by domain experts
- Crowd sourcing test by using Translation dashboard

### Rosetta4All
- 6 May - 17 May
- [EMNLP 2019](https://www.emnlp-ijcnlp2019.org) submission (maybe option 1...)
    - Abstracts due (long & short): **May 15, 2019**
    - Submissions due (long & short): May 21, 2019
    - Submissions due (demos): July 1, 2019
- [CoNLL 2019](http://www.conll.org/2019) submission (maybe option 2...)
    - Deadline: **May 31, 2019**
