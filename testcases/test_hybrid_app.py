import time

from appium import webdriver

# it's hybrid app
# idea is to switch to desired context and continue stuff there
# could be, when app redirects to url from browser (terms of agreement), etc.
# on chrome tab as separated activity unable to reproduce

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'Android'
desired_caps['appPackage'] = 'com.android.chrome'
desired_caps['appActivity'] = 'org.chromium.chrome.browser.ChromeTabbedActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)

driver.get('http://google.com')
time.sleep(2)
contexts = driver.contexts

for context in contexts:
    print(context)
#
# driver.switch_to.context('WEBVIEW_chrome')

webview = driver.contexts[1]

driver.switch_to.context(webview)

driver.find_element_by_xpath("//*[@name='q']").send_keys("Hello Appium !!!")

time.sleep(2)
driver.quit()

