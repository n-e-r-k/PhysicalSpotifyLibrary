##################################################################################################
# Name: PSL connect
# Purpose: Displays the spotify album cover
##################################################################################################
from tkinter import*
from spotipy.oauth2 import SpotifyClientCredentials
import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

username = 'Fish'
SPOTIPY_CLIENT_ID = 'c2f887c733274f7087836d78574fb588'
SPOTIPY_CLIENT_SECRET='e7be691ec4254d839d0552a085736089'
SPOTIPY_REDIRECT_URI='https://www.google.com/'
scope = 'user-read-private user-read-playback-state user-modify-playback-state'
class PSL_C(Canvas): 
    
    # Get track information
    track = spotifyObject.current_user_playing_track()
    print(json.dumps(track, sort_keys=True, indent=4))
    print()
    artist = track['item']['artists'][0]['name']
    track = track['item']['name']

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