# Web development notes
## General information	
- Do not reinvent the wheel: try to find suitable libraries/examples.   
- Corpora is in the rosetta/corpora/slavic/ folder.  
- Translation dashboard design draft, paragraphs count of each chapter in different languages and human-annotated exact match paragraph alignment score are in rosetta/Rosetta4Slavic/info/ folder.  
- Pre-processed web development data is (or should be) in the rosetta/Rosetta4Slavic/data/ folder.  
## Main page / Target language general information page
- Day / Hour Heat map from d3.js  
- Data path: data/all-para-count.tsv  
## Chapter level paragraph alignment page / Aligned paragraph page
- Example data path: data/en-chapter-9.txt and po-chapter-9.txt (exact match case)
## Fetures
### Paragraph count correction (for quotes, poems, etc.)
- Only for txt format. For xml format, we assume that p tag annotation has already consider this problem and put sentences of quotes/poems into one paragraph.
- The trigger is based the difference of the number of # paragraphs rather than percentage of difference compared with the original version.
Because the # paragraph in one chapter won't influence the number of lines taken by poems/quotes.
