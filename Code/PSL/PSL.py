# Jacob France & Brayden Fisher
# PSL Library

#--- Import ---#
from pirc522 import RFID

import spotipy
import spotipy.util as util

import time
import os
import csv
from json.decoder import JSONDecodeError

class PSL():
    def __init__(self, spotifyUsername, spotifyClientID, spotifyClientSecret, spotifyDevice, libraryDirectory = '/data.csv', redirectURL = 'http://127.0.0.1:9090', scope = 'user-read-private user-read-playback-state user-modify-playback-state', debugStatus = 1):
        #Declairing Class Variables
        self.spotifyUsername = spotifyUsername
        self.spotifyClientID = spotifyClientID
        self.spotifyClientSecret = spotifyClientSecret
        self.spotifyDevice = spotifyDevice
        self.libraryDirectory = libraryDirectory
        self.redirectURL = redirectURL
        self.scope = scope
        self.debugStatus = debugStatus

        self.rfid = RFID()

        #Setup
        self.connect()
        


    
    def load(self):
        self.database = {}

        #Data here uwu

        pass

    def save(self):
        w = csv.writer(open(self.libraryDirectory, "W"))

        # {CDI:URI} Every cassette will have a URI attached after it is written
        for cid, uri in self.database.items():
            w.writerow([cid, uri])
        
    def connect(self):

        try:

            #Attempt to connect to spotify if 
            token = util.prompt_for_user_token(self.spotifyUsername, self.scope, client_id = self.spotifyClientID, client_secret = self.spotifyClientSecret, redirect_uri = self.redirectURL)

        except (AttributeError, JSONDecodeError):

            #Remove the local .cache-username file
            os.remove(f".cache-{self.username}")
            #Attempt again
            token = util.prompt_for_user_token(self.username, self.scope)

        self.spotifyObject = spotipy.Spotify(auth=token)

        self.debugMessage(2, f"Connection to SPOTIFY established.\nPermissions aquired:\n{self.scope}")

    def read(self):

        #I suspect that this wait_for_tag() will be and issue (Due to taking up the 
        # process and not timing out making us unable to have a "EMPTY SLOT" state)
        #If thats the case then we will have to move the library
        #to "MFRC522-python" I think it's on github.

        self.rfid.wait_for_tag()
        (error, tag_type) = self.rfid.request()

        if not error:
            (error, uid) = self.rfid.anticoll()

            if not error:
                self.debugMessage(1, 'UID:'+str(uid))

    def play(self, uri):

        #Currently don't know if you can play any type of uri or
        #if only for single tracks.
        self.spotifyObject.start_playback(uris=[uri])

    def eject(self):
        pass

    def playAlbum(self, albumURI):
        #Uneeded if the play() function can play a full albumURI
        #Without needed it to be split into tracks.

    def cleanUp(self):
        self.rfid.cleanup()

    def debugMessage(self, verbosityLevel, message):
        if self.debugStatus >= verbosityLevel:
            print(message)
        else:
            pass