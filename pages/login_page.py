from common.base import Base

url = "http://49.235.92.12:8020/xadmin/"


class LoginPage(Base):
    """登录页面类"""
    username = ("xpath", '//*[@id="id_username"]')  # 用户名
    password = ("xpath", '//*[@id="id_password"]')  # 密码
    button = ("xpath", '//button[text()="登录"]')  # 登录按钮

    # 判断登录成功元素--欢迎， admin
    login_assertion = ("xpath", '//*[@id="top-nav"]/div[2]/ul/li[2]/a/strong')

    def input_username(self, text="admin"):
        '''输入用户名'''
        self.send(self.username, text)

    def input_password(self, text="yoyo123456"):
        '''输入密码'''
        self.send(self.password, text)

    def click_button(self):
        '''点击登录按钮'''
        self.click(self.button)

    def login(self, user="admin", password="yoyo123456"):
        '''登录'''
        self.driver.get(url)
        self.input_username(user)
        self.input_password(password)
        self.click_button()

    def is_login_success(self):
        '''判断是否登录成功'''
        return self.is_element_exist(self.login_assertion)


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    web = LoginPage(driver)
    web.login()
    result = web.is_login_success()
    print("登录结果：", result)
    assert result
    driver.quit()