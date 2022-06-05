import pprint
import pygame as pg
import airsim
import os
import msgpackrpc.error
import numpy as np
import cv2
import time
import control_method

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.reset()
client.enableApiControl(True)
client.armDisarm(True)

# Async methods returns Future. Call join() to wait for task to complete.
client.takeoffAsync().join()
print('Drone take off')

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


'''
# Create image directory if it doesn't already exist
try:
    os.stat('./captured_image')
except:
    os.mkdir('./captured_image')

# Export PNG Image
# Image
responses = client.simGetImages([airsim.ImageRequest("0", airsim.ImageType.Scene, False, False)])
response = responses[0]

# get numpy array
img1d = np.fromstring(response.image_data_uint8, dtype=np.uint8)

# reshape array to 4 channel image array H X W X 4
img_rgb = img1d.reshape(response.height, response.width, 3)

# original image is fliped vertically
img_rgb = np.flipud(img_rgb)

# write to png
img_rgb = cv2.flip(img_rgb, 1)
img_rgb = cv2.rotate(img_rgb, cv2.cv2.ROTATE_180)
cv2.imwrite('./captured_image/1.png',img_rgb)
print('Script Executed!')
'''