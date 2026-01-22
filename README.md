# Automated Avionics HIL Verification Framework

![Build Status](https://github.com/YOUR_USERNAME/avionics-hil-automation/actions/workflows/ci_pipeline.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Testing](https://img.shields.io/badge/Test-Pytest-green)

## Project Overview
This project implements an **Automated Hardware-in-the-Loop (HIL) Verification System** designed to validate avionics sensor performance. It simulates the interaction between a **Programmable Power Supply (PSU)** and a **Digital Multimeter (DMM)** using Object-Oriented Python drivers.

## Technical Highlights
* **Object-Oriented Design:** Implemented modular drivers (`src/drivers.py`) using SCPI command structure to abstract hardware complexity.
* **Automated Regression Testing:** Integrated a **CI/CD pipeline (GitHub Actions)** to automatically execute test procedures on every code commit.
* **Data Emulation & Analysis:** developed a shared-state physics emulator to mimic voltage rail behavior and sensor noise, with automated logging to CSV for analysis.
* **Standards Compliance:** Test logic structured to verify voltage tolerances (simulating DO-160 power input testing).

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt