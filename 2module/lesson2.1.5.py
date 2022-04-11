from seleniumlessontest import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    #browser.maximize_window()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_id ('input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    checkbox = browser.find_element_by_id('robotCheckbox').click()
    radio = browser.find_element_by_id('robotsRule').click()
    button = browser.find_element_by_class_name('btn').click()

finally:
    time.sleep(5)
    browser.quit()
