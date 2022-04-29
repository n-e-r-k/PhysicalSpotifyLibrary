##################################################################################################
# Name: PSL connect
# Purpose: Displays the spotify album cover
##################################################################################################
from tkinter import*
from spotipy.oauth2 import SpotifyClientCredentials
<<<<<<< HEAD
import sys
from pprint import pprint

username = ''
SPOTIPY_CLIENT_ID = ''
SPOTIPY_CLIENT_SECRET=''
SPOTIPY_REDIRECT_URI='https://www.google.com/'
SpotipyDevice = ''
class PSL_C(Canvas): 
   
    if len(sys.argv) > 1:
        urn = sys.argv[1]
    else:
        urn = 'spotify:album:5yTx83u3qerZF7GRJu7eFk'

    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    album = sp.album(urn)
    pprint(album)

=======
import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

username = 'Fish'
SPOTIPY_CLIENT_ID = ''
SPOTIPY_CLIENT_SECRET=''
SPOTIPY_REDIRECT_URI='https://www.google.com/'
scope = 'user-read-private user-read-playback-state user-modify-playback-state'
class PSL_C(Canvas): 
    # TODO set up init function here
    self.spotify = spotipy.Spotify(util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI))
    # Get track information
    track = spotifyObject.current_user_playing_track()
    print(json.dumps(track, sort_keys=True, indent=4))
    print()
    artist = track['item']['artists'][0]['name']
    track = track['item']['name']
>>>>>>> 9c9a367c7604889f7cbc5575769a241f4f87c6f8

    if artist !="":
        print("Currently playing " + artist + " - " + track)
#################################################################################
#
# Main Code
#
#################################################################################
# sets size of the canvas
WIDTH = 600
HEIGHT = 520
window = Tk()
window.geometry("{}x{}".format(WIDTH,HEIGHT))
window.title("PSL Connect")
p = PSL_C(window)
window.mainloop()