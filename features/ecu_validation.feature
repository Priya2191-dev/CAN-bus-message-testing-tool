Feature: ECU Data Validation
  Scenario: Validate valid speed
    Given ECU speed is 80
    When I validate the speed
    Then the speed should be valid
