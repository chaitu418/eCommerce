import pytest
from playwright.sync_api import sync_playwright
import allure
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@allure.feature('Network Traces')
def test_network_traces():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        login_page = LoginPage(page)
        dashboard_page = DashboardPage(page)
        
        page.start_tracing(path="trace.json")

        login_page.goto("https://rahulshettyacademy.com/client/dashboard/dash")
        login_page.login('manichaitanya.mc@gmail.com', 'kADveNapu!7jje6')

        dashboard_page.goto_products()
        dashboard_page.add_to_cart()
        dashboard_page.goto_cart()
        dashboard_page.goto_checkout()

        page.stop_tracing()
        allure.attach.file("trace.json", name="Network Trace", attachment_type=allure.attachment_type.JSON)

        browser.close()

if __name__ == "__main__":
    test_network_traces()
