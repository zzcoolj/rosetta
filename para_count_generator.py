import raw_txt_parser, xml_parser

# English (gold standard)
en_path = 'corpora/english-modified.txt'
# Slavic
bulgarian_path = 'corpora/slavic/Bulgarian/Mark_Tven_-_Prikljuchenijata_na_Hykylberi_Fin_-1345-b.txt'
polish_path = 'corpora/slavic/Polish/polish-modified.txt'
russian_path = 'corpora/slavic/Russian/russian-modified.txt'
ukrainian_path = 'corpora/slavic/Ukrainian/ukrainian-content.txt'
# Others
dutch_path = 'corpora/Dutch/Dutch1/dutch1.txt'  # total paragraphs count closer to English version than Dutch2
finnish_path = 'corpora/finno-ugric/Finnish/Finnish-content.txt'
german_path = 'corpora/German/german.txt'
hungarian2_path = 'corpora/finno-ugric/Hungarian/Hungarian2/hung2.txt'
#

chapter_count = 43


def all_count():
    lang_order = ['en', 'ba', 'bu', 'du', 'fi', 'ge', 'hu', 'po', 'ru', 'uk']
    lang_para_count = dict()
    lang_para_count['en'] = xml_parser.get_paragraph_info(en_path)
    lang_para_count['bu'] = raw_txt_parser.get_paragraph_info(bulgarian_path, '\tГлава ', 1, 2537, 2549 - 1)
    lang_para_count['du'] = xml_parser.get_paragraph_info(dutch_path)
    lang_para_count['po'] = xml_parser.get_paragraph_info(polish_path)
    lang_para_count['ru'] = xml_parser.get_paragraph_info(russian_path)
    lang_para_count['uk'] = raw_txt_parser.get_paragraph_info(ukrainian_path, 'Розділ ', 1, 2423, 2423)
    lang_para_count['fi'] = raw_txt_parser.get_paragraph_info(finnish_path, 'luku.\n', 2, 4628, 4768)
    lang_para_count['ge'] = xml_parser.get_paragraph_info(german_path)
    lang_para_count['hu'] = xml_parser.get_paragraph_info(hungarian2_path)
    # TODO automatic Basque
    lang_para_count['ba'] = [10, 42, 18, 25, 36, 19, 29, 86, 21, 13, 70, 49, 52, 56, 49, 73, 63, 82, 55, 45, 53, 18, 36,
                             49, 47, 100, 47, 98, 93, 46, 54, 52, 74, 72, 70, 36, 51, 65, 28, 50, 50, 75, 13]

    # heatmap: write all-para-count file
    write_para_count_heatmap([lang_para_count[lang] for lang in lang_order], 'all-para-count.tsv')
    # heatmap: write all combinations of english-target-count files
    for target_count in lang_order[1:]:
        write_para_count_heatmap([lang_para_count['en'], lang_para_count[target_count]],
                                 'en-' + target_count + '-count.tsv')

    # pie-chart: write all combinations of english-target-difference-type-count files
    for target_count in lang_order[1:]:
        write_para_count_pie([lang_para_count['en'], lang_para_count[target_count]],
                             'en-' + target_count + '-difference-type-count.csv')


def write_para_count_heatmap(lists, output_name):
    with open('translation-dashboard/data/para-count-heatmap/' + output_name, 'w+') as f:  # Creat file if not existed
        f.write('day\thour\tvalue\n')
        for i in range(len(lists)):
            for j in range(len(lists[i])):
                # day hour value <=> chapter language count
                f.write('\t'.join([str(j+1), str(i+1), str(lists[i][j]), '\n']))


def write_para_count_pie(gold_target_lists, output_name):
    """

    :param gold_target_lists: [gold-standard-count-list, target-language-count-list]
    :param output_name:
    :return:
    """
    difference_list = []
    for i in range(len(gold_target_lists[1])):
        difference_list.append(abs(gold_target_lists[1][i] - gold_target_lists[0][i]))

    type_count = dict()
    largest_difference = max(difference_list)  # Using largest different value to set type range
    cut1 = round(largest_difference/10)
    cut2 = round(largest_difference/5)
    cut3 = round(largest_difference/2)
    type_count['#diff=0(exact match)'] = len([diff for diff in difference_list if diff == 0])
    type_count['0<#diff<=' + str(cut1)] = len([diff for diff in difference_list if 0 < diff <= cut1])
    type_count[str(cut1)+'<#diff<=' + str(cut2)] = len([diff for diff in difference_list if cut1 < diff <= cut2])
    type_count[str(cut2)+'<#diff<=' + str(cut3)] = len([diff for diff in difference_list if cut2 < diff <= cut3])
    type_count['#diff>' + str(cut3)] = len([diff for diff in difference_list if diff > cut3])

    with open('translation-dashboard/data/para-count-pie-chart/' + output_name, 'w+') as f:
        f.write('typeName,frequency\n')
        for key, value in type_count.items():
            f.write(key + ',' + str(value) + '\n')


all_count()
