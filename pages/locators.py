from selenium.webdriver.common.by import By

from pages.login_page import LoginPage


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(LoginPage):
    LOGIN_URL = (By.CSS_SELECTOR, '#login_link')
    LOGIN_FORM = (By.ID, "#login_form")
    LOGIN_REGISTER_FORM = (By.ID, "#register_form")
