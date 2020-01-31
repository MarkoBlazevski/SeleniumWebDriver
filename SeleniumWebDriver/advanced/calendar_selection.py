from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CalendarSelection():

    def test1(self):
        baseUrl = "https://www.google.com"
        driver = webdriver.Chrome(r"")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        # Click flights tab
        driver.find_element_by_id("").click()
        # Find departing field
        departingFieled = driver.find_element_by_id("")
        # Click departing field
        departingFieled.click()
        # Find the date to be selected
        dateToSelect = driver.find_element(By.XPATH, "")
        # Click the date
        dateToSelect.click()


        time.sleep(3)
        driver.quit()

    def test2(self):                         # Finding the valid date
        baseUrl = "https://www.google.com"
        driver = webdriver.Chrome(r"")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        # Click flights tab
        driver.find_element_by_id("").click()
        # Find departing field
        departingFieled = driver.find_element_by_id("")
        # Click departing field
        departingFieled.click()
        calMonth = driver.find_element(By.XPATH, "")
        allValidDates = calMonth.find_elements(By.TAG_NAME, "")

        time.sleep(4)
        for date in allValidDates:
            if date.text == "31":
                date.click()
                break

chrome = CalendarSelection()
chrome.test1()