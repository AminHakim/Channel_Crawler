import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd

#open target website with webdriver
website = 'https://channelcrawler.com/eng/results2/1102862/page:1'
path = '\Python310\Chromedriver'
driver = webdriver.Chrome(executable_path=r'C:\Python310\Chromedriver\chromedriver.exe')
driver.get(website)

#wait before click sign in
time.sleep(1)

#click sort by
dropdown = Select(driver.find_element(by=By.XPATH, value='//*[@id="sort-select2"]'))
dropdown.select_by_visible_text('Subscribers (descending)')

#sort_by = driver.find_element("xpath", '//*[@id="sort-select2"]').click()

#wait before click sign in
time.sleep(3)

#let say we scrape 1st page here

#main loop
z = 1
while z < 2:
    z += 1

    initial_page = 'https://channelcrawler.com/eng/results2/1102862/page:' + str(z)
    driver.get(initial_page)