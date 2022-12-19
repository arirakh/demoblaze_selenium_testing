from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir+'\Resources')

from TestData import TestData

class BasePage():

  def __init__(self, driver):
    self.driver = driver

  def click(self, by_locator):
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

  def input_text(self, by_locator, text):
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

class Homepage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)
    self.driver.get(TestData.BASE_URL)

