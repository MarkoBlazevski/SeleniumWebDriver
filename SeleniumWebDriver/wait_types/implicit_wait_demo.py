from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ImplicitWaitDemo():

    def test(self):
        baseUrl = "https://www.google.com"
        driver = webdriver.Chrome(r"")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        loginLink = driver.find_element(By.XPATH, "")
        loginLink.click()

        emailField = driver.find_element(By.ID, "")
        emailField.send_keys("")

chrome = ImplicitWaitDemo()
chrome.test()