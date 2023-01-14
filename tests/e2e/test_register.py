import pytest
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pages.register_page import registerPage
from common import Common
import random
import secrets


#Register page
def test_register(browser):
    common = Common(browser)
    register_page = registerPage(browser)
    common.navigate()
    register_page.clickSignup()
    register_page.setEmail(f"{secrets.token_hex(8)}@gmail.com")
    register_page.inputPassword("Tadasdasdsad423423424#$@#$")
    register_page.clickApplyBtn()
    time.sleep(3)
    register_page.inputBusiness("Test Business")
    register_page.inputDBA("usual")
    register_page.inputWebsite("www.example.com")
    register_page.inputFirstName("Test Name")
    register_page.inputLastName("Test Last Name")
    register_page.inputPhoneNumber("2015555555")
    register_page.numberEmployees("20")
    register_page.businessType()
    register_page.llc()
    register_page.clickRevenue()
    register_page.selectRevenue()
    register_page.clickNextBTN()
    time.sleep(8)