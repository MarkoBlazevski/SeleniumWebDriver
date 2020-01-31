from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

class DropdownSelect():

    def test(self):
        baseUrl = "https://www.google.com"
        driver = webdriver.Chrome(r"")
        driver.maximize_window()
        driver.implicitly_wait(5)

        element = driver.find_element_by_id("")
        sel = Select(element)

        sel.select_by_value("")
        print("Select Dropdown Element by value")

        time.sleep(3)

        sel.select_by_index("")
        print("Select Dropdown Element by index")

        time.sleep(3)

        sel.select_by_visible_text("")
        print("Select Dropdown Element by visible text")

        sel.select_by_index(2) # Any int. number this is another way to select by index
        print("Select Dropdown Element by index")


chromeDropdownSelect = DropdownSelect()
chromeDropdownSelect.test()
