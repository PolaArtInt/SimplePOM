# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec

# # urls:
# checkout_url = 'https://www.saucedemo.com/v1/checkout-complete.html'

# # inventory:
# item_names = ('xpath', '//div[@class="inventory_item_name"]')
# add_btns = ('xpath', '//button[@class="btn_primary btn_inventory"]')

# # cart:
# cart_btn = ('xpath', '//a[@class="shopping_cart_link fa-layers fa-fw"]')
# cart_tag = ('xpath', '//a[@class="shopping_cart_link fa-layers fa-fw"]/span')

# # order:
# input_fname = ('xpath', '//input[@id="first-name"]')
# input_lname = ('xpath', '//input[@id="last-name"]')
# input_zipcode = ('xpath', '//input[@id="postal-code"]')
# checkout_btn = ('xpath', '//a[@class="btn_action checkout_button"]')
# continue_btn = ('xpath', '//input[@class="btn_primary cart_button"]')
# finish_btn = ('xpath', '//a[@class="btn_action cart_button"]')
# complete_msg = 'THANK YOU FOR YOUR ORDER'


# def test_positive_order(driver, fake, standard_old_auth):
#     wait = WebDriverWait(driver, timeout=10)
#
#     driver.find_elements(*add_btns)[5].click()
#     driver.find_elements(*add_btns)[0].click()
#
#     tag = driver.find_element(*cart_tag)
#     assert int(tag.text) == 2, 'Wrong items quantity in cart'
#
#     driver.find_element(*cart_btn).click()
#     driver.find_element(*checkout_btn).click()
#
#     driver.find_element(*input_fname).send_keys(fake.first_name())
#     driver.find_element(*input_lname).send_keys(fake.last_name())
#     driver.find_element(*input_zipcode).send_keys(fake.zipcode())
#
#     driver.find_element(*continue_btn).click()
#     driver.find_element(*finish_btn).click()
#
#     curr_url = driver.current_url
#     assert curr_url == checkout_url and complete_msg, 'Wrong url, success message not provided'
#
#     items_in_cart = driver.find_elements(*item_names)
#     assert len(items_in_cart) == 0, 'Cart is not empty'
#
#     tag_invisibility = wait.until(ec.invisibility_of_element_located(cart_tag))
#     assert tag_invisibility, 'Tag is visible, cart is not empty'
