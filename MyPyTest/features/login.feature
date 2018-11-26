# Created by jed at 2018/11/24
Feature: 會員登入
  As a registered member
  I want to login success
  So that I can browse the website

  Scenario Outline: 會員使用正確的帳號與密碼可以成功登入
    Given 我打開登入頁面
    When 我使用正確的帳號<account>與密碼<password>登入
    Then 成功登入會看到登入狀態<result>顯示在網頁上
    Examples:
      | account                 | password   | result                         |
      | tony.stark@avengers.gov | Ironman.42 | Hello tony.stark@avengers.gov! |