
"""
Poem in English
"""


def get_english_chapter(path, chap):
    """

    :param chap: int (In Basque version, Chapter0 is the author information. Real content starts with 1)
    :return: [paragraph (type: String)]
    """
    with open(path, 'r') as f:
        para_count = 0
        paras = []
        for line in f:
            line = line.strip()
            if line.startswith('***'):
                continue
            para_count += 1
            paras.append(line)
    return paras


def get_basque_chapter(path, chap):
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


if __name__ == '__main__':
    en_path = 'corpora/english-modified.txt'
    ba_path = 'corpora/basque'
    p = []
    for i in range(1, 44):
        p.append(len(get_basque_chapter(en_path, i)))
    print(p)