import pytest

from pages.home_page import HomePage
from playwright.sync_api import expect


def test_all_products_displayed(login_session):
    page = login_session
    product_cards = page.locator(".inventory_item")
    
    # Check number of products
    assert product_cards.count() == 6, "Expected 6 products"

def test_add_to_cart_(login_session):
    page = login_session
    page.click("text=Add to cart")
    assert page.locator(".shopping_cart_badge").inner_text() == "1"
