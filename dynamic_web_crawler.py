"""
For framing + dynamic web.
"""
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://www.armiarma.eus/unibertsala/twain/')
driver.switch_to.frame('bi')
for element in driver.find_elements_by_xpath('//p'):
    print(element.text)
