from common.base import Base


class ArticleClassifyPage(Base):
    # 文章分类
    art_clfy = ("xpath", '//*[@id="left-side"]/ul[1]/li[11]/a')
    # 增加 文章分类
    add_art_clfy = ('xpath', '//*[@id="content-block"]/div[1]/div[2]/div/a')
    # 分类：输入框
    input_clfy = ('xpath', '//*[@id="id_n"]')
    # 保存
    save = ('xpath', '//*[@id="articleclassify_form"]/div[2]/button/i')
    # 判断添加成功
    save_success = ('xpath', '//*[@id="content-block"]/div[2]')

    def click_articleclassify(self):
        '''点击文章分类按钮'''
        self.click(self.art_clfy)
        # 复数定位点击按钮
        # self.finds(self.art_clfy).click()

    def click_add_articleclassify(self):
        '''点击添加文章分类按钮'''
        self.click(self.add_art_clfy)

    def input_article(self, text="测试分类"):
        '''输入文章分类名称'''
        self.send(self.input_clfy, text)

    def click_save_button(self):
        """点击保存"""
        self.click(self.save)

    def is_add_success(self, expect_text='添加成功'):
        """判断是否保存成功"""
        text = self.get_text(self.save_success)
        print("获取到元素的文本内容：%s" % text)
        return expect_text in text


if __name__ == '__main__':
    from pages.login_page import LoginPage
    # 先登录
    from selenium import webdriver

    driver = webdriver.Chrome()
    driver.maximize_window()
    web = LoginPage(driver)
    web.login()

    article = ArticleClassifyPage(driver)
    article.click_articleclassify()
    article.click_add_articleclassify()
    article.input_article()
    article.click_save_button()
    result = article.is_add_success()
    print(result)

