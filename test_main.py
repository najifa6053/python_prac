import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

print(driver.title)
driver.get("https://www.saucedemo.com/")

user_name = driver.find_element(By.ID, "user-name")
time.sleep(5)
password = driver.find_element(By.ID, "password")
time.sleep(5)
login_button = driver.find_element(By.ID, "login-button")

user_name.send_keys("standard_user")
password.send_keys("secret_sauce")
login_button.click()
time.sleep(5)
driver.quit()