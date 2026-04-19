"""This  Script run without pytest setup
only Selenium Setup required to execute this

"""




from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException, NoSuchElementException

URL = "https://adnabu-store-assignment1.myshopify.com/"
PASSWORD = "AdNabuQA"
PRODUCT_NAME = "Snowboard"

ser_obj = Service(r"C:/DRIVERS/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)
driver.maximize_window()
wait = WebDriverWait(driver, 15)


def open_website():
    driver.get(URL)
    print("Website opened")


def enter_store_password():
    try:
        password_input = wait.until(
            EC.visibility_of_element_located((By.NAME, "password"))
        )
        password_input.send_keys(PASSWORD)

        submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_btn.click()

        print("Password entered successfully")

    except TimeoutException:
        print("Password page not displayed")


def search_product(product_name):
    try:
        # Try multiple locators for search icon
        try:
            search_icon = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "summary[aria-label='Search']"))
            )
        except:
            search_icon = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "summary.header__icon--search"))
            )

        search_icon.click()

        search_input = wait.until(
            EC.visibility_of_element_located((By.NAME, "q"))
        )
        search_input.clear()
        search_input.send_keys(product_name)
        search_input.submit()

        print(f"Searched for product: {product_name}")

    except Exception as e:
        raise Exception(f"Search failed: {str(e)}")


def select_product(product_name):
    try:
        products = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.full-unstyled-link, .card__heading a"))
        )

        for product in products:
            if product_name.lower() in product.text.lower():
                print(f"Found product: {product.text}")
                product.click()
                return

        raise Exception(f"Product '{product_name}' not found in search results")

    except Exception as e:
        raise Exception(f"Product selection failed: {str(e)}")


def add_to_cart():
    try:
        add_btn = wait.until(
            EC.element_to_be_clickable((By.NAME, "add"))
        )
        add_btn.click()

        # wait for cart confirmation
        wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "cart-notification, .cart-drawer"))
        )

        print("Product added to cart")

    except Exception as e:
        raise Exception(f"Add to cart failed: {str(e)}")


def verify_cart():
    try:
        # open cart
        try:
            cart_icon = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='cart']"))
            )
            cart_icon.click()
        except:
            pass

        cart_items = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "cart-item, .cart-item"))
        )

        assert len(cart_items) > 0
        print("Cart verification successful")

    except Exception as e:
        raise Exception(f"Cart verification failed: {str(e)}")


def test_search_and_add_to_cart():
    try:
        open_website()
        enter_store_password()
        search_product("Snowboard")
        select_product("Snowboard")
        add_to_cart()
        verify_cart()

        print("\n TEST PASSED: Product search & add to cart successful")

    except Exception as e:
        print(f"\nTEST FAILED: {str(e)}")

    finally:
        driver.quit()

test_search_and_add_to_cart()