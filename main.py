import airsim_basic_function as abf
import control_algorithm as ca
import drone_movement
import read_file
import subprocess
import sys
import os


# Run another python script and close it after it's finished
def spawn_program_and_die(program, exit_code=0):
    subprocess.Popen(program)
    sys.exit(exit_code)

if __name__ == '__main__':
    # Read Coordinate
    print('reading coordinate...')
    spawn_program_and_die(['python', 'read_file.py'])

    # Initialize
    print('initializing...')
    abf.drone_initialize()

    # Take single piece of photo
    print('taking picture...')
    abf.capture_single_picture()

    # Perform drone movements
    #print('moving drone...')
    # spawn_program_and_die(['python', 'drone_movement.py'])
