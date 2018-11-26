# coding=utf-8
'''
Created on 2016-8-13
@author: Jennifer
Project:頁面基本操作方法：如open，input_username，input_password，click_submit
'''

from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class RegistrationPage(BasePage):

    account_loc = (By.NAME, "Input.Email")
    password_loc = (By.NAME, "Input.Password")
    confirm_password_loc = (By.NAME, "Input.ConfirmPassword")
    submit_loc = (By.ID, 'registration')

    def open(self):
        # 調用page中的_open打開連接
        self._open(self.base_url, self.page_title)

    def input_account(self, account):
        self.find_element(*self.account_loc).send_keys(account)

    def input_password(self, password):
        self.find_element(self, *self.password_loc).send_keys(password)

    def input_confirm_password(self, password):
        self.find_element(self, *self.confirm_password_loc).send_keys(password)

    def form_submit(self):
        self.find_element(*self.submit_loc).submit()
