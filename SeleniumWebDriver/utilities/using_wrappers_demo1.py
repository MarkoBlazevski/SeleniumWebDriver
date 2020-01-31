from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.handy_wrappers import HandyWrappers
import time

class UsingWrappers():

    def test(self):
        baseUrl = "https://www.google.com"
        driver = webdriver.Chrome(r"")
        driver.maximize_window()
        driver.get(baseUrl)
        hw = HandyWrappers(driver)


        textField1 = hw.getElement("") # It expect locator and locatorType
        textField1.send_keys("")
        time.sleep(3)

        textField2 = hw.getElement("//*[@id='name']", locatorType="xpath") # <-- XPATH
        textField2.clear()

chromeUsingWrappers = UsingWrappers()
chromeUsingWrappers.test()
