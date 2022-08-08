from third_task.resourses.singldriver import driver


class Browser:

    @staticmethod
    def open_page(url):
        driver.get(url)

    @staticmethod
    def get_url():
        return driver.current_url

    @staticmethod
    def go_back():
        driver.back()

    @staticmethod
    def max_screen():
        driver.fullscreen_window()

    @staticmethod
    def close():
        driver.close()

    @staticmethod
    def quit():
        driver.quit()

    @staticmethod
    def get_page():
        return driver.page_source

    @staticmethod
    def count_tabs():
        return len(driver.window_handles)

    @staticmethod
    def to_new_tab():
        driver.switch_to.window(driver.window_handles[1])

    @staticmethod
    def to_previous_tab():
        driver.switch_to.window(driver.window_handles[0])

    @staticmethod
    def close_first_tab():
        Browser.to_new_tab()
        driver.close()
        Browser.to_previous_tab()

    @staticmethod
    def scroll_down():
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    @staticmethod
    def get_tab_url():
        driver.switch_to.window(driver.window_handles[1])
        return Browser.get_url()
