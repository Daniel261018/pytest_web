import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.articleclassify_page import ArticleClassifyPage
import allure


@allure.feature("功能点：编辑文章分类页面")
class TestArticleClassify():

    @allure.story("用例：编辑文章分类-成功")
    @allure.title("编辑文章分类，输入中文，编辑成功")
    @allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-6-2.html")
    def test_add_article_1(self, login_fixture, delete_articleclassify):
        '''用例描述：
            1、点文章分类导航标签 跳转列表页面
            2、点编辑 文章分类按钮，跳转到编辑页面
            3、编辑页面输入，分类名称，如:文学，test, 123456 可以输入
            4、点保存按钮 保存成功，在列表页显示分类名称：文学
        '''
        input_text = "中文"
        driver = login_fixture
        article = ArticleClassifyPage(driver)
        with allure.step("步骤1：点文章分类导航标签 跳转编辑页面"):
            article.click_articleclassify()
        with allure.step("步骤2: 点添加 文章分类按钮"):
            article.click_add_articleclassify()
        with allure.step("步骤3：编辑页面输入，分类名称，如:文学，test, 123456 可以输入"):
            article.input_article(input_text)
        with allure.step("步骤4: 点保存按钮 保存成功，在列表页显示分类名称：文学"):
            article.click_save_button()
        # 获取结果
        with allure.step("获取结果: 获取页面实际结果，判断是否添加成功"):
            result = article.is_add_success()
            print(result)
        with allure.step("断言：判断是否添加成功"):
            assert result == True

    @allure.story("用例：编辑文章分类-成功")
    @allure.title("编辑文章分类，输入英文，编辑成功")
    @allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-6-2.html")
    def test_add_article_2(self, login_fixture, delete_articleclassify):
        '''用例描述：
            1、点文章分类导航标签 跳转列表页面
            2、点编辑 文章分类按钮，跳转到编辑页面
            3、编辑页面输入，分类名称，如:文学，test, 123456 可以输入
            4、点保存按钮 保存成功，在列表页显示分类名称：文学
        '''
        input_text = "yingwen"
        driver = login_fixture
        article = ArticleClassifyPage(driver)
        with allure.step("步骤1：点文章分类导航标签 跳转编辑页面"):
            article.click_articleclassify()
        with allure.step("步骤2: 点添加 文章分类按钮"):
            article.click_add_articleclassify()
        with allure.step("步骤3：编辑页面输入，分类名称，如:文学，test, 123456 可以输入"):
            article.input_article(input_text)
        with allure.step("步骤4: 点保存按钮 保存成功，在列表页显示分类名称：文学"):
            article.click_save_button()
        # 获取结果
        with allure.step("获取结果: 获取页面实际结果，判断是否添加成功"):
            result = article.is_add_success()
            print(result)
        with allure.step("断言：判断是否添加成功"):
            assert result == True

    @allure.story("用例：重复编辑文章分类-失败")
    @allure.title("编辑文章分类，重复编辑文章分类，保存失败")
    @allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-6-2.html")
    def test_add_article_3(self, login_fixture, delete_articleclassify):
        '''用例描述：
            1、点文章分类导航标签 跳转列表页面
            2、点编辑 文章分类按钮，跳转到编辑页面
            3、编辑页面输入，分类名称输入：计算机
            4、点保存按钮 保存成功，在列表页显示分类名称：计算机
            5、再次点击编辑 文章分类按钮，跳转到编辑页面
            6、编辑页面输入，分类名称输入：计算机
        '''
        driver = login_fixture
        input_text = "计算机"
        article = ArticleClassifyPage(driver)
        with allure.step("步骤1：先编辑内容-计算机"):
            article.click_articleclassify()  # 左侧列表
            article.click_add_articleclassify()
            article.input_article(input_text)
            article.click_save_button()
            # 获取结果， 完成后回到列表页面
            result = article.is_add_success()
            print(result)
        with allure.step("断言：保存成功"):
            assert result
        with allure.step("步骤2：重复编辑-计算机"):
            # 重复编辑
            article.click_add_articleclassify()
            article.input_article(input_text)
            article.click_save_button()
            result = article.is_add_success()
            # 期望：不能重复编辑
        with allure.step("断言：保存失败"):
            assert not result
