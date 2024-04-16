import pytest
from selenium import webdriver

from pages.auth_page import AuthPage

from locators.auth_locs import AuthData
from locators.urls import URLs


@pytest.fixture(scope="function", autouse=True)
def driver():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'

    # chrome_options.add_argument("--headless")
    options.add_argument("--window-size=1280,1000")

    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()


# class OldAuth:
#     url = 'https://www.saucedemo.com/v1/'
#     input_user = ('xpath', '//input[@id="user-name"]')
#     input_pass = ('xpath', '//input[@id="password"]')
#     login_btn = ('xpath', '//input[@id="login-button"]')
#     user = 'standard_user'
#     pass_word = 'secret_sauce'


# @pytest.fixture()
# def standard_old_auth(driver):
#     driver.get(OldAuth.url)
#     driver.find_element(*OldAuth.input_user).send_keys(OldAuth.user)
#     driver.find_element(*OldAuth.input_pass).send_keys(OldAuth.pass_word)
#     driver.find_element(*OldAuth.login_btn).click()


@pytest.fixture()
def standard_auth(driver):
    page = AuthPage(driver, URLs.url)
    page.open()

    page.input_user().send_keys(AuthData.user)
    page.input_pass().send_keys(AuthData.pass_word)
    page.login_btn().click()


@pytest.fixture()
def fake():
    from faker import Faker
    fake = Faker()
    return fake
