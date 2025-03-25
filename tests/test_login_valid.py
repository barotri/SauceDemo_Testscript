import pytest
import sys
import os
from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_login_valid(page):
    login_page = LoginPage(page)
    home_page = HomePage(page)

    login_page.login("student","Password123")

    assert "Logged In Successfully" in home_page.get_login_message()
    home_page.click_logout()