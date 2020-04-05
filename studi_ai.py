from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time


driver = webdriver.Chrome('/Users/antonbelov/Desktop/Белов Антон/lesson_7/venv/chromedriver')

driver.get("https://mail.ru/")
assert "Mail.ru: почта, поиск в интернете, новости, игры" in driver.title



elem = driver.find_element_by_id('mailbox:login')
elem.send_keys('study.ai_172@mail.ru')

elem = driver.find_element_by_id('mailbox:submit')
elem.click()
time.sleep(1)

elem = driver.find_element_by_id('mailbox:password')
elem.send_keys('NewPassword172')

elem.send_keys(Keys.RETURN)
time.sleep(10)

letters = driver.find_elements_by_xpath("//a[@class='llc js-tooltip-direction_letter-bottom js-letter-list-item llc_normal']")
links = [i.get_attribute('href') for i in letters]


button = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'special-offers__more-btn'))
        )
sender = []
date = []
header = []
text = []

for i in links:
    driver.get(i)
    time.sleep(5)
    sender.append(driver.find_element_by_class_name('letter-contact').get_attribute('title'))
    date.append(driver.find_element_by_xpath("//div[@class='letter__date']").text)
    header.append(driver.find_element_by_xpath("//h2[@class='thread__subject']").text)
    text.append(driver.find_element_by_xpath("//div[@class='thread__letter thread__letter_expanded thread__letter_expanded-next thread__letter_first thread__letter_last thread__letter_single']").text)
    elem = driver.find_element_by_xpath("//a[@class='nav__item js-shortcut nav__item_active nav__item_shortcut nav__item_expanded_true nav__item_child-level_0']")
    elem.click()
    time.sleep(5)

time.sleep(5)
driver.quit()

# МВИДЕО
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# from pymongo import MongoClient
# from pprint import pprint

# driver = webdriver.Chrome('/Users/antonbelov/Desktop/Белов Антон/lesson_7/venv/chromedriver)
# driver.get('https://www.mvideo.ru/')
# assert "М.Видео" in driver.title
# name = []
# price = []
# pages = 0

# elem = driver.find_element_by_tag_name('body').send_keys(Keys.DOWN * 30)

# while True:
#     try:
#         # button = WebDriverWait(driver, 10).until(
#         #     EC.presence_of_element_located(By.xpath('//div[@data-init="ajax-category-carousel"]//a[@class="next-btn sel-hits-button-next"]'))
#         # )
#         # button.click()
#         time.sleep(3)
#         elem = driver.find_element_by_xpath(
#             '//div[@data-init="ajax-category-carousel"]//a[@class="next-btn sel-hits-button-next"]')
#         elem.click()
#         elem = driver.find_element_by_xpath(
#             '//div[@class="gallery-content accessories-new "]').find_elements_by_xpath(
#             './/li[@class="gallery-list-item"]')
#         name += [i.find_element_by_xpath('.//a[@class="sel-product-tile-title"]').text for i in elem][:4]
#         price += [i.find_element_by_xpath('.//div[@class="c-pdp-price__current"]').text for i in elem][:4]
#         pages += 1
#         print(f'раскрыт {pages} блок')
#     except Exception as e:
#         break
#         print('Парсинг окончен или ошибка: ', e)

# print('Всего раскрыто ' + str(pages) + ' блоков')
# driver.quit()


# for i in range(len(price)):
#     if price[i] != '':
#         price[i] = int(price[i][:-1].replace(' ', ''))
#     else:
#         price[i] = None

# client = MongoClient('localhost', 27017)
# db = client['mvideomdb']
# users = db.hits


# def insertmany():
#     users.insert_many(
#         [{'name': i, 'price': j} for i, j in zip(name, price)])


# def printer():
#     for i in users.find():
#         pprint(i)


# insertmany()
# printer()



