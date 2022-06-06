import read_file as rf
import airsim_basic_function as abf


# Read single row of data
print('drone_movement.py-> data...')
coordinate = rf.read_csv('./test_coordinate/target_coordinate.csv')
cor, t_row, t_col = rf.get_csv_data_single_row_adj_element(coordinate, 0, 2, 11)
line = rf.read_txt('./test_coordinate/frcnn_test_info.txt', 79)
distance = rf.line_split(line, 7)

# Take off
abf.drone_takeoff(-10, 5)

# Approach filming location
'''
Use center coordinate to adjust detail relative coordinate.
Use the distance times a value as actual direct 
distance, and use known altitude, to calculate x and y movement to reach filming coordinate.
Assume current location are the picture taking coordinate (x,y) 
'''

# Approach target
'''
Use data above to locate drone at the top center of car.
'''

# Landing
abf.drone_landing(10, 5)

