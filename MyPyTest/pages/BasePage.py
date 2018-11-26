# coding=utf-8
"""
Project:基礎類BasePage，封裝所有頁面都公用的方法，
定義open函數，重定義find_element，switch_frame，send_keys等函數。
在初始化方法中定義驅動driver，基本url，title
WebDriverWait提供了顯式等待方式。
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    """
    BasePage封裝所有頁面都公用的方法，例如driver, url ,FindElement等
    """

    # 初始化driver、url、page_title等
    # 實例化BasePage類時，最先執行的就是__init__方法，該方法的入參，其實就是BasePage類的入參。
    # __init__方法不能有返回值，只能返回None
    # self只實例本身，相較於類Page而言。
    def __init__(self, selenium_driver, base_url, page_title):
        self.driver = selenium_driver
        self.base_url = base_url
        self.page_title = page_title

    # 通過title斷言進入的頁面是否正確。
    # 使用title獲取當前窗口title，檢查輸入的title是否在當前title中，返回比較結果（True 或 False）
    def on_page(self, page_title):
        return page_title in self.driver.title

    # 打開頁面，並校驗頁面鏈接是否加載正確
    # 以_開頭的方法，在使用import *時，該方法不會被導入，保證該方法為類私有的。
    def _open(self, url, page_title):
        self.driver.get(url)
        self.driver.maximize_window()
        # 檢查是否為指定頁面
        assert self.on_page(page_title), u"開啟頁面失敗 %s" % url

    # 定義open方法，調用_open()進行打開鏈接
    def open(self):
        self._open(self.base_url, self.page_title)

    # 重寫元素定位方法
    def find_element(self, *loc):
        #        return self.driver.find_element(*loc)
        try:
            # 等待一段時間，確保元素已顯示在網頁上
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except AttributeError:
            print
            f"{self} 頁面中未能找到 {loc} 元素"

    # 重寫switch_frame方法
    def switch_frame(self, loc):
        return self.driver.switch_to_frame(loc)

    # 定義script方法，用於執行js腳本，範圍執行結果
    def script(self, src):
        self.driver.execute_script(src)

    # 重寫定義send_keys方法
    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            loc = getattr(self, "_%s" % loc)  # getattr相當於實現self.loc
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            print
            f"{self} 頁面中未能找到 {loc} 元素"

    def close(self):
        self.driver.quit()
