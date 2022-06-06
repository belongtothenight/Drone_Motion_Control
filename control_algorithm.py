import math
import airsim_basic_function as abf


'''
Dimension unit in UE4 is set to 10 times larger as real world number.
'''
filming_hight = 12


def drone_approach_filming_location(frame_count, index_of_coordinate):
    """
    Description:
        Use center coordinate to adjust detail relative coordinate.
        Use measured length to calculate x and y movement, reaching filming coordinate.
        Use total frame count(same distance, different angle) of the original video to simulate original filming
            coordinate.
        The filming path is a circle above target.
    parameter:
        Input:
            (total_frame_count: Total number of images filmed.)
            frame_count: Total number of images that is tested.
            index_of_coordinate: Which photo it is in the filming sequence.
        Output:
            None
    Link:
        None
    """
    obj_x = 9
    obj_y = 0
    total_frame_count = 1174
    l = 10 #100cm

    frame_count = float(frame_count)
    degree = frame_count/total_frame_count*360
    print('control_algorithm.py-> ' + str(degree))
    real_degree = index_of_coordinate / frame_count * degree

    drone_x = obj_x + l * math.sin(real_degree - 90)
    drone_y = obj_y + l * math.cos(real_degree - 90)
    print(f'control_algorithm.py-> filming coordinate(x,y)=({drone_x},{drone_y})')

    abf.drone_move_to_position(drone_x, drone_y, filming_hight, 5)



def drone_approach_target(x, y):
    """
    Description:
        Use data above to locate drone at the top center of car.
        x_distance:y_pixel = 9:498 (roughly tested, more need to be done on x and y-axis to obtain precise landing
            performance.)
        Use the same ratio for y distance and x pixel
    parameter:
        Input:
            x: (int) Center x coordinate from test result.
            y: (int) Center y coordinate from test result.
        Output:
        None
    Link:
        https://stackoverflow.com/questions/63789706/arithmetic-operation-on-array-causes-typeerror-unsupported-operand-types-for
    """
    drone_x_distance = float(x) / 498 * 9
    drone_y_distance = (float(y) - (1920 / 2)) / 498 * 9
    print(f'control_algorithm.py-> Approach_Target(x,y)=({drone_x_distance},{drone_y_distance})')
    abf.drone_move_to_position(drone_x_distance, drone_y_distance, filming_hight, 5)
