from Pages.DynamicIdPage import DynamicIDPageSelenium
from Pages.HomePage import HomePage
def test_dynamic_id_button_click(driver):
    home_page = HomePage(driver)
    home_page.navigate()
    home_page.click_dynamicid_link()
    dynamic_id_page = DynamicIDPageSelenium(driver)
    dynamic_id_page.click_button()
    print(dynamic_id_page.get_page_title())
    assert dynamic_id_page.get_page_title() == "Dynamic ID"
