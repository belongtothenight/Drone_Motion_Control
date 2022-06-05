import airsim_basic_function as abf
import control_algorithm as ca
import drone_movement as dm
import read_file as rf

# Initialize
abf.drone_initialize()

# Take single piece of photo
abf.capture_single_picture()

# Perform drone movements
dm.drone_movement()
