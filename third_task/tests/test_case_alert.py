from third_task.page_objects.main_page import MainPage
from third_task.page_objects.alerts_page import AlertsPage
from third_task.Base.Elements.Alert import Alert
from third_task.resourses.utils import data, compare_text
from third_task.resourses.utils import random_string
from third_task.resourses.conftest import pytest_sessiosstart, pytest_sessionfinish


def test_case_alert(pytest_sessiosstart, pytest_sessionfinish):
    main = MainPage()
    assert main.check_load(), 'main page not loaded'
    main.click_alerts_button()
    alert_page = AlertsPage()
    alert = Alert()
    alert_page.click_alerts_button()
    assert alert_page.check_load(), 'alerts page not loaded'
    alert_page.click_to_see_alert_button()
    first_alert_text = alert.get_text()
    assert compare_text(first_alert_text, data['alert_text']['first']), 'alert not opened'
    alert.click_alert_ok()
    assert not alert.alert_is_present(), 'alert not closed'
    alert_page.click_confirm_box_button()
    second_alert_text = alert.get_text()
    assert compare_text(second_alert_text, data['alert_text']['second']), 'alert not opened'
    alert.click_alert_ok()
    assert not alert.alert_is_present(), 'alert not closed'
    alert_page.click_promt_box_button()
    third_alert_text = alert.get_text()
    assert compare_text(third_alert_text, data['alert_text']['third']), 'alert not opened'
    rand_str = random_string
    alert.send_keys(rand_str)
    alert.click_alert_ok()
    assert not alert.alert_is_present(), 'alert not closed'
    text_rand = alert_page.get_rand_text()
    assert compare_text(data['alert_text']['fourth']+rand_str, text_rand), 'alert data not correct'

