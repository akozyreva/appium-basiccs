from appium.webdriver.appium_service import AppiumService

def setup_module():
    #start appium
    global appium_service
    appium_service = AppiumService()
    appium_service.start(args=['--address', '127.0.0.1', '-p', '4723'])

def teardown_module():
    appium_service.stop()


# this test opens native calc app and click on digit by nonexistent path and fails
def test_calc_click_on_digit(mobile_screen):
    mobile_screen.find_element_by_id(f"com.android.calculator1:id/digit_1").click()