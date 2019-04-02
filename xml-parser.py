"""
TODO:   1. Finish file document
        2. Algorithm review: #paragraphs isn't needed
"""
en_path = 'corpora/english.txt'
# Slavic
polish_path = 'corpora/slavic/Polish/polish.txt'
russian_path = 'corpora/slavic/Russian/russian.txt'
# Finno-ugric
hungarian1_path = 'corpora/finno-ugric/Hungarian/Hungarian1/hung1.txt'
hungarian2_path = 'corpora/finno-ugric/Hungarian/Hungarian2/hung2.txt'


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
            print('Chapter:' + str(chapter_count) + 'paragraph:' + str(paragraph_of_chapter_count))
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
            print('*wired start in sent*:' + str(line_count) + line[:10])
    print('#chapters:' + str(chapter_count))
    print('#paragraphs:' + str(total_paragraph_count))
    print('#lines:' + str(line_count))
    print(paragraphs)
    return paragraphs


get_paragraph_info(en_path)
get_paragraph_info(polish_path)
get_paragraph_info(hungarian1_path)
get_paragraph_info(hungarian2_path)
