import time

from appium import webdriver

"""
It's test, which checks calc app
Steps:
- Open Calc App
- Click 1
- Click +
- Click 7
- Click =
- Exp result = sum is 8
"""

desired_caps = dict(
    deviceName='Android',
    platformName='Android',
    appPackage='com.android.calculator2',
    appActivity='com.android.calculator2.Calculator'
)
driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub",
                          desired_capabilities=desired_caps)

#  resource-id = id in browser - must be unique

# add wait for waiting elements
driver.implicitly_wait(5)

# 1 + 7 = 8
driver.find_element_by_id("com.android.calculator2:id/digit_1").click()
driver.find_element_by_id("com.android.calculator2:id/op_add").click()
driver.find_element_by_id("com.android.calculator2:id/digit_7").click()
driver.find_element_by_id("com.android.calculator2:id/eq").click()
exp_sum = driver.find_element_by_id("com.android.calculator2:id/formula").text
print(exp_sum)
assert exp_sum == "8"