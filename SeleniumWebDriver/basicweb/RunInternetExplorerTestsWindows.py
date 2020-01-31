from selenium import webdriver
import os
# IMPORTANT: zoom on IE must be 100% or test will fail

class RunInternetExplorerTestsWindows():

    def test(self):
        driverlocation = r"" # path for driver IEDriverServer.exe
        os.environ["webdriver.ie.driver"] = driverlocation
        driver = webdriver.Ie(driverlocation)
        driver.get("https://www.google.com")


InternetExplorerTest = RunInternetExplorerTestsWindows()
InternetExplorerTest.test()
