import pytest
from playwright.sync_api import sync_playwright
import allure
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@allure.feature('End-to-End')
def test_end_to_end():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        login_page = LoginPage(page)
        dashboard_page = DashboardPage(page)
        
        login_page.goto("https://rahulshettyacademy.com/client/dashboard/dash")
        login_page.login('manichaitanya.mc@gmail.com', 'kADveNapu!7jje6')

        # Add a product to the cart