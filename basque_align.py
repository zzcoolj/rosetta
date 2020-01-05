import os
from nltk.translate import gale_church
from nltk.tokenize import sent_tokenize as stokenizer


def get_basque_chapter(folder_path, chap):
    """
    Basque corpus is collected by dynamic_web_crawler.py
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
    For tagged corpus
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


def get_bulgarian_chapter(path, chap_int, para_separ, para_separ_type, end_valid_line_num, file_total_lines):
    """
     :param file_path:
     :param para_separ:
     :param para_separ_type: 1:startswith (1 para/line); 2:endswith (1 para/line); 3:contains (n lines/para)
     :param end_valid_line_num:
     :param file_total_lines:
     :return:
     """
    with open(path, 'r', encoding='utf-8') as file:
        data = file.readlines()
    total_lines = len(data)
    if total_lines != file_total_lines:  # File information matching check
        print('[ERROR] #lines does not match.')
        print(total_lines)
        exit()
    chapter_count = 0
    chapter_content_starting_line = []
    if para_separ_type == 1:
        for i in range(total_lines):
            if data[i].startswith(para_separ):
                chapter_count += 1
                chapter_content_starting_line.append(i)
    else:
        print('[ERROR] para_separ_type invalid')
    if chapter_count != 43:
        print('[ERROR] #chapters is not 43.')
        print('#chapters: ', chapter_count)
        exit()

    paras = []
    if para_separ_type == 1 or para_separ_type == 2:
        # We say each none-empty line in chapter is a paragraph EXCEPT some special content in the last chapter.

        # TODO: Attention +2 works for Bulgarian, Ukrainian and Finnish. But it is depend on txt content structure
        # For Bulgarian: +1 is chapter title, +2 should be empty
        start_line_num = chapter_content_starting_line[chap_int - 1] + 2
        if chap_int == chapter_count:  # last chapter: special case
            end_line_num = end_valid_line_num
        else:
            end_line_num = chapter_content_starting_line[chap_int]
        if start_line_num > end_line_num:
            print('[ERROR] start_line_num > end_line_num')

        for line_num in range(start_line_num, end_line_num):
            if not str.strip(data[line_num]):  # empty line
                continue
            else:
                paras.append(str.strip(data[line_num]))
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


def align_and_show(chap_en, chap_ba, en_output_path, ba_output_path, write=True):
    """

    :param write:
    :param ba_output_path:
    :param en_output_path:
    :param chap: chapter number (int)
    :param chap_en: list of texts in the corresponding English Chapter
    :param chap_ba: ... Basque ...
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


# Structure 2
def align_sents_of_aligned_chapter_pair(chap):
    sents_list_of_aligned_chapters_en, sents_list_of_aligned_chapters_ba = get_sents_from_aligned_chapter(chap)
    en_aligned_sents = []
    ba_aligned_sents = []
    for i in range(len(sents_list_of_aligned_chapters_en)):
        en_aligned_text_list, ba_aligned_text_list = align_and_show(sents_list_of_aligned_chapters_en[i], sents_list_of_aligned_chapters_ba[i], '', '', write=False)
        en_aligned_sents.extend(en_aligned_text_list)
        ba_aligned_sents.extend(ba_aligned_text_list)

    en_output_file = "translation-dashboard/data/en-ba-psent-align/en-chapter-" + str(chap) + ".txt"
    ba_output_file = "translation-dashboard/data/en-ba-psent-align/ba-chapter-" + str(chap) + ".txt"

    with open(en_output_file, 'w', encoding='utf-8') as en_file:
        for i in range(len(en_aligned_sents)):
            en_file.write(en_aligned_sents[i].replace("<para>", " ") + '\n')
    with open(ba_output_file, 'w', encoding='utf-8') as ba_file:
        for i in range(len(ba_aligned_sents)):
            ba_file.write(ba_aligned_sents[i].replace("<para>", " ") + '\n')


