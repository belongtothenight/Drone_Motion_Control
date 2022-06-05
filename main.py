import airsim_basic_function as abf
import control_algorithm as ca
import drone_movement
import read_file as rf
import subprocess
import sys
import os


def spawn_program_and_die(program, exit_code=0):
    subprocess.Popen(program)
    sys.exit(exit_code)


# Initialize
abf.drone_initialize()

# Take single piece of photo
abf.capture_single_picture()

# Perform drone movements
spawn_program_and_die(['python', 'drone_movement.py'])
