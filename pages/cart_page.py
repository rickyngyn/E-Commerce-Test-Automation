from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_item = (By.CLASS_NAME, "cart_item")
        self.checkout = (By.ID, "checkout")
        self.continue_shopping_button = (By.ID, "continue-shopping")

    def has_items(self):
        return self.driver.find_element(*self.cart_item).is_displayed()
        
    def start_checkout(self):
        self.driver.find_element(*self.checkout).click()
    
    def continue_shopping(self):
        self.driver.find_element(*self.continue_shopping_button).click()
        
