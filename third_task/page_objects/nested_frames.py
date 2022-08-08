from third_task.Base.Elements.TextField import TextField
from third_task.Base.frame import IFrame
from third_task.Base.Elements.Button import Button
from third_task.Base.BasePage import BaseForm
from third_task.resourses.utils import data
from third_task.resourses.utils import compare_text
from third_task.resourses.logger import log
import logging


class NestedFramesPage(BaseForm):
    logs = log(logging.DEBUG)
    _text_parent = TextField("//body[text()='Parent frame']", 'xpath')
    _text_child = TextField('//p[text()]', 'xpath')
    _header = TextField('//div[@class="main-header"]', 'xpath')
    _frame_parent = IFrame('//iframe[@id="frame1"]', 'xpath')
    _frame_child = IFrame('//iframe[@srcdoc="<p>Child Iframe</p>"]', 'xpath')
    _frame_button = Button("//span[@class='text' and text()='Frames']", 'xpath')

    def __init__(self):
        self._text_parent.wait_until_loaded()
        super().__init__(self._header)

    def check_nested_frames(self):
        self._frame_parent.switch_to_frame()
        parent = self._text_parent.get_text()
        self._frame_child.switch_to_frame()
        child = self._text_child.get_text()
        IFrame.switch_to_def()
        return (compare_text(parent, data['iframe_text']['parent'])
                and compare_text(child, data['iframe_text']['child']))

    def check_load(self):
        return self._header.find_element().text == 'Nested Frames'
