from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.common.by import By 
import time


def test_checkout(driver, logged_in_user):
    #Inventory page (add item and continue)
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart()
    inventory.go_to_cart()

    #Cart page
    cart = CartPage(driver)
    cart.start_checkout()

    #Checkout page
    checkout = CheckoutPage(driver)
    checkout.fill_checkout_info("Ricky", "Ngyn", "MZN1Z6")
    checkout.continue_checkout()
    assert "checkout-step-two" in driver.current_url
    checkout.finish_checkout()

    #Complete Checkout
    assert "checkout-complete" in driver.current_url

    #Back to Home
    checkout.back_home()
    assert "inventory" in driver.current_url

def test_no_inputs(driver, logged_in_user):
    #Inventory page (add item and continue)
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart()
    inventory.go_to_cart()

    #Cart page
    cart = CartPage(driver)
    cart.start_checkout()

    #Checkout page
    checkout = CheckoutPage(driver)
    checkout.continue_checkout()
    error_msg = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert "Error: First Name is required" in error_msg


