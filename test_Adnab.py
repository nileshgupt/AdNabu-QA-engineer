"""  This script run with Pytest for generating report

"""


import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

URL = "https://adnabu-store-assignment1.myshopify.com/"
PASSWORD = "AdNabuQA"


@pytest.fixture
def driver():
    ser_obj = Service(r"C:/DRIVERS/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=ser_obj)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_search_and_add_to_cart(driver):
    wait = WebDriverWait(driver, 15)

    driver.get(URL)

    # Password handling
    try:
        password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
        password_input.send_keys(PASSWORD)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    except:
        pass

    # Search
    search_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "summary.header__icon--search")))
    search_icon.click()

    search_input = wait.until(EC.visibility_of_element_located((By.NAME, "q")))
    search_input.send_keys("Snowboard")
    search_input.submit()

    # Select correct product
    products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.full-unstyled-link, .card__heading a")))

    found = False
    for product in products:
        if "snowboard" in product.text.lower():
            product.click()
            found = True
            break

    assert found, "Snowboard product not found"

    # Add to cart
    add_btn = wait.until(EC.element_to_be_clickable((By.NAME, "add")))
    add_btn.click()

    # Verify cart
    cart_items = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "cart-item, .cart-item")))
    assert len(cart_items) > 0