# Structure 3
def chap_to_sent_align(chap):
    en_paras = []
    ba_paras = []
    with open('translation-dashboard/data/en-ba-para-align/en-chapter-' + str(chap) + '.txt', "r") as en_txt:
        for line in en_txt: # each line is a paragraph
            en_paras.append(line)
            '''
            if("<para>" in line):
                loc = line.find("<para>")
                en_paras.append(line[:loc])
                en_paras.append(line[loc+6:])
            else:
                en_paras.append(line)
            '''
    with open('translation-dashboard/data/en-ba-para-align/ba-chapter-' + str(chap) + '.txt', "r") as ba_txt:
        for line in ba_txt: # each line is a paragraph
            ba_paras.append(line)
            '''
            if ("<para>" in line):
                loc = line.find("<para>")
                ba_paras.append(line[:loc])
                ba_paras.append(line[loc + 6:])
            else:
                ba_paras.append(line)
            '''

    en_sents_lens = []
    ba_sents_lens = []
    for para in en_paras:
        en_sents = stokenizer(para)
        for i in range(len(en_sents)):
            #get the number of words in the sentence
            en_sents_lens.append(len(en_sents[i].split()))
    for para in ba_paras:
        ba_sents = stokenizer(para)
        for i in range(len(ba_sents)):
            #get the number of words in the sentence
            ba_sents_lens.append(len(ba_sents[i].split()))

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

    sent_align = gale_church.align_blocks(en_sents_lens, ba_sents_lens)
    aligned_indexes = align_index(sent_align)
    #print(aligned_indexes) #[(0, [0]), (1, [1]), (2, [2]), (3, [3]), (4, [4]), (5, [5]), (6, [6]), (7, [7]), (8, [8]), (9, [9]), (10, [10]), (11, [11]), (12, [12]), (13, [13]), (14, [14]), (15, [15]), (16, [16]), (17, [17]), (18, [18]), (19, [19]), (20, [20]), (21, [21]), (22, [22]), (23, [23]), (24, [24]), (25, [25]), (26, [26]), (27, [27]), (28, [28]), (29, [29, 30]), (30, [31]), (31, [32]), (32, [33]), (33, [34]), (34, [35]), (35, [36]), (36, [37]), (37, [38, 39]), (38, [40]), (39, [41]), (40, [42]), (41, [43]), (42, [44]), (43, [45]), (44, [46]), (45, [47]), (46, [48]), (47, [49]), (48, [50]), (49, [51]), (50, [52]), (51, [53, 54]), (52, [55]), (53, [56]), (54, [57]), (55, [58, 59]), (56, [60]), (57, [61]), (58, [62]), (59, [63]), (60, [64]), (61, [65]), (62, [66]), (63, [67]), (64, [68]), (65, [69]), (66, [70]), (67, [71]), (68, [72]), (69, [73]), (70, [74])]

    en_path = 'corpora/english-modified.txt'
    ba_folder_path = 'corpora/basque'
    chap_en = get_english_chapter(en_path, chap)
    chap_ba = get_basque_chapter(ba_folder_path, chap)
    en_output_path = 'translation-dashboard/data/en-ba-sent-align/en-chapter-' + str(chap) + '.txt'
    ba_output_path = 'translation-dashboard/data/en-ba-sent-align/ba-chapter-' + str(chap) + '.txt'

    en_aligned_text_list = []
    ba_aligned_text_list = []

    for para in chap_en:
        en_aligned_text_list.extend(stokenizer(para)) # produces list of all sentences
    for para in chap_ba:
        ba_aligned_text_list.extend(stokenizer(para)) # produces list of all sentences

    #writing
    with open(en_output_path, 'wt', encoding='utf-8') as en_file:
        for en, ba_list in aligned_indexes:
            en_file.write(en_aligned_text_list[en] + '\n')

    with open(ba_output_path, 'wt', encoding= 'utf-8') as ba_file:
        for en, ba_list in aligned_indexes:
            ba_txt_list = []
            if len(ba_list) > 1:
                for i in ba_list:
                    ba_txt_list.append(ba_aligned_text_list[i])
                ba_file.write('<sent>'.join(str(v) for v in ba_txt_list) + '\n')
            else:
                ba_file.write(ba_aligned_text_list[ba_list[0]] + '\n')

    #print(en_aligned_text_list)
    #print(ba_aligned_text_list)


if __name__ == '__main__':
    en_path = 'corpora/english-modified.txt'
    ba_folder_path = 'corpora/basque'
    bu_path = 'corpora/slavic/Bulgarian/Mark_Tven_-_Prikljuchenijata_na_Hykylberi_Fin_-1345-b.txt'

    # Structure 1
    for i in range(1, 44):
        # en_ba_output_path = 'translation-dashboard/data/en-ba-para-align/en-chapter-' + str(i) + '.txt'
        # ba_output_path = 'translation-dashboard/data/en-ba-para-align/ba-chapter-' + str(i) + '.txt'
        # align_and_show(get_english_chapter(en_path, i), get_basque_chapter(ba_folder_path, i), en_ba_output_path,
        #                ba_output_path)

        en_bu_output_path = 'translation-dashboard/data/en-bu-para-align/en-chapter-' + str(i) + '.txt'
        bu_output_path = 'translation-dashboard/data/en-bu-para-align/bu-chapter-' + str(i) + '.txt'
        align_and_show(get_english_chapter(en_path, i), get_bulgarian_chapter(bu_path, i, '\tГлава ', 1, 2537, 2549-1),
                       en_bu_output_path, bu_output_path)


    # # Structure 2
    # for i in range(1, 44):
    #     align_sents_of_aligned_chapter_pair(i)
    #
    #
    #
    #
    #
    #
    #
    #
    #
    # # Structure 3
    # print('\n' + 'Running Structure 3...')
    # for i in range(1, 44):
    #     chap_to_sent_align(i)
