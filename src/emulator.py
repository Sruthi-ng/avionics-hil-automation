import random

# --- THE FIX: SHARED "PHYSICS" STATE ---
# This dictionary acts as the "wire" connecting your devices.
# When PSU writes here, DMM reads from here.
GLOBAL_CIRCUIT_STATE = {
    "V_RAIL": 0.0
}

class VirtualDevice:
    """Simulates a physical instrument connected via Serial/VISA."""
    
    def __init__(self, name):
        self.name = name
        self.connected = False

    def connect(self):
        self.connected = True
        print(f"[{self.name}] Connected.")

    def disconnect(self):
        self.connected = False
        print(f"[{self.name}] Disconnected.")

    def query(self, command):
        """Simulates sending a SCPI command and getting a response."""
        if not self.connected:
            raise ConnectionError(f"{self.name} is not connected!")

        if command == "*IDN?":
            return f"Simulated_{self.name}_Model_X1000"
        
        if "MEAS:VOLT?" in command:
            # THE FIX: Read from the shared "Physical" simulation, not local memory
            true_voltage = GLOBAL_CIRCUIT_STATE["V_RAIL"]
            
            # Add some sensor noise (+/- 0.05V) to make it realistic
            noise = random.uniform(-0.02, 0.02) 
            return true_voltage + noise
        
        return "ERROR: Unknown Command"

    def write(self, command):
        """Simulates sending a command to set a state."""
        if not self.connected:
            raise ConnectionError(f"{self.name} is not connected!")
            
        if "VOLT " in command:
            # Parse "VOLT 5.0" -> 5.0
            try:
                val = float(command.split()[1])
                
                # THE FIX: Update the shared "Physical" simulation
                GLOBAL_CIRCUIT_STATE["V_RAIL"] = val
                print(f"[{self.name}] Output set to {val}V (Simulated)")
            except IndexError:
                print("Error parsing voltage")