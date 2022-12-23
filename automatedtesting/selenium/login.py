# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By


# Start the browser and login with standard_user
def login (user, password):
    print ('Starting the browser...')
    # --uncomment when running in Azure DevOps.
    options = ChromeOptions()
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--remote-debugging-port=9222')
    driver = webdriver.Chrome(options=options)
    print ('Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    driver.find_element(By.ID, "user-name").send_keys(user)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    print(f"User {user} logged in with password {password}")
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
    print("All items added to cart")
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    print("Cart Opened. Start removing items.")
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    driver.find_element(By.ID, "remove-sauce-labs-bike-light").click()
    driver.find_element(By.ID, "remove-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "remove-sauce-labs-fleece-jacket").click()
    driver.find_element(By.ID, "remove-sauce-labs-onesie").click()
    print("All items removed from cart")

login('standard_user', 'secret_sauce')
print ('Selenium Test Completed Successfully')