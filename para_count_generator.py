import raw_txt_parser, xml_parser

# English (gold standard)
en_path = 'corpora/english-modified.txt'
# Slavic
bulgarian_path = 'corpora/slavic/Bulgarian/Mark_Tven_-_Prikljuchenijata_na_Hykylberi_Fin_-1345-b.txt'
polish_path = 'corpora/slavic/Polish/polish-modified.txt'
russian_path = 'corpora/slavic/Russian/russian-modified.txt'
ukrainian_path = 'corpora/slavic/Ukrainian/ukrainian-content.txt'

chapter_count = 43


def all_count():
    lang_para_count = dict()
    lang_para_count['en'] = xml_parser.get_paragraph_info(en_path)
    lang_para_count['bu'] = raw_txt_parser.get_paragraph_info(bulgarian_path, '\tГлава ', 1, 2537, 2549 - 1)
    lang_para_count['po'] = xml_parser.get_paragraph_info(polish_path)
    lang_para_count['ru'] = xml_parser.get_paragraph_info(russian_path)
    lang_para_count['uk'] = raw_txt_parser.get_paragraph_info(ukrainian_path, 'Розділ ', 1, 2423, 2423)

    # write all-para-count file
    write_para_count([lang_para_count['en'], lang_para_count['bu'], lang_para_count['po'],
                      lang_para_count['ru'], lang_para_count['uk'], ], 'all-para-count.tsv')
    # write all combinations of english-target-count files
    for target_count in ['bu', 'po', 'ru', 'uk']:
        write_para_count([lang_para_count['en'], lang_para_count[target_count]], 'en-' + target_count + '-count.tsv')


def write_para_count(lists, output_name):
    with open('Rosetta4Slavic/data/para-count-heatmap/' + output_name, 'w+') as f:  # Creat file if not existed
        f.write('day\thour\tvalue\n')
        for i in range(len(lists)):
            for j in range(chapter_count):
                # day hour value <=> chapter language count
                f.write('\t'.join([str(j+1), str(i+1), str(lists[i][j]), '\n']))


all_count()
