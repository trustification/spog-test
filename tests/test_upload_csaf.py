import pytest
from playwright.sync_api import Page,expect
from fixtures.upload import * 

@pytest.fixture(scope="function", autouse=True)
def before_each(page: Page):
    # User navigation to Upload a CSAF page
    page.get_by_text("Upload CSAF").click(timeout=1200000) 
    yield   
    
def test_verify_csaf_upload(page: Page):
    verify_upload(page,"CSAF","valid.json") 

