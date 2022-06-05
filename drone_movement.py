import airsim
import pprint
import read_file as rf


# Read single row of data
print('drone_movement.py-> reading coordinate...')
coordinate = rf.read_csv('./test_coordinate/target_coordinate.csv')
cor, t_row, t_col = rf.get_csv_data_single_row_adj_element(coordinate, 0, 2, 11)
'''
    print_csv_data_single_row_adj_element() function test
        print('main.py-> coordinate array: ', cor)
        print('main.py-> total row: ', t_row)
        print('main.py-> total column: ', t_col)
    '''

# Take off
client = airsim.MultirotorClient()
client.takeoffAsync().join()
print('drone_movement.py-> Drone take off')

# Approach filming location

# Approach target

# Landing



'''
# z axis number is what each every command needs to maintained.
print('drone_movement.py-> Move up...')
client.moveByVelocityZAsync(0, 0, -10, 10, airsim.DrivetrainType.MaxDegreeOfFreedom, airsim.YawMode(True, 0)).join()
print('drone_movement.py-> Move right...')
client.moveByVelocityZAsync(0, 5, 0, 5, airsim.DrivetrainType.MaxDegreeOfFreedom, airsim.YawMode(True, 0)).join()
print('drone_movement.py-> Move front...')
client.moveByVelocityZAsync(5, 0, 5, 10, airsim.DrivetrainType.MaxDegreeOfFreedom, airsim.YawMode(True, 0)).join()

client.moveByVelocityZAsync(0, 0, -10, 10, airsim.DrivetrainType.MaxDegreeOfFreedom, airsim.YawMode(True, 0)).join()
client.moveByVelocityZAsync(0, 5, -10, 10, airsim.DrivetrainType.MaxDegreeOfFreedom, airsim.YawMode(True, 0)).join()


client.moveToPositionAsync(-10, 10, -10, 5).join()
# Async methods returns Future. Call join() to wait for task to complete.

# Get drone state
state = client.getMultirotorState()
s = pprint.pformat(state)
print("drone_movement.py-> state: %s" % s)
'''
