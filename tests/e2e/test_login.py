import pytest
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pages.register_page import registerPage
from pages.login_page import login
from common import Common
import random
import secrets


#invalid Login
def test_register(browser):
    common = Common(browser)
    common.navigate()
    login_page = login(browser)
    login_page.setEmail(f"{secrets.token_hex(8)}@gmail.com")
    login_page.inputPassword("Tadasdasdsad423423424#$@#$")
    login_page.clickSignin()
    login_page.invalidBox()

    time.sleep(5)


    #Forgot Password
def test_forgot_passwd(browser):
    common = Common(browser)
    common.navigate()
    login_page = login(browser)
    login_page.clickForgoPaswd()
    time.sleep(3)
    login_page.inputForgotPassword("test@gmail.com")
    login_page.clickReset()
    login_page.verifyReset()
    time.sleep(5)

