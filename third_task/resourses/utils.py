import json
import random
import string

with open("..//resourses//config.json") as file:
    data = json.load(file)


def rand_num_1_100():
    return random.randint(1, 100)


def compare_text(real_text, text):
    return str(real_text) == str(text)


def generate_random_string(length=random.randint(10, 20)):
    letters = string.ascii_lowercase
    b = ''.join(random.choice(letters) for i in range(length))
    return b


def get_nums_without_proc(text):
    if len(text) == 2:
        return int(text[0])
    if len(text) == 3:
        return int(text[0:2])
    if len(text) == 4:
        return int(text[0:3])


random_string = generate_random_string()
random_number = rand_num_1_100()
