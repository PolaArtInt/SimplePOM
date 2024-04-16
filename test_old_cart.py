
# inventory:
# item_names = ('xpath', '//div[@class="inventory_item_name"]')
# add_btns = ('xpath', '//button[@class="btn_primary btn_inventory"]')
# remove_btns = ('xpath', '//button[@class="btn_secondary btn_inventory"]')

# # cart:
# cart_btn = ('xpath', '//a[@class="shopping_cart_link fa-layers fa-fw"]')
# cart_tag = ('xpath', '//a[@class="shopping_cart_link fa-layers fa-fw"]/span')
# cart_remove_btn = ('xpath', '//button[@class="btn_secondary cart_button"]')


# def test_add_to_cart(driver, standard_old_auth):
#     item_name = driver.find_elements(*item_names)[3].text
#     driver.find_elements(*add_btns)[3].click()
#
#     tag = driver.find_element(*cart_tag).text
#     assert int(tag) == 1, 'Wrong items quantity in cart'
#
#     driver.find_element(*cart_btn).click()
#
#     cart_item_title = driver.find_element(*item_names).text
#     assert item_name == cart_item_title, 'Different item picked'
#
#     driver.find_element(*cart_remove_btn).click()
#
#     items_in_cart = driver.find_elements(*item_names)
#     assert len(items_in_cart) == 0, 'Cart is not empty'
