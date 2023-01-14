import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import random
import string
import secrets

class login:

#Form Elements 

    EMAIL = (By.ID,'outlined-adornment-email-login')
    PASSWORD = (By.ID,'outlined-adornment-password-login')
    SIGNIN = (By.XPATH,'//*[@id="root"]/div/div/main/div[1]/div/div/div[2]/form/div[4]/button')
    INVALID_DATA = (By.XPATH,"//div[@role='alert']")
    FORGOT_PASWD = (By.XPATH, "//a[normalize-space()='Forgot Password?']")
    FORGOT_PASWD_INPUT = (By.XPATH,"//input[@id='outlined-adornment-email-forgot']")
    RESET_BTN = (By.XPATH,"//button[normalize-space()='Reset password']")
    RESET_ALERT = (By.XPATH, "//div[@role='alert']")

#Start the webdriver
    def __init__(self, browser):
        self.browser = browser

    def clickSignin(self):
        signin_btn = self.browser.find_element(*self.SIGNIN)
        signin_btn.click()

    def inputPassword(self, password):
        password_text = self.browser.find_element(*self.PASSWORD)
        password_text.clear()
        password_text.send_keys(password)

    def setEmail(self, email):
        email_text = self.browser.find_element(*self.EMAIL)
        email_text.clear()
        email_text.send_keys(email)

    def inputPassword(self, password):
        password_text = self.browser.find_element(*self.PASSWORD)
        password_text.clear()
        password_text.send_keys(password)

    def invalidBox(self):
        close_btn = self.browser.find_element(*self.INVALID_DATA)
        close_btn.click()

    def clickForgoPaswd(self):
        forgot_paswd_link = self.browser.find_element(*self.FORGOT_PASWD)
        forgot_paswd_link.click()        

    def inputForgotPassword(self,forgot_pass):
        forgot_pass = self.browser.find_element(*self.FORGOT_PASWD_INPUT)
        forgot_pass.click()
        forgot_pass.send_keys(forgot_pass)

    def clickReset(self):
        reset_btn = self.browser.find_element(*self.RESET_BTN)
        reset_btn.click()

    def verifyReset(self):
        reset_alert = self.browser.find_element(*self.RESET_ALERT)
        reset_alert.click()
