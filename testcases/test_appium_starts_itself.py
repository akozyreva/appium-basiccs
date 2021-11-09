import time

from appium import webdriver
from appium.webdriver.appium_service import AppiumService

from variables import desired_caps_emulator

try:
    appium_service = AppiumService()
    appium_service.start()
    print(appium_service.is_running)
    print(appium_service.is_listening)
    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub",
                              desired_capabilities=desired_caps_emulator)
    driver.get("https://google.com")
    print(driver.title)
    time.sleep(2)

    driver.quit()
finally:
    appium_service.stop()