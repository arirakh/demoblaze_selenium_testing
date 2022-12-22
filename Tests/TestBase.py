import time
import unittest
import HtmlTestRunner

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir+'\Resources')

from TestData import TestData
from Pages import Homepage
from Locators import Locators

class TestDemoBlazeBase(unittest.TestCase):

  def setUp(self):
    chrome_options = webdriver.ChromeOptions()
    self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    self.driver.maximize_window()

  def tearDown(self):
    self.driver.close()
    self.driver.quit()

class TestDemoBlaze(TestDemoBlazeBase):

  def setUp(self):
    super().setUp()

  def test_homepage_loaded_success(self):
    self.homePage = Homepage(self.driver)

    self.assertIn(TestData.HOMEPAGE_TITLE, self.homePage.driver.title)
    self.homePage.screenshot('test_homepage_loaded_success')

  def test_click_menu_home(self):
    self.homePage = Homepage(self.driver)
    self.homePage.click_home()
    time.sleep(3)

    self.assertIn(TestData.HOMEPAGE_TITLE, self.homePage.driver.title)
    self.homePage.screenshot('test_click_menu_home')

  def test_click_menu_contact(self):
    self.homePage = Homepage(self.driver)
    self.homePage.click_contact()
    time.sleep(3)

    self.assertTrue(self.homePage.is_visible(Locators.CONTACT_US_TITLE))
    self.homePage.screenshot('test_click_menu_contact')

  def test_click_menu_about_us(self):
    self.homePage = Homepage(self.driver)
    self.homePage.click_about_us()
    time.sleep(3)

    self.assertTrue(self.homePage.is_visible(Locators.ABOUT_US_TITLE))
    self.homePage.screenshot('test_click_menu_about_us')

  def test_click_menu_cart(self):
    self.homePage = Homepage(self.driver)
    self.homePage.click_cart()
    time.sleep(3)

    self.assertTrue(self.homePage.is_visible(Locators.TOTAL_TEXT))
    self.homePage.screenshot('test_click_menu_cart')

  def test_click_login(self):
    self.homePage = Homepage(self.driver)
    self.homePage.click_login()
    time.sleep(3)

    self.assertTrue(self.homePage.is_visible(Locators.LOGIN_TITLE))
    self.homePage.screenshot('test_click_login')

  def test_click_signup(self):
    self.homePage = Homepage(self.driver)
    self.homePage.click_signup()
    time.sleep(3)

    self.assertTrue(self.homePage.is_visible(Locators.SIGNUP_TITLE))
    self.homePage.screenshot('test_click_signup')

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=parentdir + '\Reports'))