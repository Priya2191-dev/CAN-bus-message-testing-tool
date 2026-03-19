Feature: Message Integrity
  Scenario: Verify checksum integrity
    Given CAN data [10, 20, 30]
    When I calculate checksum
    Then integrity should be verified
