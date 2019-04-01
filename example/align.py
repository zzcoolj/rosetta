# https://github.com/NLPpupil/gale_and_church_align

import math
import scipy.stats


match = {(1, 2): 0.023114355231143552,
         (1, 3): 0.0012165450121654502,
         (2, 2): 0.006082725060827251,
         (3, 1): 0.0006082725060827251,
         (1, 1): 0.9422141119221411,
         (2, 1): 0.0267639902676399}
c = 1.467
s2 = 6.315


def prob_delta(delta):
    return scipy.stats.norm(0, 1).cdf(delta)


def length(sentence):
    punt_list = ',.!?:;~，。！？：；～”“《》'
    sentence = sentence
    return sum(1 for char in sentence if char not in punt_list)


def distance(partition1, partition2, match_prob):
    l1 = sum(map(length, partition1))
    l2 = sum(map(length, partition2))
    try:
        delta = (l2 - l1 * c) / math.sqrt(l1 * s2)
    except ZeroDivisionError:
        return float('inf')
    prob_delta_given_match = 2 * (1 - prob_delta(abs(delta)))
    try:
        return - math.log(prob_delta_given_match) - math.log(match_prob)
    except ValueError:
        return float('inf')


def align(para1, para2):
    """
    输入两个句子序列，生成句对
    句对是倒序的，从段落结尾开始向开头对齐
    """
    align_trace = {}
    for i in range(len(para1) + 1):
        for j in range(len(para2) + 1):
            if i == j == 0:
                align_trace[0, 0] = (0, 0, 0)
            else:
                align_trace[i, j] = (float('inf'), 0, 0)
                for (di, dj), match_prob in match.items():
                    if i - di >= 0 and j - dj >= 0:
                        align_trace[i, j] = min(align_trace[i, j], (
                        align_trace[i - di, j - dj][0] + distance(para1[i - di:i], para2[j - dj:j], match_prob), di,
                        dj))

    i, j = len(para1), len(para2)
    while True:
        (c, di, dj) = align_trace[i, j]
        if di == dj == 0:
            break
        yield ''.join(para1[i - di:i]), ''.join(para2[j - dj:j])
        i -= di
        j -= dj




# TODO duplicate with xml-parser
def txt_parser(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield str.strip(line)


en_path = '../example/english.txt'
# Slavic
polish_path = '../example/polish.txt'


def get_sent_in_chapter(path):
    inChapter1 = False
    chapter1_content = []
    for line in txt_parser(path):
        if line.startswith('<chapter id="1"'):
            inChapter1 = True
        elif inChapter1 and line.endswith('</chapter>'):
            break
        elif inChapter1 and line.startswith('<p>'):
            para = ' '
            para = line.replace('<p>', '')
            if line.endswith('</p>'):
                para = para.replace('</p>', '')
                chapter1_content.append(para)
                break
        elif inChapter1 and not line.startswith('<p>'):
            para += ' '
            para += line
            if line.endswith('</p>'):
                para = para.replace('</p>', '')
                chapter1_content.append(para)
                break
    print('#paragraphs: ' + str(len(chapter1_content)))
    return chapter1_content


en_sent = []
en_count = 0
import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp(' '.join(get_sent_in_chapter(en_path)))
for sent in doc.sents:
    en_count += 1
    en_sent.append(sent.text)
    print('*******'+sent.text)

po_sent = []
po_count = 0
from spacy.lang.pl import Polish
nlp = Polish()  # just the language with no model
sentencizer = nlp.create_pipe("sentencizer")
nlp.add_pipe(sentencizer)
doc = nlp(' '.join(get_sent_in_chapter(polish_path)))
for sent in doc.sents:
    po_count += 1
    po_sent.append(sent.text)
    print('-------'+sent.text)

align_en = []
align_po = []
count=0
for a, b in align(en_sent,po_sent):
    count += 1
    print('----->',a, '|||', b,'<------')
    align_en.append(a.split())
    align_po.append(b.split())

print('aligned:', count)
print('en sent count', en_count)
print('po sent count', po_count)



# word alignment using IBM Model 1 in nltk
from nltk.translate import IBMModel1
from nltk.translate import AlignedSent
corpus = []
for i in range(len(align_en)):
    corpus.append(AlignedSent(align_en[i], align_po[i]))
em_ibm1 = IBMModel1(corpus, 20)

score=dict()
word = 'she'
for target in em_ibm1.translation_table[word]:
    score[target]=em_ibm1.translation_table[word][target]
    # print(target)
    # print(em_ibm1.translation_table['I'][target])
import operator
sorted_x = sorted(score.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_x[:5])
