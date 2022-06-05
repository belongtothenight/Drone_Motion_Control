import pprint
import pygame as pg
import airsim
import os
import msgpackrpc.error
import numpy as np
import cv2
import time
import control_method
import airsim_basic_function as abf

# connect to the AirSim simulator
abf.drone_initialize()
client = airsim.MultirotorClient()#temperary

# Async methods returns Future. Call join() to wait for task to complete.
client.takeoffAsync().join()
print('Drone take off')

# Take single piece of photo
abf.capture_single_picture()

try:
    state = client.getMultirotorState()
except msgpackrpc.error.RPCError:
    print('Vehicle doesn\'t exist')
s = pprint.pformat(state)
print("state: %s" % s)

'''
print('Move up...')
client.moveByVelocityZAsync(0, 0, -10, 10, airsim.DrivetrainType.MaxDegreeOfFreedom, airsim.YawMode(True, 0)).join()
print('Move right...')
client.moveByVelocityZAsync(0, 5, 0, 5, airsim.DrivetrainType.MaxDegreeOfFreedom, airsim.YawMode(True, 0)).join()
print('Move front...')
client.moveByVelocityZAsync(5, 0, 5, 10, airsim.DrivetrainType.MaxDegreeOfFreedom, airsim.YawMode(True, 0)).join()
'''
client.moveByVelocityZAsync(0, 0, -10, 10, airsim.DrivetrainType.MaxDegreeOfFreedom, airsim.YawMode(True, 0)).join()
client.moveByVelocityZAsync(0, 5, -10, 10, airsim.DrivetrainType.MaxDegreeOfFreedom, airsim.YawMode(True, 0)).join()
# z axis number is what each every command needs to maintained.

#client.moveToPositionAsync(-10, 10, -10, 5).join()


