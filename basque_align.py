import os
from nltk.translate import gale_church
from nltk.tokenize import sent_tokenize as stokenizer


def get_basque_chapter(folder_path, chap):
    """
    :param folder_path:
    :param chap: int (In Basque version, Chapter0 is the author information. Real content starts with 1)
    :return: [paragraph (type: String)]
    """
    file_path = folder_path + '/basque-' + str(chap) + '-modified.txt'
    if not os.path.exists(file_path):
        file_path = folder_path + '/basque-' + str(chap) + '.txt'
    with open(file_path, 'r') as f:
        paras = []
        for line in f:
            line = line.strip()
            if line.startswith('***'):
                continue
            paras.append(line)
    return paras


def get_english_chapter(path, chap):
    """

    :param path:
    :param chap: int
    :return: [paragraph (type: String)]
    """
    with open(path, 'r') as f:
        in_chapter = False
        para_count = 0
        paras = []
        for line in f:
            line = line.strip()
            if line.startswith('<chapter id="' + str(chap)):
                in_chapter = True
                continue
            elif in_chapter and line.startswith('</chapter>'):
                break
            elif in_chapter:
                if line.startswith('<p>') and line.endswith('</p>'):
                    para_count += 1
                    paras.append(line[3:-4])
                    continue
                else:
                    print('[ERROR]', line)
                    exit()
            else:
                continue
    return paras


def get_sents_from_aligned_chapter(chap, folder_path='translation-dashboard/data/en-ba-para-align'):
    """

    :param chap:
    :param folder_path:
    :return: list of list of texts (sents) in one English Chapter & same for Basque
    """
    en_path = folder_path + '/en-chapter-'+str(chap)+'.txt'
    ba_path = folder_path + '/ba-chapter-'+str(chap)+'.txt'
    f_en = open(en_path, 'r', encoding='utf-8')
    f_ba = open(ba_path, 'r', encoding='utf-8')

    sents_list_of_aligned_chapters_en = []
    sents_list_of_aligned_chapters_ba = []

    aligned_paras_en = f_en.readlines()
    aligned_paras_ba = f_ba.readlines()

    sents_list_of_aligned_chapters_en = [stokenizer(para) for para in aligned_paras_en]
    sents_list_of_aligned_chapters_ba = [stokenizer(para) for para in aligned_paras_ba]

    return sents_list_of_aligned_chapters_en, sents_list_of_aligned_chapters_ba


def chapter_paras_length(chap):
    '''

    :param chap: list of texts in the corresponding English Chapter
    :return:
    '''
    # TODO improve tokenizer
    # wtokenizer and get rid of punctuation; don't replace now because the current .split method is needed to compare results from previous tests
    return [len(para.split(' ')) for para in chap]


def aligned_indexes2aligned_texts(aligned_indexes, en_list_of_texts, ba_list_of_texts, en_output_path, ba_output_path, write=True):
    print("Mappings from English sentences")
    ba_en_dict = {}
    for en, ba_list in aligned_indexes:
        ba_string = '-'.join([str(ba) for ba in ba_list])
        if ba_string not in ba_en_dict: ba_en_dict[ba_string] = []
        ba_en_dict[ba_string].append(en)
    # ba_en_dict --> {'0': [0], '1': [1], '2': [2], '3': [3], '4': [4], '5': [5], '6': [6], '7-8': [7], '9': [8]}

    final = []
    for ba_str, en_list in ba_en_dict.items():
        final.append((en_list, [int(p) for p in ba_str.split('-')]))
    print(final)  # TODO Double chekc final
    # [([0], [0]), ([1], [1]), ([2], [2]), ([3], [3]), ([4], [4]), ([5], [5]), ([6], [6]), ([7], [7, 8]), ([8], [9])]

    en_aligned_text_list = []
    ba_aligned_text_list = []
    if write:
        en_output_file = open(en_output_path, 'w')
        ba_output_file = open(ba_output_path, 'w')

    for (k, v) in final:
        print("{} -> {}".format(k, v))
        en_aligned_text = '<para>'.join([en_list_of_texts[kk] for kk in k])
        ba_aligned_text = '<para>'.join([ba_list_of_texts[vv] for vv in v])
        if write:
            en_output_file.write(en_aligned_text + '\n')
            ba_output_file.write(ba_aligned_text + '\n')
        en_aligned_text_list.append(en_aligned_text)
        ba_aligned_text_list.append(ba_aligned_text)

    return en_aligned_text_list, ba_aligned_text_list


