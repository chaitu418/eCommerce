from .base_page import BasePage
class DashboardPage(BasePage):
    
    def goto_products(self): 
        self.goto("https://rahulshettyacademy.com/client/dashboard/dash/products") 
    
    def goto_cart(self): 
        self.goto("https://rahulshettyacademy.com/client/dashboard/dash/cart") 
    
    def goto_checkout(self): 
        self.go("https://rahulshettyacademy.com/client/dashboard/dash/checkout")
    
    def add_to_card(self):
        self.click("text=Add to Cart",first=True)
        self.wait_for_load_state()
    