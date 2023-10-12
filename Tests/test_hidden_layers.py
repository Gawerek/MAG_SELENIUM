from Pages.HomePage import HomePage
from Pages.HiddenLayersPage import HiddenLayersPage

def test_hidden_layers(driver):
    home_page=HomePage(driver)
    home_page.navigate()
    home_page.click_hiddenlayers_link()
    page = HiddenLayersPage(driver)
    page.click_green_button()
    try:
        page.is_green_button_clickable()
        assert False, "The green button is clickable after the first click, which it shouldn't be."
    except:
        assert True