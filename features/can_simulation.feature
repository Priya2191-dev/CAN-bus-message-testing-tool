Feature: CAN Message Simulation

  Background:
    Given a virtual CAN bus

  Scenario: Send and receive a CAN message
    When I send a CAN message with ID 0x123 and data 1,2,3,4
    Then I should receive the same CAN message

  Scenario: Validate different CAN payload
    When I send a CAN message with ID 0x200 and data 10,20,30,40
    Then the received CAN message should match ID 0x200 and data 10,20,30,40

  Scenario: No message scenario
    When I do not send any CAN message
    Then no CAN message should be received
