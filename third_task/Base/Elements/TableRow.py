from third_task.Base.BaseElement import BaseElement


class TableRow(BaseElement):

    def return_all(self):
        data_list = []
        for i in self.find_elements():
            if len(i.text) != 0:
                data_list.append(i.text)

        return data_list
