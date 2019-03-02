# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ddt import ddt, data, unpack
import csv


import unittest
#import test_data
import time

def get_data(file_name):
    # Stwórz pustą listę
    rows = []
    # Otwórz plik CSV
    data_file = open(file_name, "rb")
    # Stwórz CSV Reader z pliku CSV
    reader = csv.reader(data_file)
    # Pomiń nagłówek
    next(reader, None)
    # Dodaj wiersze do listy
    for row in reader:
        rows.append(row)
        print row
    return rows

@ddt
class WizzairRegistartionTestDDT(unittest.TestCase):
    """
    Class for registration on wizzair.com/pl-pl/
    """
    def setUp(self):
        self.driver= webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(10)
        self.driver.get("https://wizzair.com/pl-pl/main-page#/")


    def tearDown(self):
        self.driver.quit()

    @data(*get_data("valid_names.csv"))
    @unpack
    def test_valid_registration(self, valid_name, valid_surname, valid_telephone, valid_email, valid_password, valid_country, valid_gender):
        driver = self.driver
        zaloguj_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-test="navigation-menu-signin"]')))
        zaloguj_btn.click()
        rejestracja_btn = driver.find_element_by_xpath("//button[text()='Rejestracja']")
        rejestracja_btn.click()
        name_field = driver.find_element_by_xpath('//input[@placeholder="Imię"]')
        name_field.send_keys(valid_name)
        surname_field = driver.find_element_by_xpath('//input[@placeholder="Nazwisko"]')
        surname_field.send_keys(valid_surname)
        if valid_gender == 'male':
            gender_switch = driver.find_element_by_xpath("//label[@for='register-gender-male']")
            driver.execute_script("arguments[0].click()", gender_switch)
        else:
            gender_switch = driver.find_element_by_xpath("//label[@for='register-gender-female']")
            driver.execute_script("arguments[0].click()", gender_switch)
        telephone_field = driver.find_element_by_name("mobilePhone")
        telephone_field.send_keys(valid_telephone)
        email_field =  driver.find_element_by_css_selector("input[placeholder='E-mail'][data-test='booking-register-email']")
        email_field.send_keys(valid_email)
        password_field = driver.find_element_by_xpath("//input[@data-test='booking-register-password']")
        password_field.send_keys(valid_password)
        country_field = driver.find_element_by_xpath("//input[@data-test='booking-register-country']")
        country_field.click()
        country_to_choose = driver.find_element_by_xpath("//div[@class='register-form__country-container__locations']")
        countries = country_to_choose.find_elements_by_xpath("label")
        print(valid_country)
        for label in countries:
            option=label.find_element_by_tag_name('strong')
            # print(d.text)
            if option.get_attribute("innerText") == valid_country:
                option.location_once_scrolled_into_view
                option.click()
                break
        privacy_policy = driver.find_element_by_xpath("//label[@for='registration-privacy-policy-checkbox']")
        privacy_policy.click()
        register_btn = driver.find_element_by_xpath("//button[@data-test='booking-register-submit']")
        assert register_btn.is_enabled()
        error_notices = driver.find_elements_by_xpath('//*[@class="rf-input__error__message"]/span')
        for error in error_notices:
            assert not error.is_displayed()




if __name__== '__main__':
    unittest.main(verbosity=2)
