from selenium import webdriver
import os

class RunChromeTestsWindows():

    def test(self):
        driverlocation = r"C:\Users\Tamara\Desktop\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverlocation
        driver = webdriver.Chrome(driverlocation)
        driver.get("https://www.google.com")


chromeTest = RunChromeTestsWindows()
chromeTest.test()
