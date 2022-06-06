import airsim_basic_function as abf
import subprocess
import sys
import os


'''
def spawn_program_and_die(program, exit_code=0):
    """
    Description:
        Run another python script and close it after it's finished. It's not working somehow.
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
'''


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
        https://stackoverflow.com/questions/16548668/iterating-over-a-2-dimensional-python-list
        https://www.delftstack.com/howto/python/python-run-another-python-script/
    """
    # Initialize
    print('main.py-> initializing...')
    abf.drone_initialize()

    # Perform drone movements
    print('main.py-> moving drone...')
    exec(open("drone_movement.py").read())

"""
Description:
    
parameter:
    Input:
        
    Output:
        
Link:
    
"""
