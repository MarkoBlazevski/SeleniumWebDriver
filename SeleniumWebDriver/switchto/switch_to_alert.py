from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToFrame():

    def test1(self):
        baseUrl = "https://www.google.com"
        driver = webdriver.Chrome(r"")
        driver.maximize_window()
        driver.get(baseUrl)

        # JavaScript POP-UP how to solve it
        driver.find_element(By.ID, "").send_keys("")
        driver.find_element(By.ID, "").click()
        time.sleep(3)
        alert1 = driver.switch_to.alert
        alert1.accept()  # Command .accept() Click on OK button on the POP-UP
        time.sleep(3)
        driver.find_element(By.ID, "").click() # Find confirm button
        time.sleep(3)

        alert2 = driver.switch_to.alert
        alert2.dismiss()

chrome = SwitchToFrame()
chrome.test1()