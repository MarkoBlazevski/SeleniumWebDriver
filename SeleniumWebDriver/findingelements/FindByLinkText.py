from selenium import webdriver

class FindByLinkText():

    def test(self):
        base_url = "https://www.google.com"
        driver = webdriver.Chrome(r"")
        driver.get(base_url)
        element_by_link_text = driver.find_element_by_link_text("")

        if element_by_link_text is not None:
            print("We found an element by Link Text")

        element_by_partial_link_text = driver.find_element_by_partial_link_text("")

        if element_by_partial_link_text is not None:
            print("We found an element by Partial Link Text")


chrome_by_link_text = FindByLinkText()
chrome_by_link_text.test()