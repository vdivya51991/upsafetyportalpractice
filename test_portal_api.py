import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def playwright_context():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        yield context
        browser.close()


def test_get_api_request(playwright_context):
    response = playwright_context.request.get("https://automationexercise.com/api/brandsList")

    assert response.status == 200






