import pytest
import pandas as pd
import os
from src.drivers import PowerSupply, DigitalMultimeter

# Data storage setup
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

# TEST CASE 1: Voltage Accuracy
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
        assert abs(set_v - read_v) < 0.1, f"Voltage failed at {set_v}V"

    # 4. Data Storage
    df = pd.DataFrame(results)
    df.to_csv(f"{DATA_DIR}/test_results.csv", index=False)
    
    # 5. Teardown
    psu.close()
    dmm.close()

# TEST CASE 2: Brownout Protection (Make sure this def is fully to the left!)
def test_brownout_protection():
    """
    Test 2: Brownout Check.
    Scenario: Verify the system behaves safely when voltage drops below 3.0V.
    """
    # Setup
    psu = PowerSupply("PSU_01")
    dmm = DigitalMultimeter("DMM_01")
    psu.open()
    dmm.open()
    
    # Execution: Set a dangerous low voltage
    low_voltage = 2.5
    psu.set_voltage(low_voltage)
    measured = dmm.read_voltage()
    
    # Assertion
    assert measured < 3.0, "Voltage did not drop to brownout levels!"
    
    print(f"\nBrownout Test: Input dropped to {measured:.2f}V (Success)")
    
    psu.close()
    dmm.close()