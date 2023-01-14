import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import random
import string
import secrets

class registerPage:

#Form Elements 

    EMAIL = (By.ID,'outlined-adornment-email-register')
    PASSWORD = (By.ID,'outlined-adornment-password-register')
    SIGNUP = (By.XPATH,'//*[@id="root"]/div/div/main/div[1]/div/div/div[2]/form/div[5]/a')
    APPLY_BTN = (By.XPATH, "//button[normalize-space()='Apply']")
    BUSINESS_TXT = (By.ID, 'legalBusinessName')
    DBA_TXT = (By.ID, 'businessNameDBA')
    WEBSITE_TXT = (By.ID, 'businessWebsite')
    FIRST_NAME_TXT = (By.ID, 'firstName')
    LAST_NAME_TXT = (By.ID, 'lastName')
    PHONE_NUMBER_TXT = (By.ID, 'phoneNumber')
    NUMBER_EMPLOYEES_TXT = (By.ID, 'numberOfEmployees')
    BUSINESS_TYPE_TXT = (By.XPATH, "//div[@id='businessIncorporationType']")
    LLC_TEXT = (By.XPATH, '//*[@id="menu-businessIncorporationType"]/div[3]/ul/li[1]')
    ANUAL_REVENUE =(By.ID, 'annualRevenue')
    REVENUE_SELECT = (By.XPATH, '//*[@id="menu-annualRevenue"]/div[3]/ul/li[1]')
    NEXT_BUTTON = (By.XPATH, "//button[normalize-space()='Next']")
    


#Start the webdriver
    def __init__(self, browser):
        self.browser = browser

    def clickSignup(self):
        signup_btn = self.browser.find_element(*self.SIGNUP)
        signup_btn.click()


    def setEmail(self, email):
        email_text = self.browser.find_element(*self.EMAIL)
        email_text.clear()
        email_text.send_keys(email)

    def inputPassword(self, password):
        password_text = self.browser.find_element(*self.PASSWORD)
        password_text.clear()
        password_text.send_keys(password)

    def clickApplyBtn(self):
        apply_btn = self.browser.find_element(*self.APPLY_BTN)
        apply_btn.click()

    def inputBusiness(self, business):
        business_txt = self.browser.find_element(*self.BUSINESS_TXT)
        business_txt.send_keys(business)

    def inputDBA(self, dab):
        dab_txt = self.browser.find_element(*self.DBA_TXT)
        dab_txt.send_keys(dab)

    def inputWebsite(self, website):
        website_txt = self.browser.find_element(*self.WEBSITE_TXT)                
        website_txt.send_keys(website)

    def inputFirstName(self, firstName):
        name_txt = self.browser.find_element(*self.FIRST_NAME_TXT)
        name_txt.send_keys(firstName)

    def inputLastName(self, lastName):
        lastName_txt = self.browser.find_element(*self.LAST_NAME_TXT)
        lastName_txt.send_keys(lastName)

    def inputPhoneNumber(self, phoneNumber):
        phoneNumber_txt = self.browser.find_element(*self.PHONE_NUMBER_TXT)
        phoneNumber_txt.send_keys(phoneNumber)

    def numberEmployees(self, employeeNumber):
        employeeNumber_txt = self.browser.find_element(*self.NUMBER_EMPLOYEES_TXT)
        employeeNumber_txt.send_keys(employeeNumber)

    def businessType(self):
        business_option = self.browser.find_element(By.XPATH, "//div[@id='businessIncorporationType']")
        business_option.click()

    def llc(self):
        llc_option = self.browser.find_element(*self.LLC_TEXT)
        llc_option.click()    

    def clickRevenue(self):
        revenue_click = self.browser.find_element(*self.ANUAL_REVENUE)
        revenue_click.click()


    def selectRevenue(self):
        reveneu_option = self.browser.find_element(*self.REVENUE_SELECT)
        reveneu_option.click()    

    def clickNextBTN(self):
        next_btn = self.browser.find_element(*self.NEXT_BUTTON)
        next_btn.click()    


