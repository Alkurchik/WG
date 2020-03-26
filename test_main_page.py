from .pages.main_page import MainPage
from .pages.login_page import LoginPage

def test_guest_can_go_to_register_page(browser):
    link = "http://automationpractice.com/index.php?controller=authentication&back=my-account"
    page = MainPage(browser, link)
    page.open()
    page.go_to_register_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_register_page()