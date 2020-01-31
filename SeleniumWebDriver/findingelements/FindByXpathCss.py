from selenium import webdriver

class FindByXpathCss():

    def test(self):
        base_url = "https://www.google.com"
        driver = webdriver.Chrome(r"")
        driver.get(base_url)
        element_by_xpath = driver.find_element_by_xpath("")

        if element_by_xpath is not None:
            print("We found an element by XPATH")

        element_by_css = driver.find_element_by_css_selector("")

        if element_by_css is not None:
            print("We found an elemernt by CSS")

ChromeByXpathCss = FindByXpathCss()
ChromeByXpathCss.test()
