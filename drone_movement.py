import numpy as np
import read_file as rf
import airsim_basic_function as abf
import control_algorithm as ca


# Read single row of data
print('drone_movement.py-> data...')
coordinate = rf.read_csv('./test_coordinate/target_coordinate.csv')
cor, t_row, t_col = rf.get_csv_data_single_row_adj_element(coordinate, 0, 2, 11)
line = rf.read_txt('./test_coordinate/frcnn_test_info.txt', 79)
distance = rf.line_split(line, 7)

# Take off
abf.adjust_camera_angle(-42, 0)
abf.drone_takeoff(-10, 5)
# abf.capture_single_picture('./captured_image', '1')

# Approach filming location


# Approach target
ca.drone_approach_target(cor[5], cor[4])
# abf.capture_single_picture('./captured_image', '2')


# Landing
abf.adjust_camera_angle(21, 0)
abf.drone_landing(10, 5)
