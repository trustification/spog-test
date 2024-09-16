import pytest
from playwright.sync_api import Page,expect
from fixtures.upload import * 

@pytest.fixture(scope="function", autouse=True)
def before_each(page: Page):
    # User navigation to Upload an SBOM page
    page.get_by_text("Upload SBOM").click(timeout=1200000) 
    yield   
    
def test_verify_sbom_upload(page: Page):
    verify_upload(page,"SBOM","syft.cyclonedx.json") 
