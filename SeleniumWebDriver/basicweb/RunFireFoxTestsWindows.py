from selenium import webdriver

class RunFireFoxTestsWindows():

    def test_method(self):
        # Initiate the driver instance
        driver = webdriver.Firefox(executable_path=r"")  # r or inside quotes two \\ in the path for Windows
        driver.get("https://www.google.com")

FireFox = RunFireFoxTestsWindows()

FireFox.test_method()
