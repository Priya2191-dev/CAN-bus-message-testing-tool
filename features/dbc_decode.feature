Feature: DBC Decoding
  Scenario: Decode CAN message using DBC
    Given a valid DBC file
    When I decode a CAN message
    Then I should get decoded signals
