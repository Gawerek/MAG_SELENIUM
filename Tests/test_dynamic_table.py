from Pages.HomePage import HomePage
from Pages.DynamicTablePage import DynamicTablePage

def test_dynamic_table(driver):
    home_page = HomePage(driver)
    home_page.navigate()
    home_page.click_dynamic_table_link()
    dynamic_table_page = DynamicTablePage(driver)
    assert dynamic_table_page.get_chrome_cpu_load() == dynamic_table_page.get_chrome_cpu_label(), "Chrome CPU load in the table and the label do not match"