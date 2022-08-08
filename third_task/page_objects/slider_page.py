from third_task.Base.Elements.Slider import Slider
from third_task.Base.BasePage import BaseForm
from third_task.page_objects.left_panel import LeftPanel
from third_task.Base.Elements.Input import Input


class SliderPage(BaseForm):

    _left_panel = LeftPanel()
    _slider = Slider("//input[@type='range']", 'xpath')
    _input_text = Input('//input[@id="sliderValue"]', 'xpath')

    def __init__(self):
        super().__init__(self._slider)

    def click_slider(self):
        self._left_panel.click_slider_button()

    def slider_new_value(self, value):
        self._slider.wait_until_loaded()
        self._slider.change_value(value)

    def get_input_value(self):
        return self._input_text.get_value()

    def click_progress_button(self):
        self._left_panel.click_progress_button()