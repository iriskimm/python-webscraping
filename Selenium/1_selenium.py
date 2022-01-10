from selenium import webdriver

path_to_chromedriver = "/Users/iriskim/code/chromedriver"
browser = webdriver.Chrome(path_to_chromedriver)
browser.get("http://naver.com")

# Login Button

login = browser.find_element_by_class_name("link_login")
login.click()  # clicking on a button

# other useful methods
browser.back()  # moving back to the previous page
browser.forward()  # move forward a page
browser.refresh()


# Search Box

search_box = browser.find_element_by_id("query")

from selenium.webdriver.common.keys import Keys

# entering keys (input)
search_box.send_keys("hello")
# pressing enter
search_box.send_keys(Keys.ENTER)


# getting all elements of a tag

elem = browser.find_elements_by_tag_name("a")

for e in elem:
    e.get_attribute("href")


# click using xpath

search_button = browser.find_element_by_xpath(
    '//*[@id="nx_search_form"]/fieldset/button'
)
search_button.click()


# browser.quit() # closing the window
