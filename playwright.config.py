from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    # Custom Playwright configurations can go here
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
