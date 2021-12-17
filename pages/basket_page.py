from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
# Общая проверка страницы корзины на наличие сообщения о продукте и цене
    def should_be_basket_page(self):
        self.should_be_message_with_product()
        self.should_be_message_with_price()

# Получаем сообщение о добавлении продукта
    def get_product_message(self):
        return self.browser.find_element(*BasketPageLocators.PRODUCT_MESSAGE).text

# Получение названия продукта
    def get_product_title(self):
        return self.browser.find_element(*BasketPageLocators.PRODUCT_TITLE).text

# Получение сообщения о цене товара
    def get_price_message(self):
        return self.browser.find_element(*BasketPageLocators.PRICE_MESSAGE).text

# Получить цену продукта
    def get_price_title(self):
        return self.browser.find_element(*BasketPageLocators.PRODUCT_PRICE).text

# Проверка того, что есть сообщение о продукте в коризне
# product_title - название продукта
    def should_be_message_with_product(self, product_title):
        assert product_title + " has been added to your basket." in self.get_product_message(), "Product message is not presented'"

# Проверка того, что есть сообщение о цене товаров в коризне
    def should_be_message_with_price(self, product_price):
        assert "Your basket total is now " + product_price in self.get_price_message(), "Price message is not presented'"

# Проверка сообщения о том, что корзина пустая
    def should_be_empty_basket_message(self):
        assert self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT).text, "Empty message is not presented'"

# Проверка того, что в корзине нет товаров
    def should_not_goods(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Goods are here"