from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

class Sliders():

    def test(self):
        baseUrl = "https://www.jqueryui.com/slider/"
        driver = webdriver.Chrome(r"C:\Users\Tamara\Desktop\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        driver.switch_to.frame(0)

        element = driver.find_element(By.XPATH, "//div[@id='slider']//span")
        time.sleep(4)
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(element, 100, 0).perform()
            print("Sliding Element Successful")
            time.sleep(3)
        except:
            print("Sliding failed on element")


chrome = Sliders()
chrome.test()