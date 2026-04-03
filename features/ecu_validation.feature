Feature: ECU Data Validation

  Background:
    Given ECU system is initialized

  Scenario: Validate valid speed
    Given ECU speed is 80
    When I validate the speed
    Then the speed should be valid

  Scenario: Validate boundary speed
    Given ECU speed is 120
    When I validate the speed
    Then the speed should be valid

  Scenario: Validate invalid speed
    Given ECU speed is 200
    When I validate the speed
    Then validation should fail

  Scenario: Validate invalid speed type
    Given ECU speed is "fast"
    When I validate the speed
    Then validation should fail
