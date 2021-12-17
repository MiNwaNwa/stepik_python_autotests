from .base_page import BasePage
from .locators import BasketPageLocators
from .locators import ProductPageLocators

# Класс страницы продукта
class ProductPage(BasePage):
# Нажатие кнопки добавления в коризину
    def add_to_basket(self):
        add_to_basket_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_link.click()

# Получение названия продукта
    def get_product_title(self):
        get_product_title_text = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE)
        return get_product_title_text.text

# Получение цены продукта
    def get_product_price(self):
        get_product_price_text = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return get_product_price_text.text
