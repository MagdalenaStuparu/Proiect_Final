import unittest  # importarea librariei unit test care va face programul grupat in bucati rulabile individual
from time import sleep
from typing import Tuple

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Test(unittest.TestCase):
    HOME_Page = (By.XPATH, '//a[text()="Home"]')
    CONTACT_US_LINK = (By.XPATH, '//a[text()="Contact Page"]')
    SEARCH_FILD = (By.CLASS_NAME, 'field')
    SEARCH_BTN = (By.XPATH, '//button')
    send_update_name = (By.ID, 'optinforms-form1-name-field')
    send_update_email = (By.ID, 'optinforms-form1-email-field')
    send_update_btn = (By.ID, 'optinforms-form1-button')
    send_update_click_box = (By.XPATH, '//input[@type="checkbox"]')
    expected_title = (By.CLASS_NAME, 'masthead')
    next_Article = (By.ID, "aswift_11")
    logged_in_link = (By.XPATH, '//a[text()="logged in"]')
    login_user = (By.ID, 'user_login')
    password = (By.ID, 'user_pass')
    rememberme_box = (By.ID, 'rememberme')
    loggin_btn = (By.ID, 'wp-submit')
    login_error = (By.ID, 'login_error')

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://www.alternative-energies.net/')  # url de start



    def tearDown(self):
        self.chrome.quit()



    def test_home_page_title(self):
        self.chrome.find_element(*self.HOME_Page).click()
        actual = self.chrome.title
        expected = 'Alternative-energies.net – News about renewable energy and electric vehicles'
        self.assertEqual(expected, actual, 'Page title is incorrect')

    # @unittest.skip
    def test_url_contact_page(self):
        self.chrome.implicitly_wait(10)
        self.chrome.find_element(*self.CONTACT_US_LINK).click()
        actual = self.chrome.current_url
        expected = 'https://www.alternative-energies.net/contact-page/'
        self.assertEqual(expected, actual, 'URL is incorrect')

    # @unittest.skip
    def test_page_title(self):
        self.chrome.find_element(*self.CONTACT_US_LINK).click()
        actual = self.chrome.title
        expected = 'Contact Page - Alternative-energies.net'
        self.assertEqual(expected, actual, 'Page title is incorrect')

    # def test_next_article(self):
    #     self.chrome.get('https://www.alternative-energies.net/how-to-build-a-safe-and-sustainable-worksite/')
    #     self.chrome.find_element(*self.next_Article).click()
    #     actual = self.chrome.title
    #     expected = '7 Sustainable Practices For Household Energy Consumption'
    #     self.assertEqual(expected, actual, 'Page title is incorrect')

    # @unittest.skip
    def test_search_visible(self):
        self.chrome.find_element(*self.SEARCH_FILD).send_keys('energies')  # click() #dam click pe buton
        sleep(3)
        self.chrome.find_element(*self.SEARCH_BTN).click() # dam click pe buton
        sleep(3)
        error = self.chrome.find_element(*self.SEARCH_FILD)  # salvam eroarea ca element(eroarea)
        self.assertTrue(error.is_displayed(), 'Eroarea nu e vizibila')  # afisam mai jos ca exista eroarea

    def test_send_update(self):
        self.chrome.find_element(*self.CONTACT_US_LINK).click()
        self.chrome.find_element(*self.send_update_name).send_keys('Magdalena')
        self.chrome.find_element(*self.send_update_email).send_keys('magda99ro@yahoo.com')
        sleep(3)
        self.chrome.find_element(*self.send_update_click_box).click()
        sleep(3)
        self.chrome.find_element(*self.send_update_btn).click()
        actual = self.chrome.find_element(*self.expected_title).text
        expected = 'Alternative-energies.net Newsletter'
        self.assertEqual(expected, actual, 'Page title is incorrect')

    def test_login(self):
        self.chrome.find_element(*self.CONTACT_US_LINK).click()
        self.chrome.find_element(*self.logged_in_link).click()
        self.chrome.find_element(*self.login_user).send_keys('Magdalena')
        self.chrome.find_element(*self.password).send_keys('Magdalena')
        self.chrome.find_element(*self.rememberme_box).click()
        self.chrome.find_element(*self.loggin_btn).click()
        actual = self.chrome.find_element(*self.login_error).text
        expected = 'ERROR: Empty CAPTCHA'
        self.assertEqual(expected, actual, 'Text is incorrect')

