from third_task.resourses.utils import data


class User:
    def __init__(self, user_n):
        d = data['users_data'][str(user_n)]
        self.name = d['name']
        self.surname = d['surname']
        self.email = d['email']
        self.age = d['age']
        self.salary = d['salary']
        self.dep = d['department']

    def get_data(self):
        return [self.name, self.surname, self.email, self.age, self.salary, self.dep]