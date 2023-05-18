import time

from PytestFramework.Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class SignupPage(BasePage):
    """By locators"""
    # start_for_free_btn = (By.XPATH, "//a[@class='white-button w-button']")
    name_field = (By.ID, "name")
    email_field = (By.ID, "email")
    password_field = (By.ID, "password")
    confirm_password_field = (By.ID, "password_confirmation")
    sign_up_btn = (By.XPATH, "//span[text() = 'Sign up']")
    registration_successful = (By.XPATH, "//div[text() = 'Registration Successful']")

    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)

    """Page Actions for Sign Up Page"""

    """This method Verify the Page title of the Page"""
    def get_page_title(self, title):
        return self.get_title(title)

    """This method Verify the sign button is Visible"""
    def is_signup_btn_exist(self):
        return self.is_visible(self.sign_up_btn)

    """This method Verify the User is able to Sign Up"""
    def do_signup(self, name, email, password):
        self.do_send_input(self.name_field, name)
        print("Entered name")

        self.do_send_input(self.email_field, email)
        print("Entered email address")

        self.do_send_input(self.password_field, password)
        print("Entered Password")

        self.do_send_input(self.confirm_password_field, password)
        print("Entered Confirmed Password")

        self.do_click(self.sign_up_btn)
        print("Sign Up button clicked")
        time.sleep(3)
