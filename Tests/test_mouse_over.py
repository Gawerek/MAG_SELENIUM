from Pages.HomePage import HomePage
from Pages.MouseOverPage import MouseOverPage


def test_mouse_over(driver):
    home_page = HomePage(driver)
    home_page.navigate()
    home_page.click_mouse_over_link()
    mouse_over_page = MouseOverPage(driver)
    mouse_over_page.click_link_twice()
    assert mouse_over_page.get_click_count() == 2, "Click count did not increase by 2"