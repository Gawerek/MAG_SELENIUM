from Pages.DynamicIdPage import DynamicIDPageSelenium

def test_dynamic_id_button_click(driver):
    driver.get("http://uitestingplayground.com/dynamicid")
    dynamic_id_page = DynamicIDPageSelenium(driver)
    dynamic_id_page.click_button()
    print(dynamic_id_page.get_page_title())
    assert dynamic_id_page.get_page_title() == "Dynamic ID"
