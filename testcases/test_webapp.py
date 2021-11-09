import time

from appium import webdriver

from variables import desired_caps_emulator

driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub",
                          desired_capabilities=desired_caps_emulator)
driver.get("https://google.com")
print(driver.title)
time.sleep(2)


def click_on_bottom_arrow_in_user_agreement_to_see_agree_btn(driver):
    arrow_xpath = "//img[@class='VovmId']"
    is_arrow_is_displayed = True
    while is_arrow_is_displayed is True:
        print("click on arrow")
        # if arrow is visible, click on it
        driver.find_element_by_xpath(arrow_xpath).click()
        # if arrow is still visible, continue
        time.sleep(2)
        if driver.find_element_by_xpath(arrow_xpath).is_displayed():
            continue
        else:
            print("Stop execution")
            is_arrow_is_displayed = False

click_on_bottom_arrow_in_user_agreement_to_see_agree_btn(driver)

driver.find_element_by_xpath("//div[normalize-space()='I agree']/parent::button").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='tsf']//input[@name='q']").send_keys("Hello Appium\n")
time.sleep(3)
driver.quit()