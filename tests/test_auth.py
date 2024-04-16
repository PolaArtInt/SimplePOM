from pages.auth_page import AuthPage
from pages.inventory_page import InventoryPage

from locators.auth_locs import AuthLocs, AuthData
from locators.urls import URLs


def test_auth_positive(driver, standard_auth):
    inv_page = InventoryPage(driver, URLs.inventory_url)

    assert driver.current_url == URLs.inventory_url, 'Wrong url'
    assert inv_page.inventory_header().text == 'Products', 'Wrong page header'
    assert len(inv_page.inventory_cards()) > 0, 'There are no item cards on the inventory page'

    print(f'\nStandard user...')


def test_auth_negative_wrong_login(driver):
    log_page = AuthPage(driver, URLs.url)
    log_page.open()

    log_page.input_user().send_keys(AuthData.wrong_user)
    log_page.input_pass().send_keys(AuthData.wrong_password)
    log_page.login_btn().click()

    assert driver.current_url == URLs.url, 'Wrong url'
    assert log_page.login_err_msg() == AuthLocs.login_err_msg, 'Login error'

    print(f'\nWrong login user... {log_page.login_err_msg()}')

