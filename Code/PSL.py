# Jacob France & Brayden Fisher
# PSL Library

#--- Import ---#
from distutils.log import error
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
import timeout

import time
import os
import csv
from json.decoder import JSONDecodeError

import RPi.GPIO as GPIO
from pirc522 import RFID

#--- Definitions ---#
class PSL():
    def __init__(self, credentialsDirectory, scope = 'user-read-private user-read-playback-state user-modify-playback-state', debugStatus = 1, connect = True, platform = "PI"):
        #Declairing Class Variables
        self.scope = scope
        self.debugStatus = debugStatus

        self.button = 32
        self.servo = 33

        #Setting platform
        if platform == "PC":
            self.platform = "PC"
        elif platform == "PI":
            self.platform = "PI"

            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(self.servo, GPIO.OUT)
            GPIO.setup(self.button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

            self.pwm = GPIO.PWM(self.servo, 50)
            self.pwm.start(0)

            self.rfid = RFID()

        print("Finsihed setting platform.")

        #Establish connection to spotify
        self.loadCredentials(credentialsDirectory)

        if connect:
            self.connect()
        else:
            pass
        

    def loadCredentials(self, directory):

        #Open and read from the csv in the given directory.
        #Then assign the class variables from the information 
        #that was listed on the file.

        csvFile = open(directory, mode = 'r')

        credentialsImport = csv.reader(csvFile, delimiter = ',')
        credentialsList = []

        #Convert the interable object into a list.
        for row in credentialsImport:
            credentialsList.append(row[0])

        self.spotifyUsername = credentialsList[0]
        self.spotifyClientID = credentialsList[1]
        self.spotifyClientSecret = credentialsList[2]
        self.spotifyDevice = credentialsList[3]
        self.libraryDirectory = credentialsList[4]
        self.redirectURL = credentialsList[5]

        #Cleanup by closing the file.
        csvFile.close()

        self.debugMessage(1, f"Credentials imported from {directory} correctly.")
        self.debugMessage(2, f"Username:{self.spotifyUsername}\
            \nClientID:{self.spotifyClientID}\
            \nClientSecret:{self.spotifyClientSecret}\
            \nDevice:{self.spotifyDevice}\
            \nLibrary Directory:{self.libraryDirectory}\
            \nRedirect URL:{self.redirectURL}\n")

    def load(self):

        self.database = {}

        export = csv.reader(open(self.libraryDirectory, mode = 'r'))
        try:
            for row in export:
                self.database[row[0]] = row[1]
            self.debugMessage(1, f"Database loaded.\n{self.database}")
        except:
            self.debugMessage(0, "NO DATABASE FOUND.")
        pass

    def save(self):
        file = open(self.libraryDirectory, "w")
        w = csv.writer(file)

        # {CID:URI}
        for cid, uri in self.database.items():
            w.writerow([cid, uri])

        file.close()

    def connect(self):
        try:
            self.spotifyObject = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.spotifyClientID, client_secret=self.spotifyClientSecret, redirect_uri=self.redirectURL, scope=self.scope, open_browser=False))
        except:
            print("Cache not found. Generate or supply a chache to continue.")
            exit()
        self.debugMessage(2, f"Connection to SPOTIFY established.\nPermissions aquired:\n{self.scope}")

    @timeout.timeout(1)
    def pull(self):
        result = ''
        while result == '':
            self.rfid.wait_for_tag()
            (error, tag_type) = self.rfid.request()

            if not error:
                (error, uid) = self.rfid.anticoll()

                if not error:
                    self.debugMessage(1, 'UID:'+str(uid))

            
                for section in uid:
                    result += str(section) 
        return result


    def read(self):
        try:
            product = self.pull()
            return product
        except:
            return None

    def write(self, uri):
        cid = self.pull()
        self.database[cid] = uri

    def play(self, uri):
        try:
            self.playAlbum(uri)
        except:
            self.playTrack(uri)

    def playTrack(self, uri):
        if uri != None:
            self.spotifyObject.start_playback(self.spotifyDevice, uris = [uri])
        else:
            self.spotifyObject.start_playback(self.spotifyDevice)

    def playAlbum(self, uri):
        z = 0
        trackURIS = []
        if uri != None:
            trackResults = self.spotifyObject.album_tracks(uri)
            trackResults = trackResults['items']
            self.debugMessage(1,'Playing:')
            for item in trackResults:
                self.debugMessage(1, str(z) + ': ' +item['name'])
                trackURIS.append(item['uri'])
                z+=1
            self.spotifyObject.start_playback(self.spotifyDevice, None, trackURIS)
        else:
            self.spotifyObject.start_playback(self.spotifyDevice)

    def pause(self):
        self.spotifyObject.pause_playback()

    def eject(self):
        self.setAngle(0)
        self.setAngle(90)
        self.setAngle(0)

    def setAngle(self, angle):
        duty = angle / 18 + 2
        GPIO.output(self.servo, True)
        self.pwm.ChangeDutyCycle(duty)
        time.sleep(1)
        GPIO.output(self.servo, False)
        self.pwm.ChangeDutyCycle(0)

    def cleanUp(self):
        self.rfid.cleanup()
        if self.platform == "PI":
            self.GPIO.cleanup()
        else:
            pass

    def debugMessage(self, verbosityLevel, message):
        if self.debugStatus >= verbosityLevel:
            print(message)
        else:
            pass