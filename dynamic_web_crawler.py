"""
For framing + dynamic web.
"""
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://www.armiarma.eus/unibertsala/twain/')
driver.switch_to.frame('bat')

chapter_num = 0
paragraphs_count_all = []
for link in driver.find_elements_by_xpath('//li/a'):
    # create one file for each chapter
    with open('corpora/basque/basque-' + str(chapter_num) + '.txt', 'w') as f:
        print('processing chapter ' + str(chapter_num))
        link.click()
        driver.implicitly_wait(1)
        driver.switch_to.default_content()
        driver.switch_to.frame('bi')
        paragraphs_count_chapter = 0
        for element in driver.find_elements_by_xpath('//p'):
            if not element.text or element.text == ' ':
                # jump over empty blocks
                continue
            if element.text.startswith('        '):
                # regular paragraph
                paragraph = element.text.strip()
                paragraphs_count_chapter += 1
            else:
                # title, or author information
                paragraph = '***' + element.text
            f.write(paragraph + '\n')
            # print(element.text)
        driver.switch_to.default_content()
        driver.switch_to.frame('bat')
        paragraphs_count_all.append(paragraphs_count_chapter)
        chapter_num += 1

driver.quit()
print('#chapters:', len(paragraphs_count_all))
print(paragraphs_count_all)
