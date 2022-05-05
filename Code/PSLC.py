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
from PIL import ImageTk,Image
import urllib.request
import io


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
# centers the album cover in TK
    def center_image(img, window):
        size = min(window.winfo_screenheight(), window.winfo_screenwidth())
        return img.resize((size, size))
    
    def download_image(image_url):
        width = (window.winfo_screenwidth() - img.width) // 2
        height = (window.winfo_screenheight() - img.height) // 2
        return width, height

    def artist(self, track):
        artist = track['item']['artists'][0]['name']
        return artist

    def song(self, track):
        song = track['item']['name']
        return song
    
    def album(self, track):
        album = track['album']['images'][0]['url']
        return album
    
    def show_album(window, album,):
        canvas = Tk.Canvas(window)
        canvas.config(background= "white")
        canvas.pack
        img = download_image(album)
        width, height = center_image(img, window)
        img = ImageTK.PhotoImage(img)
        canvas.create_image(width, height, image = img, anchor = 'nw')
        
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
