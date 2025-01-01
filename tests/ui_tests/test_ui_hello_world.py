import pytest
from playwright.sync_api import sync_playwright

def test_ui_hello_world():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://example.com')
        assert page.title() == 'Example Domain'
        browser.close()