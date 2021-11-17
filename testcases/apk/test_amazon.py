import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from variables import desired_caps_emulator, PROJECT_DIR

# if app is not installed, it installs it firstly, otherwise it lunches it
amazon_app_caps = {
    "app": f"{PROJECT_DIR}/app/amazon.apk",
    "appPackage": "com.amazon.mShop.android.shopping",
    "appActivity": "com.amazon.mShop.home.HomeActivity"}
desired_caps_emulator_amazon = {**desired_caps_emulator, **amazon_app_caps}

driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub",
                          desired_capabilities=desired_caps_emulator_amazon)
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 20)
currently_waiting_for = wait.until(EC.visibility_of_element_located((By.ID,
                                                                     'com.amazon.mShop.android.shopping:id/signin_to_yourAccount')))
driver.find_element_by_id("com.amazon.mShop.android.shopping:id/skip_sign_in_button").click()
time.sleep(2)
id_to_search_input = "com.amazon.mShop.android.shopping:id/rs_search_src_text"
wait.until(EC.element_to_be_clickable((By.ID, id_to_search_input)))
driver.find_element_by_id(id_to_search_input).send_keys("Shoes")
# after typing Shoes hit Enter
driver.press_keycode(66)
time.sleep(5)
driver.quit()
