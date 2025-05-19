# test_ios_app.py

import os
import pytest
from appium import webdriver
from appium.options.ios import XCUITestOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv()

USERNAME = "LT-USERNAME"
ACCESS_KEY = "LT-ACCESSKEY"

@pytest.mark.parametrize("device,version,platform", [
    ("iPhone.*", ".*", "iOS"),
])
def test_ios_app(device, version, platform):
    options = XCUITestOptions()
    options.set_capability("platformName", platform)
    options.set_capability("deviceName", device)
    options.set_capability("platformVersion", version)
    options.set_capability("isRealMobile", True)
    options.set_capability("app", "lt://APP-URL")
    options.set_capability("build", "Python iOS Build")
    options.set_capability("name", "iOS Test")
    options.set_capability("geoLocation", "HK")

    # ✅ Logging and video
    options.set_capability("video", True)
    options.set_capability("visual", True)
    options.set_capability("console", True)
    options.set_capability("network", True)

    # ✅ Auto handle alerts/popups
    options.set_capability("autoAcceptAlerts", True)
    options.set_capability("autoGrantPermissions", True)

    url = f"https://{USERNAME}:{ACCESS_KEY}@mobile-hub.lambdatest.com/wd/hub"
    driver = webdriver.Remote(command_executor=url, options=options)

    try:
        wait = WebDriverWait(driver, 30)

        # ✅ Core test actions
        wait.until(EC.presence_of_element_located((By.ID, "color"))).click()
        wait.until(EC.presence_of_element_located((By.ID, "Text"))).click()
        wait.until(EC.presence_of_element_located((By.ID, "toast"))).click()
        wait.until(EC.presence_of_element_located((By.ID, "notification"))).click()
        wait.until(EC.presence_of_element_located((By.ID, "geoLocation"))).click()

        driver.back()
        # wait.until(EC.presence_of_element_located((By.ID, "speedTest"))).click()

        # ✅ Try closing common popup/ad elements if they appear
        possible_ad_ids = ["ad_close", "dismiss_ad", "popup_close"]
        for ad_id in possible_ad_ids:
            try:
                ad = driver.find_element(By.ID, ad_id)
                if ad.is_displayed():
                    ad.click()
            except:
                pass  # Ad not found; move on

    finally:
        driver.quit()
