# E-Commerce Website Test Automation Suite

This project is a comprehensive test automation suite for an e-commerce website, covering both UI testing using Selenium and API testing using Requests.

## Features

- UI Automation with Selenium WebDriver
- Test scenarios for Login, Product Search, Add to Cart, Checkout, Logout
- Organized page-object structure
- HTML Reports for test results
- Configurable test runner using Pytest
- API testing (in progress...)

## Test Scenarios

- **Login Tests**: Valid and invalid credentials
- **Inventory Tests**: Item visibility, adding to cart
- **Cart Tests**: Cart updates and navigation
- **Checkout Tests**: Entering user info, completing orders
- **Logout Tests**: Logging out from the site

## Getting Started
**Clone the repo**
   ```bash
   git clone https://github.com/rickyngyn/E-Commerce-Test-Automation.git
   cd E-Commerce-Test-Automation
   pip install -r requirements.txt
   pytest
