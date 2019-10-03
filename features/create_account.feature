Feature: Validation Activity Create Account

   @acc
  Scenario: Validation Activity Create Account
    Given the tap in the menu SeuBarriga Híbrido
    When redirect to option SeuBarriga Híbrido
    And tap in Novo usuário?
    And fill field name with value "$VALUE"
    And fill field email with value "$VALUE"
    And fill field senha with value "$VALUE"
    And tap in the button Cadastrar
    Then screen create account must show message "Usuário inserido com sucesso"
    And do the login
    Then screen create account must show message "Bem vindo, $NAME_VALUE!"
