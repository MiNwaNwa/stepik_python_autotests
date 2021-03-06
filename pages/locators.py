from selenium.webdriver.common.by import By

# Локаторы базовой страницы
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//a[contains(@href, '/basket/')]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

# Локаторы главной страницы
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

# Локаторы страницы авторизации и регистрации
class LoginPageLocators():
    AUTHORIZE_LOGIN_LINK = (By.CSS_SELECTOR, "#id_login-username")
    AUTHORIZE_PASSWORD_LINK = (By.CSS_SELECTOR, "#iid_login-password")

    REGISTRATION_EMAIL_LINK = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_LINK = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRM_LINK = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")

# Локаторы страницы продукта
class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")

# Локаторы страницы корзины
class BasketPageLocators():
    PRODUCT_TITLE = (By.CSS_SELECTOR, "#messages .alertinner> strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages .alertinner> p > strong")

    PRODUCT_MESSAGE = (By.CSS_SELECTOR, "#messages .alertinner")
    PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages .alertinner > p")

    BUTTON_MOVE_TO_BUY = (By.XPATH, "//a[contains(@href, '/chekout/')]")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")

