import pytest
import pandas as pd
import os
from src.drivers import PowerSupply, DigitalMultimeter

# Data storage setup
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

def test_voltage_accuracy():
    """
    Test 1: Verify PSU output matches DMM reading.
    Scenario: Sweep voltage from 1V to 5V and check accuracy.
    """
    # 1. Setup
    psu = PowerSupply("PSU_01")
    dmm = DigitalMultimeter("DMM_01")
    
    psu.open()
    dmm.open()
    
    results = []
    
    # 2. Execution (The Test Loop)
    test_voltages = [1.0, 2.0, 3.3, 5.0]
    
    for set_v in test_voltages:
        psu.set_voltage(set_v)
        read_v = dmm.read_voltage()
        
        # Log data
        results.append({
            "Set_Voltage": set_v,
            "Measured_Voltage": read_v,
            "Error": abs(set_v - read_v)
        })
        
        # 3. Assertion (The Pass/Fail Criteria)
        # Allow 0.1V tolerance (Mock hardware noise)
        assert abs(set_v - read_v) < 0.1, f"Voltage failed at {set_v}V"

    # 4. Data Storage (JD Requirement)
    df = pd.DataFrame(results)
    df.to_csv(f"{DATA_DIR}/test_results.csv", index=False)
    print("\nTest Complete. Data saved to CSV.")
    
    # 5. Teardown
    psu.close()
    dmm.close()