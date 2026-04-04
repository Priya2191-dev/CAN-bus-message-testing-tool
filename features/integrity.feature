Feature: Message Integrity

  Background:
    Given valid CAN data

  Scenario: Verify checksum integrity
    When I calculate checksum
    Then integrity should be verified

  Scenario: Detect corrupted data
    When I modify CAN data
    Then integrity verification should fail

  Scenario: Verify checksum with overflow
    Given CAN data [255, 1]
    When I calculate checksum
    Then integrity should be verified
