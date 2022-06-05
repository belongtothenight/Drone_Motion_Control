import airsim_basic_function as abf
import control_algorithm as ca
# import drone_movement
import read_file as rf
import subprocess
import sys
import os


def spawn_program_and_die(program, exit_code=0):
    """
    Description:
        Run another python script and close it after it's finished
    Parameter:
        Input:
            program: (str) Execute program.
        Output:
            None
    Link:
        https://stackoverflow.com/questions/7974849/how-can-i-make-one-python-file-run-another
    """
    subprocess.Popen(program)
    sys.exit(exit_code)


if __name__ == '__main__':
    """
    Description:
        Main function.
    Parameter:
        Input:
            None
        Output:
            None
    Link:
        None
    """
    # Read Coordinate
    print('main.py: reading coordinate...')
    coordinate = rf.read_csv('./test_coordinate/target_coordinate.csv')
    print('main.py: coordinate read')
    print(coordinate)

    # Initialize
    print('main.py: initializing...')
    abf.drone_initialize()
    print('main.py: initialized')

    # Take single piece of photo
    print('main.py: taking picture...')
    abf.capture_single_picture('./captured_image', '1')
    print('main.py: picture taken')

    # Perform drone movements
    # print('moving drone...')
    # spawn_program_and_die(['python', 'drone_movement.py'])

"""
Description:
    
parameter:
    Input:
        
    Output:
        
Link:
    
"""
