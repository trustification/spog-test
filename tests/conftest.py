import pytest
from playwright.sync_api import Page


def pytest_addoption(parser):
    parser.addoption("--application", action="store", help="Application URL")
    parser.addoption("--username", action="store", help="Login Username")
    parser.addoption("--password", action="store", help="Login Password")


@pytest.fixture(autouse=True)
def setup_before_test(page: Page, request):
    page.goto(request.config.getoption("--application"))
    spog_login(page, request)
    yield


def spog_login(page: Page, request):
    if page.get_by_role("heading", name="Tracking consent").is_visible:
        page.get_by_role("button", name="Deny").click()
    page.get_by_label("Username").fill(request.config.getoption("--username"))
    page.get_by_label("Password").fill(request.config.getoption("--password"))
    page.get_by_role("button", name="Sign In").click()
    page.get_by_role("heading", name="Red Hat Trusted Profile").is_visible()
