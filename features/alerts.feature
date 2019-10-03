Feature: Validation Activity Alerts
  As a user I want to tap em all alerts and validate yours message

  @alert
  Scenario: Validation Activity Alerts
    Given the tap in the menu Alerts
    When redirect to option Alerts
    And tap in the following button Simple Alert
    Then must show the message "Pode clicar no OK ou fora da caixa para sair"
    And tap button ok
    When tap int the Restrict Alert
    Then tap in the button sair
    # When tap int the Confirm Alert
    # And tap in the button confirmar
    # Then must show the message "Confirmado"
    # And tap in the button sair
    # And tap int the Confirm Alert
    # And tap in the button deny
    # Then must show the message "Negado"
