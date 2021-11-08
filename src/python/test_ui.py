"""Demo test."""
import time

from selenium.webdriver.common.by import By

def test_ui(baseurl, firefox, screenshot_folder):
    """Dummy test used as boilerplate to validate fixtures
    Args:
        firefox (WebDriver): The webdriver being used
        screenshot_folder (str): The folder to save screenshots to
    """

    firefox.get(baseurl)

    # This is a nono, better to replace with waiting/polling mechanism
    # acceptable for demoing
    time.sleep(2)
    wc_cards = firefox.find_elements(By.XPATH, '//div[contains(@class, "wc-card")]')

    # There should only be 2 cards for the Warchest demo
    assert len(wc_cards) == 2

    # make sure we have 2 v-chips (for profit and investment)
    vchips = wc_cards[0].find_elements(By.XPATH, '//div[contains(@class, "row")]//span[contains(@class, "v-chip__content")]')
    assert len(vchips) == 4

    # Each vchip should have an icon, check for that
    for vchip in vchips:
        assert vchip.find_elements(By.XPATH, '//i[contains(@class, "v-icon")]'), f"Missing icon for:\n{vchip.get_attribute('innerHTML')}"

    print(f"Saving screenshot to: {screenshot_folder}")
    firefox.save_screenshot(f"{screenshot_folder}/landing_page.png")
