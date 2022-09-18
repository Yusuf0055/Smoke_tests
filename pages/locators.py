from selenium.webdriver.common.by import By



class AutorizationOrRegLocators():
    log_or_reg = (By.CSS_SELECTOR, "[data-e2e=\"autorization\"].link")  #Кнопка вход или регистрация
    input_phone = (By.CSS_SELECTOR,  "[type=\"tel\"].text-input__input")  #Ввод телефона для получения кода
    get_code = (By.CSS_SELECTOR,  "button.button_icon-left.button_red.button_h-39")  #Кнопка получения кода
    input_code = (By.CSS_SELECTOR,  "[placeholder=\"12 - 34\"].input-code__input")  #Ввод кода
    login_with_password = (By.CSS_SELECTOR,  "div.link.link_black.link_wu.auth-modal__footer-link")  #Кнопка вход с исп. пароля
    mail_or_phone = (By.CSS_SELECTOR,  "[type=\"text\"].text-input__input")  #Ввод почты или телефона для входа с паролем
    password = (By.CSS_SELECTOR,  "[type=\"password\"].text-input__input")  #Ввод пароля для входа
    login = (By.CSS_SELECTOR,  "button.button_icon-left.button_red.button_h-39.button.button_fluid")  #Кнопка войти


class BasketLocators():
    main_basket_link = (By.CSS_SELECTOR, "[href=\"/cart/\"].user-panel__el")
    add_to_basket = (By.CSS_SELECTOR, ".product-page__sidebar-content .add-to-cart__btn.mb-9.button_icon-left.button_red")
