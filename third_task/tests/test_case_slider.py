from third_task.page_objects.main_page import MainPage
from third_task.page_objects.slider_page import SliderPage
from third_task.resourses.utils import data, random_number, compare_text
from third_task.page_objects.progress_page import ProgressPage
from third_task.resourses.conftest import pytest_sessiosstart, pytest_sessionfinish


def test_case_slider(pytest_sessiosstart, pytest_sessionfinish):
    main_page = MainPage()
    assert main_page.check_load(), 'main page not load'
    main_page.click_widgets_button()
    slider_page = SliderPage()
    slider_page.click_slider()
    assert slider_page.check_load(), 'slider page not load'
    slider_page.slider_new_value(random_number)
    current_value = slider_page.get_input_value()
    assert compare_text(current_value, random_number), 'sliders value correct'
    slider_page.click_progress_button()
    progress_page = ProgressPage()
    assert progress_page.check_load(), 'progress page loaded'
    progress_page.click_start_until_age(data['test_data']['my_age'])
    progress_value = progress_page.get_progress_value()
    assert compare_text(progress_value, data['test_data']['my_age']), 'progress data correct'
