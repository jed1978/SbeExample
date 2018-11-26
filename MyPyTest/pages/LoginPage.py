# coding=utf-8
'''
Created on 2016-8-13
@author: Jennifer
Project:頁面基本操作方法：如open，input_username，input_password，click_submit
'''
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


# 繼承BasePage類
class LoginPage(BasePage):
    # 定位器，通過元素屬性定位元素對象
    username_loc = (By.NAME, 'Input.Email')
    password_loc = (By.NAME, 'Input.Password')
    submit_loc = (By.ID, 'account')
    userid_loc = (By.ID, "manage")

    # 操作
    # 通過繼承覆蓋（Overriding）方法：如果子類和父類的方法名相同，優先用子類自己的方法。
    # 打開網頁
    def open(self):
        # 調用page中的_open打開連接
        self._open(self.base_url, self.page_title)

    # 輸入用戶名：調用send_keys對象，輸入用戶名
    def input_account(self, account):
        #        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(account)

    # 輸入密碼：調用send_keys對象，輸入密碼
    def input_password(self, password):
        #        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    # 點擊登錄：調用send_keys對象，點擊登錄
    def form_submit(self):
        self.find_element(*self.submit_loc).submit()

    # # 用戶名或密碼不合理是Tip框內容展示
    # def show_span(self):
    #     return self.find_element(*self.span_loc).text
    #
    # # 切換登錄模式為動態密碼登錄（IE下有效）
    # def swich_DynPw(self):

    #     self.find_element(*self.dynpw_loc).click()
    # 登錄成功頁面中的用戶ID查找
    def show_userid(self):
        return self.find_element(*self.userid_loc).text
