Feature: Validation Activity About


  @about  @skip
  Scenario: Validation Activity About
      Given the tap in the menu About
      When seen the image of course
      And the activity must get message "Veja o curso aqui"
      And tap in the link "Veja o curso aqui"
      Then must be open webbrowser Chrome
