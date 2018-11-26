# Created by jed at 2018/11/23
Feature: 會員註冊
  A guest is allowed to register if he

  Scenario: 訪客成功註冊為一個會員
    Given 我進入註冊頁面
    When 我填入必填欄位進行註冊
      | locator        | type     | value               |
      | Input_Email    | email  | parker@avengers.gov |
      | Input_Password | password | 'avengers#329'      |
    Then 註冊成功後網站登入狀態顯示為'parker@avengers.gov'

