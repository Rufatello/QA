from time import sleep

from session.base_page import BasePage
from selenium.webdriver.common.by import By
# переменная для нажатия кнопки: 'Контакты'
contact = (
    By.XPATH, "//li[contains(@class, 'sbisru-Header__menu-item-2')]/a[contains(@class, 'sbisru-Header__menu-link')]")
# переменная банера
banner = (By.CLASS_NAME, 'sbisru-Contacts__logo-tensor')
# переменная текста: 'Сила в людях'
sila_text = (By.XPATH,
             '//div[@class="tensor_ru-Index__block4-content tensor_ru-Index__card"]//p[@class="tensor_ru-Index__card-title tensor_ru-pb-16"]')
# переменная для нажатия кнопки: 'Подробнее'
podrobnee = (
By.XPATH, '//div[@class="tensor_ru-Index__block4-content tensor_ru-Index__card"]//a[contains(text(), "Подробнее")]')
# переменная для изображений
image = (By.CLASS_NAME, 'tensor_ru-About__block3-image')


class Session1(BasePage):
    '''инициализация объекта страницы'''
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        '''метод для открытия ссылки'''
        self.browser.get('https://sbis.ru/')

    def contact(self):
        '''метод для элемента: "Контакты"'''
        return self.find(contact)

    def contact_is_displayed(self):
        '''метод для отображения контактов'''
        return self.contact().is_displayed()

    def contact_click(self):
        '''метод для нажатия кнопки котакты'''
        self.contact().click()

    def banner(self):
        '''метод для поиска банера'''
        return self.find(banner)

    def banner_is_displayed(self):
        '''метод для проверки отображения банера'''
        return self.banner().is_displayed()

    def banner_click(self):
        '''метод для нажания по банеру'''
        self.banner().click()

    def sila(self):
        '''метод для поиска текста: "Сила в людях"'''
        return self.find(sila_text)

    def podrobnee(self):
        '''метод для поиска: "Подробнее"'''
        return self.find(podrobnee)

    def podrobnee_click(self):
        '''метод для нажатия кнопки'''
        self.podrobnee().click()

    def scroll_to_podrobnee(self):
        '''метод для прокрутки страницы'''
        more_link = self.podrobnee()
        self.browser.execute_script("arguments[0].scrollIntoView();", more_link)
        sleep(2)

    def image(self):
        '''метод для возврата изображений'''
        return self.find_elements(image)

