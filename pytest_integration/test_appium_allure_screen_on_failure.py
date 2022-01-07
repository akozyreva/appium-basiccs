import pytest
import allure
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.webdriver.appium_service import AppiumService


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

desired_caps = dict(
        deviceName='Android',
        platformName='Android',
        appPackage='com.android.calculator2',
        appActivity='com.android.calculator2.Calculator'
    )


@pytest.fixture
def mobile_screen(request):
    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub",
                              desired_capabilities=desired_caps)
    driver.implicitly_wait(10)
    yield driver

    # Do teardown (this code will be executed after each test):

    if request.node.rep_call.failed:
        # Make the screen-shot if test failed:
        try:
            #driver.execute_script("document.body.bgColor = 'white';")
            allure.attach(driver.get_screenshot_as_png(), name=request.function.__name__,attachment_type=AttachmentType.PNG)
        except Exception as e:
            raise ValueError(f"Something is going wrong with allure screenshot creation! The error is: {e}")

    # Close browser window:
    driver.quit()

def setup_module():
    #start appium
    global appium_service
    appium_service = AppiumService()
    appium_service.start(args=['--address', '127.0.0.1', '-p', '4723'])

def teardown_module():
    appium_service.stop()


# this test opens native calc app and click on digit by nonexistent path and fails
def test_calc_click_on_digit(digit, mobile_screen):
    mobile_screen.find_element_by_id(f"com.android.calculator1:id/digit_1").click()