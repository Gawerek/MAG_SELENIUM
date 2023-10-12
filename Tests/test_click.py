from Pages.HomePage import HomePage
from Pages.ClickPage import ClickPage
def test_click(driver):
    home_page= HomePage(driver)
    home_page.navigate()
    home_page.click_click_link()
    click_page = ClickPage(driver)
    click_page.click_bad_button()
    assert click_page.is_button_green(), "Button did not turn green!"


