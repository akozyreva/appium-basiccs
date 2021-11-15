import time

from appium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from variables import desired_caps_real_device_chrome

# NB - real device is needed!
driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub",
                          desired_capabilities=desired_caps_real_device_chrome)
driver.get("https://wikipedia.org")
# Select example
# find by id and name don't work in appium
dropdown = driver.find_element_by_xpath("//select[@id='searchLanguage']")
# it's for custom select
select = Select(dropdown)
# select by text doesn't work in mob. use value instead
select.select_by_value("de")
# =========

# print all opt texts
options = driver.find_elements_by_tag_name("option")
for option in options:
    print(option.text)

driver.find_element_by_xpath("//input[@id='searchInput']").send_keys("Merkel\n")
time.sleep(2)
exp_title = driver.find_element_by_xpath("//h1").text
assert exp_title == "Angela Merkel"



print(driver.title)
time.sleep(2)



#driver.quit()