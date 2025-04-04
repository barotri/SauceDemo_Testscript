import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from playwright.sync_api import expect

def test_login_valid(page):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    login_page.login_user("Admin","admin123")
    expect(home_page.Page_Title).to_have_text("Dashboard")
    
def test_login_invalid(page):
    login_page = LoginPage(page)
    login_page.login_user("Admin","wrongpassword")
    expect(login_page.error_message).to_have_text("Invalid credentials")