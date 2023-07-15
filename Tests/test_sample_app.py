
from Pages.HomePage import HomePage
from Pages.SampleAppPage import SampleAppPage



def test_login(driver):
    home_page = HomePage(driver)
    home_page.navigate()
    home_page.click_sample_app_link()
    login_page = SampleAppPage(driver)
    login_page.login("test_user", "pwd")
    assert login_page.is_welcome_text_present("test_user"), "Welcome text not found or incorrect"