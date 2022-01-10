import time
from selenium import webdriver

browser = webdriver.Chrome('/Users/iriskim/code/chromedriver')


# opening the website
browser.get('http://naver.com')

# clicking the login button
login_button = browser.find_element_by_class_name('link_login')
login_button.click()

# entering username and password
browser.find_element_by_id('id').send_keys('my_id')
browser.find_element_by_id('pw').send_keys('my_password')

# clicking the sign in button
browser.find_element_by_id('log.login').click()

time.sleep(3)

# entering a new username
browser.find_element_by_id('id').clear() # resetting the input box
browser.find_element_by_id('id').send_keys('naver_id')



# print html info
print(browser.page_source)


# closing browser
browser.close() # close a tab
browser.quit() # close the entire window

