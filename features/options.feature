Feature: Validation Activity Option Successifuly
    As a user I want to tap in the menu Option and validate message

    @option
    Scenario: Validation Activity Option Successfully
      Given the tap in the menu Option Successifuly
      Then the activity must get message "Você achou essa opção"
