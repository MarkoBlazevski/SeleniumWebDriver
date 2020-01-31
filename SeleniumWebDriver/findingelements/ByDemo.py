from selenium import webdriver
from selenium.webdriver.common.by import By

class ByDemo():

    def test(self):
        baseUrl = "https://www.gogle.com"
        driver = webdriver.Chrome(r"")
        driver.get(baseUrl)

        elementById = driver.find_element(By.ID, "")

        if elementById is not None:
            print("We found an element by Id")

        elementByXpath = driver.find_element(By.XPATH, "")

        if elementByXpath is not None:
            print("We found an element by Xpath")

        elementByLinkText = driver.find_element(By.LINK_TEXT, "")

        if elementByLinkText is not None:
            print("We found an element by Link Text")

        elementByClassName = driver.find_element(By.CLASS_NAME, "")

        if elementByClassName is not None:
            print("We fond an element by Class Name")

        elementByPartialLinkText = driver.find_element(By.PARTIAL_LINK_TEXT, "")

        if elementByPartialLinkText is not None:
            print("We found an element by Partial Link Text")

        elementByTagName = driver.find_element(By.TAG_NAME, "")

        if elementByTagName is not None:
            print("We found an element by Tag Name")

        elementByCss = driver.find_element(By.CSS_SELECTOR, "")

        if elementByCss is not None:
            print("We found an element by CSS")

        elementByName = driver.find_element(By.NAME, "")

        if elementByName is not None:
            print("We found an element by NAME")

chromeByDemo = ByDemo()
chromeByDemo.test()
