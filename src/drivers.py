from src.emulator import VirtualDevice
import time

class Instrument:
    """Parent class for all test equipment."""
    def __init__(self, resource_name):
        self.device = VirtualDevice(resource_name)

    def open(self):
        self.device.connect()

    def close(self):
        self.device.disconnect()

class PowerSupply(Instrument):
    """Child class specific to Power Supply Units."""
    def set_voltage(self, voltage):
        # Using SCPI standard command structure
        self.device.write(f"VOLT {voltage}")
        time.sleep(0.1) # Simulate hardware settling time

class DigitalMultimeter(Instrument):
    """Child class specific to Multimeters."""
    def read_voltage(self):
        val = self.device.query("MEAS:VOLT?")
        return float(val)