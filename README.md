
# Airplane Terminal Simulation

## Overview

This project simulates the operations of airplanes and gates (terminals) using MQTT for communication. Airplanes send information about their status, while gates display relevant airplane details.

## Prerequisites

- **Python 3.x:** Ensure Python 3 is installed.
- **Paho MQTT library:** Required for MQTT communication.
  ```bash
  pip install paho-mqtt
  ```
- **MQTT Broker:** For local testing, you can use Mosquitto, an open-source MQTT broker. Follow the [installation guide](https://mosquitto.org/download/) for your operating system.

## Running the Simulation

### Standard Execution:

1. **Start the MQTT Broker:** If using Mosquitto, run `mosquitto` in a terminal.
2. **Run the Simulation:** Navigate to the project directory and run:
   ```bash
   python central.py
   ```

### Linux Alternative (No-Extension Script Files):

1. **Start the MQTT Broker:** If using Mosquitto, run `mosquitto` in a terminal.
2. **Grant Execute Permissions:** Navigate to the project directory and grant execute permissions to the script files:
   ```bash
   chmod +x filename
   ```
   Replace `filename` with the name of each script file you want to make executable.
3. **Run the Simulation:** Run the main simulation script directly:
   ```bash
   ./central
   ```

## Structure

- `airplane`: Defines the behavior and properties of airplanes.
- `gate`: Represents a gate (or terminal) in the airport.
- `flight_route`: Manages flight routes with expected times.
- `display_board`: Represents the display board at each gate.
- `utilities`: Contains utility functions used across the project.
- `constants`: Defines constants for the system.
- `timer`: Contains a timer class for tracking elapsed time.
- `line_manager`: Manages operations related to flight routes.
- `ordered_list`: Manages ordered lists used in the project.
- `central`: Main driver of the simulation, initializing and activating airplanes and gates.
- `draft`: Contains draft or test code (for development use).

## Note

Ensure the MQTT broker is running before starting the simulation.

