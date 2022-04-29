##################################################################################################
# Name: PSL connect
# Purpose: Displays the spotify album cover
##################################################################################################
from tkinter import*
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
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