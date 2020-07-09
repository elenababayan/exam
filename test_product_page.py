from pages.product_page import ProductPage


def test_should_be_add_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_button()
    page.solve_quiz_and_get_code()

