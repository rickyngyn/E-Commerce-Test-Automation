from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self,driver): 
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")
        self.back_home_button = (By.ID, "back-to-products")
    
    def fill_checkout_info(self, first, last, postal):
        self.driver.find_element(*self.first_name).send_keys(first)
        self.driver.find_element(*self.last_name).send_keys(last)
        self.driver.find_element(*self.postal_code).send_keys(postal)

    def continue_checkout(self):
        self.driver.find_element(*self.continue_button).click()

    def finish_checkout(self):
        self.driver.find_element(*self.finish_button).click()
    
    def back_home(self):
        self.driver.find_element(*self.back_home_button).click()
