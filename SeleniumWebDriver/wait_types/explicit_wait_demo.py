from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class ExplicitWaitDemo():

    def test(self):
        baseUrl = "https://www.google.com"
        driver = webdriver.Chrome(r"")
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get(baseUrl)
        # Some action
        driver.find_element(By.ID, "").click()
        driver.find_element(By.ID, "").send_keys()
        driver.find_element(By.ID, "").send_keys()
        driver.find_element(By.ID, "").send_keys()
        returnDate = driver.find_element(By.ID, "") # It could be anything date,time,string...
        returnDate.clear()
        returnDate.send_keys("")
        driver.find_element(By.ID, "").click()

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.ID, "")))
        element.click()

        time.sleep(3)
        driver.quit()

chrome = ExplicitWaitDemo()
chrome.test()
