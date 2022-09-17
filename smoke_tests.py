from pages.main_page import MainPage

def test_autorization_with_password(browser):
    link = "https://05.ru/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.input_login_and_password()

