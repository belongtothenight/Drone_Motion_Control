import airsim
import msgpackrpc.error
import cv2
import os
import sys
import numpy as np

client = airsim.MultirotorClient()


def airsim_conn():
    """
    Description:
        Confirm connection with Unreal Engine 4, and deal with connection error.
    parameter:
        Input:
            None
        Output:
            None
    Link:
        None
    """
    try:
        client.confirmConnection()
    except msgpackrpc.error.TransportError:
        print('\nairsim_basic_function-> Unreal Engine isn\'t running or Project isn\'t playing...\n')


def drone_initialize():
    """
    Description:
        Initialize AirSim simulator in Unreal Engine 4.
    parameter:
        Input:
            None
        Output:
            None
    Link:
        https://microsoft.github.io/AirSim/apis/#python-quickstart
    """
    airsim_conn()
    client.reset()
    print('airsim_basic_function-> Environment Reset!')
    client.enableApiControl(True)
    client.armDisarm(True)


def capture_single_picture(directory, image_name):
    """
    Description:
        Take one PGN photo and export to assigned directory.
    parameter:
        Input:
            directory: (str) The directory where you want to save the image. Format = './directory_name'
            image_name: (str) The name of the image. Format = 'image_name'
        Output:
            None
    Link:
        https://stackoverflow.com/questions/57150426/what-is-printf
        https://microsoft.github.io/AirSim/image_apis/#using-airsim-images-with-numpy
    """
    airsim_conn()
    # Create image directory if it doesn't already exist
    try:
        os.stat(directory)
    except:
        os.mkdir(directory)

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
    cv2.imwrite(f'{directory}/{image_name}.png', img_rgb)
    print('airsim_basic_function-> Screenshot Captured!')
    print(f'airsim_basic_function-> Store at {directory}/{image_name}.png')
