import time
import math
from seleniumlessontest import webdriver
link = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
browser.get(link)
from seleniumlessontest.webdriver.support.ui import Select
x1 = browser.find_element_by_id ('num1')
x = x1.text
y_element = browser.find_element_by_id('num2')
y = y_element.text
z = int('x') + int('y')

print(z)
select = Select(browser.find_element_by_id('dropdown'))
select.select_by_value('z')