from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class GetText():

    def test(self):
        baseUrl = "https://www.google.com"
        driver = webdriver.Chrome(r"")
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseUrl)

        openTabElement = driver.find_element(By.ID, "")
        elementText = openTabElement.text # Give us text of the element
        print("Text on element is: " + elementText)
        time.sleep(3)
        driver.quit()

chromeGetText = GetText()
chromeGetText.test()