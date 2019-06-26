import re

from .base_page import BasePage
from .locators import ProductPageLocators


import time

class ProductPage(BasePage):


    def is_button_to_cart_present(self):
        assert self.is_element_present(*ProductPageLocators.TO_CART), "Button 'to_cart' is not presented"


    def product_to_cart(self):
        to_cart_button = self.browser.find_element(*ProductPageLocators.TO_CART)

        initial_account = self.browser.find_element(*ProductPageLocators.NOW_CART_PRICE).text
        initial_account = float(re.findall(r'\d+.\d+', initial_account)[0].replace(',', '.'))


        comodity_price = self.browser.find_element(*ProductPageLocators.COMODITY_PRICE).text
        comodity_price = float(re.findall(r'\d+.\d+', comodity_price)[0].replace(',', '.'))


        to_cart_button.click()
        self.solve_quiz_and_get_code()
        time.sleep(2)
        final_account = self.browser.find_element(*ProductPageLocators.NOW_CART_PRICE).text
        final_account = float(re.findall(r'\d+.\d+', final_account)[0].replace(',', '.'))

        final_info = self.browser.find_element(*ProductPageLocators.PRODUCT_INFO).text
        assert final_info == 'Coders at Work'

        print(final_account, initial_account, comodity_price)
        assert final_account == initial_account + comodity_price, "The comodity did not append to cart"