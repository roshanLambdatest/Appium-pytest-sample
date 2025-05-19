# test_android_app.py

import os
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv()

USERNAME = "LT-USERNAME"
ACCESS_KEY = "LT-ACCESSKEY"

@pytest.mark.parametrize("device,version,platform", [
    ("Galaxy S25 Ultra", "15", "Android"),
])
def test_android_app(device, version, platform):
    options = UiAutomator2Options()
    options.set_capability("platformName", platform)
    options.set_capability("deviceName", device)
    options.set_capability("platformVersion", version)
    options.set_capability("isRealMobile", True)
    options.set_capability("app", "lt://APP-URL")  # Replace with your actual app URL
    options.set_capability("build", "Python Android Build")
    options.set_capability("name", "Android Test")
    options.set_capability("geoLocation", "HK")
    options.set_capability("visual", True)
    options.set_capability("autoGrantPermissions", True) 
    options.set_capability("autoAcceptAlerts", True)

    url = f"https://{USERNAME}:{ACCESS_KEY}@mobile-hub.lambdatest.com/wd/hub"
    driver = webdriver.Remote(command_executor=url, options=options)

    try:
        wait = WebDriverWait(driver, 30)
        wait.until(EC.presence_of_element_located((By.ID, "color"))).click()
        wait.until(EC.presence_of_element_located((By.ID, "Text"))).click()
        wait.until(EC.presence_of_element_located((By.ID, "toast"))).click()
        wait.until(EC.presence_of_element_located((By.ID, "notification"))).click()
        wait.until(EC.presence_of_element_located((By.ID, "geoLocation"))).click()
        driver.back()
        wait.until(EC.presence_of_element_located((By.ID, "speedTest"))).click()
    finally:
        driver.quit()
