import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util

import os
import csv
from json.decoder import JSONDecodeError

spotifyUsername = ''
spotifyClientID = ''
spotifyClientSecret = ''
spotifyDevice = ''
libraryDirectory = ''
redirectURL = ''

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

        spotifyUsername = credentialsList[0]
        spotifyClientID = credentialsList[1]
        spotifyClientSecret = credentialsList[2]
        redirectURL = credentialsList[5]

        #Cleanup by closing the file.
        csvFile.close()

        return spotifyUsername, spotifyClientID, spotifyClientSecret, redirectURL


def generateCache(spotifyUsername, spotifyClientID, spotifyClientSecret, redirectURL):
    try:

        #Attempt to connect to spotify if 
        token = util.prompt_for_user_token(spotifyUsername, 'user-read-private user-read-playback-state user-modify-playback-state', client_id = spotifyClientID, client_secret = spotifyClientSecret, redirect_uri = redirectURL)

    except (AttributeError, JSONDecodeError):

        #Remove the local .cache-username file
        os.remove(f".cache-{spotifyUsername}")
        #Attempt again
        token = util.prompt_for_user_token(spotifyUsername, 'user-read-private user-read-playback-state user-modify-playback-state')

        return token

def main():
    spotifyUsername, spotifyClientID, spotifyClientSecret, redirectURL = loadCredentials()
    token = generateCache(spotifyUsername, spotifyClientID, spotifyClientSecret, redirectURL)
    spotipy.Spotify(auth=token)
    print("Finished")

main()