import requests

spotifyToken = ''
spotifyURL = 'https://api.spotify.com/v1/me/player/currently-playing'
lyricsURL = 'https://api.lyrics.ovh/v1/'

requestsHeaders = {'Authorization': f'Bearer {spotifyToken}'}
spotifyResponse = requests.get(spotifyURL,headers=requestsHeaders)
spotifyJSON = spotifyResponse.json()

if(spotifyResponse.status_code == 200 or 201):
    songArtist = spotifyJSON['item']['artists'][0]['name']
    songName = spotifyJSON['item']['name']

lyricsResponse = requests.get(f'{lyricsURL}/{songArtist}/{songName}')
lyricsJSON = lyricsResponse.json()
with open('currentSongLyrics.txt','w') as writeLyrics:
    writeLyrics.write(lyricsJSON['lyrics'])
    print('Lyrics were written to currentSongLyrics.txt!')
