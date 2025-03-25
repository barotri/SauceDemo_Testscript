from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self,page):
        super().__init__(page)
        self.username_field="//input[@id='username']"
        self.password_field="//input[@id='password']"
        self.login_button="//button[@id='submit']"

    def navigate_to_login(self):
        self.navigate("https://practicetestautomation.com/practice-test-login/")

    def enter_username(self,username):
        self.fill(self.username_field,username)

    def enter_password(self,password):
        self.fill(self.password_field,password)

    def click_login(self):
        self.click(self.login_button)
    
    def login(self,username,password):
        self.navigate_to_login()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
