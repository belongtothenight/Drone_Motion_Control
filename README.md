# DroneMotionControl
### **This program is still under development**
- Developing start in 2022.06.06 10:46
- Code version: v3.2.0
- Author: Dachuan Chen

## Description
Based on the data generated from FRCNN test, this program shows how the drone will fly according to it.

## File Requirement
1. target_coordinate.csv / Detail data of FRCNN labeled coordinate.
2. frcnn_test_info.txt / General information about the FRCNN test run.

## Developing Environment
- Windows 11
- Visual Studio 2022
- Unreal Engine v4.27.2
- AirSim binary v1.7.0
- Python v3.9
   - AirSim v1.6.0 (PyCharm Interpreter/cmd)
   - pygame v2.1.2 (PyCharm Interpreter/cmd)
   - msgpack-rpc-python (cmd)

## Developing Environment Setup
### Detail installation process
1. https://microsoft.github.io/AirSim/build_windows/
2. https://microsoft.github.io/AirSim/unreal_proj/
3. https://microsoft.github.io/AirSim/unreal_custenv/

### Reminders
1. When setting up project, use default "box" project is a little bit easier.
2. No need to add any plugin in Unreal Engine 4 to do further coding.
3. AirSim is under heavy development, try updating to get new features and possible bug fixes.
4. The installation is ought for Windows 10, but visual studio still require about the same settings in Windows 11.

### Start up execution environment
1. Find "filename.sln" in your project environment directory and open with visual studio 2022 to open. (./AirSim-master/Unreal/Environments/'Custom Environment Name'/)
2. Press F5 in visual studio to startup the project.
3. Press Alt+P in Unreal Engine to run the project. Both visual studio and Unreal Engine needs to stay in current state.
4. Make sure having installed airsim in cmd and IDE, interpreter has all the necessary packages. Then, run the "main.py" file. 

### More info
1. https://microsoft.github.io/AirSim/
2. https://github.com/search?q=airsim+drone&type=Repositories
3. https://github.com/microsoft/AirSim
4. https://github.com/Zartris/Airsim-terminal-drone-control

## Code Workflow
1. Read FRCNN test result data related to each training images, one at a time.
2. Execute control algorithm to approach target.
3. Land beside the target and take a picture of it.

## File Structure
- main.py
  - airsim_basic_function.py
  - control_algorithm.py
  - drone_movement.py
  - read_file.py

## Adjustment Log
1. v1.0.0 / Prepare the simulating environment coded by CoderSpace(YT). 
2. v1.0.0 / Achieved basic control of AirSim drone.
3. v2.0.0 / Abandon 3D engine build in v1.0.0.
4. v2.0.0 / Established AirSim and Unreal Engine 4 as new simulation platform. 
5. v2.1.0 / Move functions away from main.
6. v2.1.1 / Match the missing developing environment.
7. v2.2.0 / Add "File Structure" in "README.md".
8. v2.2.0 / Enable reading data from ".csv" file.
9. v3.0.0 / Establish "drone_movement.py" work flow.
10. v3.1.0 / Enable reading data from ".txt" file.
11. v3.2.0 / Finish algorithm for drone to approach filming location.

