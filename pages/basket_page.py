from .base_page import BasePage
from .locators import BasketPageLocators
from .locators import ProductPageLocators

from selenium.common.exceptions import TimeoutException

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasketPage(BasePage):
    # def __init__(self, browser, url, product_title, product_price):
    #     self.browser = browser
    #     self.url = url
    #     self.product_title = product_title
    #     self.product_price = product_price

    def should_be_basket_page(self):
        self.should_be_message_with_product()
        self.should_be_message_with_price()

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def get_product_message(self):
        return self.browser.find_element(*BasketPageLocators.PRODUCT_MESSAGE).text

    def get_product_title(self):
        return self.browser.find_element(*BasketPageLocators.PRODUCT_TITLE).text

    def get_price_message(self):
        return self.browser.find_element(*BasketPageLocators.PRICE_MESSAGE).text

    def get_price_title(self):
        return self.browser.find_element(*BasketPageLocators.PRODUCT_PRICE).text

    def should_be_message_with_product(self, product_title):
        assert product_title + " has been added to your basket." in self.get_product_message(), "Product message is not presented'"
        assert product_title in self.get_product_title(), "Product title is not presented"

    def should_be_message_with_price(self, product_price):
        assert "Your basket total is now " + product_price in self.get_price_message(), "Price message is not presented'"
        assert product_price in self.get_price_title(),  "Price message is not presented"

    def should_be_empty_basket_message(self):
        assert self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT).text, "Empty message is not presented'"

    def should_not_goods(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Goods are here"