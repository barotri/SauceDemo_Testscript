from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self,page):
        super().__init__(page)
        self.username_field=page.locator("//input[@placeholder='Username']")
        self.password_field=page.locator("//input[@placeholder='Password']")
        self.login_button=page.locator("//input[@type='submit']")
        #Error message
        self.error_message=page.locator("//h3[@data-test='error']")

    
    def login_user(self,username,password):
        self.navigate("https://www.saucedemo.com/")
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()

    def get_error_text(self):
        return self.error_message.inner_text()

