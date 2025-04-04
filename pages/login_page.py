from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self,page):
        super().__init__(page)
        self.username_field=page.locator("//input[@placeholder='Username']")
        self.password_field=page.locator("//input[@placeholder='Password']")
        self.login_button=page.locator("//button[@type='submit']")
        #Error message
        self.error_message=page.locator("//p[text()='Invalid credentials']")

    # def navigate_to_login(self):
    #     self.navigate("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    
    def login_user(self,username,password):
        self.navigate("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()
