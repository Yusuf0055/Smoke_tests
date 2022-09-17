from .base_page import BasePage
from .locators import AutorizationOrRegLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*AutorizationOrRegLocators.log_or_reg)
        login_link.click()

    def input_login_and_password(self):
        log_w_pass = self.browser.find_element(*AutorizationOrRegLocators.login_with_password)
        log_w_pass.click()
        m_or_p = self.browser.find_element(*AutorizationOrRegLocators.mail_or_phone)
        m_or_p.send_keys("79282865866")
        paswrd = self.browser.find_element(*AutorizationOrRegLocators.password)
        paswrd.send_keys("bM1}9Z:C")
        log = self.browser.find_element(*AutorizationOrRegLocators.login)
        log.click()



