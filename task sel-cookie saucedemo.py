# Using Python Selenium Automation and the URL https://www.saucedemo.com/ display the Cookie created before login and
# after login in the console. After you login into the dashboard of the portal kindly do the logout also.
# Verify that the Cookies are being generated during the Login process.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

#cookies before login
cookies_before_login = driver.get_cookies()
print(cookies_before_login)
time.sleep(3)

#login
user_name=driver.find_element(By.ID,"user-name")
user_name.send_keys("standard_user")
password=driver.find_element(By.ID,"password")
password.send_keys("secret_sauce")
time.sleep(3)
login_button=driver.find_element(By.ID,"login-button")
login_button.click()
time.sleep(5)

#cookies after login
cookies_after_login = driver.get_cookies()
print(cookies_after_login)
time.sleep(3)

#compare the cookies before and after login
new_cookies=[cookie for cookie in cookies_after_login if cookie not in cookies_before_login]
if new_cookies:
    print("new cookies after login")
    for cookie in new_cookies:
        print(cookie)
    else:
        print("no new cookies")



#logout
# Wait for the menu to be clickable and click on it
menu_bar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
menu_bar.click()

# Wait for logout link to be clickable and click on it
logout = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
logout.click()


driver.quit()