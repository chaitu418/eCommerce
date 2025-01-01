from .base_page import BasePage
class LoginPage(BasePage):
    def login(self, username: str, password: str):
        self.fill("input[name='email']", email)
        self.fill("input[name='password']", password)
        self.click("button[type='submit']")
        self.wait_for_load_state()