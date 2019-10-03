Feature: Validation Activity Clicks

  @clicks
  Scenario: Validation Activity Clicks
    Given the tap in the menu Clicks
    When redirect to option Clicks
    And tap long click
    And tap double click
    And tap double lazy click
    Then tap in clear
