##################################################################################################
# Name: PSL connect
# Purpose: 
##################################################################################################
from tkinter import*
from time import time
from PSL import PSL

class PSL_C(Canvas): 
    WIDTH = 600
    HEIGHT = 520
    window = Tk()
    window.geometry("{}x{}".format(WIDTH,HEIGHT))
    window.title("PSL Connect")
    
    # TODO set up init function here
    def __init__(self):

        self.main = PSL('/home/pi/credentials.csv', debugstatus = 3)

    def getInfo(self):

        # Get track information
        track = self.main.spotifyObject.current_user_playing_track()
        self.song = track['song']
        self.album = track['album']
        self.tracks = self.main.spotifyObject.album_tracks(self.album)
        self.artist = track['artist']
        
    def packWindow(self):
        self.song_name = Label(self.window, text = self.song)
        self.artist_name = Label(self.window, text = self.artist)
        self.album_tracks = Label(self.window, text = self.tracks)
        self.song_name.pack
        self.artist_name.pack
        self.album_tracks.pack

    def updateWindow(self):
        self.getInfo()
        self.song_name.set(self.song)
        self.artist_name.set(self.artist)
        self.album_tracks.set(self.tracks)
        
        self.window.update_idletasks()
        
    
frst = PSL_C()
frst.window.mainloop()

while True:
    frst.updateWindow()
    time.wait(2)
