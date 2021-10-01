import os

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope='session')
def screenshot_folder():
    base_folder = "./screenshots"
    if os.path.exists("/.dockerenv"):
        base_folder = "/code/screenshots"

    yield base_folder

    # Handle any additional teardown/cleanup here


@pytest.fixture(scope='session')
def firefox_options():
    """Provides a way to modify firefox webdriver options. """
    options = Options()

    if os.environ.get("HEADLESS") and os.environ.get("HEADLESS").lower() == "true":
        options.headless = True

    yield options

    # Handle any additional teardown/cleanup here


@pytest.fixture(scope='session')
def firefox(firefox_options):
    """Spins up a firefox webdriver instance. """
    browser = webdriver.Firefox(options=firefox_options)

    yield browser

    # Handle any additional teardown/cleanup here
    if os.environ.get("TEARDOWN") and os.environ["TEARDOWN"].lower() == "true":
        browser.close()
