
Feature: Validation Activity Accordion
  As a user I want to tap all the accordion and validate yours message

  @accordion
  Scenario: Validation Activity Accordion
    Given the tap in the menu Accordion
    When redirect to option Accordion
    And tap in the following Opção 1
    Then screen accordion must get following message "Esta é a descrição da opção 1"
    And tap in the following Opção 2
    Then screen accordion must get following message "Esta é a descrição da opção 2"
    And tap in the following Opção 3
    Then screen accordion must get following message "Esta é a descrição da opção 3, Que pode, inclusive ter mais de uma linha"
    And tap in the following Opção 4
    Then screen accordion must get following message "Esta é a descrição da opção 4"
    And tap in the following Opção 5
    Then screen accordion must get following message "Esta é a descrição da opção 5"
    And tap in the following Opção 6
    Then screen accordion must get following message "Esta é a descrição da opção 6"
