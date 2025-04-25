import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from playwright.sync_api import expect

def test_login_valid_tc1(page):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    login_page.login_user("standard_user","secret_sauce")
    assert home_page.get_title() == "Swag Labs"
    
def test_login_invalid_tc2(page):
    login_page = LoginPage(page)
    login_page.login_user("Admin","wrongpassword")
    expect(login_page.error_message).to_have_text("Epic sadface: Username and password do not match any user in this service")
