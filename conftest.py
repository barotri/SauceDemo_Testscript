import os
from datetime import datetime
import pytest
#def pytest_configure(config):
    # Đặt tên file report với định dạng: report_YYYY-MM-DD_HH-MM-SS.html
#    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#    config.option.htmlpath = f"reports/report_{current_time}.html"




@pytest.fixture(scope="session")
def login_session(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    page.fill("input[data-test='username']", "standard_user")
    page.fill("input[data-test='password']", "secret_sauce")
    page.click("input[data-test='login-button']")
    
    # Verify login success
    assert "inventory.html" in page.url
    
    return page
