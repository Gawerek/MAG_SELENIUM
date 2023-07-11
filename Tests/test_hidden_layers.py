
from common import BasePage
from Pages.HiddenLayersPage import HiddenLayersPage

def test_hidden_layers(driver):
    base_page = BasePage(driver)
    page = HiddenLayersPage(driver)
    page.navigate()
    page.click_green_button()
    try:
        page.is_green_button_clickable()
        assert False, "The green button is clickable after the first click, which it shouldn't be."
    except:
        assert True