def align_sents_of_aligned_chapter_pair(chap):
    sents_list_of_aligned_chapters_en, sents_list_of_aligned_chapters_ba = get_sents_from_aligned_chapter(chap)
    en_aligned_sents = []
    ba_aligned_sents = []
    for i in range(len(sents_list_of_aligned_chapters_en)):
        en_aligned_text_list, ba_aligned_text_list = align_and_show(sents_list_of_aligned_chapters_en[i], sents_list_of_aligned_chapters_ba[i], '', '', write=False)
        en_aligned_sents.extend(en_aligned_text_list)
        ba_aligned_sents.extend(ba_aligned_text_list)

    en_output_file = "translation-dashboard/data/en-ba-sent-align/en-chapter-" + str(chap) + ".txt"
    ba_output_file = "translation-dashboard/data/en-ba-sent-align/ba-chapter-" + str(chap) + ".txt"

    with open(en_output_file, 'w', encoding='utf-8') as en_file:
        for i in range(len(en_aligned_sents)):
            en_file.write(en_aligned_sents[i].replace("<para>", " ") + '\n')
    with open(ba_output_file, 'w', encoding='utf-8') as ba_file:
        for i in range(len(ba_aligned_sents)):
            ba_file.write(ba_aligned_sents[i].replace("<para>", " ") + '\n')


def align_and_show(chap_en, chap_ba, en_output_path, ba_output_path, show_detail=False, write=True):
    """

    :param chap: chapter number (int)
    :param chap_en: list of texts in the corresponding English Chapter
    :param chap_ba: ... Basque ...
    :param show_detail:
    :return:
    """
    def align_index(index_mapping):
        """

        :param index_mapping:   [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (7, 8), (8, 9)]
        :return:                [(0, [0]), (1, [1]), (2, [2]), (3, [3]), (4, [4]), (5, [5]), (6, [6]), (7, [7, 8]), (8, [9])]
        """
        al = {}
        for (e, g) in index_mapping:
            if e not in al: al[e] = []
            al[e].append(g)

        aligned_indexes = [(k, al[k]) for k in sorted(al.keys())]
        return aligned_indexes

    chap_en_leng = chapter_paras_length(chap_en)  # [105, 184, 150, 60, 113, 218, 88, 354, 138], length of each paragraph
    chap_ba_leng = chapter_paras_length(chap_ba)  # [ 101, 154, 121, 45, 94, 192, 80, 159, 130, 116]
    index_mapping = gale_church.align_blocks(chap_en_leng, chap_ba_leng)

    aligned_indexes = align_index(index_mapping)
    en_aligned_text_list, ba_aligned_text_list = aligned_indexes2aligned_texts(aligned_indexes, chap_en, chap_ba, en_output_path, ba_output_path, write=write)
    return en_aligned_text_list, ba_aligned_text_list

