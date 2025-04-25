from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self,page):
        super().__init__(page)
        self.Page_Title=page.locator("//h1[text()='Swag Labs']")


    def get_login_message(self):
        return self.get_text(self.welcome_message)
    
    def click_logout(self):
        return self.click(self.logout_button)
    
    def get_title(self):
        return self.page.title()