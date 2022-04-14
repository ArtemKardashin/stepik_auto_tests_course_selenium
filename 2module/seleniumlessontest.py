import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x1 = browser.find_element_by_id('input_value')
    x = x1.text
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    checkbox = browser.find_element(By.CLASS_NAME, '.form-check-custom .form-check-label') #скролл вниз
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()
    radiobutton = browser.find_element_by_css_selector('.form-radio-custom .form-check-label')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()
    button = browser.find_element_by_css_selector('.btn.btn-primary')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(5)
    browser.quit()

