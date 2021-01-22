class Room:

    def __init__(self, room_number, max_capacity):
        self.room_number = room_number 
        self.max_capacity = max_capacity
        self.guests_in_room = []


    def check_guests_in_room(self):
        return len(self.guests_in_room)

    def add_guest(self, guest):
        self.guests_in_room.append(guest)

    def remove_guest(self, guest):
        total = 0

        for guest in self.guests_in_room:
            total -= 1

    # def check_room_capacity(self, rooms):
    #     if self.guests_in_room > 5:
    #         return "No more room"
    #     else
    #         return "Come in"

        # if self.check_room_capacity(rooms):
        #     return True 
        


        

    