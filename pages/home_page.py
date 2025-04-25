from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self,page):
        super().__init__(page)
        self.Page_Title=page.locator("/html/head/title")


    def get_login_message(self):
        return self.get_text(self.welcome_message)
    
    def click_logout(self):
        return self.click(self.logout_button)