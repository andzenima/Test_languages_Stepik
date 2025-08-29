# lesson_3_6__10

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

# # try with link below to test negative scenario and check assert
# link = "http://selenium1py.pythonanywhere.com/catalogue/"

# variant 1
def test_language(driver):
    driver.get(link)

    try:
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.btn-add-to-basket'))
        )
    except TimeoutException:
        assert False, "TimeoutException: 'Add to cart' button isn't found on the page"
    except NoSuchElementException:
        assert False, "NoSuchElementException: 'Add to cart' button isn't found on the page"

    time.sleep(4)

# # variant 2
# def test_language(driver):
#     driver.get(link)
#     button = driver.find_elements(By.CSS_SELECTOR, '.btn-add-to-basket')
#     assert len(button) == 1, "'Add to cart' button isn't found on the page"
#     time.sleep(4)


# run with command line
# pytest --language=ru --driver_name=chrome test_items.py
#                                   =firefox

    # "ar" > العربيّة            # "ca" > català
    # "cs" > česky              # "da" > dansk
    # "de" > Deutsch            # "el" > Ελληνικά
    # "en-gb" British English   # "fi" > suomi
    # "es" > español            # "fr" > français
    # "it" > italiano           # "ko" > 한국어
    # "nl" > Nederlands         # "pl" > polski
    # "pt" > Português          # "ro" > Română
    # "pt-br" > Português Brasileiro
    # "ru" > Русский            # "sk" > Slovensky
    # "uk" > Українська         # "zh-hans" > 简体中文