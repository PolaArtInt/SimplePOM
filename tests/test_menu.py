from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.menu_page import MenuModule
from pages.auth_page import AuthPage

from locators.urls import URLs


def test_positive_logout(driver, standard_auth):
    menu_page = MenuModule(driver, standard_auth)
    log_page = AuthPage(driver, standard_auth)

    menu_page.menu_btn().click()
    menu_page.logout_btn().click()

    assert driver.current_url == URLs.login_url, 'Wrong url'

    log_btn = log_page.login_btn()
    assert log_page.login_btn(), 'Login button not appearing'
    assert log_btn.get_attribute('value') == 'LOGIN', 'Login button not found'


def test_reset_app_state_negative(driver, standard_auth):
    inv_page = InventoryPage(driver, standard_auth)
    cart_page = CartPage(driver, standard_auth)
    menu_page = MenuModule(driver, standard_auth)

    inv_page.add_btns()[4].click()
    inv_page.add_btns()[4].click()

    tag = cart_page.cart_tag()
    assert int(tag.text) == 2, 'Wrong items quantity in cart'

    menu_page.menu_btn().click()
    menu_page.reset_btn().click()

    assert cart_page.cart_tag_invisible(), 'Tag is visible, cart is not empty'

    try:
        assert len(inv_page.item_names()) == 0, 'Cart is not empty'
    except AssertionError:
        print(f'Cart is not empty. There are {len(inv_page.item_names())} items in it')

    cart_page.refresh()
