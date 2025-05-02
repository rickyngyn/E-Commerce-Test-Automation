from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
import time


def test_cart_has_item(driver, logged_in_user):
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart()
    inventory.go_to_cart()

    cart = CartPage(driver)
    assert cart.has_items()
    
    cart.start_checkout()   

    assert "checkout-step-one" in driver.current_url

def test_return(driver, logged_in_user):
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart()
    inventory.go_to_cart()

    cart = CartPage(driver)
    cart.continue_shopping()

    assert "inventory" in driver.current_url
