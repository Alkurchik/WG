from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_register_page(self):
        self.should_be_register_url()
        self.should_be_register_form()
        self.should_be_register_form()

    def should_be_register_url(self):
        assert True

    def should_be_register_form(self):
        assert True

    def should_be_register_form(self):
        assert True