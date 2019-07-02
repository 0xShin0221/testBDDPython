Feature: Check server services

  Scenario: Check services
    Given 127.0.0.1でnginxが起動している場合
    When TCPポート80にアクセスしたら
    Then TCPセッションが確立できること
