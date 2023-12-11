from selenium.webdriver.common.by import By
import time

class LoginPage:
    def __init__(self, driver):
        self.account_elem = By.ID, 'account'
        self.password = By.NAME, 'password'
        self.login_elem = By.ID, 'submit'
        self.user_login_elem = By.XPATH, '//li[@id="userDropDownMenu"]/a'
        self.logout_elem = By.XPATH, '//li[@id="userDropDownMenu"]/ul[1]/li[15]/a'
        self.driver = driver

    def input_name(self, username):
        self.driver.find_element(*self.account_elem).send_keys(username)

    def input_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_elem).click()

    def logout(self):
        self.driver.switch_to.frame("appIframe-my")
        self.driver.find_element(*self.user_login_elem).click()
        time.sleep(1)
        self.driver.find_element(*self.logout_elem).click()

