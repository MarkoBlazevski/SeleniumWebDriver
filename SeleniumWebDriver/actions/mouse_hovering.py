from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class MouseHovering():

    def test1(self):
        baseUrl = "https://www.google.com"
        driver = webdriver.Chrome(r"")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(3)
        element = driver.find_element(By.ID, "") # Find MouseHower
        itemToClickLocator = ""   # XPATH,ID,NAME...
        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            print("Mouse Hoverd on element")
            time.sleep(3)
            topLink = driver.find_element(By.XPATH, itemToClickLocator)
            topLink.click()
            actions.move_to_element(topLink).click().perform()
            print("Item Clicked")
        except:
            print("Mouse Hover failed on element")

chrome = MouseHovering()
chrome.test1()