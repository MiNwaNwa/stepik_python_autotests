import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Описываем свой параметр для командной строки со значением по умолчанию
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose correct language")

# Описываем фикстуру с настройками своего параметра для Chrome
@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    print("\nstart browser for test..")
    yield browser
    print("\nquit browser..")
    browser.quit()