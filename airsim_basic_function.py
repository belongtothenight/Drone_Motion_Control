import airsim
import msgpackrpc.error

# connect to the AirSim simulator
def drone_initialize():
    client = airsim.MultirotorClient()
    client.confirmConnection()
    client.reset()
    print('Environment Reset!')
    client.enableApiControl(True)
    client.armDisarm(True)