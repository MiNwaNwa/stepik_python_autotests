from .base_page import BasePage
from .locators import BasePageLocators
from .locators import LoginPageLocators

# Класс страницы авторизации/регистрации
class LoginPage(BasePage):
# Вызов функций проверок того, что мы на странице авторизации/регистрации
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

# Проверка наличия слова "login" в url
    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "URL not contains word 'login'"

# Проверка, что есть форма авторизации
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.AUTHORIZE_LOGIN_LINK), "Login form is not presented"

# Проверка, что есть форма регистрации
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL_LINK), "Registration form is not presented"
        # assert True

# Переход на страницу авторизации
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

# Нажатие на кнопку регистрации
    def click_on_registration_button(self):
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        button.click()

# Ввод данных в форму регистрации
# email - почта для регистрации
# password - пароль для регистрации
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_LINK).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_LINK).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM_LINK).send_keys(password)