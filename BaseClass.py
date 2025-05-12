import pytest
from playwright.sync_api import sync_playwright

class BaseTest:
    @pytest.fixture(scope="session")
    def browser(self):
        """Launch the browser once per test session."""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)  # Set headless=True for headless mode
            yield browser
            browser.close()

    @pytest.fixture(scope="function")
    def page(self, browser):
        """Create a new page for each test."""
        page = browser.new_page()
        yield page
        page.close()

    @pytest.fixture(scope="function")
    def context(self, browser):
        """Create a new context for each test (optional)."""
        context = browser.new_context()
        yield context
        context.close()
