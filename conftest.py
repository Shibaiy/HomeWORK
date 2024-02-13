from selene import browser
import pytest


@pytest.fixture
def browser_chrome():
    chrome = browser

    chrome.config.window_width = 1080
    chrome.config.window_height = 800

    chrome.open('https://google.com')

    yield chrome

    chrome.quit()
