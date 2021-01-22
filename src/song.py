class Song:

    def __init__(self, name, artist, price):
        self.name = name
        self.artist = artist
        self.price = price
        self.list_of_songs = []

    
    def check_number_of_songs_in_room_is_0(self):
        return len(self.list_of_songs)

    def add_song_to_list(self, song):
        self.list_of_songs.append(song)
