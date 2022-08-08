from third_task.Base.BaseElement import BaseElement
from third_task.resourses.utils import get_nums_without_proc


class ProgressBar(BaseElement):

    def get_value(self):
        text = self.find_element().text
        return get_nums_without_proc(text)

