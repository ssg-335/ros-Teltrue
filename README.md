[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Wps7Fafn)

# ROS2 Lab Experiments

**Student:** Titilola Mayowa  
**Group:** 4  
**Matric Number:** 230410005

---

## Overview

This repository contains ROS2 (Robot Operating System 2) lab experiment submissions. Each experiment explores a different core concept of ROS2 development, from basic publishing to action servers and robot mapping.

---

## Experiments

### Experiment 1 – ROS2 Publisher & LaserScan
Demonstrates a basic ROS2 publisher node that reads and publishes `sensor_msgs/LaserScan` data. Includes a YAML launch/configuration file and screenshots of the output.

**Key concepts:** ROS2 publishers, `sensor_msgs`, YAML configuration

---

### Experiment 2 – Screenshots / Observations
Contains screenshots documenting ROS2 environment setup and node behaviour observations.

---

### Experiment 3 – Custom Publisher Node (`my_robot_pkg`)
A Python ROS2 package containing a `TalkerNode` that publishes a `std_msgs/String` message with student group information to the `group_info` topic every 2.5 seconds.

**Package:** `my_robot_pkg`  
**Node:** `talker_node`  
**Topic:** `/group_info`  
**Message type:** `std_msgs/String`

---

### Experiment 4 – ROS2 Services (`ros_service_demo`)
Implements a client–server pattern using the `example_interfaces/AddTwoInts` service interface.

- **Server** (`add_two_ints_server.py`): Listens on `/add_two_ints` and returns the sum of two integers.
- **Client** (`add_two_ints_client.py`): Sends two integers (via command-line arguments) and logs the result.

**Package:** `ros_service_demo`  
**Service:** `/add_two_ints`  
**Interface:** `example_interfaces/AddTwoInts`

---

### Experiment 5 – ROS2 Actions (`my_robot_action_pkg`)
Implements the ROS2 action pattern using a custom `DoTask` action interface.

- **Action definition** (`DoTask.action`):
  - Goal: `int32 task_duration`
  - Result: `bool success`, `string message`
  - Feedback: `float32 progress`
- **Server** (`action_server.py`): Executes a timed task, publishing progress feedback (0–100 %) at regular intervals.
- **Client** (`action_client.py`): Sends a goal and logs feedback until the task completes.

**Package:** `my_robot_action_pkg`  
**Action:** `/do_task`

---

### Experiment 6 – Robot Mapping
Contains map files generated from a robot navigation session using ROS2 navigation tools (e.g., `nav2` / `slam_toolbox`).

- `my_map.pgm` – Occupancy grid image of the mapped environment.
- `my_map.yaml` – Map metadata (resolution: 0.05 m/px, origin, thresholds).

**Map resolution:** 0.05 m/pixel  
**Coordinate origin:** (-1.27, -2.49, 0)

---

## Requirements

- ROS2 (Humble / Foxy or later)
- Python 3
- `example_interfaces` package
- `sensor_msgs`, `std_msgs` packages
- `nav2` / `slam_toolbox` (Experiment 6)
