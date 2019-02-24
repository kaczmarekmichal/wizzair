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
        self.driver.implicitly_wait(15)
        #zabezpieczenie do ladowania sie strony


    def test_wrong_email(self):

        #złe podjeście - trudne w utrzymaniu - numer 28
        # zaloguj_btns =self.driver.find_elements_by_tag_name('button')
        # zaloguj_btns[28].click()
        # zaloguj_btns =self.driver.find_elements_by_class_name('navigation__button')
        # zaloguj_btns.click()


        login_btn =self.driver.find_element_by_xpath("//button[@data-test='navigation-menu-signin']")
        #własny selctor na podstawie inspekcji strony w chromie - data-test poniewaz było jedne unikalne wystapienie
        login_btn.click()


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


        if test_data.sex =='male':
            gender_switch = self.driver.find_element_by_xpath("//label[@for='register-gender-male']")
            self.driver.execute_script("arguments[0].click()",gender_switch)
        #wywołanie JS - nie można kliknac normalnie - element przykryty
        else:
            gender_switch = self.driver.find_element_by_xpath("//label[@for='register-gender-female']")
            self.driver.execute_script("arguments[0].click()",gender_switch)


        mobile_phone_field = self.driver.find_element_by_xpath("//input[@name='mobilePhone']")
        mobile_phone_field.send_keys(test_data.mobile_phone)

        email_field = self.driver.find_element_by_xpath("//input[@data-test='booking-register-email']")
        email_field.send_keys(test_data.email)

        password_field = self.driver.find_element_by_xpath("//input[@data-test='booking-register-password']")
        password_field.send_keys(test_data.password)

        # //input[@data-test='booking-register-country']

        country_register_field = self.driver.find_element_by_xpath("//input[@data-test='booking-register-country']")
        # country_register_field.send_keys(test_data.country)
        # - wysylanie reczne ponizej wybor z listy

        country_register_field.click()
        country_field = self.driver.find_element_by_xpath("//div[@class='register-form__country-container__locations']/label[164]")
        country_field.location_once_scrolled_into_view
        #scrollowanie do elementu niewidocznego
        country_field.click()

        # //div[@class='register-form__country-container__locations']/label[164]  - numer Polski w liście wyboru


        # privacy_policy_checkbox = self.driver.find_element_by_xpath("//input[@name='privacyPolicy']") - wrong aproach - could not click
        privacy_policy_checkbox = self.driver.find_element_by_xpath("//label[@for='registration-privacy-policy-checkbox']")
        privacy_policy_checkbox.click()

        # //button[@data-test='booking-register-submit']

        register_btn = self.driver.find_element_by_xpath("//button[@data-test='booking-register-submit']")
        register_btn.click()

        # //span[@class='rf-input__error__message']//span[text()='Nieprawidłowy adres e-mail']

        error_notice = self.driver.find_element_by_xpath("//span[@class='rf-input__error__message']/span[text()='Nieprawidłowy adres e-mail']")

        error_notice.is_enabled()



        time.sleep(5)

if __name__ =='__main__':
    unittest.main()
