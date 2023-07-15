
from Pages.HomePage import HomePage
from Pages.VerifyTextPage import VerifyTextPage

def test_welcome_text(driver):
    home_page = HomePage(driver)
    home_page.navigate()
    home_page.click_verify_text_link()
    verify_text_page = VerifyTextPage(driver)
    assert verify_text_page.is_welcome_text_present(), f"Welcome text not found in text: {verify_text_page.welcome_text_element.text}"
