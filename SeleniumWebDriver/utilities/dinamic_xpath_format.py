from selenium import webdriver
from selenium.webdriver.common.by import By

class DynamicXpathFormat():

    def test(self):
        baseUrl = "https://www.google.com"
        driver = webdriver.Chrome(r"")
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        # Login
        driver.find_element(By.LINK_TEXT, "").click()
        email = driver.find_element(By.ID, "")  # User email
        email.send_keys("")
        password = driver.find_element(By.ID, "")  # User password
        password.send_keys("")
        driver.find_element(By.NAME, "").click()

        # Search
        searchBox = driver.find_element(By.ID, "")
        searchBox.send_keys("")

        # Select
        _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]" # XPATH we can replace {0} with some text
        _courseLocator = _course.format("JavaScriptfor beginners") # Dinamic XPATH

        courseElement = driver.find_element(By.XPATH, _courseLocator)
        courseElement.click()

chrome = DynamicXpathFormat()
chrome.test()