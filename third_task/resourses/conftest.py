import pytest
from third_task.resourses.browser_manager import Browser
from third_task.resourses.utils import data


@pytest.fixture(scope='session')
def pytest_sessiosstart():
    Browser.open_page(data['links']['main_page'])
    Browser.max_screen()


@pytest.fixture(scope='session')
def pytest_sessionfinish(request):
    def quit():
        Browser.quit()
    request.addfinalizer(quit)

