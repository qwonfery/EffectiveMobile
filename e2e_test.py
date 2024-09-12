import unittest

from dotenv import dotenv_values
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestPurchase(unittest.TestCase):

    def setUp(self):
        config = dotenv_values()
        self.url = config['TEST_URL']
        browser = config['BROWSER']
        match browser:
            case 'firefox':
                self.driver = webdriver.Firefox()
            case 'chrome':
                self.driver = webdriver.Chrome()
            case 'edge':
                self.driver = webdriver.Edge()
            case _:
                raise ValueError('Неподдерживаемый браузер')

    def authorization(self):
        self.driver.get(self.url)

        username_input = self.driver.find_element(By.ID, "user-name")
        password_input = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")
        login_button.click()

        self.assertEqual(self.driver.current_url, self.url + '/inventory.html')

    def choosing_item(self):
        add_to_cart_button = self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light')
        add_to_cart_button.click()

        basket_reference = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
        basket_reference.click()

        self.assertEqual(self.driver.current_url, self.url + "/cart.html")

    def purchase_confirmation(self):
        checkout_button = self.driver.find_element(By.ID, 'checkout')
        checkout_button.click()

        self.assertEqual(self.driver.current_url, self.url + "/checkout-step-one.html")

    def checkout_step_one(self):
        first_name_input = self.driver.find_element(By.ID, "first-name")
        second_name_input = self.driver.find_element(By.ID, "last-name")
        zip_input = self.driver.find_element(By.ID, "postal-code")

        first_name_input.send_keys("John")
        second_name_input.send_keys("Lennon")
        zip_input.send_keys("88005553535")

        continue_button = self.driver.find_element(By.ID, 'continue')
        continue_button.click()

        self.assertEqual(self.driver.current_url, self.url + "/checkout-step-two.html")

    def checkout_step_two(self):
        finish_button = self.driver.find_element(By.ID, "finish")
        finish_button.click()

        self.assertEqual(self.driver.current_url, self.url + "/checkout-complete.html")

    def test_purchase(self):
        self.authorization()
        self.choosing_item()
        self.purchase_confirmation()
        self.checkout_step_one()
        self.checkout_step_two()


if __name__ == '__main__':
    unittest.main()
