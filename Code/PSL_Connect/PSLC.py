##################################################################################################
# Name: PSL connect
# Purpose: Displays the spotify album cover
##################################################################################################
from tkinter import*
import os
import sys
import json
from turtle import update
import spotipy 
import webbrowser
import spotipy.util as util
import PSL
from json.decoder import JSONDecodeError


class PSL_C(Canvas): 
    WIDTH = 600
    HEIGHT = 520
    window = Tk()
    window.geometry("{}x{}".format(WIDTH,HEIGHT))
    window.title("PSL Connect")
    
    # TODO set up init function here
    def __init__(self):

        main = PSL.PSL('<full path to credentials directory>', debugstatus = 3)


        # Get track information
        track = main.spotifyObject.current_user_playing_track()
        print(json.dumps(track, sort_keys=True, indent=4))
        print()

    def artist(self, track):
        artist = track['item']['artists'][0]['name']
        return artist

    def song(self, track):
        song = track['item']['name']
        return song

    song_name = Label(window, text = song)
    artist_name = Label(window, text = artist)
    song_name.pack
    artist_name.pack
    def update(song_name, artist_name, song, artist, window):
        song_name[song]
        window.after(1000, update)
        
        artist_name[artist]
        window.after(1000, update)
    update()
    window.mainloop()
