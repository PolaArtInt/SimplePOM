# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec


# # urls:
# url = 'https://www.saucedemo.com/v1/'
# login_url = 'https://www.saucedemo.com/v1/index.html'
# inventory_url = 'https://www.saucedemo.com/v1/inventory.html'

# # menu module:
# menu_btn = ('xpath', '//div[@class="bm-burger-button"]//button')
# logout_btn = ('xpath', '//a[@id="logout_sidebar_link"]')
# reset_btn = ('xpath', '//a[@id="reset_sidebar_link"]')

# # inventory:
# add_btns = ('xpath', '//button[@class="btn_primary btn_inventory"]')

# # cart:
# cart_tag = ('xpath', '//a[@class="shopping_cart_link fa-layers fa-fw"]/span')

# # login page:
# login_btn = ('xpath', '//input[@id="login-button"]')


# def test_positive_logout(driver, standard_old_auth):
#     wait = WebDriverWait(driver, timeout=10)
#
#     driver.find_element(*menu_btn).click()
#     wait.until(ec.element_to_be_clickable(logout_btn)).click()
#
#     assert driver.current_url == login_url, 'Wrong url'
#
#     log_btn_clickable = wait.until(ec.element_to_be_clickable(login_btn))
#     assert log_btn_clickable, 'Login button is not appearing'
#
#     log_btn_text = driver.find_element(*login_btn).get_attribute('value')
#     assert log_btn_text == 'LOGIN', 'Login button not found'


# def test_reset_app_state_positive(driver, standard_old_auth):
#     wait = WebDriverWait(driver, timeout=10)
#
#     driver.find_elements(*add_btns)[4].click()
#     driver.find_elements(*add_btns)[4].click()
#
#     tag = driver.find_element(*cart_tag)
#     assert int(tag.text) == 2, 'Wrong items quantity in cart'
#
#     driver.find_element(*menu_btn).click()
#
#     wait.until(ec.visibility_of_element_located(reset_btn)).click()
#
#     items_in_cart = driver.find_elements(*cart_tag)
#     assert len(items_in_cart) == 0, 'Cart is not empty'
#
#     tag_invisibility = wait.until(ec.invisibility_of_element_located(cart_tag))
#     assert tag_invisibility, 'Tag is visible, cart is not empty'
#
#     driver.refresh()
