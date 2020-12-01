import os
Downloadslst = os.listdir("") #Change this to wherever you download your songs to.
Downloads = ""

def mp3_sorter(path):   
    for files_withmp3 in path:
        if files_withmp3.endswith("mp3"):
            songs_infile.append(files_withmp3.lower())
    for each_song in songs_infile:
        print(each_song.capitalize())


def find_file(text):
    for songs_related in songs_infile:
        if text in songs_related:
            options.append(songs_related)
    for songs in options:
        song_dict[options.index(songs) + 1] = songs
    print('\n'.join("{}: {}".format(k,v) for k,v in song_dict.items()))
        
def pick_song_from_part_of_name(path,song_choice):
    for songs in options:
        if song_choice in songs:
            return os.startfile(path + songs)
        elif song_choice == str(list(song_dict.keys())[list(song_dict.values()).index(songs)]):
            return os.startfile(path + songs)
    

while True:
    songs_infile = []
    options = []
    song_dict = {}

    mp3_sorter(Downloadslst)
    song = input("Enter a song or artist. ").lower()
    find_file(song)
    choice = input("What song would you like? ")
    print("\n")
    pick_song_from_part_of_name(Downloads,choice)
