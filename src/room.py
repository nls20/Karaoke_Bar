class Room:

    def __init__(self, room_number, max_capacity, price):
        self.room_number = room_number 
        self.max_capacity = max_capacity
        self.price = price 
        self.guests_in_room = []
        self.playlist = []

    def check_guests_in_room(self):
       return len(self.guests_in_room)

    def add_guest(self, guest):
        self.guests_in_room.append(guest)

    def remove_guest(self, guest):
        total = 0

        for guest in self.guests_in_room:
            total -= 1
    
    def check_room_has_capacity(self, guest):
        if guest in self.guests_in_room > 5:
            return True
        else: 
            return False 

    def add_song_to_room(self, song):
        if song in self.playlist:
            self.playlist[song] += 1
        else:
            return "Song not found"


      


        

    