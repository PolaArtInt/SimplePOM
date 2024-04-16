
# urls:
# url = 'https://www.saucedemo.com/v1/'
# inventory_url = 'https://www.saucedemo.com/v1/inventory.html'

# # auth:
# input_user = ('xpath', '//input[@id="user-name"]')
# input_pass = ('xpath', '//input[@id="password"]')
# login_btn = ('xpath', '//input[@id="login-button"]')
# locked_msg = 'Epic sadface: Sorry, this user has been locked out.'
# login_err_msg = 'Epic sadface: Username and password do not match any user in this service'
# user = 'standard_user'
# pass_word = 'secret_sauce'
# wrong_user = 'user'
# wrong_password = 'user'

# # inventory:
# prod_header = ('xpath', '//div[@class="product_label"]')
# item_cards = ('xpath', '//div[@class="inventory_item"]')


# def test_standart_login(driver, standard_old_auth):
#     inventory_header = driver.find_element(*prod_header).text
#     inventory_cards = driver.find_elements(*item_cards)
#
#     assert driver.current_url == inventory_url, 'Wrong url'
#     assert inventory_header == 'Products', 'Wrong page header'
#     assert len(inventory_cards) > 0, 'There are no item cards on the inventory page'
#     print(f'\nStandard user...')
#
#
# def test_auth_negative_wrong_login(driver):
#     driver.get(url)
#     driver.find_element(*input_user).send_keys(wrong_user)
#     driver.find_element(*input_pass).send_keys(wrong_password)
#     driver.find_element(*login_btn).click()
#
#     assert login_err_msg, 'Wrong login'
#     assert driver.current_url == url, 'Wrong url'
#     print(f'\nWrong login user...')
