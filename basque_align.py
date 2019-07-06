import os
from nltk.translate import gale_church


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


def chapter_paras_length(chap):
    # TODO improve tokenizer
    return [len(para.split(' ')) for para in chap]


def align_and_show(chap, chap_en, chap_ba, show_detail=False):
    f_en = open('translation-dashboard/data/en-ba-para-align/en-chapter-' + str(chap) + '.txt', 'w')
    f_ba = open('translation-dashboard/data/en-ba-para-align/ba-chapter-' + str(chap) + '.txt', 'w')

    chap_en_leng = chapter_paras_length(chap_en)
    chap_ba_leng = chapter_paras_length(chap_ba)
    a = gale_church.align_blocks(chap_en_leng, chap_ba_leng)
    al = {}
    for (e, g) in a:
        if e not in al: al[e] = []
        al[e].append(g)

    all = [(k, al[k]) for k in sorted(al.keys())]
    print("Mappings from English sentences")

    ba_en_dict = {}
    for en, ba_list in all:
        ba_string = '-'.join([str(ba) for ba in ba_list])
        if ba_string not in ba_en_dict: ba_en_dict[ba_string] = []
        ba_en_dict[ba_string].append(en)

    final = []
    for ba_str, en_list in ba_en_dict.items():
        final.append((en_list, [int(p) for p in ba_str.split('-')]))
    # print(all)
    print(final)  # TODO Double chekc final

    for (k, v) in final:
        print("{} -> {}".format(k, v))
        f_en.write('<para>'.join([chap_en[kk] for kk in k]) + '\n')
        f_ba.write('<para>'.join([chap_ba[vv] for vv in v]) + '\n')

    if show_detail:
        print("\nText of the aligned sentences:")
        for (i, v) in all:
            print("{} {}\n---".format(i, chap_en[i]))
            for j in v:
                print("{} {}".format(j, chap_ba[j]))
            print()


if __name__ == '__main__':
    en_path = 'corpora/english-modified.txt'
    ba_folder_path = 'corpora/basque'
    for i in range(1, 44):
        print('Chapter:', str(i))
        if i == 44:
            align_and_show(i, get_english_chapter(en_path, i), get_basque_chapter(ba_folder_path, i), show_detail=True)
        else:
            align_and_show(i, get_english_chapter(en_path, i), get_basque_chapter(ba_folder_path, i))
        # if i == 3: exit()
