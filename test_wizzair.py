# _*_ coding: utf-8 _*_
import unittest
from selenium import webdriver
import time
import test_data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


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


        login_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-test="navigation-menu-signin"]')))
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

        error_notice = self.driver.find_elements_by_xpath("//span[@class='rf-input__error__message']/span[text()='Nieprawidłowy adres e-mail']")
        assert error_notice[1].is_displayed()

        self.assertEqual(error_notice[1].get_attribute('innerText'), u'Nieprawidłowy adres e-mail')

        self.driver.save_screenshot('koniec.png')

        error_notice = self.driver.find_elements_by_xpath("//div[@id='regmodal-scroll-hook-4']/div[2]/span/span")
        assert error_notice[0].is_enabled()

        /div/span[contains(text),'Nieprawidłowy adres e-mail']





    def test_all_fields_empty(self):

        login_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-test="navigation-menu-signin"]')))
        login_btn.click()


        rejestracja_btn =self.driver.find_element_by_xpath("//button[text()='Rejestracja']")
        rejestracja_btn.click()

        register_btn = self.driver.find_element_by_xpath("//button[@data-test='booking-register-submit']")
        register_btn.click()

        # //span[@class='rf-input__error__message']/span/strong[text()='Wpisz imię!']

        #error name field
        error_notice_name= self.driver.find_element_by_xpath("//span[@class='rf-input__error__message']/span/strong[text()='Wpisz imię!']")
        assert error_notice_name.is_displayed()
        self.assertEqual(error_notice_name.get_attribute('innerText'), u'Wpisz imię!')

        #error last name field
        error_notice_last_name= self.driver.find_element_by_xpath("//span[@class='rf-input__error__message']/span/strong[text()='Wpisz nazwisko!']")
        assert error_notice_last_name.is_displayed()
        self.assertEqual(error_notice_last_name.get_attribute('innerText'), u'Wpisz nazwisko!')

        # //span[@class='rf-input__error__message']/span[text()='Wybierz']

        #error gender not selected
        error_notice_gender= self.driver.find_element_by_xpath("//span[@class='rf-input__error__message']/span[text()='Wybierz']")
        assert error_notice_gender.is_displayed()
        self.assertEqual(error_notice_gender.get_attribute('innerText'), u'Wybierz')

        # error phone number
        error_notice_phone_number= self.driver.find_element_by_xpath("//span[@class='rf-input__error__message']/span[text()='Wpisz numer telefonu']")
        assert error_notice_phone_number.is_displayed()
        self.assertEqual(error_notice_phone_number.get_attribute('innerText'), u'Wpisz numer telefonu')

        # error email adress
        error_notice_email_adres= self.driver.find_element_by_xpath("//span[@class='rf-input__error__message']/span[text()='Wpisz adres e-mail']")
        assert error_notice_email_adres.is_displayed()
        self.assertEqual(error_notice_email_adres.get_attribute('innerText'), u'Wpisz adres e-mail')

        #error password   // lista bo źle się wyświetla
        error_notice_password = self.driver.find_elements_by_xpath("//span[@class='rf-input__error__message']/span[text()='Wpisz hasło']")
        assert error_notice_password[1].is_displayed()
        self.assertEqual(error_notice_password[1].get_attribute('innerText'), u'Wpisz hasło')



        # error - privacy policy unchecked
        # //span[@class='rf-input__error__message']/span[text()='Zaakceptuj informację o polityce prywatności']
        error_notice_privacy_policy = self.driver.find_element_by_xpath("//span[@class='rf-input__error__message']/span[text()='Zaakceptuj informację o polityce prywatności']")
        assert error_notice_privacy_policy.is_displayed()
        self.assertEqual(error_notice_privacy_policy.get_attribute('innerText'),u'Zakceptuj informację o polityce prywatności')


    def test_not_acceptance_privacy_policy(self):


        login_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-test="navigation-menu-signin"]')))
        login_btn.click()


        rejestracja_btn =self.driver.find_element_by_xpath("//button[text()='Rejestracja']")
        rejestracja_btn.click()


        name_field = self.driver.find_element_by_xpath("//input[@placeholder='Imię']")
        name_field.send_keys(test_data.valid_name)

        last_name_field = self.driver.find_element_by_xpath("//input[@placeholder='Nazwisko']")
        last_name_field.send_keys(test_data.valid_surname)


        if test_data.sex =='male':
            gender_switch = self.driver.find_element_by_xpath("//label[@for='register-gender-male']")
            self.driver.execute_script("arguments[0].click()",gender_switch)
        else:
            gender_switch = self.driver.find_element_by_xpath("//label[@for='register-gender-female']")
            self.driver.execute_script("arguments[0].click()",gender_switch)


        mobile_phone_field = self.driver.find_element_by_xpath("//input[@name='mobilePhone']")
        mobile_phone_field.send_keys(test_data.mobile_phone)

        email_field = self.driver.find_element_by_xpath("//input[@data-test='booking-register-email']")
        email_field.send_keys(test_data.email)

        password_field = self.driver.find_element_by_xpath("//input[@data-test='booking-register-password']")
        password_field.send_keys(test_data.password)


        country_register_field = self.driver.find_element_by_xpath("//input[@data-test='booking-register-country']")

        country_register_field.click()
        country_field = self.driver.find_element_by_xpath("//div[@class='register-form__country-container__locations']/label[164]")
        country_field.location_once_scrolled_into_view
        country_field.click()


        register_btn = self.driver.find_element_by_xpath("//button[@data-test='booking-register-submit']")
        register_btn.click()

        error_notice_privacy_policy = self.driver.find_element_by_xpath("//span[@class='rf-input__error__message']/span[text()='Zaakceptuj informację o polityce prywatności']")
        assert error_notice_privacy_policy.is_displayed()
        self.assertEqual(error_notice_privacy_policy.get_attribute('innerText'),u'Zakceptuj informację o polityce prywatności')


        self.driver.save_screenshot('koniec.png')


    def test_invalid_phone_number(self):


        login_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-test="navigation-menu-signin"]')))
        login_btn.click()


        rejestracja_btn =self.driver.find_element_by_xpath("//button[text()='Rejestracja']")
        rejestracja_btn.click()


        name_field = self.driver.find_element_by_xpath("//input[@placeholder='Imię']")
        name_field.send_keys(test_data.valid_name)

        last_name_field = self.driver.find_element_by_xpath("//input[@placeholder='Nazwisko']")
        last_name_field.send_keys(test_data.valid_surname)


        if test_data.sex =='male':
            gender_switch = self.driver.find_element_by_xpath("//label[@for='register-gender-male']")
            self.driver.execute_script("arguments[0].click()",gender_switch)
        else:
            gender_switch = self.driver.find_element_by_xpath("//label[@for='register-gender-female']")
            self.driver.execute_script("arguments[0].click()",gender_switch)


        mobile_phone_field = self.driver.find_element_by_xpath("//input[@name='mobilePhone']")
        mobile_phone_field.send_keys(test_data.invalid_mobile_phone)

        email_field = self.driver.find_element_by_xpath("//input[@data-test='booking-register-email']")
        email_field.send_keys(test_data.email)

        password_field = self.driver.find_element_by_xpath("//input[@data-test='booking-register-password']")
        password_field.send_keys(test_data.password)


        country_register_field = self.driver.find_element_by_xpath("//input[@data-test='booking-register-country']")

        country_register_field.click()
        country_field = self.driver.find_element_by_xpath("//div[@class='register-form__country-container__locations']/label[164]")
        country_field.location_once_scrolled_into_view
        country_field.click()


        register_btn = self.driver.find_element_by_xpath("//button[@data-test='booking-register-submit']")
        register_btn.click()

        error_notice_invalid_phone_number = self.driver.find_element_by_xpath("//span[@class='rf-input__error__message']/span[text()='Please enter a valid mobile phone number']")
        assert error_notice_invalid_phone_number.is_displayed()
        self.assertEqual(error_notice_invalid_phone_number.get_attribute('innerText'),u'Podaj poprawny numer telefonu')


        self.driver.save_screenshot('koniec.png')



if __name__ =='__main__':
    unittest.main()
