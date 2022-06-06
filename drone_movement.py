import numpy as np
import read_file as rf
import airsim_basic_function as abf
import control_algorithm as ca


# Read data
print('drone_movement.py-> gathering data...')
coordinate = rf.read_csv('./test_coordinate/target_coordinate.csv')
cor, t_row, t_col = rf.get_csv_data_single_row_adj_element(coordinate, 0, 2, 11)
line1 = rf.read_txt('./test_coordinate/frcnn_test_info.txt', 15)
frame_count = rf.line_split(line1, 4)
line2 = rf.read_txt('./test_coordinate/frcnn_test_info.txt', 79)
distance = rf.line_split(line2, 7)

# Take off
abf.adjust_camera_angle(-42, 0)
abf.drone_takeoff(-10, 5)
abf.capture_single_picture('./captured_image', '1')

# Approach filming location
ca.drone_approach_filming_location(frame_count, 1)
abf.capture_single_picture('./captured_image', '2')

# Approach target
ca.drone_approach_target(cor[5], cor[4])
abf.adjust_camera_angle(-60, 0)
abf.capture_single_picture('./captured_image', '3')


# Landing
#abf.adjust_camera_angle(0, 0)
abf.drone_landing(10, 5)
abf.adjust_camera_angle(0, 0)