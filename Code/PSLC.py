##################################################################################################
# Name: PSL connect
# Purpose: 
##################################################################################################
from tkinter import*
from PSL import PSL



class PSL_C(Canvas): 
    WIDTH = 600
    HEIGHT = 520
    window = Tk()
    window.geometry("{}x{}".format(WIDTH,HEIGHT))
    window.title("PSL Connect")
    
    # TODO set up init function here
    def __init__(self):

        main = PSL('/home/pi/credentials.csv', debugstatus = 3)

        # Get track information
        track = main.spotifyObject.current_user_playing_track()
        print(track['Album'])
        
    song_name = Label(window, text = song)
    artist_name = Label(window, text = artist)
    song_name.pack
    artist_name.pack

    def update(song_name, artist_name, song, artist, window):
        song_name[song]
        window.after(1000, update)
        
        artist_name[artist]
        window.after(1000, update)
    
frst = PSL_C()

#update()
#window.mainloop()
