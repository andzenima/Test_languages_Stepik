import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox

# for correct displaying of Cyrillic in parameterizers
def pytest_make_parametrize_id(config, val): return repr(val)

def pytest_addoption(parser):
    # lang parameter in command line (en by default)
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en/ru/de/fr")

    # driver parameter in command line (chrome (by default) / firefox)
    parser.addoption('--driver_name', action = 'store', default = "chrome", help = "Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def driver(request):

    # get parameter in command line driver_name
    driver_name = request.config.getoption("driver_name")

    driver = None

    user_language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    options_firefox = OptionsFirefox()
    options_firefox.set_preference("intl.accept_languages", user_language)

    if driver_name == "chrome":
        print("\n<<<<<< start chrome driver >>>>>>")
        driver = webdriver.Chrome(options=options)
    elif driver_name == "firefox":
        print("\n<<<<<< start Firefox >>>>>>")
        driver = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("--driver_name should be chrome or firefox")

    print(f"\n<<<<<< start driver for {user_language} language >>>>>>")

    driver.implicitly_wait(5)

    yield driver

    print("\n<<<<<< quit driver >>>>>>")
    driver.quit()