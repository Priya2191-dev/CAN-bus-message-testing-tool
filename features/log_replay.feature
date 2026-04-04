Feature: CAN Log Replay

  Scenario: Replay CAN log
    Given a valid CAN log
    When I replay the log
    Then CAN messages should be printed

  Scenario: Replay multiple CAN frames
    Given multiple CAN frames
    When I replay the log
    Then all messages should be printed

  Scenario: Invalid log format
    Given an invalid CAN log
    When I replay the log
    Then replay should fail
