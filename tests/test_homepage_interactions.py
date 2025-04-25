import pytest

from pages.home_page import HomePage
from playwright.sync_api import expect


def test_all_products_displayed(login_session):
    page = HomePage(login_session)
    # Check number of products
    assert page.get_product_cards() == 6, "Expected 6 products"

def test_add_to_cart_(login_session):
    page = HomePage(login_session)
    page.add_to_cart_by_index(0)
    # Check if cart badge is updated
    assert page.shopping_cart_badge.inner_text() == "1"
    
def test_logout_from_homepage(login_session):
    page = HomePage(login_session)
    page.click_logout()
    expect(login_session).to_have_url("https://www.saucedemo.com/")
