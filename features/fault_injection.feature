Feature: Fault Injection

  Background:
    Given normal CAN data

  Scenario: Inject fault into CAN data
    When I inject a fault
    Then data should be corrupted at index 0

  Scenario: Inject fault at specific position
    When I inject a fault at index 1
    Then data should be corrupted at index 1

  Scenario: Invalid fault index
    When I inject a fault at index 5
    Then fault injection should fail

  Scenario: Invalid fault value
    When I inject a fault with value 300
    Then fault injection should fail
