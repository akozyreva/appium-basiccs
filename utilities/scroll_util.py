class ScrollUtil:

    @staticmethod
    def scroll_to_text_by_android_ui_automator(text, driver):
        driver.find_element_by_android_uiautomator \
            (f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("{text}").instance(0))').click()

    @staticmethod
    def swipe_up(how_many_swipes, driver):
        for _ in range(how_many_swipes):
            driver.swipe(229, 1377, 229, 1823, 1000)

    @staticmethod
    def swipe_down(how_many_swipes, driver):
        for _ in range(how_many_swipes):
            driver.swipe(229, 1823, 229, 1377, 1000)

    @staticmethod
    def swipe_left(how_many_swipes, driver):
        for i in range(1, how_many_swipes + 1):
            driver.swipe(900, 600, 200, 600, 1000)

    @staticmethod
    def swipe_right(how_many_swipes, driver):
        for i in range(1, how_many_swipes + 1):
            driver.swipe(200, 600, 900, 600, 1000)