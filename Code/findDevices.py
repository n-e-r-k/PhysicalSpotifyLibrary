from PSL import PSL

main = PSL('/home/pi/credentials.csv', debugStatus = 3)

devNum = 0

for device in main.spotifyObject.devices:
    print(f"device {devNum}:" + device)
    devNum += 1