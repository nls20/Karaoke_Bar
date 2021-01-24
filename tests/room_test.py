import unittest 

from src.guest import *
from src.song import *
from src.room import *

class TestRoom (unittest.TestCase):

    def setUp(self):
        self.room1 = Room("Room 1", 5, 20.00)
        self.room2 = Room("Room 2", 5, 20.00)
     
        rooms = [self.room1, self.room2]
     
        self.guest = Guest("Dolly Parton", 60.00)
        self.guest_2 = Guest("Janet Joplin", 50.00)

        self.song1 = Song("Toxic", "Britney Spears", 1.50)
        self.song2 = Song("Wonderwall", "Oasis", 1.50)

        songs = [self.song1, self.song2]

    def test_room_has_number(self):
      self.assertEqual("Room 1", self.room1.room_number)

    def check_guests_in_room_starts_with_none(self):
        self.assertEqual(0, self.room1.check_guests_in_room())

    def test_can_add_guest_to_room_1(self):
        self.room1.add_guest(self.guest)
        self.assertEqual(1, self.room1.check_guests_in_room())

    def test_can_add_guest_to_room_2(self):
        self.room2.add_guest(self.guest)
        self.assertEqual(1, self.room2.check_guests_in_room())

    def test_can_remove_guest_to_room_1(self):
        self.room1.remove_guest(self.guest)
        self.assertEqual(0, self.room1.check_guests_in_room())

    def test_can_remove_guest_to_room_2(self):
        self.room2.remove_guest(self.guest)
        self.assertEqual(0, self.room2.check_guests_in_room())

    def is_room_at_max_capacity(self):
        self.assertEqual(True, self.room1.check_guests_in_room(6))

    def is_room_at_max_capacity(self):
        self.assertEqual(False, self.room1.check_guests_in_room(4))

    def test_can_add_song_to_room_1(self):
        self.room1.add_song_to_room(self.song1)

    def test_song_not_found(self):
        self.assertEqual("Song not found", self.room1.add_song_to_room(self.song1))
      



 
