from time import sleep
from session.session_2 import Session2
import logging
logging.basicConfig(level=logging.INFO)


def test_button8(browser):
    logging.info("Тест запущен")
    simple_page = Session2(browser)
    simple_page.open()
    simple_page.contact().click()
    assert 'Ярославская обл.' == simple_page.region()
    logging.info("Тест успешно завершен")


def test_button9(browser):
    logging.info("Тест запущен...")
    simple_page = Session2(browser)
    simple_page.open()
    simple_page.contact().click()
    simple_page.partner_list_yar()
    assert len(simple_page.partner_list_yar()) > 0 and 'Ярославская обл.' == simple_page.region()
    logging.info("Тест успешно завершен")


def test_button10(browser):
    logging.info("Тест запущен...")
    ''' Не совсем понятно, мне нужно сравнить значения: заголовка, url, региона и партнеров с предыдущими значениями
    или просто проверить что подставились верные значения???
    '''
    simple_page = Session2(browser)
    simple_page.open()
    simple_page.contact().click()
    partner_yar = simple_page.partner_list_yar()
    simple_page.region_click()
    sleep(3)
    simple_page.kam_reg().click()
    sleep(3)
    simple_page.partner_list_kam()
    a = browser.title.split('—')
    assert len(simple_page.partner_list_kam()) > 0
    assert 'Камчатский край' == simple_page.region() and len(simple_page.partner_list_kam()) > 0
    assert partner_yar != simple_page.partner_list_kam()
    assert '41-kamchatskij-kraj' == simple_page.get_current_url_part()
    assert a[1].strip() == 'Камчатский край'
    logging.info("Тест успешно завершен")
