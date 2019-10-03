Feature: Validation Activity Swipe

  @swipe
  Scenario: Validation Activity Swipe
    Given the tap in the menu Swipe
    When redirect to screen Swipe
    Then screen Swipe must get following message "Mova a tela pra esquerda"
    And tap and left swipe
    Then screen Swipe must get following message "E veja se você consegue"
    And tap and left swipe
    Then screen Swipe must get following message "Chegar até o fim"
