import time
from selenium.webdriver.common.by import By


def test_carousel(firefox, screenshot_folder):
    """Dummy test used as boilerplate to validate fixtures
    Args:
        firefox (WebDriver): The webdriver being used
        screenshot_folder (str): The folder to save screenshots to
    """
    firefox.get("https://www.dispatchhealth.com/")

    time.sleep(5)

    # Find Filter - High to Low
    firefox.find_elements_by_link_text("View Filters")[0].click()

    # Select High to Low
    firefox.find_element_by_xpath("/html/body/div[2]/div[1]/main/article/div/div[7]/div/div/div/div[2]/div/div/div/div/div/div/section/section[1]/section/section/div/div/div/div/div/select/option[3]").click()

    carousel = firefox.find_element_by_xpath("//section[contains(@class, 'revwid-reviews')]")

    stop_index = 1
    for review in carousel.find_elements_by_xpath("./div[contains(@class, 'revwid-review')]"):
        assert review.find_element_by_class_name("revwid-review-rating-text").text == "5 out of 5 stars"
        if stop_index == 3:
            break
        stop_index += 1
