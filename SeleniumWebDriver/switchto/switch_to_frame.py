from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToFrame():

    def test(self):
        baseUrl = "https://www.google.com"
        driver = webdriver.Chrome(r"")
        driver.get(baseUrl)
        driver.execute_script("window.scrollBy(0, 1000);")

        # Switch to frame using Id
        driver.switch_to.frame("") # Name,ID..

        # Switch to frame using name
        #driver.switch_to.frame("")

        # Switch to frame using numbers
        # driver.switch_to.frame(0)
        time.sleep(3)

        # Action
        searchBox = driver.find_element(By.ID, "")
        searchBox.send_keys("")
        time.sleep(3)

        # Switch back to parent frame
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(3)
        driver.find_element(By.ID, "").send_keys("")

chrome = SwitchToFrame()
chrome.test()
