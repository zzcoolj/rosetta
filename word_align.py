"""
Starting with the aligned paragraphs in each chapter.
"""
import operator
import pickle
import dill
import csv
from nltk import FreqDist
from nltk.translate import AlignedSent
from nltk.translate import IBMModel1, IBMModel2, IBMModel3, IBMModel4, IBMModel5


def sentence_alignment_from_one_paragraph(en_para, po_para):
    en_sent = []
    po_sent = []
    align_en = []
    align_po = []
    en_count = 0
    po_count = 0
    count = 0

    # English sentence segmenter
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(str.strip(en_para))
    for sent in doc.sents:
        en_count += 1
        en_sent.append(sent.text)
        # print('*******'+sent.text)

    # Polish sentence segmenter
    nlp = Polish()  # just the language with no model
    sentencizer = nlp.create_pipe("sentencizer")
    nlp.add_pipe(sentencizer)
    doc = nlp(str.strip(po_para))
    for sent in doc.sents:
        po_count += 1
        po_sent.append(sent.text)
        # print('-------'+sent.text)

    for a, b in align(en_sent, po_sent):
        count += 1
        # print('----->', a, '|||', b, '<------')
        align_en.append(a.split())
        align_po.append(b.split())
    # print('en sent count', en_count)
    # print('po sent count', po_count)
    # print('aligned:', count)

    return align_en, align_po


def para_as_sent(en_path, trans_path):
    with open(en_path, 'r', encoding='utf-8') as file:
        en_paragraphs = file.readlines()
    with open(trans_path, 'r', encoding='utf-8') as file:
        trans_paragraphs = file.readlines()

    if len(en_paragraphs) != len(trans_paragraphs):
        print('[ERROR: Paragraphs are not aligned.]')

    corpus = []
    for i in range(len(en_paragraphs)):
        # TODO tokenizer
        en_sent = en_paragraphs[i].split()
        trans_sent = trans_paragraphs[i].split()

        corpus.append(AlignedSent(en_sent, trans_sent))
    return corpus


def search_word_translation(ibm_model, word, firstN=5):
    score = dict()
    for target in ibm_model.translation_table[word]:
        score[target] = ibm_model.translation_table[word][target]
        # print(target)
        # print(em_ibm1.translation_table['I'][target])
    sorted_x = sorted(score.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_x[:firstN]


def word_count(file_path):
    # Only for English so far.
    with open(file_path, "r", encoding='utf-8') as myfile:
        data = myfile.read().replace('\n', ' ')
    data = data.split(' ')
    fdist1 = FreqDist(data)
    return fdist1


def write_common_words_translations(model, wc, topN, output):
    with open(output, 'wt', encoding='utf-8') as trans_file:
        trans_writer = csv.writer(trans_file, delimiter='\t')
        for (word, count) in wc.most_common(topN):
            # print(search_word_translation(model, word))
            for (trans, score) in search_word_translation(model, word):
                if trans is None:
                    trans = 'None'
                trans_writer.writerow([word, trans, score])


if __name__ == '__main__':
    aligned_paras = []
    wc = FreqDist()
    for i in range(1, 44):
        en_path = 'translation-dashboard/data/en-ba-para-align/en-chapter-' + str(i) + '.txt'
        ba_path = 'translation-dashboard/data/en-ba-para-align/ba-chapter-' + str(i) + '.txt'
        aligned_paras.extend(para_as_sent(en_path, ba_path))
        wc += word_count(en_path)
    model = IBMModel1(aligned_paras, 20)

    # Save model and word count
    with open('align_models/ibm1.model', 'wb') as m_file:
        dill.dump(model, m_file)
    with open('align_models/en.wc', 'wb') as wc_file:
        pickle.dump(wc, wc_file)
    write_common_words_translations(model, wc, 200, 'align_models/word-align.csv')


# test comment (alex)