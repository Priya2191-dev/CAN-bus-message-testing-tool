# 🚗 CAN Bus Message Testing Tool

## Objective

A comprehensive Python-based automation framework for validating CAN (Control Area Network) communication, including message simulation, ECU validation, fault injection, integrity checks, DBC decoding and log replay.

This project demonsrates end-to-end automotive testing practices using pytest, BDD (behave) and CI/CD pipelines.

## Overview

This project simulates, validates, decodes, and tests CAN messages for
automotive systems.

## Features

-   CAN Message Simulation:

    Simulate CAN messages using virtual CAN bus.

    Validate message transmission and reception.
    
-   ECU Data Validation:

    Validate ECU parameters like speed.

    Boundary and negative testing
    
-   Fault Injection:

    Inject faults into CAN payload.

    Simulate real world sensor/data corruption.
    
-   Message Integrity:

    Checksum based integrity validation.

    Detect corrupted CAN data.
    
-   DBC Decoding:

    Decode CAN messages using DBC file.

    Extract signal level information.
    
-   CAN Log Replay:

    Replay recorded CAN logs.

    Useful for debugging and simulation.
    
## Installations

git clone https://github.com/Priya2191-dev/CAN-bus-message-testing-tool.git

cd CAN-bus-message-testing-tool

pip install -r requirements.txt

## Tech Stack

- Language: Python
- Testing: Pytest, Behave(BDD)
- CI/CD: Github Actions
- Library: Cantools
- Reporting: Allure Reports

## Testing Strategy

- Unit Testing using pytest
- Behavior-Driven Testing using Behave
- Edge Case Handling
- Negative Scenario

## CI/CD Pipeline

- Runs on every push & pull request.
- Executes:

  Pytest(Unit tests)

  Behave(BDD tests)

- Generates:

  Allure reports

  Coverage reports

## Reports & Outputs

- Allure Test Reports
- Behave Execution Logs
- Coverage Report

## Author

Priyanka Lale
