Feature: CAN Message Simulation
  Scenario: Send and receive CAN message
    Given a virtual CAN bus
    When I send a CAN message
    Then I should receive the same CAN message
