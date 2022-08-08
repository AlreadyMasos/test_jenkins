from third_task.Base.BasePage import BaseForm
from third_task.Base.Elements.Button import Button
from third_task.Base.Elements.ProgressBar import ProgressBar


class ProgressPage(BaseForm):

    _startstop_button = Button('//button[@id]', 'xpath')
    _progress_bar = ProgressBar('//div[@role="progressbar"]', 'xpath')

    def __init__(self):
        super().__init__(self._startstop_button)

    def click_start_until_age(self, age):
        self._startstop_button.element_click()
        while self._progress_bar.get_value() != int(age):
            if self._progress_bar.get_value() == 0:
                break
        self._startstop_button.element_click()

    def get_progress_value(self):
        return self._progress_bar.get_value()