import requests
import time
import allure

@allure.feature('API Performance')
def test_api_response_time():
    urls = [ "https://rahulshettyacademy.com/client/dashboard/dash/api/products", "https://rahulshettyacademy.com/client/dashboard/dash/api/products/1", "https://rahulshettyacademy.com/client/dashboard/dash/api/cart", "https://rahulshettyacademy.com/client/dashboard/dash/api/checkout", "https://rahulshettyacademy.com/client/dashboard/dash/api/user/profile" ]

    for url in urls:
        start_time=time.time()
        response=requests.get(url)
        end_time=time.time() 
        response_time=end_time-start_time
        
        assert response.status_code == 200
        assert response_time < 2 #ensure repsonse time is less that 2 seconds
        
        print(f"API: {url} Response Time: {response_time}")
        allure.attach(url, name=f"{url} Response Time", attachment_type=allure.attachment_type.TEXT)
        
    if __name__ == "__main__":
        test_api_response_time()