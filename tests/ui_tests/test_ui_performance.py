import pytest
from playwright.sync_api import sync_playwright
import time
import allure
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@allure.feature('UI Performance')
def test_ui_performance():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        login_page = LoginPage(page)
        login_page.go_to("https://rahulshettyacademy.com/client/dashboard/dash")
        login_page.login('manichaitanya.mc@gmail.com', 'kADveNapu!7jje6') 
        
        urls = [ "https://rahulshettyacademy.com/client/dashboard/dash", "https://rahulshettyacademy.com/client/dashboard/dash/products", "https://rahulshettyacademy.com/client/dashboard/dash/products/1", "https://rahulshettyacademy.com/client/dashboard/dash/cart", "https://rahulshettyacademy.com/client/dashboard/dash/checkout" ]
        for url in urls: 
            start_time = time.time() 
            dashboard_page.goto(url) 
            dashboard_page.wait_for_load_state() 
            end_time = time.time() 
            load_time = end_time - start_time 
            assert load_time < 3 # Ensure page load time is less than 3 seconds 
            print(f"Page: {url} loaded in {load_time} seconds") 
            allure.attach(str(load_time), name=f"{url} Load Time", attachment_type=allure.attachment_type.TEXT) 
        browser.close() 

if __name__ == "__main__": 
    test_ui_performance()