from behave import *
from pages.RegistrationPage import RegistrationPage
from selenium import webdriver

use_step_matcher("re")

expected_page_title = "Sign up - BookOnline.web"

registrationPage = RegistrationPage(webdriver.Chrome(), "https://localhost:5001/Identity/Account/Register", expected_page_title)

@given("我進入註冊頁面")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """



@when("我填入必填欄位進行註冊")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When 我填入必填欄位進行註冊
                              | locator | type | value |
                              | Input_Email | textbox | parker @ avengers.gov |
                              | Input_Password | password | \'avengers#329\'      |')


@then("註冊成功後網站登入狀態顯示為'parker@avengers\.gov'")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then 註冊成功後網站登入狀態顯示為\'parker@avengers.gov\'')