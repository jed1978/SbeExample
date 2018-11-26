from behave import *
from pages.LoginPage import LoginPage
from selenium import webdriver

use_step_matcher("re")
expected_page_title = "Log in - BookOnline.web"
loginPage = LoginPage(webdriver.Chrome(), "https://localhost:5001/Identity/Account/Login", expected_page_title)


@given("我打開登入頁面")
def step_impl(context):
    loginPage.open()


@when("我使用正確的帳號(?P<account>.+)與密碼(?P<password>.+)登入")
def step_impl(context, account, password):
    loginPage.input_account(account)
    loginPage.input_password(password)
    loginPage.form_submit()


@then("成功登入會看到登入狀態(?P<result>.+)顯示在網頁上")
def step_impl(context, result):
    assert result == loginPage.show_userid()
    loginPage.close()
