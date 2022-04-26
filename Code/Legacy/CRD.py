#Jacob France

import serial
import time
import os
import json
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError

print('Import Finished')

#--- SETUP ---#

#Defines COM Number for serial communications.
#NOTE:We will remove the serial capabilities because we will move from
#using an arduino to onboard GPIO.
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

#To ensure time for COM to setup.
time.sleep(2)

print('Serial Communications Established')

#Dirctory of PKL 
Direc = '/home/pi/obj/data.pkl'

#Global Varibles
UID = 0
Data = {}
TrackURIS = []
CurrentUID = None
DC = False

print('Global Variables Assigned')

#Spotipy config
#NOTE:Will not work without a valid username, Client ID, Client Secret
#I had to take off my personal account, but just ask me and I can get them to
#you.

username = ''
SPOTIPY_CLIENT_ID = 'c2f887c733274f7087836d78574fb588'
SPOTIPY_CLIENT_SECRET='e7be691ec4254d839d0552a085736089'
SPOTIPY_REDIRECT_URI='https://www.google.com/'
SpotipyDevice = ''
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

print('Spotify [Client ID, Client Secret, Redirect URL, Playing Device, Scope] Established')

#Login process. This was taken straight from the spotipy docs. It seems to work,
#But I don't have a full understanding of how it works.

try:
    token = util.prompt_for_user_token(username, scope, client_id= SPOTIPY_CLIENT_ID,
                           client_secret= SPOTIPY_CLIENT_SECRET,
                           redirect_uri=SPOTIPY_REDIRECT_URI)
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)

spotifyObject = spotipy.Spotify(auth=token)

print('Connection With Spotify Authorization Established')
print('End Of Setup')

#--- definitions ---#

#NOTE: This whole definitions section will need to rewrote in
#object oriented paradigm. Also, We need to remove any serial
#commands and rewrite them using new libraries directly
#controlling the GPIO.

def nfcRead(sec, sep):
    for i in range(sec):
        string_n = serialReadLine()
        if sep in string_n:
            new = string_n.split(sep)
            ser.close()
            ser.open()
            ser.isOpen()
            return(new[1])
    ser.close()
    ser.open()
    ser.isOpen()
    return None

def serialReadLine():
    b = ser.readline()
    running = True
    while running:
        try:
            decodeStr = b.decode()
            return(decodeStr)
        except:
            print('error_reading')


def loadDict(Fname):
    with open(Fname, 'rb') as f:
        return pickle.load(f)

def saveDict(Dicton, Fname):
    with open(Fname, 'wb') as f:
        pickle.dump(Dicton, f, pickle.HIGHEST_PROTOCOL)

def playAlbum(AlbumUID, PlayingDevice):
    z = 0
    TrackURIS = []
    if AlbumUID != None:
        trackResults = spotifyObject.album_tracks(AlbumUID)
        trackResults = trackResults['items']
        print('Playing:')
        for item in trackResults:
            print(str(z) + ': ' +item['name'])
            TrackURIS.append(item['uri'])
            z+=1
        spotifyObject.start_playback(PlayingDevice, None, TrackURIS)
    else:
        spotifyObject.start_playback(PlayingDevice)

print('End Of Definitions')

#--- main ---#

print('Card Reader Operations: Start')

Data = dict(loadDict(Direc))

print('Database:')
print(Data)

#NOTE: This is the main code, this should largely stay the same
#throught the conversion. Let me know through push requests if
#you would like to make changes to this section.
##########################################################################################################
# Main Code
##########################################################################################################~
while True:
    UID = nfcRead(5,'!')

    if UID == '':
        UID = None
        print('UID equals none')
    elif UID != None:
        URI = Data[UID]
        print('UID has data')

    if UID != None:
        if UID != CurrentUID:
            playAlbum(URI, SpotipyDevice)
            print('Playing:', URI)
            DC = False
        elif DC == True:
            if UID == CurrentUID:
                playAlbum(None, SpotipyDevice)
                print('Resume Playing:')
                DC = False
    elif UID == None:
        if DC != True:
            if UID != CurrentUID:
                spotifyObject.pause_playback(SpotipyDevice)
                print('UID = None: Pausing Playback:')
                DC = True

    if UID != None:
        CurrentUID = UID

    time.sleep(2)
