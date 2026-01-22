# Avionics HIL Verification Framework

![Build Status](https://github.com/YOUR_USERNAME/avionics-hil-automation/actions/workflows/ci_pipeline.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Test](https://img.shields.io/badge/Test-Pytest-green)

## Project Overview
This project implements an **Automated Hardware-in-the-Loop (HIL) Verification System** designed to validate avionics sensor modules. It simulates the interaction between a **Programmable Power Supply (PSU)** and a **Digital Multimeter (DMM)** to verify voltage stability and sensor accuracy under varying load conditions.

The framework utilizes **Object-Oriented Python** for instrument abstraction (SCPI/VISA simulation) and integrates with **GitHub Actions** to execute regression tests automatically on every code commit.

## System Architecture
* **Drivers:** OOP-based wrappers for SCPI commands (PowerSupply, DigitalMultimeter classes).
* **Emulator:** A shared-state backend simulating electrical rail physics and sensor noise.
* **Testing:** Pytest framework with automated pass/fail criteria based on tolerance thresholds.
* **Data:** Automated telemetry logging to CSV for post-test analysis.

## Key Features
* **Automated Regression Testing:** CI/CD pipeline ensures tests run on every push.
* **Hardware Abstraction Layer (HAL):** Decouples test logic from physical hardware, allowing for dry-run simulations.
* **Telemetry Logging:** Captures voltage setpoints, measured values, and error deltas.

## Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt