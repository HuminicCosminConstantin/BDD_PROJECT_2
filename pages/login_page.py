from selenium.webdriver.common.by import By

from base_page import BasePage

class LoginPage(BasePage):
    LOGIN_PAGE_URL = f'https://demo.nopcommerce.com/login'
    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    LOGIN_BTN = (By.XPATH, "//button[@class='button-1 login-button']")
    MAIN_ERROR =(By.XPATH, "//div[@class='message-error validation-summary-errors']")

# Scenario 1
    def navigate_to_login_page(self):
        self.browser.get(self.LOGIN_PAGE_URL)

    def insert_email(self, email):
        self.insert(locator=self.EMAIL, text=email)

    def insert_any_password(self):
        self.insert(locator=self.PASSWORD, text="Password")

    def click_login_button(self):
        self.click(locator=self.LOGIN_BTN)

    def main_error_is_displayed(self):
        assert self.is_displayed(locator=self.MAIN_ERROR)


# Scenario 2
#     def no_insert_email(self):
#         email = self.browser.find_element(*self.EMAIL)
#         email.send_keys("Email")
#
#     def insert_any_password(self):
#         password = self.browser.find_element(*self.PASSWORD)
#         password.send_keys("Password")

