from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self,page):
        super().__init__(page)
        self.Page_Title=page.locator("//h1[text()='Swag Labs']")
        self.logout_button=page.locator("//a[@id='logout_sidebar_link']")
        self.welcome_message=page.locator("//span[@class='title']")
        self.product_card=page.locator(".inventory_item")
        self.burger_menu=page.locator("//button[@id='react-burger-menu-btn']")
        #self.add_to_cart_button=page.locator("//button[@='Add to cart']")
        self.shopping_cart_badge=page.locator(".shopping_cart_badge")
    def add_to_cart_by_index(self,index):
        self.product_card.nth(index).locator(".btn_inventory").click() 
        
    def get_product_cards(self):
        return self.product_card.count()
    
    def get_login_message(self):
        return self.get_text(self.welcome_message)
    
    def click_logout(self):
        self.burger_menu.click()
        self.logout_button.click()
    
    def get_title(self):
        return self.page.title()