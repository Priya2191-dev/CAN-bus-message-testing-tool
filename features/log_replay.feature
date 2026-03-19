Feature: CAN Log Replay
  Scenario: Replay CAN log
    Given a CAN log
    When I replay the log
    Then messages should be printed
