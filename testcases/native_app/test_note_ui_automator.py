import time

from appium import webdriver

from utilities.scroll_util import ScrollUtil

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

# gestures
# swipe down -4 times to see, that it really scrolling
time.sleep(2)
driver.swipe(229, 1823, 229, 1377, 1000)
driver.swipe(229, 1823, 229, 1377, 1000)
driver.swipe(229, 1823, 229, 1377, 1000)
driver.swipe(229, 1823, 229, 1377, 1000)

# swipe up
ScrollUtil.swipe_up(4, driver)

# get 1 note above and get coordinates of it, then swipe from right to left and remove it.
coordinates = driver.find_element_by_android_uiautomator('new UiSelector().text("Test Note 3")').location
driver.swipe(859, 652, coordinates['x'], coordinates['y'])
# and then agree to remove
time.sleep(1)
popup_msg = driver.find_element_by_id("android:id/message").text
assert popup_msg == "Remove?"
driver.find_element_by_id("android:id/button1").click()

# window size
handle_one_size = driver.get_window_size()
handle_two_size = driver.get_window_size("handleName")
print(handle_one_size)
print(handle_two_size)

