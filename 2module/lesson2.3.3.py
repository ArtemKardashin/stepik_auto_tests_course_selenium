import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser.get(link)
    submit1 = browser.find_element(By.CSS_SELECTOR, '[type=submit]').click()
    alert = browser.switch_to.alert
    alert.accept()
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CLASS_NAME, 'form-control')
    input1.send_keys(y)
    submit = browser.find_element(By.CLASS_NAME, 'btn').click()

finally:
    time.sleep(5)
    browser.quit()

# browser.switch_to.window(window_name) - переключение на вторую вкладку
# new_window = browser.window_handles[1] откурыть вторую вкладку
# first_window = browser.window_handles[0] - запомнить имя текущей вкладки