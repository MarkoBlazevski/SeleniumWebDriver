from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class GetAttribute():

    def test(self):
        baseUrl = "https://www.google.com"
        driver = webdriver.Chrome(r"")
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseUrl)

        element = driver.find_element_by_id("")
        result = element.get_attribute("class") # <-- In the place of "class" it can be id,type,name...any attribute

        print("Value of Attribute is: " + result)
        time.sleep(3)
        driver.quit()

chromeGetAttribute = GetAttribute()
chromeGetAttribute.test()