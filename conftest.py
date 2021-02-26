import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language',
                     action='store',
                     default=None,
                     help='Choose language ru, en, (etc.)')


'''
Встроенная фикстура request может получать данные о текущем запущенном тесте
'''


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    print("\nChrome browser start...")
    yield browser
    browser.quit()
    print("\nChrome browser finish...")
