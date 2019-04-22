import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Investment(unittest.TestCase):

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
           time.sleep(1)

           #Add Investment
           elem = driver.find_element_by_xpath('// *[ @ id = "content-main"] / div[2] / table / tbody / tr[2] / td[1] / a').click()
           time.sleep(1)
           elem = driver.find_element_by_xpath('//*[@id="id_customer"]').click()
           select = Select(driver.find_element_by_xpath('// *[ @ id = "id_customer"]'))
           elem = select.select_by_index("2")
           elem = driver.find_element_by_xpath('//*[@id="id_category"]')
           elem.send_keys("Property")
           elem = driver.find_element_by_xpath('//*[@id="id_description"]')
           elem.send_keys("401K with UNMC")
           elem = driver.find_element_by_xpath('//*[@id="id_acquired_value"]')
           elem.send_keys("18000")
           elem = driver.find_element_by_xpath('//*[@id="id_recent_value"]')
           elem.send_keys("25000")
           time.sleep(1)
           elem = driver.find_element_by_xpath('// *[ @ id = "investment_form"] / div / div / input[1]').click()
           time.sleep(2)

           # Edit Investment
           elem = driver.find_element_by_xpath('//*[@id="result_list"]/tbody/tr[2]/th/a').click()
           time.sleep(1)
           elem = driver.find_element_by_xpath('//*[@id="id_description"]')
           elem.send_keys(Keys.CONTROL + 'a')
           elem.send_keys(Keys.DELETE)
           elem.send_keys("401K with UNL")
           time.sleep(1)
           elem = driver.find_element_by_xpath('//*[@id="id_acquired_value"]')
           elem.send_keys(Keys.CONTROL + 'a')
           elem.send_keys(Keys.DELETE)
           elem.send_keys("30000")
           time.sleep(1)
           elem = driver.find_element_by_xpath('//*[@id="investment_form"]/div/div/input[1]').click()
           time.sleep(1)

           #Delete Investment
           elem = driver.find_element_by_xpath('//*[@id="result_list"]/tbody/tr[2]/th/a').click()
           time.sleep(1)
           elem = driver.find_element_by_xpath('//*[@id="investment_form"]/div/div/p/a').click()
           time.sleep(1)
           elem = driver.find_element_by_xpath('// *[ @ id = "content"] / form / div / input[2]').click()
           time.sleep(2)


   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
       unittest.main()