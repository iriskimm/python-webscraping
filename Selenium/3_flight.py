from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome("/Users/iriskim/code/chromedriver")

# browser.maximize_window() # maximizing the window

url = "https://flight.naver.com"

browser.get(url)  # opening the url


# 가는 날  선택
browser.find_element_by_xpath('//button[text()="가는 날"]').click()

time.sleep(1)

# selecting this month's day 27, 28
browser.find_elements_by_xpath(
    '//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[5]/button'
)[0].click()
browser.find_elements_by_xpath(
    '//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[6]/button'
)[0].click()


# 도착지 선택
browser.find_element_by_xpath(
    '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]'
).click()

search_box = browser.find_element_by_xpath(
    '//*[@id="__next"]/div/div[1]/div[10]/div[1]/div/input'
)
search_box.send_keys("YYZ")
browser.find_element_by_xpath(
    '//*[@id="__next"]/div/div[1]/div[10]/div[2]/section/div/a/div[1]/i[1]'
).click()
