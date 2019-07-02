Feature: Check server services

  Scenario Outline: Check services
    Given <host>でnginxが起動している場合
    When TCPポート<port>にアクセスしたら
    Then TCPセッションが確立できること

    Examples: Services
    | host      | port |
    | 127.0.0.1 | 80   |
    | 127.0.0.1 | 22   |
