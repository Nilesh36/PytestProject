
import allure

from PytestFramework.Config.config import TestData
from PytestFramework.Pages.Random_Info import Random_Data
from PytestFramework.Pages.SignUpPage import SignupPage
from PytestFramework.Tests_Suits.test_base import BaseTest
from PytestFramework.Pages.Subscription import Subscription


class Test_Suits(BaseTest):

    @allure.description("Sign up page title verification Scenario")
    @allure.step("Sign Up Page title Verification")
    def test_page_title(self):
        self.signuppage = SignupPage(self.driver)
        title = self.signuppage.get_page_title(TestData.SignUp_Page_title)
        assert title == TestData.SignUp_Page_title

    @allure.description("Sign Up Scenario")
    @allure.step("Sign Up Test")
    def test_signup(self):
        self.signuppage = SignupPage(self.driver)
        self.signuppage.do_signup(Random_Data.name_generated, Random_Data.email_generated,
                                  "Ultra@9809")
        title = self.signuppage.get_page_title(TestData.Dashboard_Page_title)
        assert title == TestData.Dashboard_Page_title

    @allure.description("Verify the User is able to take Subscription ")
    @allure.step("Subscription Test")
    def test_subscription(self):
        self.subscription = Subscription(self.driver)
        self.subscription.take_subscription(Random_Data.card_number,Random_Data.expiry_date, Random_Data.cvc_number, Random_Data.name_generated)
        title = self.subscription.get_title(TestData.Content_idea_title)
        assert title == TestData.Content_idea_title
        print("Subscription taken successful")

    @allure.description("Verify User is able to search the Content")
    @allure.step("Content Search Test")
    def test_content_search(self):
        self.subscription = Subscription(self.driver)
        self.subscription.search_content_ideas(TestData.Keyword, TestData.Audience)

