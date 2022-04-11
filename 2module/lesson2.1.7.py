from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    #browser.maximize_window()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_id('treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    checkbox = browser.find_element_by_css_selector('[type=checkbox]').click()
    radio = browser.find_element_by_id('robotsRule').click()
    button = browser.find_element_by_class_name('btn').click()

finally:
    time.sleep(5)
    browser.quit()