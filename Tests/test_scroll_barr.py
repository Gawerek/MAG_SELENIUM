import time

from Pages.HomePage import HomePage
from Pages.ScrollBarsPage import ScrollbarsPage



def test_scrollbars_page(driver):
    home_page = HomePage(driver)
    home_page.navigate()
    home_page.click_scroll_barr_link()
    scrollbars_page = ScrollbarsPage(driver)
    scrollbars_page.scroll_to_button_and_click()
