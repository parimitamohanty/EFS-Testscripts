import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Customer(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_efs(self):
           user = "instructor"
           pwd = "instructor1a"
           driver = self.driver
           driver.maximize_window()
           driver.get("https://efs-parimitamohanty.herokuapp.com/admin")#directs to website
           elem = driver.find_element_by_id("id_username")
           elem.send_keys(user)
           elem = driver.find_element_by_id("id_password")
           elem.send_keys(pwd)
           elem.send_keys(Keys.RETURN)
           time.sleep(3)
           elem = driver.find_element_by_xpath('//*[@id="content-main"]/div[2]/table/tbody/tr[1]/td[1]/a').click()
           time.sleep(1)

           #Add new customer

           elem = driver.find_element_by_id("id_name")
           elem.send_keys("Parimita")
           elem = driver.find_element_by_id("id_address")
           elem.send_keys("nebraska")

           elem = driver.find_element_by_id("id_cust_number")
           elem.send_keys("99")

           elem = driver.find_element_by_id("id_city")
           elem.send_keys("Omaha")

           elem = driver.find_element_by_id("id_state")
           elem.send_keys("NE")

           elem = driver.find_element_by_id("id_zipcode")
           elem.send_keys("68106")

           elem = driver.find_element_by_id("id_email")
           elem.send_keys("pmohanty@unomaha.edu")

           elem = driver.find_element_by_id("id_cell_phone")
           elem.send_keys("4025948250")
           elem = driver.find_element_by_xpath('//*[@id="customer_form"]/div/div/input[1]').click()
           time.sleep(1)

           #View and Edit Customer list
           elem = driver.find_element_by_id("user-tools").click()
           time.sleep(1)
           elem = driver.find_element_by_xpath('// *[ @ id = "app-layout"] / div / div / div / div[2] / div / div / div / div / div[1] / div / div / p[2] / a').click()
           time.sleep(1)
           elem = driver.find_element_by_xpath('// *[ @ id = "app-layout"] / div / div / div / div[3] / table / tbody / tr[4] / td[9] / a').click()

           elem = driver.find_element_by_id("id_cell_phone")
           time.sleep(1)
           elem.send_keys(Keys.CONTROL + "a")
           elem.send_keys(Keys.DELETE)
           elem.send_keys("4021111111")
           time.sleep(1)
           elem = driver.find_element_by_xpath('// *[ @ id = "app-layout"] / div / div / div / form / button').click() #Click update
           time.sleep(1)

           #Delete User
           elem = driver.find_element_by_xpath('// *[ @ id = "app-layout"] / div / div / div / div[3] / table / tbody / tr[4] / td[10] / a').click()
           time.sleep(1)
           elem = driver.switch_to.alert.accept() #Accepts to delete the field
           time.sleep(2)

           #View Portfolio
           elem = driver.find_element_by_xpath('// *[ @ id = "app-layout"] / div / div / div / div[3] / table / tbody / tr[1] / td[11] / a').click()
           time.sleep(2)


           # time.sleep(2)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
       unittest.main()