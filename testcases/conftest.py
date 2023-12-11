import pytest
from selenium.webdriver.edge.service import Service
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenuim.day05.pytest_framework.config.config import chandao_url

# fixture为session级别是可以跨.py模块调用的,也就是当我们有多个.py文件的用例时候，
# 如果多个用例只需调用一次fixture，那就可以设置为scope="session"，
# 并且写到conftest.py文件里.conftest.py文件名称是固定的，pytest会自动识别该文件。
# 放到工程的根目录下，就可以全局调用了，如果放到某个package包下，那就只在该package内有效
@pytest.fixture(scope='session')
def login():
    # 打开浏览器
    service = Service(EdgeChromiumDriverManager().install())  # 浏览器驱动
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    driver.get(chandao_url)
    yield driver
    #关闭浏览器
    driver.quit()