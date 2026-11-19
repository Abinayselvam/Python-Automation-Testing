from .base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.username = "username"
        self.password = "password"
        self.login_button = "login"

    def enter_username(self, username):
        self.page.fill(self.username, username)

    def enter_password(self, password):
        self.page.fill(self.password, password)

    def click_login(self):
        self.page.click(self.login_button)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()