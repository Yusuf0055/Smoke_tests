from selenium.common.exceptions import NoSuchElementException


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(10)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def clicked(self, how, what):
        try:
            element = self.browser.find_element(how, what)
            element.click()
        except (NoSuchElementException):
            return False
        return True

