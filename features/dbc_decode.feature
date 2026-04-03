Feature: DBC Decoding

  Background:
    Given a valid DBC file

  Scenario: Decode CAN message using DBC
    When I decode a CAN message
    Then I should get decoded signals

  Scenario: Decode custom CAN payload
    When I decode a CAN message with data 50,0,0,0,0,0,0,0
    Then decoded signals should not be empty

  Scenario: Invalid DBC file handling
    When I decode using an invalid DBC file
    Then decoding should fail
