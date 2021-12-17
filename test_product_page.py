from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

from .supportSteps.generators import generateRandomStringNumbersLetters

import pytest

# Класс тестирования видимости и невидимости данных атворизованным пользователем с главной страницы
# Маркируем класс user_opportunity
@pytest.mark.user_opportunity
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
# Установочный тест: регистрирует пользователя
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.register_new_user(generateRandomStringNumbersLetters(9) + "@mail.ru", generateRandomStringNumbersLetters(9))
        login_page.click_on_registration_button()

# Тест: Авторизованный пользователь не видит сообщение об успешно добавленных товарах на странице продукта
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_success_message()

# Тест: Авторизованный пользователь может добавить товар в корзину
    # Маркируем need_review
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_basket_link()
        product_page.add_to_basket()

# Параметризация: передаем ссылки для проверки в тесте
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                               marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
                                  ]
                         )
# Тест: Гость может добавить товар в корзину
# link - ссылка из параметризации
# Маркируем need_review
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_title = product_page.get_product_title()
    product_price = product_page.get_product_price()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_message_with_product(product_title)
    basket_page.should_be_message_with_price(product_price)

# Тест: Гость не видит сообщение о добавленных товарах на странице продукта
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_success_message()

# Тест: Гость не видит сообщение об успешно добавленных товарах на странице продукта
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_success_message()

# Тест: После добавления продукта в корзину и перехода туда, сообщение о добавлении исчезает
# Помечаем тест, как временно падающий
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_dissapeare_message()

# Тест: Гость видит ссылку на страницу авторизации/регистрации со страницы продукта
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

# Тест: Гость может перейти на страницу авторизации/регистрации со страницы продукта
# Маркируем need_review
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

# Тест: Гость не видит товаров при переходе в корзину со страницы продукта
# Маркируем need_review
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket_message()
    basket_page.should_not_goods()
