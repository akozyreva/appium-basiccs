import time

from appium import webdriver

"""
It's test, which checks creation of new contact on native app.
Steps:
- Open Contacts App
- Switch from Phone (default) to Contacts Section
- Click to add new contact
- Fill in Name and Phone
- Save it
- Check that contact is saved - new contact page is opened, contact name is checked and visibility of phone num
"""

desired_caps = dict(
    deviceName='Android',
    platformName='Android',
    appPackage='com.android.contacts',
    appActivity='com.android.contacts.activities.DialtactsActivity'
)
driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub",
                          desired_capabilities=desired_caps)

#  resource-id = id in browser - must be unique

# on my phone - btn to hide/open phone num menu with numbers
# driver.find_element_by_id("com.android.contacts:id/menu_item_image").click()

# add wait for waiting elements
driver.implicitly_wait(5)


# switch to contacts section
driver.find_element_by_xpath("(//android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.ImageView)[2]").click()
# click on btn new contact
# when we have content-desc, we can use accessibility_id instead
driver.find_element_by_accessibility_id('New contact').click()
# driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='New contact']").click()

# time.sleep(3)
# xpaths like bellow took a lot of time, that's why important to ask devs for ids
# input name
driver.find_element_by_xpath("//android.widget.EditText[@text='Name']").send_keys("Test Contact")

# input phone
driver.find_element_by_xpath("//android.widget.EditText[@text='Phone number']").send_keys("12345")

# hide keyboard
driver.hide_keyboard()

# click save
driver.find_element_by_accessibility_id("Done").click()

# check, that contact is really created
# time.sleep(2)
exp_contact_name = driver.find_element_by_id("com.android.contacts:id/name").text
assert exp_contact_name == "Test Contact"
print("Exp contact name is checked")

is_phone_displayed = driver.find_element_by_xpath("//android.widget.TextView[@text='12345']").is_displayed()
print(is_phone_displayed)
assert is_phone_displayed is True
