from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

class DragAndDrop():

    def test(self):
        baseUrl = "https://www.jqueryui.com/droppable/"
        driver = webdriver.Chrome(r"C:\Users\Tamara\Desktop\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        driver.switch_to.frame(0)

        fromElement = driver.find_element(By.ID, "draggable")  # Element to drag
        toElement = driver.find_element(By.ID, "droppable")    # Element where to drop
        time.sleep(3)
        try:
            actions = ActionChains(driver)
            # actions.drag_and_drop(fromElement, toElement).perform()
            actions.click_and_hold(fromElement).move_to_element(toElement).release().perform() # This is the second way to do sma thing
            print("Drag And Drop element successful")
            time.sleep(3)
        except:
            print("Drag And Drop failed on element")

chrome = DragAndDrop()
chrome.test()