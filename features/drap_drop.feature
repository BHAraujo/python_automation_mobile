Feature: Validation Activity Drag Drop
    As a user I want to drag drop all elements and validate the sequece by in the end

  @drag
  Scenario: Validation Activity Drag Drop
    Given the tap in the menu Drag Drop
    When redirect to option Drag Drop
    And Drag "Esta" and Drop "lista"
    And Drag "Drop!" and Drop "longo"
    And Drag "para" and Drop "desejado"
    Then take a screenshot e compare with screenshot origin
