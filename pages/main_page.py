from .base_page import BasePage
from .locators import AutorizationOrRegLocators
from .locators import BasketLocators

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


    def go_to_basket_page(self):
        assert self.clicked(*BasketLocators.main_basket_link), "Кнопка корзина не работает"

    def should_be_basket_url(self):
        assert "cart" in self.browser.current_url, "cart отсутствует в адресе страницы"

    def add_to_cart(self):
        self.clicked(*BasketLocators.add_to_basket)



