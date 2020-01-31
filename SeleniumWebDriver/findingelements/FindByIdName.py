from selenium import webdriver

class FindByIdName():

    def test(self):
        base_url = "https://www.google.com"
        driver = webdriver.Chrome(r"")
        driver.get(base_url)
        element_by_id = driver.find_element_by_id("")

        if element_by_id is not None:
            print("We found an element by Id")

        element_by_name = driver.find_element_by_name("")

        if element_by_name is not None:
            print("We found element by Name")


ChromeByIdName = FindByIdName()
ChromeByIdName.test()
