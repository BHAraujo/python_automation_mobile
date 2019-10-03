Feature: Validation Activity Splash

  @splash
  Scenario: Validation Activity Splash
    Given the tap in the menu Splash
    When redirect to option Splash
    Then the activity must get message "Splash!"
