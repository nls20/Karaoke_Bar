class Guest:

    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def pay_for_song(self, song):
        if self.sufficient_funds(song):
            self.wallet -= song.price

    def pay_for_room(self, room):
        if self.sufficient_funds(room):
            self.wallet -= room.price

    def sufficient_funds(self, item):
        return self.wallet >= item.price



