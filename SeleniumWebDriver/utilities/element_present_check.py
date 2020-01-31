from selenium import webdriver
from utilities.handy_wrappers import HandyWrappers


class ElementPresentCheck():

    def test(self):
        baseUrl = "https://www.google.com"
        driver = webdriver.Chrome(r"")
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(baseUrl)

        elementResult1 = hw.isElementPresent(locator="", byType="")
        print(str(elementResult1))

        elementResult2 = hw.elementPresentCheck(locator="", byType="")
        print(str(elementResult2))

chrome = ElementPresentCheck()
chrome.test()