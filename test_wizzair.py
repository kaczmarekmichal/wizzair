# _*_ coding: utf-8 _*_
import unittest
from selenium import webdriver
import time
import test_data


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
        # zaloguj_btns =self.driver.find_elements_by_tag_name('button')
        # zaloguj_btns[28].click()
        # zaloguj_btns =self.driver.find_elements_by_class_name('navigation__button')
        # zaloguj_btns.click()


        zaloguj_btn =self.driver.find_element_by_xpath("//button[@data-test='navigation-menu-signin']")
        #własny selctor na podstawie inspekcji strony w chromie - data-test poniewaz było jedne unikalne wystapienie
        zaloguj_btn.click()


        rejestracja_btn =self.driver.find_element_by_xpath("//button[text()='Rejestracja']")
        #własny selector - wyszukiwanie po znaczacym tekscie
        rejestracja_btn.click()

        # rejestracja_btn = self.driver.find_element_by_xpath('//*[@id="login-modal"]/form/div/p/button')
        # rejestracja_btn.click()

        # input = self.driver.find_element_by_name("firstName")
        name_field = self.driver.find_element_by_xpath("//input[@placeholder='Imię']")
        name_field.send_keys(test_data.valid_name)

        last_name_field = self.driver.find_element_by_xpath("//input[@placeholder='Nazwisko']")
        last_name_field.send_keys(test_data.valid_surname)



        gender_switch = self.driver.find_element_by_xpath("//label[@for='register-gender-male']")
        self.driver.execute_script("arguments[0].click()",gender_switch)
        # input.click()
        #inny sposob - po label

        # input = self.driver.find_element_by_name("lastName")
        # input.send_keys("Dickinson")


        time.sleep(5)

if __name__ =='__main__':
    unittest.main()
