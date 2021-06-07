import requests,json
from requests.api import delete

#THIS WILL DELETE THE PLAYLIST YOU CHOSE SO MAKE SURE THAT YOU MAKE A DUPLICATE UNLESS YOU DON'T CARE!
#THIS WILL DELETE THE PLAYLIST YOU CHOSE SO MAKE SURE THAT YOU MAKE A DUPLICATE UNLESS YOU DON'T CARE!
#THIS WILL DELETE THE PLAYLIST YOU CHOSE SO MAKE SURE THAT YOU MAKE A DUPLICATE UNLESS YOU DON'T CARE!
userID = input("Please enter your Spotify USERID(https://open.spotify.com/user/(USERID) everything after the id doesn't matter: ")
OAuth_Token = input("Please enter the token you generated!(https://developer.spotify.com/console/get-playlists/).\nGo to that site and click \"GET TOKEN\" then select the \"playlist-modify-public, playlist-modify-private, playlist-read-private, and playlist-read-collaborative\" buttons and generate the token!: ")
allplaylistsURL = 'https://api.spotify.com/v1/me/playlists'
headers = {"Authorization": f"Bearer {OAuth_Token}"}
artistDict = {}
playlistDict = {}

def checkExistingPlaylist():
    getPlaylists = requests.get(allplaylistsURL,headers=headers)
    jsonPlaylists = getPlaylists.json()
    for playlists in jsonPlaylists['items']:
        if playlists['name'] == 'Song Checker':
            songCheck = playlists['id']
            songAddition = f'https://api.spotify.com/v1/playlists/{songCheck}/tracks?uris='
            playlistChange = f'https://api.spotify.com/v1/playlists/{songCheck}'
        if playlists['name'] != 'Song Checker':
            playlistDict[jsonPlaylists['items'].index(playlists)] = playlists['name']
    for number,playlist in playlistDict.items():
        print(f'{number}) {playlist}')
    playlistNumber = int(input("What playlist are you interested in checking?: ")) 
    playlistURL = 'https://api.spotify.com/v1/playlists/' + jsonPlaylists['items'][playlistNumber]['id'] + '/tracks'
    playlistName = json.dumps({"name": playlistDict[playlistNumber] + ' NEW', "description": "This is the new playlist", "public": True})
    getPlaylists = requests.get(playlistURL,headers=headers)
    jsonSongs = getPlaylists.json()
    songNum = 0
    while len(jsonSongs['items']) > 0:
        getPlaylists = requests.get(playlistURL,headers=headers)
        jsonSongs = getPlaylists.json()
        for songs in range(len(jsonSongs['items'])):
            print('On song #' + str(songNum + 1) + ' | ' + jsonSongs['items'][songs]['track']['artists'][0]['name'] + ' - ' + jsonSongs['items'][songs]['track']['name'])
            songID = jsonSongs['items'][songs]['track']['id']
            uri = f'spotify:track:{songID}'
            deleteData = json.dumps({"tracks":[{"uri": uri,"positions": [0]}]})
            artistName = jsonSongs['items'][songs]['track']['artists'][0]['name']
            if (artistName) in artistDict:
                artistDict[artistName] += 1
            else:
                artistDict[artistName] = 1
            requests.delete(playlistURL,headers=headers,data=deleteData)
            requests.post(songAddition + uri,headers=headers)
            songNum += 1
    requests.put(playlistChange,headers=headers,data=playlistName)
    for k,v in artistDict.items():
        print(k + ': ' + str(v))

def createTempPlaylist(user_id):
    createPlaylistURL = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    data = json.dumps({"name":"Song Checker","description":"Playlist to go through songs!","public":False})
    getPlaylists = requests.get(allplaylistsURL,headers=headers)
    jsonPlaylists = getPlaylists.json()
    for playlists in jsonPlaylists['items']:
        if playlists['name'] != 'Song Checker':
            requests.post(createPlaylistURL,data=data,headers=headers)
            checkExistingPlaylist()
            break
        else:
            checkExistingPlaylist()
            break

createTempPlaylist(userID)
