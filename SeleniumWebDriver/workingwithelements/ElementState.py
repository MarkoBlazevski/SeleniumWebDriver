from selenium import webdriver

class ElementState():

    def isEnabled(self):
        baseUrl = "https://www.google.com"
        driver = webdriver.Chrome(r"")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly.wait(5)

        element1 = driver.find_element_by_id("")
        element1State = element1.is_enabled()  #True for enabled and False for disabled
        print("Element 1 is Enabled? --> " + str(element1State))

        element2 = driver.find_element_by_id("")
        element2State = element1.is_enabled()  # True for enabled and False for disabled
        print("Element 2 is Enabled? --> " + str(element2State))

        element3 = driver.find_element_by_id("")
        element3State = element1.is_enabled()  # True for enabled and False for disabled
        print("Element 3 is Enabled? --> " + str(element3State))

        element3.send_keys("")  # Or wich one is Enabled

chromeElement = ElementState()
chromeElement.isEnabled()