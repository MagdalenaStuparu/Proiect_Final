import unittest  # importarea librariei unit test care va face programul grupat in bucati rulabile individual
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Test(unittest.TestCase):
    CONTACT_US_LINK = (By.XPATH, '//a[text()="Contact Page"]')
    SEARCH_FILD = (By.CLASS_NAME, 'field')
    SEARCH_BTN = (By.XPATH, '//button')
    send_update_name = (By.ID, 'optinforms-form1-name-field')
    send_update_email = (By.ID, 'optinforms-form1-email-field')
    send_update_btn = (By.ID, 'optinforms-form1-button')
    send_update_click_box = (By.XPATH, '//input[@type="checkbox"]')

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://www.alternative-energies.net/')  # url de start
        self.chrome.find_element(*self.CONTACT_US_LINK).click()


    def tearDown(self):
        self.chrome.quit()

    # @unittest.skip
    def test_url(self):
        self.chrome.implicitly_wait(10)
        actual = self.chrome.current_url
        expected = 'https://www.alternative-energies.net/contact-page/'
        self.assertEqual(expected, actual, 'URL is incorrect')

    # @unittest.skip
    def test_page_title(self):
        actual = self.chrome.title
        expected = 'Contact Page - Alternative-energies.net'
        self.assertEqual(expected, actual, 'Page title is incorrect')

    # @unittest.skip
    def test_search_visible(self):
        self.chrome.find_element(*self.SEARCH_FILD).send_keys('energies')  # click() #dam click pe buton
        sleep(3)
        self.chrome.find_element(*self.SEARCH_BTN).click() # dam click pe buton
        sleep(3)
        error = self.chrome.find_element(*self.SEARCH_FILD)  # salvam eroarea ca element(eroarea)
        self.assertTrue(error.is_displayed(), 'Eroarea nu e vizibila')  # afisam mai jos ca exista eroarea

    def test_send_update(self):
        self.chrome.find_element(*self.send_update_name).send_keys('Magdalena')
        self.chrome.find_element(*self.send_update_email).send_keys('magda99ro@yahoo.com')
        sleep(3)
        self.chrome.find_element(*self.send_update_click_box).click()
        sleep(3)
        self.chrome.find_element(*self.send_update_btn).click()
        # error= error = self.chrome.find_element(*self.send_update_name)
        # self.assertTrue(error.is_displayed(), 'Eroarea nu e vizibila')