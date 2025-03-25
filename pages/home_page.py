from pages.base_page import BasePage

class HomePage(BasePage):
    def __init(self,page):
        super().__init__(page)
        self.welcome_message="//*[text()='Logged In Successfully']"
        self.logout_button="//*[@href='https://practicetestautomation.com/practice-test-login/']"


    def get_login_message(self):
        return self.get_text(self.welcome_message)
    
    def click_logout(self):
        self.click(self.logout_button)