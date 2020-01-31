from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Screenshots():

    def test(self):
        baseUrl = "https://www.google.com"
        driver = webdriver.Chrome(r"")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.find_element(By.ID, "user_email").send_keys("abc@email.com")
        driver.find_element(By.ID, "user_password").send_keys("abc")
        driver.find_element(By.NAME, "commit").click()
        destinationFileName = ""  # PATH "C:\\User.....test.png"

        try:
            driver.save_screenshot(destinationFileName) # This command take screenshot
            print("Screenshot saved to directory ---> ::" + destinationFileName)
        except NotADirectoryError:
            print("Not a directory issue")

chrome = Screenshots()
chrome.test()