import spotipy
import spotipy.util as util

username = ''
SPOTIPY_CLIENT_ID = ''
SPOTIPY_CLIENT_SECRET=''
SPOTIPY_REDIRECT_URI='https://www.google.com/'
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

spotify = spotipy.Spotify(util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI))
results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()