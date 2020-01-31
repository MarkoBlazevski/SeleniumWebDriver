from selenium import webdriver
import time

class JavaScriptExecution():

    def test(self):
        driver = webdriver.Chrome(r"")
        driver.maximize_window()
        # driver.get("https://www.google.com")
        driver.execute_script("window.location = 'https://www.google.com'; ") # JavaScriptExecution
        driver.implicitly_wait(5)

        # element = driver.find_element(By.ID, "name")
        element = driver.execute_script("return document.getElementById('name');") # JavaScriptExecution
        element.send_keys("Test")

chrome = JavaScriptExecution()
chrome.test()