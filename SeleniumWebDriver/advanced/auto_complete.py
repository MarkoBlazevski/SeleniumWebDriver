from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class AutoComplete():

    def test1(self):
        baseUrl = "https://www.google.com"
        driver = webdriver.Chrome(r"")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        # Send partial data
        

        time.sleep(3)
        # Find the item and click


        time.sleep(3)
        driver.quit()