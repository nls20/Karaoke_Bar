import unittest
from src.song import *
from src.guest import *
from src.bar import *
from src.room import *

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Toxic", "Britney Spears", 2.00)
        self.song2 = Song("Wonderwall", "Oasis", 2.00)

    def test_song_has_name(self):
        self.assertEqual("Toxic", self.song1.name)

    def test_song_has_artist(self):
        self.assertEqual("Britney Spears", self.song1.artist)

    def test_song_has_price(self):
        self.assertEqual(2.00, self.song1.price)

    def check_songs_in_room_starts_with_none(self):
        self.assertEqual(0, self.song1.check_number_of_songs_in_room_is_0())

    def test_can_song_to_list(self):
        self.song1.add_song_to_list(self.song1)
        self.assertEqual(1, self.song1.check_number_of_songs_in_room_is_0())

    

