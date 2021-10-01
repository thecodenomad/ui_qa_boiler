"""Dummy test to prove out docker container."""


def test_dummy(firefox, screenshot_folder):
    """Dummy test used as boilerplate to validate fixtures
    Args:
        firefox (WebDriver): The webdriver being used
        screenshot_folder (str): The folder to save screenshots to
    """

    firefox.get("http://www.google.com")
    print(f"Saving screenshot to: {screenshot_folder}")
    firefox.save_screenshot(f"{screenshot_folder}/google.png")
