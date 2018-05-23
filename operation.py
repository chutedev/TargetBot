from selenium import webdriver
import time
from basic2 import fullname, usphone, email, addy1, addy2, zip, card, cvv, exp


path = '/Users/gavinnewcomer/PycharmProjects/basic/venv/lib/python3.7/site-packages/chromedriver_binary/chromedriver'
checkout_bypass = 'https://www.target.com/co-deliverymethod'


class Targetbot:

    def __init__(self, fullname, usphone, email, addy1, addy2, zip, card, cvv, exp):
        self.fullname = fullname
        self.usphone = usphone
        self.email = email
        self.addy1 = addy1
        self.addy2 = addy2
        self.zip = zip
        self.card = card
        self.cvv = cvv
        self.exp = exp
        self.checkout_bypass = 'https://www.target.com/co-deliverymethod'
        self.link = 'https://www.target.com/p/pop-star-wars-tlj-10-porg/-/A-53224691'

    def operation(self):
        driver = webdriver.Chrome(path)
        driver.get(self.link)

        add_to_cart = driver.find_element_by_css_selector(".iIlUzD")
        add_to_cart.click()
        time.sleep(1.5)
        driver.get(self.checkout_bypass)

        time.sleep(4)
        email_input = driver.find_element_by_id('trackingEmail')
        email_input.click()
        email_input.send_keys(self.email)

        time.sleep(2)
        proceed2_button = driver.find_element_by_xpath("//button[@class='Button-s1all4g7-0 dCkCUP']")
        proceed2_button.click()

        time.sleep(1.5)
        fullname_input = driver.find_element_by_id('fullName')
        fullname_input.click()
        fullname_input.send_keys(self.fullname)

        add_line1_input = driver.find_element_by_id('line1')
        add_line1_input.click()
        add_line1_input.send_keys(self.addy1)

        add_2_button = driver.find_element_by_xpath("//a[@name='line2']")
        add_2_button.click()

        add_line2_input = driver.find_element_by_id('line2')
        add_line2_input.click()
        add_line2_input.send_keys(self.addy2)

        zip_input = driver.find_element_by_id('zipCode')
        zip_input.click()
        zip_input.send_keys(self.zip)

        phone_input = driver.find_element_by_id('USPhone')
        phone_input.click()
        phone_input.send_keys(self.usphone)

        time.sleep(2)
        proceed3_button = driver.find_element_by_xpath("//div[@class='h-display-flex h-margin-t-default']/button")
        proceed3_button.click()
        time.sleep(2)
        '''
        proceed4_button = driver.find_element_by_xpath("//button[@class='Button-s1all4g7-0 DWNOX']")
        proceed4_button.click()
        '''
        credit_card_input = driver.find_element_by_id('creditCardInput-cardNumber')
        credit_card_input.click()
        credit_card_input.send_keys(self.card)

        expiration_input = driver.find_element_by_id('creditCardInput-expiration')
        expiration_input.click()
        expiration_input.send_keys(self.exp)

        sec_code_input = driver.find_element_by_id('creditCardInput-cvv')
        sec_code_input.click()
        sec_code_input.send_keys(self.cvv)

        card_name_input = driver.find_element_by_id('creditCardInput-cardName')
        card_name_input.click()
        card_name_input.send_keys(self.fullname)

        review_button = driver.find_element_by_xpath("//button[@class='Button-s1all4g7-0 dCkCUP']")
        review_button.click()

        time.sleep(2)
        checkout_button = driver.find_element_by_xpath("//button[@class='Button-s1all4g7-0 dCkCUP']")
        checkout_button.click()

        time.sleep(10)

x = Targetbot(fullname, usphone, email, addy1, addy2, zip, card, cvv, exp)
x.operation()