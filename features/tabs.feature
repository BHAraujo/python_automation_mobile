Feature: Validation Activity Tabs

  @tabs
  Scenario: Validation Activity Tabs
    Given the tap in the menu Tabs
    When redirect to option Tabs
    Then the activity must get message "Este é o conteúdo da Aba 1"
    And tap in the second tab
    Then the activity must get message "Este é o conteúdo da Aba 2"
