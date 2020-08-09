import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.articleclassify_page import ArticleClassifyPage
import allure
import os
from common.read_yaml import get_yaml_data

# 测试数据单独拿出来
cur_path = os.path.dirname(os.path.realpath(__file__))
yaml_path = os.path.join(os.path.dirname(cur_path), "test_data", "data_demo.yml")
test_datas = get_yaml_data(yaml_path)


@allure.feature("功能点：编辑文章分类页面")
class TestArticleClassify():

    @allure.story("用例：编辑文章分类-成功")
    @allure.title("{title}")
    @allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-6-2.html")
    @pytest.mark.parametrize("test_input, expected, title", test_datas["test_add_canshuhua"])
    def test_add_article_1(self, test_input, expected, title, login_fixture, delete_articleclassify):
        '''用例描述：
            1、点文章分类导航标签 跳转列表页面
            2、点编辑 文章分类按钮，跳转到编辑页面
            3、编辑页面输入，分类名称，如:文学，test, 123456 可以输入
            4、点保存按钮 保存成功，在列表页显示分类名称：文学
        '''
        driver = login_fixture
        article = ArticleClassifyPage(driver)
        with allure.step("步骤1：点文章分类导航标签 跳转编辑页面"):
            article.click_articleclassify()
        with allure.step("步骤2: 点添加 文章分类按钮"):
            article.click_add_articleclassify()
        with allure.step("步骤3：编辑页面输入，分类名称，如:文学，test, 123456 可以输入"):
            article.input_article(test_input)
        with allure.step("步骤4: 点保存按钮 保存成功，在列表页显示分类名称：文学"):
            article.click_save_button()
        # 获取结果
        with allure.step("获取结果: 获取页面实际结果，判断是否添加成功"):
            result = article.is_add_success()
            print(result)
        with allure.step("断言：判断是否添加成功"):
            assert result == expected
