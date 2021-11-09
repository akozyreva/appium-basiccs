from appium import webdriver

desired_caps = dict(
    deviceName='Android',
    platformName='Android',
    appPackage='com.android.contacts',
    appActivity='com.android.contacts.activities.DialtactsActivity'
)
driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub",
                          desired_capabilities=desired_caps)

