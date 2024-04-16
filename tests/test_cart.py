from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage


def test_add_to_cart(driver, standard_auth):
    inv_page = InventoryPage(driver, standard_auth)
    cart_page = CartPage(driver, standard_auth)

    item_title = inv_page.item_names()[3].text
    inv_page.add_btns()[3].click()

    tag = cart_page.cart_tag().text
    assert int(tag) == 1, 'Wrong items quantity in cart'

    cart_page.cart_btn().click()

    cart_item_title = inv_page.item_name().text
    assert item_title == cart_item_title, 'Different item picked'

    cart_page.cart_remove_btn().click()

    assert len(inv_page.item_names()) == 0, 'Cart is not empty'
