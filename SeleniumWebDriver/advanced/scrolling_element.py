from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ScrollingElement():


        # Best way to do this is with javaScript execution
    def test(self):
        baseUrl = "https://www.google.com"
        driver = webdriver.Chrome(r"")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        # Scroll Down

        driver.execute_script("window.scrollBy(0, 800);")      # <----Those are pixels
        time.sleep(5)
        # Scroll Up

        driver.execute_script("window.scrollBy(0, -800);")
        time.sleep(5)
        # Scroll Element Into View

        element = driver.find_element(By.ID, "")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(5)
        driver.execute_script("window.scrollBy(0, -150);")

        # Native Way To Scroll Element Into View
        time.sleep(5)
        driver.execute_script("window.scrollBy(0, -800);")
        location = element.location_once_scrolled_into_view
        print("Location" + str(location))


chrome = ScrollingElement()
chrome.test()