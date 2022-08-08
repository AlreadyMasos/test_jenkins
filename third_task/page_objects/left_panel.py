from third_task.Base.Elements.Button import Button
from third_task.Base.BasePage import BaseForm
from third_task.resourses.browser_manager import Browser


class LeftPanel(BaseForm):

    _nested_frames_button = Button("//span[@class='text' and text()='Nested Frames']", 'xpath')
    _frames_button = Button("//span[@class='text' and text()='Frames']", 'xpath')
    _alerts_button = Button('//span[contains(text(),"Alerts")]', 'xpath')
    _elements_button = Button("//div[@class='element-group'][1]", 'xpath')
    _afw_button = Button("//div[@class='element-group'][3]", 'xpath')
    _web_tables_button = Button("//span[text()='Web Tables']", "xpath")
    _slider_button = Button('//span[contains(text(),"Slider")]', 'xpath')
    _progress_button = Button('//span[contains(text(),"Progress Bar")]', 'xpath')

    def __init__(self):
        super().__init__(self._elements_button)

    def click_nested_frames_button(self):
        Browser.scroll_down()
        self._nested_frames_button.element_click()

    def alerts_button_click(self):
        self._alerts_button.element_click()

    def afw_button_click(self):
        self._afw_button.element_click()

    def tables_button_click(self):
        self._web_tables_button.element_click()

    def click_frames_button(self):
        self._frames_button.element_click()

    def click_slider_button(self):
        Browser.scroll_down()
        self._slider_button.element_click()

    def click_progress_button(self):
        Browser.scroll_down()
        self._progress_button.element_click()