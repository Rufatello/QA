# from selenium.webdriver.common.by import By
#
# from session.base_page import BasePage
#
# loading_file = (By.LINK_TEXT, 'Скачать локальные версии')
# download_file = (By.LINK_TEXT, 'Скачать (Exe 11.45 МБ)')
#
#
# class Session3(BasePage):
#     def __init__(self, browser):
#         super().__init__(browser)
#
#     def open(self):
#         self.browser.get('https://sbis.ru/')
#
#     def file_click(self):
#         return self.find(loading_file)
#
#     def download(self):
#         download_link = self.find(download_file)
#         download_link.click()
