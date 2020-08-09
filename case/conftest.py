import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def login_fixture():
    driver = webdriver.Chrome()
    driver.maximize_window()
    web = LoginPage(driver)
    web.login()  # 前置操作
    return driver


@pytest.fixture(scope="function")
def delete_articleclassify():
    print("连接你的数据库，清理数据")

