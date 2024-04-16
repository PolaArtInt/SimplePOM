from pages.base_page import BasePage
from locators.auth_locs import AuthLocs


class AuthPage(BasePage):
    def input_user(self):
        return self.is_visible(AuthLocs.input_user)

    def input_pass(self):
        return self.is_visible(AuthLocs.input_pass)

    def login_btn(self):
        return self.is_clickable(AuthLocs.login_btn)

    @staticmethod
    def login_err_msg():
        return AuthLocs.login_err_msg
