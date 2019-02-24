# _*_ coding: utf-8 _*_
import unittest
from selenium import webdriver
import time

class WizzairTest(unittest.TestCase):

    """
    Class for registartion on wizzair.com
    """
    def tearDown(self):
        self.driver.quit()

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://wizzair.com/pl-pl#")


    def test_wrong_email(self):

        #złe podjeście - trudne w utrzymaniu - numer 28
        zaloguj_btns =self.driver.find_elements_by_tag_name('button')
        zaloguj_btns[28].click()

        rejestracja_btn = self.driver.find_element_by_xpath('//*[@id="login-modal"]/form/div/p/button')
        rejestracja_btn.click()

        time.sleep(5)

if __name__ =='__main__':
    unittest.main()
