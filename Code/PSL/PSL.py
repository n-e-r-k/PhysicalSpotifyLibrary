# Jacob France & Brayden Fisher
# PSL Library

#NOTE: Double comments are meant to be removed when running on the raspberry pi.
#PC vs PCL version? - yeah that makes sense. Remind brayden to incorperate this library into his code
#so that way the consumer 

#--- Import ---#
##from pirc522 import RFID

import spotipy
import spotipy.util as util

import os
import csv
from json.decoder import JSONDecodeError

class PSL():
    def __init__(self, credentialsDirectory, scope = 'user-read-private user-read-playback-state user-modify-playback-state', debugStatus = 1):
        #Declairing Class Variables
        self.scope = scope
        self.debugStatus = debugStatus

        ##self.rfid = RFID()

        #Setup
        self.loadCredentials(credentialsDirectory)
        self.connect()
        

    def loadCredentials(self, directory):

        csvFile = open(directory, mode = 'r')

        credentialsImport = csv.reader(csvFile, delimiter = ',')
        credentialsList = []

        for row in credentialsImport:
            credentialsList.append(row)

        print(credentialsList)

        #TBH this section probably goes beyond the scope of the project and is a waste of time...
        #But I do wanna see it work tho.

        self.spotifyUsername = str(credentialsList[0])
        self.spotifyClientID = str(credentialsList[1])
        self.spotifyClientSecret = str(credentialsList[2])
        self.spotifyDevice = str(credentialsList[3])
        self.libraryDirectory = str(credentialsList[4])
        self.redirectURL = str(credentialsList[5])

        #ISSUE: It seems that the stringed verstion of the list entries are apearing with the brackets of a list in these fields?
        #IDK its like 2:31 am and I need to sleep. Good luck future me.

        print(self.spotifyUsername)

        csvFile.close()

        self.debugMessage(1, f"Credentials imported from {directory} correctly.")


    
    def load(self):

        self.database = {}

        export = csv.DictReader(open(self.libraryDirectory, mode = 'r'))

        print(export)

        pass

    def save(self):
        w = csv.writer(open(self.libraryDirectory, "W"))

        # {CDI:URI}
        for cid, uri in self.database.items():
            w.writerow([cid, uri])
        
    def connect(self):

        try:

            #Attempt to connect to spotify if 
            token = util.prompt_for_user_token(self.spotifyUsername, self.scope, client_id = self.spotifyClientID, client_secret = self.spotifyClientSecret, redirect_uri = self.redirectURL)

        except (AttributeError, JSONDecodeError):

            #Remove the local .cache-username file
            os.remove(f".cache-{self.spotifyUsername}")
            #Attempt again
            token = util.prompt_for_user_token(self.spotifyUsername, self.scope)

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

    def cleanUp(self):
        self.rfid.cleanup()

    def debugMessage(self, verbosityLevel, message):
        if self.debugStatus >= verbosityLevel:
            print(message)
        else:
            pass

#--- Main ---#

#Tell brayden to put this directory into somewhere not tracked by git for convience.
#Also, we need to find a way to do a relative path to the python file. 'Cause, having
#to do direct paths IN the code would ruin the "plug-and-play" -ability.
main = PSL('')
PSL.play('spotify:track:1NWK3gKPZPATIdSKLNGV8D')