from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By 
import time

def test_cart(driver, logged_in_user):
    inventory = InventoryPage(driver)
    assert inventory.is_loaded()
    inventory.add_item_to_cart()
    inventory.go_to_cart()
    
    assert "cart" in driver.current_url

def test_backout(driver, logged_in_user):
    inventory = InventoryPage(driver)
    inventory.burger_menu()
    time.sleep(1) #Allow menu and its encapsulated elements to be loaded
    assert inventory.menu_loaded()
    inventory.logout()

    assert inventory.login_loaded()

def test_items(driver, logged_in_user):
    inventory = InventoryPage(driver)
    inventory.add_items_to_cart()
    cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart_count == "6"
    

    