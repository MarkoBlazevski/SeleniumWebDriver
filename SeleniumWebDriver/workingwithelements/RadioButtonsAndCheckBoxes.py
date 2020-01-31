from selenium import webdriver
import time

class RadioButtonsAndCheckBoxes():

    def test(self):
        baseUrl = "https://www.google.com"
        driver = webdriver.Chrome(r"")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        radioBtn = driver.find_element_by_id("")
        radioBtn.click()

        time.sleep(3)

        radioBtn1 = driver.find_element_by_id("")
        radioBtn1.click()

        time.sleep(3)

        checkBox = driver.find_element_by_id("")
        checkBox.click()

        time.sleep(3)

        checkBox1 = driver.find_element_by_id("")
        checkBox1.click()

        print("Radio button is selected? " + str(radioBtn.is_selected())) #True if selected, False is not slected
        print("Radio button 1 is selected? " + str(radioBtn1.is_selected()))  # True if selected, False is not slected
        print("Checkbox is selected? " + str(checkBox.is_selected()))  # True if selected, False is not slected
        print("Checkbox 1 is selected? " + str(checkBox1.is_selected()))  # True if selected, False is not slected

chromeRadioButtonsAndCheckBoxes = RadioButtonsAndCheckBoxes()
chromeRadioButtonsAndCheckBoxes.test()