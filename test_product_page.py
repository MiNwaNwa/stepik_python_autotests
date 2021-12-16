import time
import pytest

from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
# import

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   # pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                   #              marks=pytest.mark.xfail),
#                                   # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
#                                   ]
#                          )

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_title = product_page.get_product_title()
    product_price = product_page.get_product_price()
    print("title = ", product_title)
    print("price = ", product_price)
    product_page.add_to_basket()



    # time.sleep(5)
    product_page.solve_quiz_and_get_code()

    basket_page = BasketPage(browser, browser.current_url)
    print("get_product_message = ", basket_page.get_product_message())
    print("get_price_message", basket_page.get_price_message())
    basket_page.should_be_message_with_product(product_title)
    basket_page.should_be_message_with_price(product_price)
    # basket_page.should_be_message_with_price()
    # time.sleep(15)

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_title = product_page.get_product_title()
    product_price = product_page.get_product_price()
    print("title = ", product_title)
    print("price = ", product_price)
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_title = product_page.get_product_title()
    product_price = product_page.get_product_price()
    print("title = ", product_title)
    print("price = ", product_price)
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_dissapeare_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    time.sleep(5)
    login_page.should_be_login_page()