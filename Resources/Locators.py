from selenium.webdriver.common.by import By

class Locators():
  NAVBAR_BRAND = (By.ID, 'nava')
  MENU_HOME = (By.PARTIAL_LINK_TEXT, 'Home')
  MENU_CONTACT = (By.LINK_TEXT, 'Contact')
  MENU_ABOUT_US = (By.LINK_TEXT, 'About us')
  MENU_CART = (By.ID, 'cartur')
  MENU_LOGIN = (By.ID, 'login2')
  MENU_SIGNUP = (By.ID, 'signin2')

  CONTACT_US_TITLE = (By.ID, 'exampleModalLabel')
  ABOUT_US_TITLE = (By.ID, 'videoModalLabel')
  TOTAL_TEXT = (By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/h2')
  LOGIN_TITLE = (By.ID, 'logInModalLabel')
  SIGNUP_TITLE = (By.ID, 'signInModalLabel')