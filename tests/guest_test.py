import unittest 

from src.guest import *
from src.bar import *
from src.song import *
from src.room import *

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Dolly Parton", 60.00)
        self.guest_2 = Guest("Janet Joplin", 50.00)

        self.bar = Bar("The Karaoke Bar", 15.00, 100.00)

        self.song1 = Song("Toxic", "Britney Spears", 2.00)
        self.song2 = Song("Wonderwall", "Oasis", 2.00)

        self.room1 = Room("Room 1", 5, 20.00)
        self.room2 = Room("Room 2", 5, 20.00)


    def test_guest_has_name(self):
        self.assertEqual("Dolly Parton", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(60.00, self.guest.wallet)

    def test_sufficient_funds__true_if_enough(self):
        self.assertEqual(True, self.guest.sufficient_funds(self.song1))

    def test_guest_can_buy_song_decreases_money(self): 
        self.guest.pay_for_song(self.song1)
        self.assertEqual(58.00, self.guest.wallet)

    def test_guest_can_buy_room_decreases_money(self): 
        self.guest.pay_for_room(self.room1)
        self.assertEqual(40.00, self.guest.wallet)

    

