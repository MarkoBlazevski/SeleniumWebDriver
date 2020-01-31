from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndSendKeys():

    def test(self):
        baseUrl = "https://www.google.com"
        driver = webdriver.Chrome(r"")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        loginLink = driver.find_element(By.XPATH, "")
        loginLink.click()

        emailField = driver.find_element(By.ID, "")
        emailField.send_keys("test")

        passwordField = driver_find_element(By.ID, "")
        passwordField.send_keys("test")

        time.sleep(5)

        emailField.clear()

        time.sleep(5)

        emailField.send_keys("test")

chromeClickAndSendKeys = ClickAndSendKeys()
chromeClickAndSendKeys()
