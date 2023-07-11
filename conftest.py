import pytest
from selenium import webdriver
from Pages.DynamicIdPage import DynamicIDPageSelenium


def pytest_addoption(parser):
    """Dodanie dodatkowych argumentów wywołania."""
    parser.addoption(
        "--no-headless", action="store_true", default=False, help="Do not use Chrome headless mode. Default: False."
    )
    parser.addoption(
        "--webdriver-path", action="store",
        help="Path to a webdriver. If not given, it is assumed it is in the $PATH. Overrides --no-default-path"
    )
    parser.addoption("--Dkey", action="store",
                     help="Master password for central en/decryption")




@pytest.fixture(scope="module")
def driver(request):
    """Selenium WebDriver configuration."""

    driver_options = webdriver.ChromeOptions()

    # Add Chrome options
    driver_options.add_argument("--enable-automation")
    driver_options.add_argument("--disable-browser-side-navigation")
    driver_options.add_argument("--disable-dev-shm-usage")
    driver_options.add_argument("--disable-gpu")
    driver_options.add_argument("--disable-infobars")
    driver_options.add_argument("--lang=pl")
    driver_options.add_argument("--no-sandbox")
    if not request.config.getoption("--no-headless"):
        driver_options.add_argument("--headless=chrome")

    # Get the webdriver_path from pytest.ini, if specified
    webdriver_path = request.config.getoption("--webdriver-path")
    if webdriver_path:
        driver_instance = webdriver.Chrome(options=driver_options)


    else:
        driver_instance = webdriver.Chrome(options=driver_options)

    # Set the window size
    driver_instance.set_window_size(1920, 1080)

    yield driver_instance

    # Clean up
    driver_instance.quit()
