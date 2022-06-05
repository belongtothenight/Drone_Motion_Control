import airsim
import pprint


#def drone_movement():
client = airsim.MultirotorClient()

# Async methods returns Future. Call join() to wait for task to complete.
client.takeoffAsync().join()
print('Drone take off')


# Get drone state
state = client.getMultirotorState()
s = pprint.pformat(state)
print("state: %s" % s)



print('Move up...')
client.moveByVelocityZAsync(0, 0, -10, 10, airsim.DrivetrainType.MaxDegreeOfFreedom, airsim.YawMode(True, 0)).join()
print('Move right...')
client.moveByVelocityZAsync(0, 5, 0, 5, airsim.DrivetrainType.MaxDegreeOfFreedom, airsim.YawMode(True, 0)).join()
print('Move front...')
client.moveByVelocityZAsync(5, 0, 5, 10, airsim.DrivetrainType.MaxDegreeOfFreedom, airsim.YawMode(True, 0)).join()

client.moveByVelocityZAsync(0, 0, -10, 10, airsim.DrivetrainType.MaxDegreeOfFreedom, airsim.YawMode(True, 0)).join()
client.moveByVelocityZAsync(0, 5, -10, 10, airsim.DrivetrainType.MaxDegreeOfFreedom, airsim.YawMode(True, 0)).join()
# z axis number is what each every command needs to maintained.

# client.moveToPositionAsync(-10, 10, -10, 5).join()
