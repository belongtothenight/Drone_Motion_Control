# IITF_FinalProject_DroneMotionControl
Developing start in 2022.06.05 09:50
Code version: v2.0.0
Author: Dachuan Chen

## Description
Based on the data generated from FRCNN test, this program shows how the drone will fly according to it.

## File Requirement
1. target_coordinate.csv / Detail data of FRCNN labeled coordinate.
2. frcnn_test_info.txt / General information about the FRCNN test run.

## Developing Environment
1. Windows 11
2. Visual Studio 2022
3. Unreal Engine v4.27.2
4. Python v3.9
5. pip v21.3.1
6. AirSim binary v1.7.0
7. AirSim v1.6.0
8. pygame v2.1.2
9. pynput v1.7.6

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
4. Make sure having installed airsim in cmd and IDE, put your codes into your IDE and execute.

### More info
1. https://microsoft.github.io/AirSim/
2. https://github.com/search?q=airsim+drone&type=Repositories
3. https://github.com/microsoft/AirSim
4. https://github.com/Zartris/Airsim-terminal-drone-control

## Code Workflow
1. Read FRCNN test result data related to each training images, one at a time.
2. Execute control algorithm to approach target.
3. Land beside the target and take a picture of it.

## Adjustment Log
1. v1 / Prepare the simulating environment coded by CoderSpace(YT)
2. v1 / Achieved basic control of AirSim drone

