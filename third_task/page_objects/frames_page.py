from third_task.Base.BasePage import BaseForm
from third_task.Base.Elements.TextField import TextField
from third_task.Base.frame import IFrame
from third_task.resourses.utils import compare_text
from third_task.resourses.logger import log
import logging


class FramePage(BaseForm):
    logs = log(logging.DEBUG)
    _first_frame = IFrame('//iframe[@id="frame1"]', 'xpath')
    _second_frame = IFrame('//iframe[@id="frame2"]', 'xpath')
    _first_frame_text = TextField('//h1[@id="sampleHeading"]', 'xpath')
    _second_frame_text = TextField('//h1[@id="sampleHeading"]', 'xpath')

    def __init__(self):
        super().__init__(self._first_frame)

    def first_frame_string(self):
        self._first_frame.switch_to_frame()
        text1 = self._first_frame_text.get_text()
        self._first_frame.switch_to_def()
        return text1

    def second_frame_string(self):
        self._second_frame.switch_to_frame()
        text2 = self._second_frame_text.get_text()
        self._second_frame.switch_to_def()
        return text2
