from time import sleep
from session.session_1 import Session1
import logging

logging.basicConfig(level=logging.INFO)


def test_button(browser):
    logging.info("Тест запущен")
    simple_page = Session1(browser)
    simple_page.open()
    sleep(10)
    assert simple_page.contact_is_displayed()
    logging.info("Тест успешно завершен")


def test_button_2(browser):
    logging.info("Тест запущен")
    simple_page = Session1(browser)
    simple_page.open()
    simple_page.contact_click()
    assert simple_page.banner_is_displayed()
    logging.info("Тест успешно завершен")


def test_button_3(browser):
    logging.info("Тест запущен")
    simple_page = Session1(browser)
    simple_page.open()
    simple_page.contact_click()
    sleep(3)
    simple_page.banner_click()
    sleep(3)
    new_window = browser.window_handles[-1]
    browser.switch_to.window(new_window)
    expected_url = 'https://tensor.ru/'
    assert browser.current_url == expected_url
    logging.info("Тест успешно завершен")


def test_button_4(browser):
    logging.info("Тест запущен")
    simple_page = Session1(browser)
    simple_page.open()
    simple_page.contact_click()
    sleep(3)
    simple_page.banner_click()
    sleep(3)
    new_window = browser.window_handles[-1]
    browser.switch_to.window(new_window)
    assert 'Сила в людях' == simple_page.sila().text
    logging.info("Тест успешно завершен")


def test_button_5(browser):
    logging.info("Тест запущен")
    simple_page = Session1(browser)
    simple_page.open()
    simple_page.contact_click()
    sleep(3)
    simple_page.banner_click()
    sleep(3)
    new_window = browser.window_handles[-1]
    browser.switch_to.window(new_window)
    simple_page.scroll_to_podrobnee()
    simple_page.podrobnee_click()
    assert 'https://tensor.ru/about' == browser.current_url
    logging.info("Тест успешно завершен")


def test_button_6(browser):
    logging.info("Тест запущен")
    simple_page = Session1(browser)
    simple_page.open()
    simple_page.contact_click()
    sleep(3)
    simple_page.banner_click()
    sleep(3)
    new_window = browser.window_handles[-1]
    browser.switch_to.window(new_window)
    simple_page.scroll_to_podrobnee()
    simple_page.podrobnee_click()
    images = simple_page.image()
    first_image_width = images[0].get_attribute('width')
    first_image_height = images[0].get_attribute('height')
    # Проверяем размеры всех изображений
    for image in images:
        width = image.get_attribute('width')
        height = image.get_attribute('height')
        assert width == first_image_width
        assert height == first_image_height
    logging.info("Тест успешно завершен")
