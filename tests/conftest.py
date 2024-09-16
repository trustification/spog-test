import pytest
from playwright.sync_api import Page


def pytest_addoption(parser):
    parser.addoption("--username", action="store", help="Login Username")
    parser.addoption("--password", action="store", help="Login Password")


@pytest.fixture(autouse=True)
def setup_before_test(page: Page, request, base_url):
    page.goto('/', timeout=80000, wait_until="commit")
    spog_login(page, request)
    yield


def spog_login(page: Page, request):
    button = page.query_selector('button[name="Deny"]')
    if button:
        button.click()
    page.get_by_label("Username").fill(request.config.getoption("--username"), timeout=1200000)
    page.locator("#password").fill(request.config.getoption("--password"))
    page.get_by_role("button", name="Sign In").click()
    page.get_by_role("heading", name="Red Hat Trusted Profile").is_visible()
