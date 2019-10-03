Feature: Validation Activity Alerts

  @alert
  Scenario: Validation Activity Alerts
    Given the tap in the menu Alerts
    When redirect to option Alerts
    And tap in the following button Simple Alert
    Then must show the message "Pode clicar no OK ou fora da caixa para sair"
