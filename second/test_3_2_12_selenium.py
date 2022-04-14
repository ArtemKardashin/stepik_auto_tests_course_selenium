
from selenium import webdriver
import time
import unittest

class Testreg(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
    #browser.maximize_window()
        browser.get(link)


        input1 = browser.find_element_by_css_selector('[placeholder="Input your first name"]')
        input1.click()
        input1.send_keys('First name')
        input2 = browser.find_element_by_class_name('first_block .form-control.second')
        input2.send_keys('Last name')
        input3 = browser.find_element_by_class_name('first_block .form-control.third')
        input3.send_keys('email@email.ru')

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'верно')
    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
    #browser.maximize_window()
        browser.get(link)

    # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector('[placeholder="Input your first name"]')
        input1.click()
        input1.send_keys('First name')
        input2 = browser.find_element_by_class_name('first_block .form-control.second')
        input2.send_keys('Last name')
        input3 = browser.find_element_by_class_name('first_block .form-control.third')
        input3.send_keys('email@email.ru')

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'ошибка сука')

    def test_reg3(self):
        self.assertEqual(abs(-42), 42, "верно")

    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "ошибка")
if __name__ == "__main__":
        unittest.main()