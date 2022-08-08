from third_task.page_objects.main_page import MainPage
from third_task.page_objects.alerts_page import AlertsPage
from third_task.resourses.utils import compare_text
from third_task.page_objects.nested_frames import NestedFramesPage
from third_task.page_objects.frames_page import FramePage
from third_task.resourses.conftest import pytest_sessiosstart, pytest_sessionfinish


def test_case_frames(pytest_sessiosstart, pytest_sessionfinish):
    main_page = MainPage()
    assert main_page.check_load(), 'main page loaded'
    main_page.click_alerts_button()
    alert_page = AlertsPage()
    alert_page.click_nested_frames_button()
    nested_page = NestedFramesPage()
    assert nested_page.check_load(), 'nested frames page loaded'
    assert nested_page.check_nested_frames(), 'frames content correct'
    alert_page.click_frames_button()
    frame_page = FramePage()
    assert frame_page.check_load(), 'frames page loaded'
    first_frame_text = frame_page.first_frame_string()
    second_frame_text = frame_page.second_frame_string()
    assert compare_text(first_frame_text, second_frame_text), 'strings if frames correct'

