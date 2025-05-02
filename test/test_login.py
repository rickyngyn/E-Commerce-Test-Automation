from pages.login_page import LoginPage
from selenium.webdriver.common.by import By


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "wrong_sauce")

    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert "Epic sadface: Username and password do not match any user in this service" in error_message