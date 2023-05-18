import time
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from PytestFramework.Pages.BasePage import BasePage


class Subscription(BasePage):
    """By locators"""
    skip_btn = (By.XPATH, "//button[normalize-space()='Skip']")
    monthly_tab = (By.XPATH, "//div[text() = 'Monthly']")
    card_number_field = (By.XPATH, "//input[@id='cardNumber']")
    expiry_date_field = (By.XPATH, "//input[@id='cardExpiry']")
    cvc_number_field = (By.XPATH, "//input[@id='cardCvc']")
    name_on_card_field = (By.XPATH, "//input[@id='billingName']")
    subscribe_btn = (By.XPATH, "//div[@class='SubmitButton-IconContainer']")
    start_creating_content_btn = (By.XPATH, "//button[normalize-space()='Start Creating Content']")
    enter_keyword_field = (By.XPATH, "//input[@name='keywords']")
    enter_audience_field = (By.XPATH, "//input[@name='audience']")
    get_ideas_btn = (By.XPATH, "//span[normalize-space()='GET IDEAS']")

    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)

    """This method Verify the Page title"""
    def get_page_title(self, title):
        return self.get_title(title)

    """This Method Verify that User is able to take the Subscription"""
    def take_subscription(self, card_no, exp_date, cvc_no, cardholder_name):
        self.do_click(self.skip_btn)
        print("Clicked on the Skip button")
        time.sleep(2)

        # Find the element that contains the shadow root
        container_element = self.driver.find_element(By.CSS_SELECTOR,
                                                     "#kt_app_content > div > div > div > stripe-pricing-table")

        # Retrieve the shadow root using JavaScript
        shadow_root = self.driver.execute_script("return arguments[0].shadowRoot", container_element)

        # Find the iframe within the shadow root
        iframe_element = shadow_root.find_element(By.CSS_SELECTOR, "iframe")

        # Switch to the iframe
        self.driver.switch_to.frame(iframe_element)

        # Find the element within the iframe
        wait = WebDriverWait(self.driver, 10)
        inner_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                   "#root > div > div > div.PricingTable-grid > div > "
                                                                   "div > "
                                                                   "div.PriceColumn-priceAndButton.flex-container"
                                                                   ".direction-column > button > div")))

        # Interact with the inner element
        inner_element.click()

        self.do_send_input(self.card_number_field, card_no)
        print("Entered Card number")

        self.do_send_input(self.expiry_date_field, exp_date)
        print("Entered Expiry date")

        self.do_send_input(self.cvc_number_field, cvc_no)
        print("Entered CVC number")

        self.do_send_input(self.name_on_card_field, cardholder_name)
        print("Entered Name on the card")

        self.do_click(self.subscribe_btn)
        print("Clicked Subscribe button")
        time.sleep(2)

        # alert = self.driver.switch_to.alert  # Switch the focus to the alert
        # alert.accept()

    """This method Verify that the user is able to Search the content ideas"""
    def search_content_ideas(self, keyword_text, audience_text):
        self.do_click(self.start_creating_content_btn)
        print("Clicked Start creating content button")

        self.do_send_input(self.enter_keyword_field, keyword_text)
        print("Entered Keyword or Services offered")

        self.do_send_input(self.enter_audience_field, audience_text)
        print("Entered Audience")

        self.do_click(self.get_ideas_btn)
        print("Clicked Get Ideas button")
        time.sleep(3)

        print("Content search successfully")
