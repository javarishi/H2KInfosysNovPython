from selenium import webdriver

import time
# Initialize Driver
driver = webdriver.Firefox(executable_path=r'/RISHI/H2K/Eclipse/Selenium/geckodriver/geckodriver.exe')
try:
    driver.get("https://github.com/")
    print("Done!")
    time.sleep(5)
except Exception as ex:
    print("Error while doing operation", ex)
    time.sleep(5)
finally:
    print("Closed!")
    driver.close()

