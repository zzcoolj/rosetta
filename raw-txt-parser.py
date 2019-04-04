"""
Target languages and files:

    1.  Bulgarian   Mark_Tven_-_Prikljuchenijata_na_Hykylberi_Fin_-1345-b.txt
                    Chapter separator:      "\tГлава "
                    Paragraph separator:    each line
                    Special:                each line starts with '\t' except '\n' lines
    2.  Ukranian    ukranian-content.txt (copy from website)
                    Chapter separator:      "Розділ "
                    Paragraph separator:    each line
    3.  Finnish     Finnish-content.txt (copy from HTML no images version)
                    Chapter separator:      ends with "luku."
                    Paragraph separator:    each line
                    Special:                content ends at line 4628 (included)
"""


def get_paragraph_info(file_path, para_separ, para_separ_type, end_valid_line_num, file_total_lines):
    """

    :param file_path:
    :param para_separ:
    :param para_separ_type: 1:startswith 2:endswith
    :param end_valid_line_num:
    :param file_total_lines:
    :return:
    """
    with open(file_path, 'r', encoding='utf-8') as file:
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
    elif para_separ_type == 2:
        for i in range(total_lines):
            if data[i].endswith(para_separ):
                chapter_count += 1
                chapter_content_starting_line.append(i)
    else:
        print('[ERROR] para_separ_type invalid')
    if chapter_count != 43:
        print('[ERROR] #chapters is not 43.')
        print('#chapters: ', chapter_count)
        exit()
    print(chapter_content_starting_line[:5])

    # We say each none-empty line in chapter is a paragraph EXCEPT some special content in the last chapter.
    paragraphs = []
    for i in range(len(chapter_content_starting_line)):
        paragraph_count_per_chapter = 0
        start_line_num = chapter_content_starting_line[i] + 2  # For Bulgarian: +1 is chapter title, +2 should be empty
        if i == chapter_count-1:  # last chapter: special case
            end_line_num = end_valid_line_num
        else:
            end_line_num = chapter_content_starting_line[i+1]
        if start_line_num > end_line_num:
            print('[ERROR] start_line_num > end_line_num')

        for line_num in range(start_line_num, end_line_num):
            if not str.strip(data[line_num]):  # empty line
                continue
            else:
                paragraph_count_per_chapter += 1
        paragraphs.append(paragraph_count_per_chapter)

    print('#chapters: ' + str(chapter_count))
    print('#paragraphs: ' + str(sum(paragraphs)))
    print(paragraphs)
    return paragraphs


get_paragraph_info('corpora/slavic/Bulgarian/Mark_Tven_-_Prikljuchenijata_na_Hykylberi_Fin_-1345-b.txt', '\tГлава ',
                   1, 2537, 2549-1)
get_paragraph_info('corpora/slavic/Ukrainian/ukrainian-content.txt', 'Розділ ', 1, 2423, 2423)
get_paragraph_info('corpora/finno-ugric/Finnish/Finnish-content.txt', 'luku.\n', 2, 4628, 4768)
