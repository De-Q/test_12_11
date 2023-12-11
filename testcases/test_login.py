import time
import unittest

from selenium.webdriver.common.by import By
from selenuim.day03.objectpage.login_page import LoginPage
from selenuim.day03.log.log import logger

#模块名，类名，方法名都需要以test开头命名
class TestAdminLogin:
    def test_admin(self, login):
        """
            验证有效的用户名和密码登录系统
        """
        self.driver = login
        self.login_page = LoginPage(self.driver)
        self.login_page.input_name('admin')
        self.login_page.input_password('Tu990742')
        self.login_page.click_login()

        time.sleep(4)
        assert '地盘 - 禅道' in self.driver.title  # 通过页面title判断是否登录成功
        self.login_page.logout()    #退出登录

        logger.info("有效的用户名和密码登录系统")


    # def test_none_account(self):
    #     """
    #     验证密码为空时的登录情况
    #     """
    #     time.sleep(3)
    #     self.driver.switch_to.default_content()
    #     self.driver.find_element(By.ID, 'account').send_keys('admin')
    #     self.driver.find_element(By.ID, 'submit').click()
    #     time.sleep(1)
    #     alert_log = self.driver.switch_to.alert
    #     alert_log.accept()