from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time

import pytest

# Класс тестирования перехода гостем на страницу авторизации/регистрации с главной страницы
# Маркируем класс login_guest
@pytest.mark.login_guest
class TestLoginFromMainPage():
# Тест: Гость видит ссылку перехода на страницу авторизации/регистрации
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

# Тест: Гость может перейти на страницу авторизации/регистрации
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

# Тест: Гость не видит товаров при переходе в корзину с главной страницы
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.should_be_basket_link()
    page.go_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket_message()
    basket_page.should_not_goods()