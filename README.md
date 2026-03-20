# 🚗 CAN Bus Message Testing Tool

A comprehensive Python-based automation framework for validating ECU
communication over CAN networks.

## Overview

This project simulates, validates, decodes, and tests CAN messages for
automotive systems.

## Features

-   CAN Message Simulation:

    It validates message flow, timing behaviour, integration logic.
    
-   ECU Data Validation:

    Ensures parameters such as speed, RPM or temperature remains within acceptable limits.
    
-   Message Integrity Testing:

    Identify transmission error and maintain system reliability.
    
-   DBC-Based CAN Decoding:

    Decodes raw CAN messages into human readable signals using DBC database.
    
-   CAN Log Replay Testing:

    Replays recorded CAN traffic logs to simulate real world driving scenarios.
    
-   Automated ECU Fault Injection:

    Introduces control fault into CAN messages to check ECU robustness and to validate fault tolerance & safety mechanisms.
    
## Installations

git clone https://github.com/Priya2191-dev/CAN-bus-message-testing-tool.git

cd CAN-bus-message-testing-tool

pip install -r requirements.txt

## Interactive Simulation Demo

Run the CAN bus testing tool demo

[Open in google collab] (https://colab.research.google.com/github/Priya2191-dev/CAN-bus-message-testing-tool/blob/main/notebook/CAN-bus-message-testing-tool.ipynb)

## Testing

- Auomation Testing (Pytest + BDD)

- CI/CD Integration

## Usages

Run tests:

- pytest

- behave

## CI/CD

GitHub Actions pipeline runs pytest and behave automatically.

## Technologies

-   python-can
-   cantools
-   pytest
-   behave

## Author

Priyanka Lale