# Structure 3
def 
    # en_paras = []
    # ba_paras = []
    # with open('translation-dashboard/data/en-ba-para-align/en-chapter-' + str(chap) + '.txt', "r") as en_txt:
    #     for line in en_txt:
    #         if("<para>" in line):
    #             loc = line.find("<para>")
    #             en_paras.append(line[:loc])
    #             en_paras.append(line[loc+6:])
    #         else:
    #             en_paras.append(line)
    # with open('translation-dashboard/data/en-ba-para-align/ba-chapter-' + str(chap) + '.txt', "r") as ba_txt:
    #     for line in ba_txt:
    #         if ("<para>" in line):
    #             loc = line.find("<para>")
    #             ba_paras.append(line[:loc])
    #             ba_paras.append(line[loc + 6:])
    #         else:
    #             ba_paras.append(line)
    #
    # en_sents_lens = []
    # ba_sents_lens = []
    # for en, ba in a: # for each paragraph
    #     en_sents = stokenizer(en_paras[en])
    #     ba_sents = stokenizer(ba_paras[ba])
    #     for i in range(len(en_sents)):
    #         #get the number of words in the sentence
    #         en_sents_lens.append(len(en_sents[i].split()))
    #     for i in range(len(ba_sents)):
    #         #get the number of words in the sentence
    #         ba_sents_lens.append(len(ba_sents[i].split()))
    # # print(en_sents_lens) # [25, 14, 12, 3, 21, 30, 28, 7, 12, 34, 51, 15, 33, 4, 31, 22, 7, 14, 41, 9, 26, 60, 13, 3, 20, 8, 13, 40, 16, 29, 17, 6, 12, 40, 17, 10, 16, 32, 23, 16, 18, 25, 7, 5, 19, 14, 13, 16, 17, 22, 10, 69, 51, 13, 30, 33, 35, 5, 40, 13, 16, 17, 22, 10, 69, 51, 13, 30, 33, 35, 5, 40, 32, 22, 17, 5, 8, 1, 3, 3, 3, 1, 22, 23]
    # # print(ba_sents_lens) # [18, 12, 11, 5, 23, 32, 19, 8, 8, 30, 41, 15, 28, 5, 24, 17, 8, 11, 29, 10, 22, 45, 12, 4, 18, 4, 9, 34, 13, 13, 9, 15, 5, 14, 48, 15, 6, 11, 14, 8, 18, 16, 15, 23, 6, 5, 19, 12, 16, 17, 13, 18, 11, 13, 34, 37, 16, 17, 13, 18, 11, 13, 34, 37, 22, 21, 15, 4, 5, 1, 3, 5, 2, 9, 10, 19]
    # sent_align = gale_church.align_blocks(en_sents_lens, ba_sents_lens)
    # # print(sent_align)
    # # [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (29, 30), (30, 31), (31, 32), (32, 33), (33, 34), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 41), (43, 42), (44, 42), (45, 43), (46, 43), (47, 44), (48, 45), (49, 46), (50, 47), (51, 48), (52, 49), (53, 50), (54, 51), (55, 52), (56, 53), (57, 54), (58, 54), (59, 55), (60, 55), (61, 56), (62, 57), (63, 57), (64, 58), (65, 59), (66, 60), (67, 61), (68, 62), (69, 62), (70, 63), (71, 63), (72, 64), (73, 65), (74, 66), (75, 67), (76, 68), (77, 69), (78, 70), (79, 71), (80, 72), (81, 73), (82, 74), (83, 75)]
    #
    #
    # #write
    # f_en = open('translation-dashboard/data/en-ba-para-align/en-chapter-' + str(chap) + '.txt', 'w')
    # f_ba = open('translation-dashboard/data/en-ba-para-align/ba-chapter-' + str(chap) + '.txt', 'w')

    # if show_detail:
    #     print("\nText of the aligned sentences:")
    #     for (i, v) in all:
    #         print("{} {}\n---".format(i, chap_en[i]))
    #         for j in v:
    #             print("{} {}".format(j, chap_ba[j]))
    #         print()


if __name__ == '__main__':
    # Structure 1
    en_path = 'corpora/english-modified.txt'
    ba_folder_path = 'corpora/basque'
    for i in range(1, 44):
        print('Chapter:', str(i))
        en_file_path = 'translation-dashboard/data/en-ba-para-align/en-chapter-' + str(i) + '.txt'
        ba_file_path = 'translation-dashboard/data/en-ba-para-align/ba-chapter-' + str(i) + '.txt'
        if i == 44:
            align_and_show(get_english_chapter(en_path, i), get_basque_chapter(ba_folder_path, i), en_file_path, ba_file_path, show_detail=True)
        else:
            align_and_show(get_english_chapter(en_path, i), get_basque_chapter(ba_folder_path, i), en_file_path, ba_file_path)
        # if i == 3: exit()

    # Structure 2
    for i in range(1, 44):
        align_sents_of_aligned_chapter_pair(i)


