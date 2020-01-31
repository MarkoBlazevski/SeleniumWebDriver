from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WorkingWithElementsList():

    def testListOfElements(self):
        baseUrl = "https://www.google.com"
        driver = webdriver.Chrome(r"")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        elementsList = driver.find_elements(By.XPATH, "")
        size = len(elementsList)
        print("Size of the list: " + str(size))

        for elements in elementsList:
            isSelected = elements.is_selected()

            if not isSelected:
                elements.click()
                time.sleep(3)

chromeWorkingWithElementsList = WorkingWithElementsList()
chromeWorkingWithElementsList.testListOfElements()