import pytest
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
desired_caps = dict(
        deviceName='Android',
        platformName='Android',
        appPackage='com.android.calculator2',
        appActivity='com.android.calculator2.Calculator'
    )


def setup_module():
    #start appium
    global appium_service
    appium_service = AppiumService()
    appium_service.start(args=['--address', '127.0.0.1', '-p', '4723'])


def setup_function():
    # start driver
    global driver
    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub",
                              desired_capabilities=desired_caps)
    driver.implicitly_wait(5)


def teardown_function():
    driver.quit()


def teardown_module():
    appium_service.stop()


# this test opens native calc app and click on digit
@pytest.mark.parametrize("digit", [1, 2])
def test_calc_click_on_digit(digit):
    driver.find_element_by_id(f"com.android.calculator2:id/digit_{digit}").click()