import time

from appium import webdriver

from variables import desired_caps_real_device_chrome

# example of how you can switch between 2 apps - in this example chrome and firefox

driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub",
                          desired_capabilities=desired_caps_real_device_chrome)
driver.get("https://google.com")
print(driver.title)
time.sleep(2)
print(driver.current_activity)
time.sleep(3)
driver.start_activity("org.mozilla.firefox", "org.mozilla.fenix.HomeActivity")
print(driver.title)
print(driver.current_activity)
driver.quit()