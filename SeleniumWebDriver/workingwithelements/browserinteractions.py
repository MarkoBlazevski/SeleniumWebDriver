from selenium import webdriver

class BrowserInteraction():

    def test(self):
        baseUrl = ("https://www.google.com")
        driver = webdriver.Chrome(r"")

        # Window Maximize
        driver.maximize_window()
        # Open Url
        driver.get(baseUrl)
        # Get title
        title = driver.title
        print("Title of the web page is: " + title)
        # Get Current Url
        currentUrl = driver.current_url
        print("Current Url of the web page is: " + currentUrl)
        #Browser Refresh
        driver.refresh()
        print("Browser Refreshed 1st time")
        driver.get(currentUrl)
        print("Browser Refreshed 2nd time")
        # Open another Url
        driver.get("")
        currentUrl = driver.current_url
        print("Current Url of the page is: " + currentUrl)
        #Browser Back
        driver.back()
        print("Go one step back in browser history")
        currentUrl = driver.current_url
        print("Current Url of the page is: " + currentUrl)
        # Browser Forward
        driver.forward()
        print("Go one step forward in browser history")
        currentUrl = driver.current_url
        print("Current Url of the page is: " + currentUrl)
        # Get Page Source
        driver.page_source
        pageSource = driver.page_source
        # Browser Close / Quit
        #driver.close()
        driver.quit()


chromeBrowserInteraction = BrowserInteraction()
chromeBrowserInteraction.test()