from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir+'\Resources')

from TestData import TestData
from Locators import Locators

class BasePage():

  def __init__(self, driver):
    self.driver = driver

  def click(self, by_locator):
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

  def input_text(self, by_locator, text):
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

  def is_visible(self, by_locator):
    element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    return bool(element)

  def screenshot(self, test_name):
    self.driver.save_screenshot('Screenshots/' + test_name + '.png')

class Homepage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)
    self.driver.get(TestData.BASE_URL)

  def click_navbar(self):
    self.click(Locators.NAVBAR_BRAND)

  def click_home(self):
    self.click(Locators.MENU_HOME)

  def click_contact(self):
    self.click(Locators.MENU_CONTACT)

  def click_about_us(self):
    self.click(Locators.MENU_ABOUT_US)

  def click_cart(self):
    self.click(Locators.MENU_CART)

  def click_login(self):
    self.click(Locators.MENU_LOGIN)

  def click_signup(self):
    self.click(Locators.MENU_SIGNUP)

