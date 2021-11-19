import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from utilities.scroll_util import ScrollUtil

"""
It creates notes and shows possibilities of UIAutomator class
Seq of steps:
1. Open notes app
2. Open properties and choose list representation, choose manually sorting
3. Create 4 notes with random content.
4. In grid notes click on note 3 (above one). Then go back
5. Scroll down to the last note (note 0) and click on it.
6. Scroll down 4 times.
7. Scroll up 4 times.
8. Swipe note 3 and remove it
9. Long tap on note 2 and remove it.
10. Drag and drop note 1 to note0 and replace it with note0
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
# enable drag and drop possibility
driver.find_element_by_android_uiautomator('new UiSelector().text("Manually")').click()
time.sleep(1)
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
# and then agree to remove Note 3
time.sleep(1)
popup_msg = driver.find_element_by_id("android:id/message").text
assert popup_msg == "Remove?"
driver.find_element_by_id("android:id/button1").click()

# window size
handle_one_size = driver.get_window_size()
handle_two_size = driver.get_window_size("handleName")
print(handle_one_size)
print(handle_two_size)

# long tap -> add menu is showed -> click to remove -> accept it
note_2 = driver.find_element_by_android_uiautomator('new UiSelector().text("Test Note 2")')

actions = TouchAction(driver)
actions.long_press(note_2)
actions.perform()

driver.find_element_by_id("com.gcteam.tonote:id/menu_item_view").click()
driver.find_element_by_id("android:id/button1").click()

time.sleep(2)
note_1 = driver.find_element_by_android_uiautomator('new UiSelector().text("Test Note 1")')
note_0 = driver.find_element_by_android_uiautomator('new UiSelector().text("Test Note 0")')
# drag and drop - change order of 1 and 0 notes
actions = TouchAction(driver)
# actions.perform()
actions.press(note_1).wait(3000).move_to(note_0).perform().release()