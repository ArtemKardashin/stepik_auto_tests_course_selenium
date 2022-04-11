import time
import webbrowser
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
try:
    browser=webdriver.Chrome()
    link = 'http://suninjuly.github.io/file_input.html'
    browser.get(link)
    first = browser.find_element(By.CSS_SELECTOR,"[name='firstname']")
    first.send_keys('First name text')
    lastname = browser.find_element(By.CSS_SELECTOR,"[name='lastname']")
    lastname.send_keys('last name familiya')
    email = browser.find_element(By.CSS_SELECTOR,"[name='email']")
    email.send_keys('test@test.ru')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_example.txt"
    file_path = os.path.join(current_dir, file_name)
    download = browser.find_element(By.ID, 'file')
    download.send_keys(file_path)
    submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

finally:
    time.sleep(5)
    browser.quit()


