import spotipy
from spotipy.oauth2 import util

def song(spotifyUsername, spotifyClientID, spotifyClientSecret, spotifyDevice, libraryDirectory = '/data.csv', redirectURL = 'http://127.0.0.1:9090', scope = 'user-read-private user-read-playback-state user-modify-playback-state', debugStatus = 1):
        #Declairing Class Variables
        spotifyUsername = spotifyUsername
        spotifyClientID = spotifyClientID
        spotifyClientSecret = spotifyClientSecret
        spotifyDevice = spotifyDevice
        libraryDirectory = libraryDirectory
        redirectURL = redirectURL
        scope = scope
        debugStatus = debugStatus

def connect(self):

        try:

            #Attempt to connect to spotify if 
            token = util.prompt_for_user_token(spotifyUsername, scope, client_id = spotifyClientID, client_secret = spotifyClientSecret, redirect_uri = redirectURL)

        return token


song('braydenfisher02@gmail.com', , )

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

spotify = spotipy.Spotify(auth=connect())
results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()