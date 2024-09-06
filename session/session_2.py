import logging

from session.base_page import BasePage
from selenium.webdriver.common.by import By

# переменная для нажатия кнопки: 'Контакты'
contact = (
    By.XPATH, "//li[contains(@class, 'sbisru-Header__menu-item-2')]/a[contains(@class, 'sbisru-Header__menu-link')]")
# переменная, где хранится наименование региона
region = (By.CLASS_NAME, 'sbis_ru-Region-Chooser__text')
# переменная, где хранится информация о партнерах Ярославля
partners_list_yar = (By.CLASS_NAME, 'sbisru-Contacts-List__item')
# переменная, для нажатия кнопки: 'Камчатский край'
kam_reg = (By.XPATH,
           '//li[contains(@class, "sbis_ru-Region-Panel__item") and contains(., "Камчатский край")]')
# переменная, где хранится информация о Камчатки
partners_list_kam = (By.CLASS_NAME, 'sbisru-Contacts-List__item')
logging.basicConfig(level=logging.INFO)


class Session2(BasePage):
    def __init__(self, browser):
        '''инициализация объекта страницы'''
        super().__init__(browser)

    def open(self):
        '''метод для открытия ссылки'''
        self.browser.get('https://sbis.ru/')

    def contact(self):
        '''метод для нажатия кнопки: Контакты'''
        return self.find(contact)

    def region(self):
        '''метод для получения наименования региона'''
        region_element = self.find(region)
        return region_element.text

    def region_elements(self):
        '''метод для получения элемента региона'''
        return self.find(region)

    def partner_list_yar(self):
        '''Находит и возвращает список элементов партнеров для Ярославской области'''
        return self.find_elements(partners_list_yar)

    def region_click(self):
        '''Нажимает на элемент региона.'''
        self.region_elements().click()

    def kam_reg(self):
        '''метод возвращает кнопку камчатский край'''
        return self.find(kam_reg)

    def partner_list_kam(self):
        '''метод возвращает партнеров для Камчатского края '''
        return self.find_elements(partners_list_kam)

    def get_current_url(self):
        '''метод возвращает текущий url'''
        return self.browser.current_url

    def get_current_url_part(self):
        '''метод очистки текущего url'''
        url_parts = self.get_current_url().split('/')[4].split('?')[0]
        return url_parts
