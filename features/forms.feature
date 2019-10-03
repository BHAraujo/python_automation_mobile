Feature: Validation Activity Forms

  @forms
  Scenario: Validation Activity Forms
      Given the click in the menu Forms
      When the title screen must be "CT Appium"
      And fill of field name "Automation"
      And select the option "PS4"
      And tap checkbox of date
      And disable switch of time
      And tap in the button Lazy save
      Then validate following values
      | Name       | Console   | Slider | Checkbox   | Data         | Hora    |
      | Automation | PS4       |  25    |  Marcado   |  01/01/2000  | 06:00   |
      And tap in the button clear
      Then the grade must be cleaned
