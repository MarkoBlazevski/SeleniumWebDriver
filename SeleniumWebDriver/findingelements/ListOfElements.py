from selenium import webdriver
from selenium.webdriver.common.by import By

class ListOfElements():

     def test(self):
         baseUrl = "https://www.google.com"
         driver = webdriver.Chrome(r"C:\Users\Tamara\Desktop\chromedriver.exe")
         driver.get(baseUrl)

         elementListByClassName = driver.find_elements_by_class_name("")
         length1 = len(elementListByClassName)

         if elementListByClassName is not None:
             print("ClassName -> Size of the list is:" + str(length1))

         elementListByTagName = driver.find_elements(By.TAG_NAME, "")
         length2 = len(elementListByTagName)

         if elementListByTagName is not None:
             print("TagName -> Size of the list is:" + str(length2))

         elementListById = driver.find_elements_by_id("")
         length3 = len(elementListById)

         if elementListById is not None:
             print("Id -> Size of the list is:" + str(length3))

         elementListByName = driver.find_elements_by_name("")
         length4 = len(elementListByName)

         if elementListByClassName is not None:
             print("Name -> Size of the list is:" + str(length4))

         elementListByXpath = driver.find_elements_by_xpath("")
         length5 = len(elementListByXpath)

         if elementListByXpath is not None:
             print("Xpath -> Size of the list is:" + str(length5))

         elementListByLinkText = driver.find_elements_by_link_text("")
         length6 = len(elementListByLinkText)

         if elementListByLinkText is not None:
             print("LinkText -> Size of the list is:" + str(length6))

         elementListByPartialLinkText = driver.find_elements_by_partial_link_text("")
         length7 = len(elementListByPartialLinkText)

         if elementListByPartialLinkText is not None:
             print("PartialLinkText -> Size of the list is:" + str(length7))

         elementListByCss = driver.find_elements_by_css_selector("")
         length8 = len(elementListByCss)

         if elementListByCss is not None:
             print("Css -> Size of the list is:" + str(length8))






chromeListOfElements = ListOfElements()
chromeListOfElements.test()