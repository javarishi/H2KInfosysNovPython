from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from learn_day019.UserID import username, password

# Initialize Driver
driver = webdriver.Firefox(executable_path=r'/RISHI/H2K/Eclipse/Selenium/geckodriver/geckodriver.exe')

try:
    driver.get("https://github.com/")
    print("Done!")

    sign_in = driver.find_element_by_link_text("Sign in")
    print(sign_in)
    sign_in.click()
    print("sign_in page load wait")
    w = WebDriverWait(driver, 8)
    w.until(EC.presence_of_all_elements_located((By.ID,"login_field")))
    print("Page load happened")
    driver.find_element_by_id("login_field").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    print("UserName Password Entered.. Logging in")
    driver.find_element_by_name("commit").click()
    print("Waiting for Page Loading")
    time.sleep(5)
    w = WebDriverWait(driver, 8)
    w.until(EC.presence_of_all_elements_located((By.ID,"dashboard")))
    print("Page load happened.. Interacting with Static Elements")
    time.sleep(5)
    print("Find Stable Component First")
    repos_container = driver.find_element_by_class_name("js-repos-container")
    print("Accessing List Element with Dynamic Content")
    repo_list_ul = repos_container.find_element_by_class_name("list-style-none")
    items = repo_list_ul.find_elements_by_tag_name("li")
    for item in items:
        print(item.text)
    time.sleep(5)
    print("Accessing search field - static component with ID")

except Exception as ex:
    print("Error while doing operation", ex)
    time.sleep(5)
finally:
    print("Closed!")
    driver.close()
