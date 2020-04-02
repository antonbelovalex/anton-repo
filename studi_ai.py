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

# letters = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
#         (By.XPATH,"//a[@class='llc js-tooltip-direction_letter-bottom js-letter-list-item llc_normal']"))
#       )
links = [i.get_attribute('href') for i in letters]
#driver.quit()

print(links)
#
# button = WebDriverWait(driver,10).until(
#             EC.presence_of_element_located((By.CLASS_NAME, 'special-offers__more-btn'))
#         )
# sender = []
# date = []
# header = []
# text = []
#
# for i in links:
#     driver.get(i)
#     time.sleep(5)
#     sender.append(driver.find_element_by_class_name('letter-contact').get_attribute('title'))
# #     date.append(driver.find_element_by_xpath("//div[@class='letter__date']").text)
# #     header.append(driver.find_element_by_xpath("//h2[@class='thread__subject']").text)
# #     text.append(driver.find_element_by_xpath("//div[@class='thread__letter thread__letter_expanded thread__letter_expanded-next thread__letter_first thread__letter_last thread__letter_single']").text)
# #     elem = driver.find_element_by_xpath("//a[@class='nav__item js-shortcut nav__item_active nav__item_shortcut nav__item_expanded_true nav__item_child-level_0']")
# #     elem.click()
# #     time.sleep(5)
#
# time.sleep(5)

# print(sender)

