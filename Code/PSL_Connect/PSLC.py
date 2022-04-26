##################################################################################################
# Name: PSL connect
# Purpose: Displays the spotify album cover
##################################################################################################
from tkinter import*
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class PSL_C(Canvas): 
    
    lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    results = spotify.artist_top_tracks(lz_uri)

    for track in results['tracks'][:10]:
        print('track    : ' + track['name'])
        print('audio    : ' + track['preview_url'])
        print('cover art: ' + track['album']['images'][0]['url'])
        print()


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