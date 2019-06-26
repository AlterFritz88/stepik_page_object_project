from .base_page import BasePage
from .locators import CartPageLocators



class CartPage(BasePage):
    def the_cart_is_empty_message(self):
        assert 'Your basket is empty' in self.browser.find_element(*CartPageLocators.EMPTY_MES).text

    def the_cart_is_empty(self):
        self.is_not_element_present(*CartPageLocators.CART)