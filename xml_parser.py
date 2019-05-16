"""
TODO:   1. Finish file document
        2. Algorithm review: #paragraphs isn't needed

Target languages and files:
    1.  Russian

"""
en_path = 'corpora/english-modified.txt'
# Slavic
polish_path = 'corpora/slavic/Polish/polish-modified.txt'
russian_path = 'corpora/slavic/Russian/russian-modified.txt'
# Finno-ugric
hungarian1_path = 'corpora/finno-ugric/Hungarian/Hungarian1/hung1.txt'
hungarian2_path = 'corpora/finno-ugric/Hungarian/Hungarian2/hung2.txt'
# Others
dutch_path = 'corpora/Dutch/Dutch1/dutch1.txt'  # total paragraphs count closer to English version than Dutch2
german_path = 'corpora/German/german.txt'


def txt_parser(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield str.strip(line)


def get_paragraph_info(file_path):
    paragraphs = []

    line_count = 0
    chapter_count = 0
    paragraph_of_chapter_count = 0
    total_paragraph_count = 0
    inParagraph_flag = False
    temp_special_start_line = -1

    for line in txt_parser(file_path):
        line_count += 1
        if line.startswith('<chapter ') and line.endswith('>'):
            paragraph_of_chapter_count = 0
            chapter_count += 1
        elif line == '</chapter>':
            print('[Chapter ' + str(chapter_count) + '] paragraph count: ' + str(paragraph_of_chapter_count))
            paragraphs.append(paragraph_of_chapter_count)

        elif line.startswith('<p>') and line.endswith('</p>'):
            if line_count == temp_special_start_line+1:
                paragraph_of_chapter_count += 1
                total_paragraph_count += 1
                inParagraph_flag = False
            paragraph_of_chapter_count += 1
            total_paragraph_count += 1
        elif line.startswith('<p>') and line.endswith('</p></chapter>'):
            if line_count == temp_special_start_line+1:
                paragraph_of_chapter_count += 1
                total_paragraph_count += 1
                inParagraph_flag = False
            paragraph_of_chapter_count += 1
            total_paragraph_count += 1
            print('Chapter:' + str(chapter_count) + 'paragraph:' + str(paragraph_of_chapter_count))
            paragraphs.append(paragraph_of_chapter_count)

        elif line.startswith('<p>') and not line.endswith('</p>'):
            if line_count == temp_special_start_line+1:
                paragraph_of_chapter_count += 1
                total_paragraph_count += 1
            inParagraph_flag = True
            temp_special_start_line = line_count
            # print('[special start]' + str(line_count) + line)
        elif inParagraph_flag is True and line.endswith('</p>'):
            paragraph_of_chapter_count += 1
            total_paragraph_count += 1
            inParagraph_flag = False
            # print('[special end]' + str(line_count) + line)
        elif inParagraph_flag is True and not line.endswith('</p>'):
            # print('[special content]' + str(line_count) + line)
            pass
        else:
            print('[wired start in line ' + str(line_count) + ']' + line[:10])

    print('#chapters:' + str(chapter_count))
    print('#paragraphs:' + str(total_paragraph_count))
    print('#paragraphs based on list:' + str(sum(paragraphs)))
    print('#lines:' + str(line_count))
    print(paragraphs)
    return paragraphs


# get_paragraph_info(en_path)
# get_paragraph_info(polish_path)
# # Select Hungarian2 for research because it has less difference in paragraph count compared with gold standard.
# # get_paragraph_info(hungarian1_path)
# get_paragraph_info(hungarian2_path)
# get_paragraph_info(russian_path)
# get_paragraph_info(dutch_path)
# get_paragraph_info(german_path)
