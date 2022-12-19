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

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=parentdir + '\Reports'))