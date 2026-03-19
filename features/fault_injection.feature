Feature: Fault Injection
  Scenario: Inject fault into CAN data
    Given normal CAN data
    When I inject a fault
    Then data should be corrupted
