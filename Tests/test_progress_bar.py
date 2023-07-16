
from Pages.HomePage import HomePage
from Pages.ProgressBar import ProgressBarPage

def test_progress_bar(driver):
    home_page = HomePage(driver)
    home_page.navigate()
    home_page.click_progress_bar_link()
    progress_bar_page = ProgressBarPage(driver)
    progress_bar_page.click_start_button()
    progress_bar_page.click_stop_button_when_progress_reaches(75)