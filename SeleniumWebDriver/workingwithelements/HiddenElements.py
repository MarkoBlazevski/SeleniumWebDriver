from selenium import webdriver
import time

class HiddenElements():

    def testHiddenElements(self):
        baseUrl = "https://www.google.com"
        driver = webdriver.Chrome(r"")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        # Find the state of the text box
        textBoxElement = driver.find_element_by_id_("")
        textBoxState = textBoxElement.is_displayed() # True if is  visible, False if is  Hidden
        # Exception if is not present in the DOM
        print("Text is visible? " + str(textBoxState))
        # Click the Hide button
        driver.find_element_by_id("").click()
        # Find the state of the text box
        textBoxElement = driver.find_element_by_id_("")
        textBoxState = textBoxElement.is_displayed()
        print("Text is visible? " + str(textBoxState))
        # Click the Show button if it is present
        driver.find_element_by_id("").click()
        # Find the state of the text box
        textBoxState = textBoxElement.is_displayed()
        print("Text is visible? " + str(textBoxState))

        # Browser close
        driver.quit()

    def testExpedia(self):
        baseUrl = "https://www.expeia.com"
        driver = webdriver.Chrome(r"")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        driver.find_element_by_id("").click()

        dropdownElement = driver.find_element_by_id("")
        print("Element visible? " + str(dropdownElement.is_displayed()))

chromeHiddenElements = HiddenElements()
chromeHiddenElements.testHiddenElements()
chromeHiddenElements.testExpedia()