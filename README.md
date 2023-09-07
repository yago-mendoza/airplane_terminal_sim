
# Airplane Terminal Simulation

## Overview

This project simulates the operations of airplanes and gates (terminals) using MQTT for communication. Airplanes send information about their status, while gates display relevant airplane details.

## Prerequisites

- **Python 3.x:** ensure Python 3 is installed.
- **Paho MQTT library:** required for MQTT communication.
  
  ```bash
  pip install paho-mqtt
  ```
- **MQTT Broker:** for local testing, you can use Mosquitto, an open-source MQTT broker. Follow the [installation guide](https://mosquitto.org/download/) for your operating system.

## Running the Simulation


1. **Start the MQTT Broker:** 
   - Search for "Mosquitto Broker" in the Start menu and click on it to run.
   - Alternatively, open a command prompt and run:
     
     ```bash
     mosquitto
     ```
   Ensure the broker is running without errors. It will listen for incoming MQTT messages.

2. **Run the Simulation:** 
   - Open a new command prompt.
   - Navigate to the directory where you extracted the project files using the `cd` command.
   - Once in the project directory, run:
     
     ```bash
     python central.py
     ```
   This will start the simulation, and you should see output related to airplanes and gates based on the logic in the code.

3. **Monitor the MQTT Messages (Optional):**
   - If you want to see the MQTT messages being published and subscribed, you can use Mosquitto's command-line clients.
   - Open a new command prompt and run:
     
     ```bash
     mosquitto_sub -v -t '#'
     ```
   This command subscribes to all messages, allowing you to monitor the communication.

4. **Stop the Simulation:** 
   - Return to the command prompt where the simulation is running.
   - Press `CTRL+C` to stop the simulation.

5. **Stop the MQTT Broker:** 
   - Return to the command prompt where the Mosquitto broker is running.
   - Press `CTRL+C` to stop the broker.

## Structure

- `airplane`: defines the behavior and properties of airplanes.
- `gate`: represents a gate (or terminal) in the airport.
- `flight_route`: manages flight routes with expected times.
- `display_board`: represents the display board at each gate.
- `utilities`: contains utility functions used across the project.
- `constants`: defines constants for the system.
- `timer`: contains a timer class for tracking elapsed time.
- `line_manager`: manages operations related to flight routes.
- `ordered_list`: manages ordered lists used in the project.
- `central`: main driver of the simulation, initializing and activating airplanes and gates.
- `draft`: contains draft or test code (for development use).


