from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToWindow():

    def test(self):
        baseUrl = "https://www.google.com"
        driver = webdriver.Chrome(r"")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        # Find parent handle -> Main Window
        parentHandle = driver.current_window_handle
        print("Parent Handle: " + parentHandle)

        # Find open window button and click it
        driver.find_element(By.ID, "").click()
        time.sleep(3)

        # Find all handles, there shoul be two handles after clicking open window button
        handles = driver.window_handles

        # Switch to window and perfome action
        for handle in handles:
            print("Handle: " + handle)
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                print("Swithed to window:: " + handle)
                action = driver.find_element(By.ID, "")
                action.send_keys("")
                time.sleep(5)
                driver.close()
                break

        # Switch back to parent handle
        driver.switch_to.window(parentHandle)
        driver.find_element(By.ID, "").send_keys("")
        time.sleep(3)
