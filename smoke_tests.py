from pages.main_page import MainPage

def test_autorization_with_password(browser):
    link = "https://05.ru/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.input_login_and_password()


def test_basket(browser):
    link = "https://05.ru/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_basket_url()

def test_add_to_cart(browser):
    link = "https://05.ru/catalog/portativ/phones/189741/"
    page = MainPage(browser, link)
    page.open()
    page.add_to_cart()
    page.go_to_basket_page()

