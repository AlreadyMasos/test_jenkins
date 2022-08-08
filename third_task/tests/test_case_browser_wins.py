from third_task.page_objects.handles_page import HandlePage
from third_task.resourses.browser_manager import Browser
from third_task.page_objects.main_page import MainPage
from third_task.page_objects.links_page import LinksPage
from third_task.resourses.conftest import pytest_sessiosstart, pytest_sessionfinish


def test_case_browser_wins(pytest_sessiosstart, pytest_sessionfinish):
    main_page = MainPage()
    assert main_page.check_load(), 'main page not loaded'
    main_page.click_alerts_button()
    hand_page = HandlePage()
    assert hand_page.check_load(), 'handlers page not loaded'
    hand_page.browser_win_click()
    hand_page.click_new_tab_button()
    assert hand_page.check_new_tab(), 'sample tab not correct'
    Browser.close_first_tab()
    assert hand_page.check_load(), 'handlers page not loaded'
    hand_page.links_button_click()
    link_page = LinksPage()
    assert link_page.check_load(), 'link page not loaded'
    link_page.home_link_click()
    assert main_page.check_load(), 'main page not loaded'
    Browser.to_previous_tab()
    assert link_page.check_load(), 'link page not loaded'
