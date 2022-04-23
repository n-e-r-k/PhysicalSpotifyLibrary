
import time
import pickle5 as pickle
import os
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError

Direc = '/home/pi/obj/data.pkl'

UID = 0
Data = {}
TrackURIS = []
CurrentUID = None
DC = False

username = ''
SPOTIPY_CLIENT_ID = ''
SPOTIPY_CLIENT_SECRET=''
SPOTIPY_REDIRECT_URI='https://www.google.com/'
SpotipyDevice = ''
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

try:
    token = util.prompt_for_user_token(username, scope, client_id= SPOTIPY_CLIENT_ID,
                           client_secret= SPOTIPY_CLIENT_SECRET,
                           redirect_uri=SPOTIPY_REDIRECT_URI)
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)

spotifyObject = spotipy.Spotify(auth=token)

class CO:
    def __init__(self):
        pass

    def nfcRead(sec, sep):
        return None

    def loadDict(Directory):
        with open(Directory, 'rb') as f:
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

Data = dict(CO.loadDict(Direc))

while True:
    UID = CO.nfcRead(5,'!')

    if UID == '':
        UID = None
        print('UID equals none')
    elif UID != None:
        URI = Data[UID]
        print('UID has data')

    if UID != None:
        if UID != CurrentUID:
            CO.playAlbum(URI, SpotipyDevice)
            print('Playing:', URI)
            DC = False
        elif DC == True:
            if UID == CurrentUID:
                CO.playAlbum(None, SpotipyDevice)
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
