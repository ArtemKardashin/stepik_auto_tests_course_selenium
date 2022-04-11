import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser.get(link)
    submit1 = browser.find_element(By.CLASS_NAME, 'trollface.btn').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window((new_window))
    x1 = browser.find_element(By.ID, 'input_value')
    x = x1.text
    y = calc(x)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    submit = browser.find_element(By.CLASS_NAME, 'btn').click()
finally:
    time.sleep(5)
    browser.quit()