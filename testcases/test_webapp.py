import time

from appium import webdriver

desired_caps = dict(
    deviceName="HUAWEI P20 Lite",
    udid="9WV4C19221015777",
    platformName="Android",
    platformVersion="9",
    browserName="Chrome"
)

driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub",
                          desired_capabilities=desired_caps)
driver.get("https://google.com")
print(driver.title)
time.sleep(2)
driver.quit()