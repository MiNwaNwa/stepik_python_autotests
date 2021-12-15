from .base_page import BasePage
from .locators import BasketPageLocators
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_link.click()

    def get_product_title(self):
        get_product_title_text = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE)
        return get_product_title_text.text

    def get_product_price(self):
        get_product_price_text = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return get_product_price_text.text
