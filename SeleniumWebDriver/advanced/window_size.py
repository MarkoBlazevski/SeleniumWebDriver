from selenium import webdriver

class WindowSize():

    def test(self):
        driver = webdriver.Chrome(r"")
        driver.get("https://www.google.com")
        driver.implicitly_wait(5)

        height = driver.execute_script("return window.innerHeight;") # Also can we use command driver.get_window_size()
        width = driver.execute_script("return window.innerWidth;")
        print("Height: " + str(height))
        print("Width: " + str(width))
        driver.quit()


chrome = WindowSize()
chrome.test()
