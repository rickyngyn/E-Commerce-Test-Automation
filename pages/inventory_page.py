from selenium.webdriver.common.by import By 


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.inventory_container = (By.ID, "inventory_container")
        self.item1 = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.item2 = (By.ID, "add-to-cart-sauce-labs-bike-light")
        self.item3 = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.item4 = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
        self.item5 = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.item6 = (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")
        self.burger_icon = (By.ID, "react-burger-menu-btn")
        self.menu = (By.CLASS_NAME, "bm-item-list")
        self.logout_button = (By.ID, "logout_sidebar_link")
        self.login_container = (By.CLASS_NAME, "login_container")
        
    def is_loaded(self):
        return self.driver.find_element(*self.inventory_container).is_displayed()
    
    def add_item_to_cart(self): 
        self.driver.find_element(*self.item1).click()

    def add_items_to_cart(self): 
        self.driver.find_element(*self.item1).click()
        self.driver.find_element(*self.item2).click()
        self.driver.find_element(*self.item3).click()
        self.driver.find_element(*self.item4).click()
        self.driver.find_element(*self.item5).click()
        self.driver.find_element(*self.item6).click()
    
    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()
    
    def burger_menu(self):
        self.driver.find_element(*self.burger_icon).click()

    def menu_loaded(self):
        return self.driver.find_element(*self.menu).is_displayed()
    
    def logout(self):
        self.driver.find_element(*self.logout_button).click()
    
    def login_loaded(self):
        return self.driver.find_element(*self.login_container).is_displayed()
    


        
