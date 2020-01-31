from selenium import webdriver

class FindByClassTag():

    def test(self):
        baseUrl = "https://www.google.com"
        driver = webdriver.Chrome(r"")
        driver.get(baseUrl)
        elementByClassName = driver.find_element_by_class_name("")

        if elementByClassName is not None:
            print("We found an element by Class Name")

        elementByTagName = driver.find_element_by_tag_name("")

        if elementByTagName is not None:
            print("We found an element by Tag Name")


chromeByClassTag = FindByClassTag()
chromeByClassTag.test()