from PSL import PSL

main = PSL('/home/pi/credentials.csv', debugStatus = 3)

devNum = 0

devices = main.spotifyObject.devices()

print(devices)