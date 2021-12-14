from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    AUTHORIZE_LOGIN_LINK = (By.CSS_SELECTOR, "#id_login-username")
    AUTHORIZE_PASSWORD_LINK = (By.CSS_SELECTOR, "#iid_login-password")

    REGISTRATION_LOGIN_LINK = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_LINK = (By.CSS_SELECTOR, "#id_registration-password1")