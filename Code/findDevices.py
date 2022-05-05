from PSL import PSL

main = PSL('/home/pi/credentials.csv', debugStatus = 3)

print(main.spotifyObject.devices)