from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    AUTHORIZE_LOGIN_LINK = (By.CSS_SELECTOR, "#id_login-username")
    AUTHORIZE_PASSWORD_LINK = (By.CSS_SELECTOR, "#iid_login-password")

    REGISTRATION_LOGIN_LINK = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_LINK = (By.CSS_SELECTOR, "#id_registration-password1")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")


class BasketPageLocators():
    PRODUCT_TITLE = (By.CSS_SELECTOR, "#messages .alertinner> strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages .alertinner> p > strong")

    PRODUCT_MESSAGE = (By.CSS_SELECTOR, "#messages .alertinner")
    PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages .alertinner > p")
