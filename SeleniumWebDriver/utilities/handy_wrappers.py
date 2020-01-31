
from selenium.webdriver.common.by import By

class HandyWrappers():

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()

        if locatorType == "id":
            return By.ID

        elif locatorType == "xpath":
            return By.XPATH

        elif locatorType == "name":
            return By.NAME

        elif locatorType == "tagname":
            return By.TAG_NAME

        elif locatorType == "linktext":
            return By.LINK_TEXT

        elif locatorType == "CSS":
            return By.CSS_SELECTOR

        elif locatorType == "classname":
            return By.CLASS_NAME

        else:
            print("Locator type" + locatorType + "is NOT correct/supported.")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("Element is found.")
        except:
            print("Element is Not found.")
        return element

    def isElementPresent(self, locator, byType):
        try:
            element = self.driver.find_element(byType, locator)
            if element is not None:
                print("Element is found.")
                return True
            else:
                return False

        except:
            print("Element is Not found.")
            return False


    def elementPresentCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0 :
                print("Element is found.")
                return True
            else:
                print("Element is Not found.")
                return False

        except:
            print("Element is Not found.")
            return False
