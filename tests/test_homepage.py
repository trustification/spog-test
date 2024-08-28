import re

from playwright.sync_api import Page

def test_search_sbom(page: Page):
    page.get_by_placeholder("Search for an SBOM, advisory").fill("quarkus")
    page.locator("#search").click()
