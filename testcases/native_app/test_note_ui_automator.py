import time

from appium import webdriver

"""
It creates notes and shows possibilities of UIAutomator class
"""

desired_caps = dict(
    deviceName='Android',
    platformName='Android',
    appPackage='com.gcteam.tonote',
    appActivity='com.gcteam.tonote.ui.MainActivity'
)
driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub",
                          desired_capabilities=desired_caps)

#  resource-id = id in browser - must be unique

# add wait for waiting elements
driver.implicitly_wait(5)

# make representation of notes as list
driver.find_element_by_id("com.gcteam.tonote:id/menu_item_view").click()
driver.find_element_by_android_uiautomator('new UiSelector().text("List")').click()
driver.back()
# create 10 notes
for i in range(4):
    driver.find_element_by_id("com.gcteam.tonote:id/fab").click()
    if i == 0:
        # for 1 time it shows automatic saving - enable it
        driver.find_element_by_id("android:id/button3").click()

    if i == 1:
        # for 2 time it shows popup with functions which provide app
        driver.find_element_by_id("com.gcteam.tonote:id/okButton").click()
    time.sleep(1)
    driver.find_element_by_id("com.gcteam.tonote:id/titleEdit").send_keys(f"Test Note {i}")
    content = f"Content of Note {i}" * 100
    driver.find_element_by_id("com.gcteam.tonote:id/contentEdit").send_keys(content)
    if i < 1:
        driver.find_element_by_id("com.gcteam.tonote:id/menu_item_save").click()
    else:
        driver.find_element_by_accessibility_id("Navigate up").click()

# https://developer.android.com/reference/androidx/test/uiautomator/UiSelector
time.sleep(2)
# clicking by text (must be visible)
driver.find_element_by_android_uiautomator('new UiSelector().text("Test Note 3")').click()
driver.find_element_by_accessibility_id("Navigate up").click()

# scrolling - find item by partial text
# https://developer.android.com/reference/androidx/test/uiautomator/UiScrollable
driver.find_element_by_android_uiautomator\
    ('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("Note 0").instance(0))').click()
driver.find_element_by_accessibility_id("Navigate up").click()