import airsim
import msgpackrpc.error
import cv2
import os
import numpy as np

client = airsim.MultirotorClient()


def airsim_conn():
    try:
        client.confirmConnection()
    except msgpackrpc.error.TransportError:
        print('\nUnreal Engine isn\'t running or Project isn\'t playing...\n')


# Initialize AirSim simulator
def drone_initialize():
    airsim_conn()
    client.reset()
    print('Environment Reset!')
    client.enableApiControl(True)
    client.armDisarm(True)


# Take one PGN photo
def capture_single_picture():
    airsim_conn()
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

    # Flip and rotate image
    img_rgb = cv2.flip(img_rgb, 1)
    img_rgb = cv2.rotate(img_rgb, cv2.cv2.ROTATE_180)

    # write to png
    cv2.imwrite('./captured_image/1.png', img_rgb)
    print('Screenshot Captured!')
