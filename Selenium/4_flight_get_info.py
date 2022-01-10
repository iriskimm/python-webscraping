from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("/Users/iriskim/code/chromedriver")
url = "https://flight.naver.com/flights/international/ICN-YYZ-20220127/YYZ-ICN-20220128?adult=1&fareType=Y"
browser.get(url)  # opening the url


# wait until the desired element appears
try:
    elem = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div[3]/div[1]/div')
        )
    )
    print(elem.text)  # 첫번째 결과 출력

finally:
    browser.quit()
