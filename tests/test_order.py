from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.order_page import OrderPage

from locators.urls import URLs


def test_order_positive(driver, fake, standard_auth):
    inv_page = InventoryPage(driver, standard_auth)
    cart_page = CartPage(driver, standard_auth)
    order_page = OrderPage(driver, standard_auth)

    inv_page.add_btns()[0].click()

    tag = cart_page.cart_tag()
    assert int(tag.text) == 1, 'Wrong items quantity in cart'

    cart_page.cart_btn().click()
    order_page.checkout_btn().click()

    order_page.input_fname().send_keys(fake.first_name())
    order_page.input_lname().send_keys(fake.last_name())
    order_page.input_zipcode().send_keys(fake.zipcode())

    order_page.continue_btn().click()
    order_page.finish_btn().click()

    assert driver.current_url == URLs.checkout_url and order_page.complete_msg, \
        'Wrong url, success message not provided'

    items_in_cart = inv_page.item_names()
    assert len(items_in_cart) == 0, 'Cart is not empty'
    assert cart_page.cart_tag_invisible(), 'Tag is visible, cart is not empty'


