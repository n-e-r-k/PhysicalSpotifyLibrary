# Jacob France & Brayden Fisher
# PSL Library

#--- Import ---#
import spotipy
import spotipy.util as util

import time
import os
import csv
from json.decoder import JSONDecodeError

#--- Definitions ---#
class PSL():
    def __init__(self, credentialsDirectory, scope = 'user-read-private user-read-playback-state user-modify-playback-state', debugStatus = 1, connect = True, platform = "PI"):
        #Declairing Class Variables
        self.scope = scope
        self.debugStatus = debugStatus

        self.button = 32
        self.servo = 36

        #Setting platform
        if platform == "PC":
            self.platform = "PC"
        elif platform == "PI":
            self.platform = "PI"
            #Make the imports more standard?
            import RPi.GPIO
            from pirc522 import RFID

            self.GPIO = RPi.GPIO()
            self.GPIO.setmode(self.GPIO.BCM)
            self.GPIO.setup(self.servo, self.GPIO.OUT)

            self.pwm = self.GPIO.PWM(self.servo, 50)
            self.pwm.start(0)

            self.rfid = RFID()

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

        #Check if there is a timeout part of that function.

        self.rfid.wait_for_tag()
        (error, tag_type) = self.rfid.request()

        if not error:
            (error, uid) = self.rfid.anticoll()

            if not error:
                self.debugMessage(1, 'UID:'+str(uid))
        
        return uid

    def play(self, uri):

        #Currently don't know if you can play any type of uri or
        #if only for single tracks.

        if uri == None:
            #Pause playback?
            pass
        
        self.spotifyObject.start_playback()

    def pause(self):
        
        self.spotifyObject.pause_playback()

    def eject(self):
        self.setAngle(0)
        self.setAngle(90)

    def setAngle(self, angle):
        duty = angle / 18 + 2
        self.GPIO.output(self.servo, True)
        self.pwm.ChangeDutyCycle(duty)
        time.sleep(1)
        self.GPIO.output(self.servo, False)
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

#--- Main(TEMP) ---#
#Should only be a library. Leaving this just for testing.


#Tell brayden to put this directory into somewhere not tracked by git for convience.
#Also, we need to find a way to do a relative path to the python file. 'Cause, having
#to do direct paths IN the code would ruin the "plug-and-play" -ability.

#main = PSL('/home/nerk/Documents/Code/Keys/credentials.csv', debugStatus = 3, connect = False, platform = "PC")
#main.load()
