from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def go_to(self, url):
        self.page.goto(url)

    def wait_for_load_state(self):
        self.page.wait_for_load_state("networkidle")

    def fill(self, selector:str, value: str):
        self.page.fill(selector, value)

    def click(self, selector: str):
        self.page.click(selector)

    def get_text(self, selector: str) -> str:
        return slef.page.getcontent(selector)

    def get_title():
        return self.page.title()

    def get_url():
        return self.page.url()

    def get_element(self, selector: str):
        return self.page.query_selector(selector)

    def get_elements(self, selector: str):
        return self.page.query_selector_all(selector)
