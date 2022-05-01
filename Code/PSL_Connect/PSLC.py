##################################################################################################
# Name: PSL connect
# Purpose: Displays the spotify album cover
##################################################################################################
from tkinter import*
import os
import sys
import json
import spotipy 
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError


class PSL_C(Canvas): 
    # TODO set up init function here
    def __init__(self):

        username = 'Fish'
        SPOTIPY_CLIENT_ID = ''
        SPOTIPY_CLIENT_SECRET=''
        SPOTIPY_REDIRECT_URI='https://www.google.com/'
        scope = 'user-read-private user-read-playback-state user-modify-playback-state'

        self.spotify = spotipy.Spotify(util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI))
        # Get track information
        track = spotifyObject.current_user_playing_track()
        print(json.dumps(track, sort_keys=True, indent=4))
        print()

    def artist():
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
p = PSL_C()
e = Entry(window)
e.pack

def callback():
        f = open("htfl.txt","a") #Replace htfl with artist name and song
        f.write(e.get())
        print (e.get())

b = Button(master, text="get", width=10, command=callback)

b.pack()



file = open() #Have it read the artist and song name out

#print(file.read(1))
a = file.read()
b = file.read()
print(file.read())

T = Text(master, height=9, width=30)
T.insert(END,a)
T.pack()

def update():
    with open() as f:
        data = f.read()
        T.delete("1.0", "end")  # if you want to remove the old data
        T.insert(END,data)
    T.after(1000, update)
window.mainloop()