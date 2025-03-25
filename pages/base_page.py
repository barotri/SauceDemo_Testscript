from playwright.sync_api import Page

class BasePage():
    def __init__(self,page: Page):
        self.page=page
    
    def navigate(self,url):
        self.page.goto(url)
    
    def click(self,locator):
        self.page.click(locator)

    def fill(self,locator,text):
        self.page.fill(locator,text)

    def get_text(self,locator):
        return self.page.inner_text(locator)