import numpy
import airsim_basic_function as abf


'''
Dimension unit in UE4 is set to 10 times larger as real world number.
'''


def drone_approach_filming_location():
    """
    Description:
        Use center coordinate to adjust detail relative coordinate.
        Use the distance times a value as actual direct distance, and use known altitude, to calculate x and y movement
            to reach filming coordinate.
        Use total frame count(same distance, different angle) of the original video to simulate original filming
            coordinate.
    parameter:
        Input:

        Output:

    Link:

    """
    print('')


def drone_approach_target(x, y):
    """
    Description:
        Use data above to locate drone at the top center of car.
        x_distance:y_pixel = 9:498
        Use the same ratio for y distance and x pixel
    parameter:
        Input:

        Output:

    Link:
        https://stackoverflow.com/questions/63789706/arithmetic-operation-on-array-causes-typeerror-unsupported-operand-types-for
    """
    drone_x_distance = float(x) / 498 * 9
    drone_y_distance = (float(y) - (1920 / 2)) / 498 * 9
    print(f'control_algorithm.py-> Approach_Target(x,y)=({drone_x_distance},{drone_y_distance})')
    abf.drone_move_to_position(drone_x_distance, drone_y_distance, 10, 5)
